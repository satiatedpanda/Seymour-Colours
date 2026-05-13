import json
from hexcodeClass import Hexcode
from seymourhelper import int_to_rgb


def get_piece_type_delta(delta_hex_name: str):
    armor_types = ["VELVET_TOP_HAT", "CASHMERE_JACKET", "SATIN_TROUSERS", "OXFORD_SHOES", "3p"]
    in_name_types = ["Helm", "Chestplate", "Leggings", "Boots", "3p"]
    types_in_current_delta = []
    for ptype in in_name_types:
        if ptype in delta_hex_name:
            types_in_current_delta.append(armor_types[in_name_types.index(ptype)])
    return types_in_current_delta, len(types_in_current_delta)

def assign(hexcode: Hexcode) -> dict[str, object]:
    sub_dict = {}
    hexcode.assign_all_attributes()
    delta_hex, delta_hex_name, piece_delta, abs_distance = hexcode.pdelta
    types_in_current_delta, types_delta_len = get_piece_type_delta(delta_hex_name)
    if len(types_in_current_delta) != 0:
        if "3p" in types_in_current_delta:
            name_append = "CASHMERE_JACKET+SATIN_TROUSERS+OXFORD_SHOES"
        else:
            name_append = "+".join(types_in_current_delta)
    else:
        name_append = "VELVET_TOP_HAT+CASHMERE_JACKET+SATIN_TROUSERS+OXFORD_SHOES"
    delta_sub_dict = {}
    closest_sub_sub_dict = {}
    closest_sub_sub_dict["delta_hex"] = delta_hex
    closest_sub_sub_dict["delta_hex_name"] = delta_hex_name
    closest_sub_sub_dict["delta"] = piece_delta
    closest_sub_sub_dict["abs_distance"] = abs_distance
    delta_sub_dict[name_append] = closest_sub_sub_dict

    if types_delta_len != 0:
        if types_in_current_delta[0] == "3p":
            h_delta_hex, h_delta_hex_name, h_piece_delta, h_abs_distance = hexcode.delta(hexcode.hexcode, "VELVET_TOP_HAT")
            closest_sub_sub_dict = {}
            closest_sub_sub_dict["delta_hex"] = h_delta_hex
            closest_sub_sub_dict["delta_hex_name"] = h_delta_hex_name
            closest_sub_sub_dict["delta"] = h_piece_delta
            closest_sub_sub_dict["abs_distance"] = h_abs_distance
            delta_sub_dict["VELVET_TOP_HAT"] = closest_sub_sub_dict
        else:
            armor_types = ["VELVET_TOP_HAT", "CASHMERE_JACKET", "SATIN_TROUSERS", "OXFORD_SHOES"]
            hypixel_hexes_in_dict = []
            while True:
                for typs in types_in_current_delta:
                    if typs in armor_types:
                        armor_types.remove(typs)
                if len(armor_types) == 0:
                    break
                for typs in armor_types[:]:
                    first_delta_hex, first_delta_hex_name, first_piece_delta, first_abs_distance = hexcode.delta(hexcode.hexcode, typs)
                    if first_delta_hex_name not in hypixel_hexes_in_dict:
                        closest_sub_sub_dict = {}
                        closest_sub_sub_dict["delta_hex"] = first_delta_hex
                        closest_sub_sub_dict["delta_hex_name"] = first_delta_hex_name
                        closest_sub_sub_dict["delta"] = first_piece_delta
                        closest_sub_sub_dict["abs_distance"] = first_abs_distance
                        delta_sub_dict[typs] = closest_sub_sub_dict
                        first_types, _ = get_piece_type_delta(first_delta_hex_name)
                        for typss in first_types:
                            if typss in armor_types:
                                armor_types.remove(typss)
                            if len(armor_types) == 0:
                                break
                        hypixel_hexes_in_dict.append(first_delta_hex_name)
                    else:
                        tst = list(delta_sub_dict.keys())
                        for piece_type in tst:
                            if delta_sub_dict[piece_type]["delta_hex_name"] == first_delta_hex_name:
                                value =  delta_sub_dict.pop(piece_type)
                                new_name = piece_type + f"+{typs}"
                                delta_sub_dict[new_name] = value
                break
    sorted_dict = dict(sorted(delta_sub_dict.items(), key=lambda item: item[1]["delta"]))

    sub_dict["delta"] = sorted_dict
    sub_dict["grayness"] = hexcode.grayness
    sub_dict["major_digits"] = hexcode.major_digits
    sub_dict["isPalendrome"] = hexcode.isPalendrome
    sub_dict["isPatternAxAxAx"] = hexcode.isPatternAxAxAx
    sub_dict["isPatternABCABC"] = hexcode.isPatternABCABC
    sub_dict["isPatternAABBCC"] = hexcode.isPatternAABBCC
    sub_dict["isThreextwo_nums"] = hexcode.isthreextwo_nums
    sub_dict["inCollectionRange"] = hexcode.inCollectionRange
    sub_dict["everything_else"] = hexcode.everthing_else
    sub_dict["num_same_digit"] = hexcode.num_same_digit

    return sub_dict

