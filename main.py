# Copy exceptions from: https://gitlab.com/Aegide/aegide.gitlab.io/-/blob/main/public/infiniteFusionData.js

# Mapping of non gen1-2 pokemon from natdex to infinite dex
id_list: dict[int, int] = {
    298: 252, 360: 253, 424: 254, 429: 255, 430: 256, 438: 257, 439: 258, 440: 259,
    446: 260, 458: 261, 461: 262, 462: 263, 463: 264, 464: 265, 465: 266, 466: 267, 467: 268, 468: 269,
    469: 270, 470: 271, 471: 272, 472: 273, 473: 274, 474: 275, 252: 276, 253: 277, 254: 278, 255: 279,
    256: 280, 257: 281, 258: 282, 259: 283, 260: 284, 280: 285, 281: 286, 282: 287, 475: 288, 292: 289,
    352: 290, 374: 291, 375: 292, 376: 293, 399: 294, 442: 295, 448: 296, 443: 297, 444: 298, 445: 299,
    303: 300, 345: 301, 346: 302, 347: 303, 348: 304, 408: 305, 409: 306, 410: 307, 411: 308, 289: 309,
    359: 310, 355: 311, 356: 312, 477: 313, 321: 314, 493: 315, 387: 316, 388: 317, 389: 318, 390: 319,
    391: 320, 392: 321, 393: 322, 394: 323, 395: 324, 299: 325, 476: 326, 679: 327, 680: 328, 681: 329,
    624: 330, 625: 331, 405: 332, 306: 333, 330: 334, 350: 335, 373: 336, 601: 337, 571: 338, 700: 339,
    382: 340, 383: 341, 384: 342, 483: 343, 484: 344, 487: 345, 486: 346, 491: 347, 649: 348, 643: 349,
    644: 350, 646: 351, 407: 352, 426: 353, 428: 354, 286: 355, 291: 356, 354: 357, 479: 358, 579: 359,
    547: 360, 553: 361, 563: 362, 596: 363, 598: 364, 607: 365, 608: 366, 609: 367, 612: 368, 623: 369,
    771: 370, 707: 371, 663: 372, 778: 373, 637: 374, 633: 375, 634: 376, 635: 377, 380: 378, 381: 379,
    386: 380, 385: 381, 290: 382, 400: 383, 447: 384, 287: 385, 288: 386, 320: 387, 403: 388, 404: 389,
    304: 390, 305: 391, 328: 392, 329: 393, 349: 394, 371: 395, 372: 396, 599: 397, 600: 398, 570: 399,
    406: 400, 315: 401, 425: 402, 427: 403, 285: 404, 353: 405, 577: 406, 578: 407, 546: 408, 551: 409,
    552: 410, 562: 411, 595: 412, 597: 413, 610: 414, 611: 415, 622: 416, 661: 417, 662: 418, 636: 419,
    618: 420,
    # Sableye
    302: 421,
    # Venipede
    543: 422,
    # Whirlipede
    544: 423,
    # Scolipede
    545: 424,
    # Tyrunt
    696: 425,
    # Tyrantrum
    697: 426,
    # Snorunt
    361: 427,
    # Glalie
    362: 428,
    # Froslass
    478: 429,
    # Oricorios
    # Get their own special rules because 1 pokemon with 4 forms split across 4 dex numbers
    # Trubbish
    568: 434,
    # Garbodor
    569: 435,
    # Carvanha
    318: 436,
    # Sharpedo
    319: 437,
    # Phantump
    708: 438,
    # Trevenant
    709: 439,
    # Noibat
    714: 440,
    # Noivern
    715: 441,
    # Swablu
    333: 442,
    # Altaria
    334: 443,
    # Goomy
    704: 444,
    # Sliggoo
    705: 445,
    # Goodra
    706: 446,
    # Regirock
    377: 447,
    # Regice
    378: 448,
    # Registeel,
    379: 449,
    # Necrozma
    800: 450,
    # Stufful
    759: 451,
    # Bewear
    760: 452,
    # Dhelmise
    781: 453,
    # Mareanie
    747: 454,
    # Toxapex
    748: 455,
    # Hawlucha
    701: 456,
    # Cacnea
    331: 457,
    # Cacturne
    332: 458,
    # Sandygast
    769: 459,
    # Palossand
    770: 460,
    # Amaura
    698: 461,
    # Aurorus
    699: 462
}

oricorio_baile = {
    "id": 430,
    "name": {
        "english": "Oricorio Baile",
        "japanese": "オドリドリ",
        "chinese": "花舞鸟",
        "french": "Plumeline"
    },
    "type": ["Fire", "Flying"],
    "base": {
        "HP": 75,
        "Attack": 70,
        "Defense": 70,
        "Sp. Attack": 98,
        "Sp. Defense": 70,
        "Speed": 93
    },
    "species": "Dancing Pokémon",
    "description": "This Oricorio has drunk red nectar. If its Trainer gives the wrong order, this passionate Pokémon becomes fiercely angry.",
    "evolution": {},
    "profile": {
        "height": "0.6 m",
        "weight": "3.4 kg",
        "egg": ["Flying"],
        "ability": [("Dancer", False)],
        "gender": "25:75"
    },
    "image": {
        "sprite": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/sprites/741.png",
        "thumbnail": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/thumbnails/741.png",
        "hires": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/hires/741.png"
    }
}

