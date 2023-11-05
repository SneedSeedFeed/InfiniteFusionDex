import re;
import os;
from pathlib import Path;

def main():
    # This query checks whether the file meets the right format
    query = re.compile(r"[0-9]{1,3}\.[0-9]{1,3}[a-z]{0,1}\.png")
    # Get all sprites
    sprites = os.listdir("CustomBattlers")
    # Did we find any bad ones, we gotta early exit to protect from crappy code that will crash when we don't have the right format
    found_bad = False
    for sprite in sprites:
        if len(re.findall(query, sprite)) == 0:
            found_bad = True
            print(sprite)
    if found_bad:
        exit("Found sprites that don't meet format, exiting as they need to be fixed before continuing.")

    # Sort sprites by head number, then by body number, then by variant letter
    sprites = sorted(sprites, key=lambda sprite: (int(sprite.split(".")[0]), int(strip_letters(sprite.split(".")[1])), tertiary_condition(sprite.split(".")[1][-1])))
    sprite_dict = {}
    # Group variants by head and body number
    for sprite in sprites:
        first_num = sprite.split(".")[0]
        second_num = strip_letters(sprite.split(".")[1])
        if (first_num, second_num) not in sprite_dict:
            sprite_dict[(first_num, second_num)] = [sprite]
        else:
            sprite_dict[(first_num, second_num)].append(sprite)

    bad_sprites = []
    # Check if the variants are in the right order
    for variants in sprite_dict.values():
        for index, sprite in enumerate(variants):
            if index == 0:
                # First sprite is checked against None as there's no previous sprite
                if not is_valid_variant(None, sprite):
                    bad_sprites.append((None, sprite, correct_name(None, sprite)))
                    cur_sprite_path = Path("CustomBattlers", sprite)
                    new_sprite_path = Path("CustomBattlers", correct_name(None, sprite))
                    cur_sprite_path.rename(new_sprite_path)
            else:
                if not is_valid_variant(variants[index-1], sprite):
                    bad_sprites.append((variants[index-1], sprite, correct_name(variants[index-1], sprite)))
                    
                    cur_sprite_path = Path("CustomBattlers", sprite)
                    new_sprite_path = Path("CustomBattlers", correct_name(variants[index-1], sprite))
                    cur_sprite_path.rename(new_sprite_path)
    
    with open("sprite_errors.txt", "w") as f:
        blank = "NONE"
        for bad_sprite in bad_sprites:
            if bad_sprite[0] is None:
                f.write(f"{blank:<12}|{bad_sprite[1]:<12}|{bad_sprite[2]:<12}\n")
            else:
                f.write(f"{bad_sprite[0]:<12}|{bad_sprite[1]:<12}|{bad_sprite[2]:<12}\n")
        
    

def strip_letters(snippet: str) -> str:
    letters = "abcdefghijklmnopqrstuvwxyz"
    snippet = snippet.rstrip(letters)
    return snippet

def tertiary_condition(last_char: str) -> int:
    # Gets the ascii value of the last character, if it's a number, it's 0, otherwise it's the ascii value
    if last_char.isnumeric():
        return 0
    else:
        return ord(last_char)
    
def is_valid_variant(prev_sprite: str | None, cur_sprite: str) -> bool:
    # We use .isdigit on the last character of the body to check if it's the first variant
    if prev_sprite is None:
        # If the previous sprite is None, we're on the first sprite, so we just check to make sure the last character of the body is a number
        return cur_sprite[-5].isdigit()
    else:
        # If it's A and the previous sprite is the first variant it's all good
        if prev_sprite[-5].isdigit() and cur_sprite[-5] == "a":
            return True
        elif prev_sprite[-5].isdigit() and cur_sprite[-5] != "a":
            # Not A then bad
            return False
        letters = ["a","b","c","d","e","f","g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r","s","t","u","v","w","x","y","z"]
        # Gets the letter after the previous sprite's variant letter
        correct_letter = letters[letters.index(prev_sprite[-5])+1]
        # If the current sprite's variant letter isn't the correct one, it's bad
        if cur_sprite[-5] != correct_letter:
            return False
        else:
            return True
        
def correct_name(prev_sprite: str | None, cur_sprite:str) -> str:
    get_numbers = re.compile(r"[0-9]{1,3}\.[0-9]{1,3}")
    # If it's meant to be the first sprite we just pull the numbers and add .png
    if prev_sprite is None:
        cur_sprite = get_numbers.findall(cur_sprite)[0]
        return f"{cur_sprite}.png"
    # if it ends with a.png we just remove the a since it's meant to be the first sprite
    if cur_sprite.endswith("a.png"):
        return cur_sprite.replace("a.png", ".png")
    else:
        letters = ["a","b","c","d","e","f","g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r","s","t","u","v","w","x","y","z"]
        try:
            # Gets the letter after the previous sprite's variant letter
            new_letter = letters[letters.index(prev_sprite[-5])+1]
            cur_sprite = get_numbers.findall(cur_sprite)[0]
            # Appends it to the end of head.body
            return f"{cur_sprite}{new_letter}.png"
        except ValueError:
            # ValueError means the previous sprite was the first variant so we just have to chuck an a on the end
            cur_sprite = get_numbers.findall(cur_sprite)[0]
            return f"{cur_sprite}a.png"

    


if __name__ == "__main__":
    main()