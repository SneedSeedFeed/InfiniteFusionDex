use serde::{Deserialize, Serialize};

#[derive(Deserialize, Debug, Serialize)]
pub struct RawPokemon {
    pub id: u16,
    pub name: RawNames,
    #[serde(rename = "type")]
    pub types: Vec<Type>,
    pub base: RawStats,
    pub species: String,
    pub description: String,
    pub evolution: RawEvolutions,
    pub profile: RawProfile,
    pub image: RawImage,
    pub fusion_type_override: Option<Type>,
}

#[derive(Deserialize, Debug, Serialize)]
pub struct RawNames {
    pub english: String,
    pub japanese: String,
    pub chinese: String,
    pub french: String,
}

#[derive(Deserialize, Debug, Serialize)]
pub struct RawStats {
    #[serde(rename = "HP")]
    pub hp: u8,
    #[serde(rename = "Attack")]
    pub attack: u8,
    #[serde(rename = "Defense")]
    pub defense: u8,
    #[serde(rename = "Sp. Attack")]
    pub special_attack: u8,
    #[serde(rename = "Sp. Defense")]
    pub special_defense: u8,
    #[serde(rename = "Speed")]
    pub speed: u8,
}

#[derive(Deserialize, Debug, Serialize)]
pub struct RawProfile {
    pub height: String,
    pub weight: String,
    pub egg: Vec<String>,
    pub ability: Vec<(String, bool)>,
    pub gender: String,
}

#[derive(Deserialize, Debug, Serialize)]
pub struct RawImage {
    pub sprite: String,
    pub thumbnail: String,
    pub hires: String,
}

#[derive(Deserialize, Debug, Serialize)]
pub struct RawEvolutions {
    pub prev: Option<(String, String)>,
    pub next: Option<Vec<(String, String)>>,
}

#[derive(Debug, PartialEq, Eq, Hash, Clone, Copy, Deserialize, Serialize)]
pub enum Type {
    Bug,
    Dark,
    Dragon,
    Electric,
    Fairy,
    Fighting,
    Fire,
    Flying,
    Ghost,
    Grass,
    Ground,
    Ice,
    Normal,
    Poison,
    Psychic,
    Rock,
    Steel,
    Water,
}
