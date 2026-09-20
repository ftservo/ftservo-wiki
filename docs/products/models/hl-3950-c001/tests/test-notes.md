# HLS3950M 测试记录 / Test record

[原始数据 / Raw data](../test-result.json)

## 已记录 / Recorded

| 字段 / Field | 原始导出 / Export value |
| --- | --- |
| 工装记录型号 / Fixture model | HLS3950M |
| 样本序列号 / Serial | SN12212 |
| 测试开始 / Started | 2026-08-18T19:50:11+08:00 |
| 测试结束 / Finished | 2026-08-18T19:51:10+08:00 |
| 原始文件 / Source | SN12212_20260818-195011_52de9cb9.json |
| 采集结果 / Status | completed |
| 结束原因 / Finish reason | stall |
| 测点数量 / Raw measurements | 52 |

## 适用范围 / Scope

本结果沿用型号页已有的 HLS3950M 示例。JSON 记录的型号不含 C001 后缀，也未记录固件；使用前需对照实物和测试台账确认适用性，不据此认证全部型号后缀。

This is the existing HLS3950M example on this model page. The JSON model omits the C001 suffix and does not establish firmware compatibility. Confirm the physical sample and test log before applying it to a specific variant.

## 未记录 / Not recorded

本文件未补测以下条件：环境温度、散热方式、完整机械安装与负载方法、传感器校准、操作者、连续运行能力及可追溯的完整型号后缀。原始测点内包含电压读数，但不能将单点电压当作已确认的稳压电源设定。

Ambient temperature, cooling, complete mounting/load procedure, sensor calibration, operator, continuous-duty capability and a traceable full model suffix were not established here. Per-sample voltage readings are not evidence of a verified supply setpoint.

## 曲线显示 / Plot processing

原始 52 点保持不变。与工装相同，按采集顺序截断首次明显回落后的测点，本次显示 50 个峰值前测点；可切换原始折线与 181 点平滑趋势。量程和单位读取 JSON；效率采用工装的保形插值，其余曲线使用鲁棒 LOWESS。平滑值不是新增实测数据，也不替代额定或堵转规格。

All 52 raw points are preserved. The fixture's peak cutoff displays 50 points before the torque drop. Switch between measured lines and the 181-point smoothed trend. Axis ranges and units come from JSON; efficiency uses shape-preserving interpolation, and other series use robust LOWESS. Estimates are not new measurements or product ratings.
