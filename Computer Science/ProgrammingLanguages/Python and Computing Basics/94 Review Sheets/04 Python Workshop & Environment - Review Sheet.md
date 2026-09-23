# 4.13 Common misconceptions consolidated

1. **“Installing Python determines what `python` means everywhere.”** Shell resolution, aliases, launchers, active environments, and existing installations determine selection.
2. **“The REPL and a script are two languages.”** They use the same Python language under different interaction and state-lifetime conditions.
3. **“Activation creates or secures an environment.”** Creation builds it; activation adjusts one shell’s command resolution; neither is a hostile-code sandbox.
4. **“`pip` installs import names.”** It installs distributions, which provide one or more import packages under potentially different names.
5. **“Copying `.venv` reproduces a project.”** Environment directories can contain platform- and path-specific state. Reconstruct from declared inputs.
6. **“The latest version is automatically the correct version.”** A project admits versions through a compatibility contract and test evidence.
7. **“Catching every exception makes a program robust.”** Indiscriminate handling can misclassify defects, corrupt evidence, and continue from invalid state.
8. **“A successful local run proves portability.”** It establishes one environment-scoped observation.
