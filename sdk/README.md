# Official SDK submodules

Each directory is pinned to a commit in an official `ftservo` repository and
retains its own license and history. Clone this Wiki with all SDK content:

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
```

Initialize an existing checkout with:

```bash
git submodule update --init --recursive
```

Review and test upstream changes before updating a pinned commit. Do not edit a
submodule here unless the change will also be contributed to its upstream SDK
repository.

