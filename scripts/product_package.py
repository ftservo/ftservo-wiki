"""Maintain bilingual product packages using only the Python standard library.

Existing specification pages are never regenerated. refresh owns only the
marked resource table; software.md and mechanical.md are edited by engineers.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MODEL_ROOTS = (ROOT / "docs/products/models", ROOT / "docs/en/products/models")
BEGIN = "<!-- product-resources:start -->"
END = "<!-- product-resources:end -->"
KINDS = {
    "datasheet": ("型号规格书", "Model datasheet"),
    "pinout": ("接口与针序图", "Connector and pinout"),
    "memory_table": ("型号内存表 / 固件说明", "Model memory table / firmware notes"),
    "drawing": ("2D 安装图", "2D mounting drawing"),
    "cad": ("STEP / 3D 模型", "STEP / 3D model"),
    "example": ("型号验证示例", "Model-tested example"),
    "test_result": ("原始测试数据", "Raw test data"),
    "test_conditions": ("测试记录与条件说明", "Test record and conditions"),
}
APP_LAYERS = {
    "SCS": ("scscl", "SCSCL", "memory-scscl.md"),
    "STS": ("sms_sts", "SMS_STS", "memory-sms-sts.md"),
    "SMS": ("sms_sts", "SMS_STS", "memory-sms-sts.md"),
    "HLS": ("hls", "HLSCL", "memory-hls.md"),
}


def read_json(path: Path):
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def asset_path(folder: Path, value: str) -> Path:
    """All downloadable files must belong to this exact model folder."""
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise ValueError(f"Invalid asset path: {value!r}")
    relative = PurePosixPath(value)
    if relative.is_absolute() or ".." in relative.parts or any(p.startswith(".") for p in relative.parts):
        raise ValueError(f"Asset path must stay inside its model: {value}")
    resolved = (folder / relative).resolve()
    if not resolved.is_relative_to(folder.resolve()):
        raise ValueError(f"Asset path escapes its model: {value}")
    return resolved


def new_manifest(model_id: str, name: str, family: str, interface: str, revision=None):
    return {
        "schema_version": 1,
        "model_id": model_id,
        "model_name": name,
        "family": family,
        "interface": interface,
        "document_revision": revision,
        "sources": [],
        "assets": [
            {"kind": kind, "status": "not_applicable" if kind == "memory_table" and interface == "PWM" else "missing",
             "path": None, "revision": None, "source": None}
            for kind in KINDS
        ],
    }


def resource_section(manifest: dict, en: bool) -> str:
    title = "Resources and document status" if en else "资料下载与完整性"
    note = ("Only files included in this model package have download links. Missing resources are not yet supplied; family guides do not verify model-specific settings."
            if en else "仅为本型号资料包中已收录的文件提供下载链接。“待补充”表示尚未提供，系列教程不能代替型号专用参数确认。")
    lines = [BEGIN, f"## {title} {{#resources}}", "", note, "",
             "| Resource | Status / file | Revision |" if en else "| 资料 | 状态 / 文件 | 版本 |",
             "| --- | --- | --- |"]
    from urllib.parse import quote
    for item in manifest["assets"]:
        label = KINDS[item["kind"]][int(en)]
        status = item["status"]
        if status == "available":
            link = f"[{PurePosixPath(item['path']).name}]({quote(item['path'], safe='/')})"
        elif status == "not_applicable":
            link = "Not applicable" if en else "不适用"
        else:
            link = "Not supplied" if en else "待补充"
        lines.append(f"| {label} | {link} | {item.get('revision') or '—'} |")
    lines += ["", "[Package manifest](manifest.json) · [Request missing resources](#support)" if en
              else "[下载资料清单](manifest.json) · [申请缺失资料](#support)", "",
              "For an offline ZIP with both languages and available attachments, see [product-package export](../../../downloads.md#product-packages)." if en
              else "需要包含中英文说明和已收录附件的离线 ZIP，参见[型号资料包导出](../../../downloads.md#product-packages)。", END]
    return "\n".join(lines)


def route_section(en: bool) -> str:
    if en:
        return """## Start your integration

