import game_logic

# Converts a comma-separated string of color names or initials into a list of initials.
def convertUserColourInput(user_input: str):
    colour_map = game_logic.Game.getSettingsData("colours")
    name_to_initial = {name.lower(): initial for initial, name in colour_map.items()}
    
    raw_inputs = [c.strip().lower() for c in user_input.split(",")]
    converted_list = []

    for item in raw_inputs:
        initial = item.upper()
        if initial in colour_map:
            converted_list.append(initial)

        elif item in name_to_initial:
            converted_list.append(name_to_initial[item])
        else:
            print(f"ERROR in 'convertUserColourInput': '{item}' is not a valid colour.")
            return False
            
    return converted_list