def all_hexcodes_json():
    MULTIPLIER = 16**5 # 16^5
    FILE_RANGE = 16
    TOTAL_NUMS = MULTIPLIER*FILE_RANGE
    print(MULTIPLIER)
    for file_number in range(FILE_RANGE):
        json_dict = {}
        lower_bound = file_number * MULTIPLIER
        upper_bound = (file_number+1) * MULTIPLIER
        for integer in range(lower_bound, upper_bound):
            current_hexcode = Hexcode(int_to_rgb(integer))
            sub_dict = assign(current_hexcode)
            json_dict[current_hexcode.hexcode] = sub_dict

            comparison_integer = integer - lower_bound
            if comparison_integer%5000 == 0:
                if comparison_integer == 0:
                    print(f"{file_number} started")
                num = comparison_integer + (file_number * MULTIPLIER)
                print(f"File {file_number}: {comparison_integer*100/MULTIPLIER:.3f}% - Whole Program: {num*100/(TOTAL_NUMS):.3f}%", end="\r")

        with open(f"hexes_list\\hexes_{file_number}.json", "w") as fd:
            json.dump(json_dict, fd, indent=4)
            print(f"\nwrote {file_number}")
        print(f"\n")
    print("\nProgram complete")

def jsonspliiter():
    for file_number in range(16):  
        col: dict = {}
        col_split_1 = {}
        col_split_2 = {}
        with open(f"hexes_list\\hexes_{file_number}.json", "r") as fd:
            col = json.load(fd)
        half_col_len = len(col)//2
        for integer, (hex, subdict) in enumerate(col.items()):
            if integer < half_col_len:
                col_split_1[hex] = subdict
            else:
                col_split_2[hex] = subdict         
        with open(f"hexes_list\\hexes_{file_number}.0.json", "w") as fd:
            json.dump(col_split_1, fd, indent=4)
            print(f"\nwrote {file_number}.0")
        with open(f"hexes_list\\hexes_{file_number}.8.json", "w") as fs:
            json.dump(col_split_2, fs, indent=4)
            print(f"\nwrote {file_number}.8")            