oricorio_pom_pom = {
    "id": 431,
    "name": {
        "english": "Oricorio Pom-Pom",
        "japanese": "オドリドリ",
        "chinese": "花舞鸟",
        "french": "Plumeline"
    },
    "type": ["Electric", "Flying"],
    "base": {
        "HP": 75,
        "Attack": 70,
        "Defense": 70,
        "Sp. Attack": 98,
        "Sp. Defense": 70,
        "Speed": 93
    },
    "species": "Dancing Pokémon",
    "description": "This Oricorio has drunk bright yellow nectar. When it sees someone looking glum, it will try to cheer them up with a dance.",
    "evolution": {},
    "profile": {
        "height": "0.6 m",
        "weight": "3.4 kg",
        "egg": ["Flying"],
        "ability": [("Dancer", False)],
        "gender": "25:75"
    },
    "image": {
        "sprite": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/sprites/741.png",
        "thumbnail": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/thumbnails/741.png",
        "hires": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/hires/741.png"
    }
}

oricorio_pau = {
    "id": 432,
    "name": {
        "english": "Oricorio Pau",
        "japanese": "オドリドリ",
        "chinese": "花舞鸟",
        "french": "Plumeline"
    },
    "type": ["Psychic", "Flying"],
    "base": {
        "HP": 75,
        "Attack": 70,
        "Defense": 70,
        "Sp. Attack": 98,
        "Sp. Defense": 70,
        "Speed": 93
    },
    "species": "Dancing Pokémon",
    "description": "This Oricorio has sipped pink nectar. It gets so caught up in its dancing that it sometimes doesn't hear its Trainer's orders.",
    "evolution": {},
    "profile": {
        "height": "0.6 m",
        "weight": "3.4 kg",
        "egg": ["Flying"],
        "ability": [("Dancer", False)],
        "gender": "25:75"
    },
    "image": {
        "sprite": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/sprites/741.png",
        "thumbnail": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/thumbnails/741.png",
        "hires": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/hires/741.png"
    }
}

oricorio_sensu = {
    "id": 432,
    "name": {
        "english": "Oricorio Sensu",
        "japanese": "オドリドリ",
        "chinese": "花舞鸟",
        "french": "Plumeline"
    },
    "type": ["Ghost", "Flying"],
    "base": {
        "HP": 75,
        "Attack": 70,
        "Defense": 70,
        "Sp. Attack": 98,
        "Sp. Defense": 70,
        "Speed": 93
    },
    "species": "Dancing Pokémon",
    "description": "This Oricorio has sipped purple nectar. Some dancers use its graceful, elegant dancing as inspiration.",
    "evolution": {},
    "profile": {
        "height": "0.6 m",
        "weight": "3.4 kg",
        "egg": ["Flying"],
        "ability": [("Dancer", False)],
        "gender": "25:75"
    },
    "image": {
        "sprite": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/sprites/741.png",
        "thumbnail": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/thumbnails/741.png",
        "hires": "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/hires/741.png"
    }
}


def main():
    import json
    from ability_overrides import AbilityOverrides
    from fusion_type_overrides import FusionTypeOverrides
    from type_overrides import TypeOverrides
    with open("pokedex.json", "r", encoding="utf8") as f:
        full_dex = json.load(f)

    infinite_dex = []
    ability_overrides = AbilityOverrides()
    type_overrides = TypeOverrides()
    fusion_type_overrides = FusionTypeOverrides()
    for pokemon in full_dex:
        if pokemon["id"] < 252 or pokemon["id"] in id_list.keys():
            # Modify abilities
            if pokemon["id"] in ability_overrides:
                pokemon["profile"]["ability"] = ability_overrides[pokemon["id"]]
            else:
                pokemon["profile"]["ability"] = fix_ability(pokemon["profile"]["ability"])

            # Modify types
            if pokemon["id"] in type_overrides:
                pokemon["type"] = type_overrides[pokemon["id"]]

            # Append info about the fusion type
            if pokemon["id"] in fusion_type_overrides:
                pokemon["fusion_type_override"] = fusion_type_overrides[pokemon["id"]]

            # Change the Natdex ID to the Infinite Dex ID
            if pokemon["id"] >= 252:
                pokemon["id"] = id_list[pokemon["id"]]
            infinite_dex.append(pokemon)

    infinite_dex.append(oricorio_sensu)
    infinite_dex.append(oricorio_pau)
    infinite_dex.append(oricorio_baile)
    infinite_dex.append(oricorio_pom_pom)

    infinite_dex.sort(reverse=False, key=lambda a: a["id"])
    with open("infinite_dex.json", "w", encoding="utf8") as f:
        json.dump(infinite_dex, f, indent=2, ensure_ascii=False)


# Just replaces the string "true"/"false" with an actual boolean value
def fix_ability(abilities: list[list]) -> list[tuple]:
    return [(ability[0], ability[1] == "true") for ability in abilities]


if __name__ == "__main__":
    main()
