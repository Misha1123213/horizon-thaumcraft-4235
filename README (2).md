# horizon-thaumcraft-4235

Рабочее место порта **Thaumcraft 1.7.10-4.2.3.5** на **Horizon Nightly d91cab6** (`d91cab68ded29bd2b004f7050c468fb98c41a00b`).

Важно: это не “перенос jar”. Java/Forge-код Thaumcraft в Horizon не исполняется; сюда входят только локально извлекаемые данные/ассеты и новый Rust-код для поведения. Оригинальные файлы TC4 не коммитим: скрипты читают ваш локальный `Thaumcraft_1.7.10_4.2.3.5.jar` и кладут результат в игнорируемые папки.

## Структура

- `native/thaumcraft-core/` — native-мод `.hnmod` по образцу официальных Horizon native mods. Сейчас это безопасный stub: строка в `Options > Mods`, без изменения геймплея.
- `content/thaumcraft/` — content-мод `.hmod` (manifest API `0.2`) для статических блоков/предметов/рецептов/моделей, когда они будут сгенерированы локально.
- `tools/audit_thaumcraft.py` — инвентаризация jar: классы, ассеты, пакеты, звуки/lang/textures; с `--extract` локально распаковывает `assets/` и `data/` для content-слоя.
- `docs/PORTING_PLAN.md` — карта “что из TC4 куда идёт” и этапы.
- `docs/LEGAL.md` — границы по активам Mojang/Microsoft и Azanor/Thaumcraft.

## Быстрый старт локально

```bash
# 1) аудит jar
python3 tools/audit_thaumcraft.py --jar /path/to/Thaumcraft_1.7.10_4.2.3.5.jar --out build/audit.md

# 2) локально извлечь ассеты/данные в content/thaumcraft (не коммитить)
python3 tools/audit_thaumcraft.py --jar /path/to/Thaumcraft_1.7.10_4.2.3.5.jar --extract content/thaumcraft

# 3) проверка native stub против Horizon d91cab6
git clone https://github.com/horizon-rust/horizon-mods
cd horizon-mods
python3 native/tools/native.py check /path/to/horizon-thaumcraft-4235/native/thaumcraft-core

# 4) сборка через лаунчер
horizon-launcher native-build /path/to/horizon-thaumcraft-4235/native/thaumcraft-core/mixins/thaumcraft_core --trust-native-code
```

## Публикация

Репозиторий сейчас пустой. После первого коммита:

```bash
git remote add origin https://github.com/Misha1123213/horizon-thaumcraft-4235.git
git add .
git commit -m "Scaffold Horizon Thaumcraft 4.2.3.5 port"
git push -u origin main
```

Для кнопки “Добавить с GitHub” в лаунчере нужен релиз/тег/коммит, а не изменяющаяся ветка.