def worst_delta():
    worst_helm: dict = {}
    worst_chest: dict = {}
    worst_legs: dict = {}
    worst_boots: dict = {}   
    for file_number in range(16):  
        for sub_file_number in range(0, 9, 8):
            col: dict = {}
            with open(f"hexes_list\\hexes_{file_number}.{sub_file_number}.json", "r") as fd:
                col = json.load(fd)
            for idx, rgbhex in enumerate(col.keys()):
                delta_dict: dict = col[rgbhex]["delta"]
                for unique_deltas, sub_dicts in delta_dict.items():
                    if "VELVET_TOP_HAT" in unique_deltas:
                        if len(worst_helm) == 0:
                            sub_dicts["hex"] = rgbhex
                            worst_helm = sub_dicts
                        else:
                            if worst_helm["delta"] < sub_dicts["delta"]:
                                sub_dicts["hex"] = rgbhex
                                worst_helm = sub_dicts
                    if "CASHMERE_JACKET" in unique_deltas:
                        if len(worst_chest) == 0:
                            sub_dicts["hex"] = rgbhex
                            worst_chest = sub_dicts
                        else:
                            if worst_chest["delta"] < sub_dicts["delta"]:
                                sub_dicts["hex"] = rgbhex
                                worst_chest = sub_dicts
                    if "SATIN_TROUSERS" in unique_deltas:
                        if len(worst_legs) == 0:
                            sub_dicts["hex"] = rgbhex
                            worst_legs = sub_dicts
                        else:
                            if worst_legs["delta"] < sub_dicts["delta"]:
                                sub_dicts["hex"] = rgbhex
                                worst_legs = sub_dicts
                    if "OXFORD_SHOES" in unique_deltas:
                        if len(worst_boots) == 0:
                            sub_dicts["hex"] = rgbhex
                            worst_boots = sub_dicts
                        else:
                            if worst_boots["delta"] < sub_dicts["delta"]:
                                sub_dicts["hex"] = rgbhex
                                worst_boots = sub_dicts           
            print(f"{file_number}.{sub_file_number} done")                                                                     

    for key, val in worst_helm.items():
        print(f"{key}: {val}")
    for key, val in worst_chest.items():
        print(f"{key}: {val}")
    for key, val in worst_legs.items():
        print(f"{key}: {val}")
    for key, val in worst_boots.items():
        print(f"{key}: {val}")                  

def highest_abs():
    worst_helm: dict = {}
    worst_chest: dict = {}
    worst_legs: dict = {}
    worst_boots: dict = {}   
    for file_number in range(16):  
        for sub_file_number in range(0, 9, 8):
            col: dict = {}
            with open(f"hexes_list\\hexes_{file_number}.{sub_file_number}.json", "r") as fd:
                col = json.load(fd)
            for idx, rgbhex in enumerate(col.keys()):
                delta_dict: dict = col[rgbhex]["delta"]
                for unique_deltas, sub_dicts in delta_dict.items():
                    if "VELVET_TOP_HAT" in unique_deltas:
                        if len(worst_helm) == 0:
                            sub_dicts["hex"] = rgbhex
                            worst_helm = sub_dicts
                        else:
                            if worst_helm["abs_distance"] < sub_dicts["abs_distance"]:
                                sub_dicts["hex"] = rgbhex
                                worst_helm = sub_dicts
                    if "CASHMERE_JACKET" in unique_deltas:
                        if len(worst_chest) == 0:
                            sub_dicts["hex"] = rgbhex
                            worst_chest = sub_dicts
                        else:
                            if worst_chest["abs_distance"] < sub_dicts["abs_distance"]:
                                sub_dicts["hex"] = rgbhex
                                worst_chest = sub_dicts
                    if "SATIN_TROUSERS" in unique_deltas:
                        if len(worst_legs) == 0:
                            sub_dicts["hex"] = rgbhex
                            worst_legs = sub_dicts
                        else:
                            if worst_legs["abs_distance"] < sub_dicts["abs_distance"]:
                                sub_dicts["hex"] = rgbhex
                                worst_legs = sub_dicts
                    if "OXFORD_SHOES" in unique_deltas:
                        if len(worst_boots) == 0:
                            sub_dicts["hex"] = rgbhex
                            worst_boots = sub_dicts
                        else:
                            if worst_boots["abs_distance"] < sub_dicts["abs_distance"]:
                                sub_dicts["hex"] = rgbhex
                                worst_boots = sub_dicts           
            print(f"{file_number}.{sub_file_number} done")                                                                     

    for key, val in worst_helm.items():
        print(f"{key}: {val}")
    for key, val in worst_chest.items():
        print(f"{key}: {val}")
    for key, val in worst_legs.items():
        print(f"{key}: {val}")
    for key, val in worst_boots.items():
        print(f"{key}: {val}")                  


if __name__ == "__main__":
    highest_abs()

