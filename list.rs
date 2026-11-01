// Options > Mods row for the scaffold. No gameplay changes yet.
fn thaumcraft_core_listed(mods: &mut Vec<crate::game::native_hooks::NativeMod>) {
    use crate::game::thaumcraft_core as m;
    mods.push(crate::game::native_hooks::NativeMod {
        id: m::ID.into(),
        title: format!("{} {}", m::NAME, m::VERSION),
        description: m::DESCRIPTION.into(),
        keys: Vec::new(),
    });
}
