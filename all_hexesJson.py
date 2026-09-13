import json
from hexcodeClass import Hexcode
from seymourhelper import int_to_rgb, rgbdecouple, Hypixel_Dictionary, avgabsSet, CIEVals
from collections import Counter
# import pandas


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
            hexcode.piecetype = "VELVET_TOP_HAT"
            h_delta_hex, h_delta_hex_name, h_piece_delta, h_abs_distance = hexcode.delta()
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
                    hexcode.piecetype = typs
                    first_delta_hex, first_delta_hex_name, first_piece_delta, first_abs_distance = hexcode.delta()
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
    print("This will modify existing hexes list database. \nAre you sure you want to continue? (Y/n)")
    cnt = 0
    while True:
        warning_answer = input("-> ")
        if warning_answer == "Y":
            break
        if warning_answer == "n" or cnt > 1:
            print("exiting program...")
            exit()
        print("Invalid answer.\nContinue? (Y/n)")
        cnt += 1
    MULTIPLIER = 16**5 # 16^5
    FILE_RANGE = 16
    TOTAL_NUMS = MULTIPLIER*FILE_RANGE
    print(MULTIPLIER)
    for file_number in range(FILE_RANGE):
        json_dict = {}
        lower_bound = file_number * MULTIPLIER
        upper_bound = (file_number+1) * MULTIPLIER
        half = ((upper_bound-lower_bound)//2) + lower_bound - 1
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
            
            if integer == half:
                with open(f"hexes_list\\hexes_{file_number}.0.json", "w") as fd:
                    json.dump(json_dict, fd, indent=4)
                    print(f"\nwrote {file_number}.0")
                json_dict.clear() 

        with open(f"hexes_list\\hexes_{file_number}.8.json", "w") as fd:
            json.dump(json_dict, fd, indent=4)
            print(f"\nwrote {file_number}.8")
        print(f"\n")
    print("\nProgram complete")

# def jsonsplititer():
#     for file_number in range(16):  
#         col: dict = {}
#         col_split_1 = {}
#         col_split_2 = {}
#         with open(f"hexes_list\\hexes_{file_number}.json", "r") as fd:
#             col = json.load(fd)
#         half_col_len = len(col)//2
#         for integer, (hex, subdict) in enumerate(col.items()):
#             if integer < half_col_len:
#                 col_split_1[hex] = subdict
#             else:
#                 col_split_2[hex] = subdict         
#         with open(f"hexes_list\\hexes_{file_number}.0.json", "w") as fd:
#             json.dump(col_split_1, fd, indent=4)
#             print(f"\nwrote {file_number}.0")
#         with open(f"hexes_list\\hexes_{file_number}.8.json", "w") as fs:
#             json.dump(col_split_2, fs, indent=4)
#             print(f"\nwrote {file_number}.8")            

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

def all_teirs():
    nums = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

    RANGE_FILES = 16
    LOWER = 0
    for file_number in range(LOWER,RANGE_FILES+LOWER):  
        for sub_file_number in range(0, 9, 8):
            col: dict = {}
            with open(f"hexes_list\\hexes_{file_number}.{sub_file_number}.json", "r") as fd:
                col = json.load(fd)
            for idx, rgbhex in enumerate(col.keys()):
                delta_dict: dict = col[rgbhex]["delta"]
                for unique_deltas, sub_dicts in delta_dict.items():
                    if "VELVET_TOP_HAT" in unique_deltas:
                        if sub_dicts["delta"] < 2.000:
                            nums[0][0] += 1
                        elif sub_dicts["delta"] < 5.000:
                            nums[0][1] += 1
                        else:
                            nums[0][2] += 1                            
                    if "CASHMERE_JACKET" in unique_deltas:
                        if sub_dicts["delta"] < 2.000:
                            nums[1][0] += 1
                        elif sub_dicts["delta"] < 5.000:
                            nums[1][1] += 1
                        else:
                            nums[1][2] += 1   

                    if "SATIN_TROUSERS" in unique_deltas:
                        if sub_dicts["delta"] < 2.000:
                            nums[2][0] += 1
                        elif sub_dicts["delta"] < 5.000:
                            nums[2][1] += 1
                        else:
                            nums[2][2] += 1                              
                    if "OXFORD_SHOES" in unique_deltas:
                        if sub_dicts["delta"] < 2.000:
                            nums[3][0] += 1
                        elif sub_dicts["delta"] < 5.000:
                            nums[3][1] += 1
                        else:
                            nums[3][2] += 1                             

            print(f"{file_number}.{sub_file_number} done")                                                                     

    print(nums)
    for i in nums:
        print(i, sum(i))
        for idx, tier in enumerate(i):
            print(f"{idx+1}: {tier}       -     probability: {(100*tier)/(RANGE_FILES*1048576):.3f}%")

def all_abs():
    nums = [[],[],[],[]]

    RANGE_FILES = 16
    LOWER = 0
    for file_number in range(LOWER,RANGE_FILES+LOWER):  
        for sub_file_number in range(0, 9, 8):
            col: dict = {}
            with open(f"hexes_list\\hexes_{file_number}.{sub_file_number}.json", "r") as fd:
                col = json.load(fd)
            for idx, rgbhex in enumerate(col.keys()):
                delta_dict: dict = col[rgbhex]["delta"]
                for unique_deltas, sub_dicts in delta_dict.items():
                    if "VELVET_TOP_HAT" in unique_deltas:
                        nums[0].append(sub_dicts["abs_distance"])
                    if "CASHMERE_JACKET" in unique_deltas:
                        nums[1].append(sub_dicts["abs_distance"])  
                    if "SATIN_TROUSERS" in unique_deltas:
                        nums[2].append(sub_dicts["abs_distance"])                       
                    if "OXFORD_SHOES" in unique_deltas:
                        nums[3].append(sub_dicts["abs_distance"])                           

            print(f"{file_number}.{sub_file_number} done")                                                                     

    H = ["helm", "chest", "legs", "boots"]
    for dix, i in enumerate(nums):
        i = Counter(i)
        i = sorted(i.items())
        print(H[dix])
        for j in i:
            key, value = j
            print(f"{key}: {value}")
        
        print("\n\n\n")


def max_abs():
    print_lst = []
    RANGE_FILES = 16
    LOWER = 0
    for file_number in range(LOWER,RANGE_FILES+LOWER):  
        for sub_file_number in range(0, 9, 8):
            col: dict = {}
            with open(f"hexes_list\\hexes_{file_number}.{sub_file_number}.json", "r") as fd:
                col = json.load(fd)
            for idx, rgbhex in enumerate(col.keys()):
                delta_dict: dict = col[rgbhex]["delta"]
                for unique_deltas, sub_dicts in delta_dict.items():
                    hex_name =  sub_dicts["delta_hex_name"]
                    abs_dist = sub_dicts["abs_distance"]
                    deltas = sub_dicts["delta"]
                    deltas = f"{deltas:.3f}"
                    if "VELVET_TOP_HAT" in unique_deltas and abs_dist == 310:
                        print_lst.append(f"helm: {rgbhex} - {hex_name} - {deltas} - {abs_dist}")
                    if "CASHMERE_JACKET" in unique_deltas and abs_dist == 260:
                        print_lst.append(f"chest: {rgbhex} - {hex_name} - {deltas} - {abs_dist}")
                    if "SATIN_TROUSERS" in unique_deltas and abs_dist == 236:
                        print_lst.append(f"legs: {rgbhex} - {hex_name} - {deltas} - {abs_dist}")
                    if "OXFORD_SHOES" in unique_deltas and abs_dist == 254:
                        print_lst.append(f"boots: {rgbhex} - {hex_name} - {deltas} - {abs_dist}")                      

            print(f"{file_number}.{sub_file_number} done")                                                                     

    for i in print_lst:
        print(i)

def optimizedpossibilites(target_hexcode="FFFFFF"):
    num_t0 = 0
    num_t1 = 0
    num_t2 = 0
    r: int
    g: int
    b: int
    max_variance = 80
    delta_dict: dict[str, float] = {}

    r, g, b = rgbdecouple(target_hexcode)
    cieT = CIEVals(target_hexcode).cie
    cieTARG = ("target", cieT[0], cieT[1], cieT[2])
    red_lower, red_upper = (max(0, r-max_variance), min(256, r+max_variance)) #lower bound, upper bound
    green_lower, green_upper = (max(0, g-max_variance), min(256, g+max_variance))
    blue_lower, blue_upper = (max(0, b-max_variance), min(256, b+max_variance))
    print(f"Total Hexes to search: {(red_upper-red_lower)*(green_upper-green_lower)*(blue_upper-blue_lower)}", end="\r")
    for red_val in range(red_lower, red_upper):
        for green_val in range(green_lower, green_upper):
            for blue_val in range(blue_lower, blue_upper):
                if (abs(red_val-r)+abs(blue_val-b)+abs(green_val-g)) > 135:
                    continue                      
                hexcode = Hexcode(int_to_rgb(red_val * 65536 + green_val * 256 + blue_val))          
                # _, _, delta, _ = hexcode.delta({f"{target_hexcode}": "target"})
                _, _, delta, _ = hexcode.fastdelta({f"{target_hexcode}": cieTARG})                
                if delta < 1.0:
                    num_t0 += 1
                if delta < 2.0:
                    num_t1 += 1
                    delta_dict[hexcode.hexcode] = delta
                elif delta < 5.0:
                    num_t2 += 1
                    delta_dict[hexcode.hexcode] = delta
    print("                                                  ", end="\r")
    user_input = input("type 'Y' for list of hexes, sorted by delta\n")
    # user_input = ""
    if "Y" in user_input:
        print(f"-----\n{target_hexcode} - t1: {num_t1}, t2: {num_t2}-----\n")
        delta_dict = dict(sorted(delta_dict.items(), key=lambda item: item[1]))
        for k, v in delta_dict.items():
            print(f"{k} - {v}")
    else:
        print(f"#{target_hexcode}, {num_t0}, {num_t1}, {num_t2}")

def findtargethex(comparison_hex: str, input_delta: str):
    #Finds the target hex if youre only given a delta and 1 hexcode. Needs 4-5 decimal places for precision
    #Delta must be below 5
    r: int
    g: int
    b: int
    max_variance = 80
    delta_dict: dict[str, float] = {}
    final_dict = {}

    r, g, b = rgbdecouple(comparison_hex)
    cieT = CIEVals(comparison_hex).cie
    cieTARG = ("target", cieT[0], cieT[1], cieT[2])
    red_lower, red_upper = (max(0, r-max_variance), min(256, r+max_variance)) #lower bound, upper bound
    green_lower, green_upper = (max(0, g-max_variance), min(256, g+max_variance))
    blue_lower, blue_upper = (max(0, b-max_variance), min(256, b+max_variance))
    print(f"Total Hexes to search: {(red_upper-red_lower)*(green_upper-green_lower)*(blue_upper-blue_lower)}", end="\r")
    for red_val in range(red_lower, red_upper):
        for green_val in range(green_lower, green_upper):
            for blue_val in range(blue_lower, blue_upper):
                if (abs(red_val-r)+abs(blue_val-b)+abs(green_val-g)) > 105:
                    continue             
                temp_hex = int_to_rgb(red_val * 65536 + green_val * 256 + blue_val)         
                hexcode = Hexcode(temp_hex)                         
                _, _, delta, _ = hexcode.fastdelta({f"{comparison_hex}": cieTARG})                
                if delta < 5.0:
                    delta_dict[temp_hex] = delta
    print("                                                  ", end="\r")
    delta_dict = dict(sorted(delta_dict.items(), key=lambda item: abs(item[1]-float(input_delta))))
    sig_figs = len(input_delta)-1
    if input_delta[-1] != "0":
        for k, v in delta_dict.items():
            t = str(v)[:sig_figs]
            if t == input_delta[:-1]:
                final_dict[k] = v
    else:
        sig_figs = len(input_delta.rstrip("0"))-1
        for k, v in delta_dict.items():
            t = str(v)[:sig_figs]
            s = input_delta[:sig_figs]
            if t == s:
                final_dict[k] = v        
    print_lst = ["Best Guess", "2nd", "3rd", "4th", "5th"]
    for idx, (k, v) in enumerate(final_dict.items()):
        if idx < 5:
            print(f"{print_lst[idx]}: {k} - {v}")
        else:
            break

def optimizedposALL():
    dictonary = Hypixel_Dictionary()
    for Hyhex, HYhex_name in dictonary.items():
        num_t0 = 0
        num_t1 = 0
        num_t2 = 0
        r: int
        g: int
        b: int
        max_variance = 80

        r, g, b = rgbdecouple(Hyhex)
        cieT = CIEVals(Hyhex).cie
        cieTARG = ("target", cieT[0], cieT[1], cieT[2])
        red_lower, red_upper = (max(0, r-max_variance), min(256, r+max_variance)) #lower bound, upper bound
        green_lower, green_upper = (max(0, g-max_variance), min(256, g+max_variance))
        blue_lower, blue_upper = (max(0, b-max_variance), min(256, b+max_variance))
        print(f"Total Hexes to search: {(red_upper-red_lower)*(green_upper-green_lower)*(blue_upper-blue_lower)}", end="\r")
        for red_val in range(red_lower, red_upper):
            for green_val in range(green_lower, green_upper):
                for blue_val in range(blue_lower, blue_upper):
                    if (abs(red_val-r)+abs(blue_val-b)+abs(green_val-g)) > 105:
                        continue                      
                    hexcode = Hexcode(int_to_rgb(red_val * 65536 + green_val * 256 + blue_val))          
                    # _, _, delta, _ = hexcode.delta({f"{target_hexcode}": "target"})
                    _, _, delta, _ = hexcode.fastdelta({f"{Hyhex}": cieTARG})                
                    if delta < 1.0:
                        num_t0 += 1
                    if delta < 2.0:
                        num_t1 += 1
                    elif delta < 5.0:
                        num_t2 += 1
        print("                                                  ", end="\r")
        print(f"{HYhex_name}, {Hyhex}, t0: {num_t0}, t1: {num_t1}, t2: {num_t2}")

  

if __name__ == "__main__":
    # all_abs()
    # all_hexcodes_json()
    #all_teirs()
    #worst_delta()
    # highest_abs()
    # max_abs()
    # optimizedpossibilites("#FF700A")
    # findtargethex("#b266ff", "1.999")
    # optimizedposALL() 
    optimizedpossibilites("00ee00")
    # optimizedpossibilites("169F57")
    # optimizedpossibilites("82E3D8")
    # optimizedpossibilites("2AB5A5")
    # optimizedpossibilites("D579FF")
    # optimizedpossibilites("6E00A0")
    # optimizedpossibilites("BB0000")
    # optimizedpossibilites("FF4242")
    # optimizedpossibilites("FFC234")
    # optimizedpossibilites("FFF7E6")