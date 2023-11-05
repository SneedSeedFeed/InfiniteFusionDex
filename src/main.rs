use fusion_dex_compiler::RawPokemon;
use std::collections::HashMap;

use std::time::Instant;

fn main() {
    let pokemon: Vec<RawPokemon> =
        serde_json::from_str(include_str!("../infinite_dex.json")).unwrap();
    let dex_bytes = bincode::serialize(&pokemon).unwrap();
    std::fs::write("infinite_dex.bin", dex_bytes).unwrap();
    let path = std::path::Path::new("CustomBattlers");
    if path.is_dir() {
        let files = std::fs::read_dir(path).unwrap();
        let mut sprite_count: HashMap<(u16, u16), u8> = HashMap::new();
        let start = Instant::now();
        files.into_iter().for_each(|file| {
            let file = file.unwrap();
            let binding = file.path();
            let file_extension = binding.extension().unwrap();
            let binding = file.file_name().into_string().unwrap();
            if file_extension == "png" {
                let split = binding.split('.').collect::<Vec<_>>();
                let head = split[0].parse::<u16>().unwrap();
                let body = {
                    let strip = split[1].strip_suffix(|c: char| !c.is_ascii_digit());
                    if let Some(strip) = strip {
                        strip.parse::<u16>().unwrap()
                    } else {
                        split[1].parse::<u16>().unwrap()
                    }
                };
                *sprite_count.entry((head, body)).or_insert(0) += 1;
            }
        });
        println!("Files processed in {}ms", start.elapsed().as_millis());

        let start = Instant::now();
        let count_bytes = bincode::serialize(&sprite_count).unwrap();
        std::fs::write("sprite_count.bin", count_bytes).unwrap();
        println!("Binary saved in {}ms", start.elapsed().as_millis());
        let new_map = sprite_count
            .iter()
            .map(|((head, body), count)| (format!("{}.{}", head, body), *count))
            .collect::<HashMap<_, _>>();
        let count_json = serde_json::to_string(&new_map).unwrap();
        std::fs::write("sprite_count.json", count_json).unwrap();
        println!("JSON saved in {}ms", start.elapsed().as_millis());
    }
}
