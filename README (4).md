# content/thaumcraft

Здесь должен появиться content-мод `.hmod`, но **ассеты и data не коммитятся**.

Локально:

```bash
python3 ../../tools/audit_thaumcraft.py --jar /path/to/Thaumcraft_1.7.10_4.2.3.5.jar --extract .
```

После извлечения вручную превращайте статические блоки/предметы в `data/thaumcraft/horizon/block|item/*.json` по официальному формату Horizon content mods. Всё с поведением уходит в `native/`.
