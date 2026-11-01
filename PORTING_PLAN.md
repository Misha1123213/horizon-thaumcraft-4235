# План порта Thaumcraft 1.7.10-4.2.3.5 -> Horizon d91cab6

Исходный jar: `Thaumcraft_1.7.10_4.2.3.5.jar`, modid `Thaumcraft`, зависимость `Baubles 1.0.1.10`.
Целевой Horizon: nightly `d91cab68ded29bd2b004f7050c468fb98c41a00b`, launcher >= 0.2.23.

## Слой 0 — audit (готово к запуску)
`tools/audit_thaumcraft.py` считает классы/ассеты и строит `build/audit.md`. На текущем jar ориентировочно: 942 class, 1090 asset files, 71 block classes, 84 item classes, 136 entity/AI classes, 80 tile entities, 24 GUI, 26 containers, 170 client renderers.

## Слой 1 — content `.hmod`
Переносится только статическое: textures/lang/models/sounds + простые блоки/предметы через `data/thaumcraft/horizon/{block,item}/*.json`.
Не переносится content-слоем: research, vis/warp, поведение wand/foci, tile entities, golems, GUI, shaders, dimension, мирген в коде.

## Слой 2 — native `.hnmod`
Минимальный stub уже в `native/thaumcraft-core`: добавляет строку мода в `Options > Mods` через hook `native_mods`.
Дальше каждая подсистема — отдельный модуль/инжекции:
1. `aspects` — реестр аспектов TC4, иконки, имена, синтез/состав.
2. `scanning` — Thaumometer: raycast по блоку/предмету, начисление research points, подсказки.
3. `research` — Thaumonomicon: категории, страницы, зависимости, unlock state per-player.
4. `wand` — wand/rod/cap, vis storage, charging, casting foci.
5. `alchemy` — crucible, arcane furnace, essentia, jars, tubes, reservoir.
6. `infusion` — altar matrix, instability, recipes, enchantments.
7. `golems` — golem entity, cores, AI tasks, seals.
8. `world` — ores, trees, nodes, taint/flux, eldritch dimension/obelisks.
9. `client_fx` — particles, shaders, sounds, custom renderers.

## Правило parity
Для каждой механики держим “спецификацию TC4” в `docs/spec/<system>.md`: вход, выход, edge cases, отличия MC 1.7.10 -> Horizon 26.3. Тесты: unit-тесты Rust для чистой логики + ручные сценарии в мире.
