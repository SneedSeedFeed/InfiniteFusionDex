use fusion_dex_compiler::RawPokemon;

fn main() {
    let pokemon: Vec<RawPokemon> =
        serde_json::from_str(include_str!("../infinite_dex.json")).unwrap();
    let dex_bytes = bincode::serialize(&pokemon).unwrap();
    std::fs::write("infinite_dex.bin", dex_bytes).unwrap();
}