| Your task | Start here | What to check |
| --- | --- | --- |
| Write control software | [Software integration](software.md) | Interface, application layer, read-first bring-up and validation record |
| Design a bracket or joint | [Mechanical integration](mechanical.md) | Drawings, CAD, datum, output shaft and cable clearance |
| Collect engineering files | [Resources and status](#resources) | Available files and outstanding information |

"""
    return """## 开始集成

| 我要做什么 | 从这里开始 | 需要确认什么 |
| --- | --- | --- |
| 编写控制程序 | [程序开发](software.md) | 接口、应用层、先读后动的联调步骤与验证记录 |
| 设计支架或关节 | [结构设计](mechanical.md) | 图纸、模型、基准、输出轴及线缆空间 |
| 收集工程文件 | [资料下载与完整性](#resources) | 已提供的附件与待补充资料 |

"""


def support_section(en: bool) -> str:
    if en:
        return """## Request resources or report an issue {#support}

Use your existing FEETECH technical-support contact and include the full label/model suffix, firmware version (if known), and the document revision you are using.

- Software: controller/OS, SDK version or commit, adapter/interface, supply voltage, confirmed ID/baud rate (bus models only), minimal reproduction and logs.
- Mechanics: drawing/CAD revision, marked dimensions, required travel, horn/bracket, load and lever arm, duty cycle, and the point of interference.
- Missing files: name the exact item in the resource table (for example, this model's STEP and a dimensioned mounting drawing).

This package currently provides a specification summary and integration checklists. File availability does not imply that your firmware, load case or assembly has been validated.
"""
    return """## 申请资料与反馈问题 {#support}

向已有的飞特技术支持联系人提供完整标签型号及后缀、固件版本（如已知）和正在使用的资料版本。

- 程序问题：主控与系统、SDK 版本或提交号、适配器与接口、供电电压、已确认的 ID / 波特率（仅总线型号）、最小复现步骤及日志。
- 结构问题：图纸 / 模型版本、标注尺寸、所需行程、舵盘 / 支架、负载与力臂、工作周期及干涉位置。
- 缺少资料：直接说明资料表中的具体项目，例如“本型号 STEP 和带公差的安装图”。

本资料包当前提供规格摘要和集成检查步骤；文件可下载不代表已验证你的固件、负载工况或装配方案。
"""


def software_page(m: dict, en: bool) -> str:
    name, interface, family = m["model_id"].upper(), m["interface"], m["family"]
    pwm = interface == "PWM"
    layer = APP_LAYERS.get(family) if not pwm else None
    if en:
        intro = f"# {name} · Software integration\n\n[Overview and files](main.md) · [Mechanical integration](mechanical.md)\n\nControl interface: **{interface}**. Confirm the full model suffix against the physical label.\n\n"
        if pwm:
            route = """## PWM control path

Use your controller's timer/PWM peripheral. Serial-bus SDK examples, device IDs, baud rates and register tables do not apply to this PWM interface.

Before outputting a signal, obtain this model's connector orientation/pinout, signal voltage, pulse period, pulse-width limits, neutral/stop setting, and angle-versus-speed behavior. Do not assume a universal pulse range or infer continuous rotation from a catalog angle label. These model-specific control parameters are not supplied in this package yet.

## First controlled test

1. Confirm the exact supply range, polarity, shared ground, pinout and signal level from this model's documentation; keep PWM output disabled while wiring.
2. Disconnect the load/linkage and leave room for possible start-up motion. Arrange an accessible power disconnect.
3. Configure only the documented pulse period and neutral/stop setting; if either is unknown, stop here and request the missing data.
4. Apply a small, documented change and confirm direction and angle/speed behavior. Do not sweep an assumed full range.
5. Establish software bounds, startup behavior and signal-loss behavior before attaching the mechanism.
"""
        else:
            route = "## Choose the application layer\n\n"
            if layer:
                route += f"Family reference: **{family}** → Python `{layer[0]}`; Arduino / C++ `{layer[1]}`. Read the [family memory-table guide](../../../reference/{layer[2]}) and [packet protocol](../../../reference/protocol.md). This identifies the family entry point, not confirmed addresses, units or modes for this model and firmware.\n\n"
            else:
                route += "This package does not yet establish an SDK application layer or memory-table version for this model. A TTL interface alone does not establish compatibility with SCSCL, SMS_STS or HLSCL. Obtain the model/firmware documentation before selecting a class or sending register writes.\n\n"
            route += """| Development environment | Existing guide |
| --- | --- |
| PC / Raspberry Pi / Jetson | [Python](../../../sdk/python.md) |
| Arduino / ESP32 / PlatformIO | [Arduino / ESP32](../../../sdk/arduino.md) |
| Linux C++ / STM32 HAL | [Linux / STM32](../../../sdk/linux-stm32.md) |

These are shared SDK guides; no model-specific hardware-tested example is supplied in this package yet.

## Read first, then move

1. Confirm power, shared ground, connector pinout and the matching TTL or RS-485 interface using [wiring](../../../getting-started/wiring.md) and [adapter](../../../tools/adapters.md) guidance. Pinout drawings for the exact model take precedence over wire colors.
2. Connect one servo with the mechanism unloaded, keep clear of start-up movement, and confirm its current ID and baud rate using the documented discovery procedure. No default ID or baud rate is asserted here.
3. Verify the SDK class and firmware/memory-table revision; then run a unicast Ping and supported read-only queries. Log responses and timeouts before writing anything.
4. Establish torque-enable state, mode, units and software/mechanical limits. Use only a validated small motion with a matching example; never copy a position/register limit from another family.
5. Add unique IDs, bounded retries, communication-loss handling and multi-servo operation after single-servo validation.

See [first motion](../../../getting-started/first-motion.md) for the shared workflow and [troubleshooting](../../../troubleshooting.md) for diagnosis.
"""
        return intro + route + """
## Required model-specific information

Check the [resource table](main.md#resources). Pinout, control limits, protection thresholds, firmware behavior and model-tested code remain unconfirmed unless supplied and explicitly identified there. A missing value is not zero or a default.

## Record a reproducible integration

| Record | Your value |
| --- | --- |
| Full physical label / firmware | Record before testing |
| Controller, OS and toolchain | Record exact versions |
| SDK commit / example path (bus) or PWM configuration | Record exact revision and parameters |
| Supply / adapter / wiring revision | Record measured conditions |
| Initial state, command and expected result | Start with the smallest validated operation |
| Actual response, timeouts and stop behavior | Save logs; include test date and load condition |

Share this record with [technical support](main.md#support) when requesting a model-specific example.
"""
    intro = f"# {name} · 程序开发\n\n[型号概览与资料](main.md) · [结构设计](mechanical.md)\n\n控制接口：**{interface}**。先将完整型号后缀与实物标签核对。\n\n"
    if pwm:
        route = """## PWM 控制路线

使用主控的定时器 / PWM 外设。串行总线 SDK 示例、设备 ID、波特率和寄存器表不适用于本页列出的 PWM 接口。

输出信号前，需要本型号的连接器朝向与针序、信号电平、脉冲周期、脉宽上下限、中位 / 停止值，以及角度控制或转速控制方式。不能默认采用某个“通用脉宽范围”，也不能只凭目录角度标记推断连续旋转。这些型号专用控制参数目前尚未收录。

## 首次受控测试

1. 根据本型号资料核对电源范围、极性、共地、针序和信号电平；接线时保持 PWM 输出关闭。
2. 先脱开负载或连杆，为可能的上电动作留出空间，并准备可随时切断的电源。
3. 仅配置文档确认的周期和中位 / 停止值；任何一项未知时，先申请资料，不继续输出试探信号。
4. 在已确认范围内做小幅变化，检查方向及角度 / 转速响应；不要直接全行程扫描。
5. 确认软件限位、上电行为和丢信号行为，再连接机构。
"""
    else:
        route = "## 选择应用层\n\n"
        if layer:
            route += f"系列入口：**{family}** → Python `{layer[0]}`；Arduino / C++ `{layer[1]}`。参阅[系列内存表指南](../../../reference/{layer[2]})与[数据包协议](../../../reference/protocol.md)。这里仅确定系列入口，不代表已确认本型号及固件的寄存器地址、单位或模式。\n\n"
        else:
            route += "当前资料包尚未确认本型号适用的 SDK 应用层及内存表版本。TTL 接口本身不能证明兼容 SCSCL、SMS_STS 或 HLSCL；取得对应型号和固件的资料后，再选择类或发送寄存器写入。\n\n"
        route += """| 开发环境 | 已有指南 |
| --- | --- |
| PC / 树莓派 / Jetson | [Python](../../../sdk/python.md) |
| Arduino / ESP32 / PlatformIO | [Arduino / ESP32](../../../sdk/arduino.md) |
| Linux C++ / STM32 HAL | [Linux / STM32](../../../sdk/linux-stm32.md) |

以上是共享 SDK 教程；本资料包目前尚未提供经本型号实物验证的专用示例。

## 先读后动的联调顺序

1. 按[供电与接线](../../../getting-started/wiring.md)及[适配器指南](../../../tools/adapters.md)确认电源、共地、针序与匹配的 TTL / RS-485 接口。具体型号针序图优先于线色经验。
2. 先只连接一只舵机、脱开机构负载并留出上电动作空间，按确认过的发现流程读取当前 ID 与波特率；本页不假定出厂默认值。
3. 核实 SDK 类及固件 / 内存表版本，先运行单播 Ping 和受支持的只读查询，记录返回值与超时，再考虑写入。
4. 确认扭矩使能状态、控制模式、单位及软件 / 机械限位。使用匹配示例进行已验证的小幅运动，不套用其他系列的位置范围或寄存器限制。
5. 单机验证通过后，再加入唯一 ID、有限重试、失联处理和多机控制。

共享流程见[第一次运动](../../../getting-started/first-motion.md)，异常定位见[常见问题](../../../troubleshooting.md)。
"""
    return intro + route + """
## 必须补齐的型号信息

查看[资料清单](main.md#resources)。除非已有文件并明确注明适用范围，否则针序、控制限制、保护阈值、固件行为和型号验证代码仍需确认。缺失值不等于零，也不等于默认值。

## 留下可复现的接入记录

| 记录项 | 项目填写内容 |
| --- | --- |
| 实物完整标签 / 固件 | 测试前记录 |
| 主控、系统、工具链 | 记录准确版本 |
| SDK 提交号 / 示例路径（总线）或 PWM 配置 | 记录代码版本及实际参数 |
| 电源 / 适配器 / 接线图版本 | 记录实测条件 |
| 初始状态、命令与预期结果 | 从最小已验证操作开始 |
| 实际响应、超时及停止行为 | 保存日志，注明日期与负载状态 |

申请型号专用示例时，将记录交给[技术支持](main.md#support)。
"""


def mechanical_page(m: dict, en: bool) -> str:
    name = m["model_id"].upper()
    if en:
        return f"""# {name} · Mechanical integration

[Overview and files](main.md) · [Software integration](software.md)

## Start with the engineering files

Check the [resource table](main.md#resources) for this exact model's dimensioned 2D drawing and STEP model. Neither is currently supplied in this package. The outline dimensions on the overview, if present, are insufficient to release a mounting part for manufacture.

Use a dimensioned, approved drawing for tolerances and interfaces; use STEP for assembly and clearance checks. STL is suitable for visualization or fit prototypes only when its units and scale are confirmed; do not derive manufacturing tolerances from its mesh. Ask the manufacturer to resolve any drawing/CAD discrepancy.

## Check before designing the bracket

| Interface | Confirm from this model's documents |
| --- | --- |
| Envelope and datum | Units, origin, axes, housing size, projections and mounting faces |
| Mounting holes | Hole centers, diameters, threads, usable screw depth, screw length and tightening requirements |
| Output / horn / secondary shaft | Spline or shaft definition, horn compatibility, retention and protrusion |
| Joint zero and travel | Drawing zero, electrical zero, rotation direction, usable travel and hard stops |
| Cable and connector | Exit direction, mating connector, unplugging space, bend allowance and full-travel routing |
| Load and supports | Force direction, lever arm, continuous/peak torque, duty cycle, radial/axial load limits and any external bearing requirements |

These dimensions and load limits are not supplied here; do not borrow them from another model or suffix. Model-specific horn, screw and bearing recommendations require confirmation.

## Assembly verification sequence

1. Record CAD/drawing revision and units. Check key dimensions against the physical sample before detailed bracket design.
2. Align the housing mounting datum and output axis in the assembly; place the horn at a documented reference position.
3. Check the full confirmed travel for housing/horn/bracket interference and cable tension, including assembly tolerances.
4. Confirm screw engagement, tool access and service access without bottoming screws or loading the case incorrectly.
5. Verify control direction and zero unloaded using the [software workflow](software.md), then attach the mechanism and expand motion gradually within verified limits.

## Load evaluation and handoff

Stall torque is not a continuous rating. Record the actual force direction, lever arm, acceleration, duty cycle, temperature and impact conditions. A single torque-test curve does not establish continuous, radial or axial load capacity.

Deliver the assembly revision, drawing/CAD revisions, horn/bracket part IDs, installed zero, allowed travel and marked clearance screenshots to the control developer. Return any unresolved geometry or loading questions through [technical support](main.md#support).
"""
    return f"""# {name} · 结构设计

[型号概览与资料](main.md) · [程序开发](software.md)

## 先取得工程文件

查看[资料清单](main.md#resources)，确认本完整型号的带尺寸 2D 安装图与 STEP 模型。目前本资料包尚未收录这两类文件。概览中的外形尺寸（如有）不足以直接出具加工安装件。

公差与配合以批准的尺寸图为依据，STEP 用于装配及干涉检查。STL 需先确认单位与比例，适合展示或试装原型，不应从三角网格反推制造公差。图纸与模型不一致时，应由厂家确认。

## 画支架前核对

| 接口 | 需从本型号资料确认 |
| --- | --- |
| 外形与基准 | 单位、原点、坐标方向、壳体尺寸、突出物和安装基准面 |
| 安装孔 | 孔距、孔径、螺纹、有效旋入深度、螺钉长度及紧固要求 |
| 输出轴 / 舵盘 / 从动轴 | 轴齿或轴型定义、舵盘配套关系、固定方式与突出高度 |
| 关节零位与行程 | 图纸零位、电气零位、旋转方向、可用行程与硬限位 |
| 线缆与连接器 | 出线方向、配对连接器、插拔空间、弯曲余量及全行程走线 |
| 负载与支承 | 受力方向、力臂、持续 / 峰值扭矩、工作周期、径向 / 轴向承载及外部支承要求 |

上述接口尺寸与承载限制目前尚未收录，不借用相似型号或其他后缀的数据。配套舵盘、螺钉和轴承方案需要型号级确认。

## 装配验证顺序

1. 记录图纸 / 模型版本与单位，先对照实物样品校核关键尺寸，再细化支架。
2. 在装配中对齐壳体安装基准与输出轴，将舵盘放在已确认的参考位置。
3. 在已确认的完整行程内检查壳体、舵盘、支架干涉及线缆拉扯，计入装配公差。
4. 检查螺钉啮合、工具及维修空间，避免螺钉顶底或不当挤压壳体。
5. 按[程序开发流程](software.md)先空载确认方向和零位，再连接机构，在已验证的限位内逐步扩大动作。

## 负载评估与交接

堵转扭矩不是持续工作额定值。记录实际受力方向、力臂、加速度、工作周期、温升和冲击条件；单次扭矩曲线不能确定持续承载、径向承载或轴向承载能力。

向程序开发者交付装配版本、图纸 / CAD 版本、舵盘与支架编号、安装零位、允许行程和带标注的干涉检查截图。未解决的几何与负载问题通过[技术支持](main.md#support)确认。
"""


def validate_manifest(folder: Path, manifest: dict):
    errors = []
    if manifest.get("schema_version") != 1 or manifest.get("model_id") != folder.name:
        errors.append("schema_version or model_id does not match folder")
    for key in ("model_name", "family", "interface"):
        if not isinstance(manifest.get(key), str) or not manifest[key].strip():
            errors.append(f"Missing identity field: {key}")
    if not isinstance(manifest.get("sources"), list):
        errors.append("sources must be a list")
    assets = manifest.get("assets")
    if not isinstance(assets, list):
        return errors + ["assets must be a list"]
    if sorted(a.get("kind", "") for a in assets if isinstance(a, dict)) != sorted(KINDS):
        errors.append("assets must contain each defined kind exactly once")
    for item in assets:
        if not isinstance(item, dict):
            errors.append("Each asset must be an object")
            continue
        if item.get("status") not in {"missing", "available", "not_applicable"}:
            errors.append(f"Invalid status: {item.get('kind')}")
        elif item["status"] == "available":
            try:
                path = asset_path(folder, item.get("path"))
                if not path.is_file() or path.stat().st_size == 0:
                    errors.append(f"Missing or empty asset: {item.get('path')}")
                if not item.get("source"):
                    errors.append(f"Source required: {item.get('path')}")
                if path.is_file() and item.get("kind") == "test_result" and path.suffix == ".json":
                    result = read_json(path)
                    if not result.get("measurements") or not result.get("range_profile", {}).get("axes"):
                        errors.append("Test JSON needs measurements and range_profile.axes")
                    if not item.get("test_model") or result.get("model") != item["test_model"]:
                        errors.append("Test JSON model must match the reviewed test_model field")
            except (ValueError, TypeError, OSError) as exc:
                errors.append(str(exc))
        elif item.get("path") is not None:
            errors.append(f"Unavailable asset must not have a path: {item.get('kind')}")
    if manifest.get("interface") == "PWM":
        memory = next((a for a in assets if isinstance(a, dict) and a.get("kind") == "memory_table"), {})
        if memory.get("status") != "not_applicable":
            errors.append("PWM package must mark the bus memory table not_applicable")
    return errors


def validate(model_id=None):
    errors = []
    ids = {p.name for root in MODEL_ROOTS for p in root.iterdir() if p.is_dir()}
    if model_id:
        ids = {model_id}
    for key in sorted(ids):
        manifests = []
        for locale, root in zip(("zh", "en"), MODEL_ROOTS):
            folder = root / key
            for name in ("main.md", "software.md", "mechanical.md", "manifest.json"):
                if not (folder / name).is_file():
                    errors.append(f"{locale}/{key}: missing {name}")
            try:
                manifest = read_json(folder / "manifest.json")
                manifests.append(manifest)
                problems = validate_manifest(folder, manifest)
                errors.extend(f"{locale}/{key}: {error}" for error in problems)
                if not problems and (folder / "main.md").is_file():
                    content = (folder / "main.md").read_text(encoding="utf-8")
                    if resource_section(manifest, locale == "en") not in content:
                        errors.append(f"{locale}/{key}: resource table out of date; run refresh")
                    if 'class="servo-characteristic-chart"' in content:
                        test = next(a for a in manifest["assets"] if a["kind"] == "test_result")
                        if test["status"] != "available":
                            errors.append(f"{locale}/{key}: chart requires an available test result")
                        for source in re.findall(r'class="servo-characteristic-chart"[^>]*data-source="([^"]+)"', content):
                            if source != "../" + str(test.get("path")):
                                errors.append(f"{locale}/{key}: chart source does not match manifest test_result")
            except (OSError, ValueError, TypeError) as exc:
                errors.append(f"{locale}/{key}: {exc}")
        if len(manifests) == 2:
            if manifests[0] != manifests[1]:
                errors.append(f"{key}: bilingual manifests differ")
            else:
                for item in manifests[0].get("assets", []):
                    if isinstance(item, dict) and item.get("status") == "available":
                        try:
                            files = [asset_path(root / key, item["path"]) for root in MODEL_ROOTS]
                            if all(p.is_file() for p in files) and files[0].read_bytes() != files[1].read_bytes():
                                errors.append(f"{key}: bilingual asset bytes differ: {item['path']}")
                        except ValueError:
                            pass
    if errors:
        raise ValueError("\n".join(errors))
    return len(ids)


def refresh(model_id=None):
    changes = []
    for root in MODEL_ROOTS:
        folders = [root / model_id] if model_id else sorted(p for p in root.iterdir() if p.is_dir())
        for folder in folders:
            manifest = read_json(folder / "manifest.json")
            errors = validate_manifest(folder, manifest)
            if errors:
                raise ValueError(f"{folder}: " + "; ".join(errors))
            path = folder / "main.md"
            content = path.read_text(encoding="utf-8")
            if content.count(BEGIN) != 1 or content.count(END) != 1:
                raise ValueError(f"{path}: resource markers must occur exactly once")
            replacement = resource_section(manifest, root == MODEL_ROOTS[1])
            changes.append((path, content[:content.index(BEGIN)] + replacement + content[content.index(END) + len(END):]))
    for path, content in changes:
        write(path, content)


def package(model_id: str, output: Path):
    validate(model_id)
    if output.exists():
        raise ValueError(f"Refusing to overwrite existing file: {output}")
    if output.resolve().is_relative_to((ROOT / "docs").resolve()):
        raise ValueError("Export outside docs to avoid publishing stale ZIP files")
    contents = {}
    for locale, root in zip(("zh", "en"), MODEL_ROOTS):
        folder = root / model_id
        manifest = read_json(folder / "manifest.json")
        names = {"main.md", "software.md", "mechanical.md", "manifest.json"}
        names.update(item["path"] for item in manifest["assets"] if item["status"] == "available")
        # Images directly referenced by pages are included, but arbitrary drafts,
        # credentials and unlisted engineering files are never swept into a ZIP.
        for name in ("main.md", "software.md", "mechanical.md"):
            for match in re.finditer(r"!\[[^\]]*\]\(([^ )]+)\)", (folder / name).read_text(encoding="utf-8")):
                from urllib.parse import unquote
                image = unquote(match[1])
                if not image.startswith(("https://", "http://")):
                    names.add(image)
        for name in sorted(names):
            path = asset_path(folder, name)
            contents[f"{model_id}/{locale}/{name}"] = path.read_bytes()
    contents[f"{model_id}/README.txt"] = (
        "FEETECH product package / 型号资料包\n"
        "Open zh/main.md or en/main.md in a Markdown reader.\n"
        "用 Markdown 阅读器打开 zh/main.md 或 en/main.md；缺失资料见清单。\n"
        "Shared SDK/wiring links and interactive charts require the online Wiki; SDKs are not bundled.\n"
        "共享教程链接及交互曲线请使用在线 Wiki；此包不包含 SDK。\n"
        f"https://ftservo.github.io/ftservo-wiki/products/models/{model_id}/main/\n"
    ).encode("utf-8")
    checksums = "\n".join(f"{hashlib.sha256(data).hexdigest()}  {name}" for name, data in sorted(contents.items())) + "\n"
    contents[f"{model_id}/SHA256SUMS.txt"] = checksums.encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(contents.items()):
            archive.writestr(name, data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "refresh", "package"))
    parser.add_argument("--model", help="Exact lowercase model folder ID; omit to check/refresh all")
    parser.add_argument("--output", type=Path, help="New ZIP path outside docs (package only)")
    args = parser.parse_args()
    if args.model and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.model):
        parser.error("--model must be a lowercase model ID")
    try:
        if args.command == "package":
            if not args.model or not args.output:
                parser.error("package requires --model and --output")
            package(args.model, args.output)
            print(f"Exported: {args.output}")
        elif args.command == "refresh":
            refresh(args.model)
            print("Resource tables refreshed; run validate and mkdocs build --strict.")
        else:
            print(f"Validated {validate(args.model)} bilingual model packages.")
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
