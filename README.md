# thaumcraft-core (native)

Stub native mod для Horizon Nightly `d91cab6`. Сейчас только регистрирует мод в `Options > Mods`; геймплей не меняет.

Проверка:

```bash
python3 native/tools/native.py check /path/to/horizon-thaumcraft-4235/native/thaumcraft-core
```

Сборка:

```bash
horizon-launcher native-build /path/to/horizon-thaumcraft-4235/native/thaumcraft-core/mixins/thaumcraft_core --trust-native-code
```
