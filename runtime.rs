//! Thaumcraft 4.2.3.5 Horizon native port: safe scaffold.
//! No Thaumcraft code/assets here; behaviour is reimplemented from a written spec.

pub const ID: &str = "thaumcraft_core";
pub const NAME: &str = "Thaumcraft Core";
pub const VERSION: &str = "4.2.3.5";
pub const DESCRIPTION: &str = "Scaffold for a hand-ported Thaumcraft 4.2.3.5 core. Currently lists the mod only.";

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn metadata_is_stable() {
        assert_eq!(ID, "thaumcraft_core");
        assert_eq!(VERSION, "4.2.3.5");
        assert!(DESCRIPTION.contains("4.2.3.5"));
    }
}
