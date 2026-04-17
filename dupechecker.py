import math
from seymourhelper import delta

data_dict = {}
dupe_dict = {}
negated_dupe_dict = {}
formated_dupe_list = []

#gets all dupes
with open("seymourdatabase.txt", "r") as fd:
    database = fd.read().split("\n")
    database.pop()
    for string in database:
        str_list = string.split()
        if str_list[1] in data_dict:
            y= ["VELVET_TOP_HAT", "CASHMERE_JACKET", "SATIN_TROUSERS", "OXFORD_SHOES"]
            pieces_in_dict = ["Helm", "Chestplate", "Leggings", "Boots"]
            removed_pieces = []
            data_dict[str_list[1]].append(str_list[0])
            z=sorted(data_dict[str_list[1]], key=y.index)
            # name_str = "dupe" + str(len(dupe_dict)+1)
            piece_str = ""
            negated_piece_str = ""
            for idx,val in enumerate(z):
                piecetype = pieces_in_dict[y.index(val)]
                if piecetype in piece_str:
                    if y.index(val) < 2:
                        piece_str = piece_str.replace(piecetype, f"dupe {piecetype}s")
                    else:
                        piece_str = piece_str.replace(piecetype, f"dupe {piecetype}")
                else:
                    if idx == 0:
                        piece_str = piece_str + f"{piecetype}"
                    else:
                        piece_str = piece_str + "+" + piecetype
            for i in range(len(pieces_in_dict)-1,-1,-1):
                if pieces_in_dict[i] in piece_str:
                    removed_pieces.append(pieces_in_dict.pop(i))
            negated_piece_str = "+".join(pieces_in_dict)
            piece_str = piece_str.replace("Helm", "H").replace("Chestplate", "C").replace("Leggings", "L").replace("Boots", "B").replace("+","").replace("Hs", "H")
            # dupe_dict[str_list[1]] = name_str+", "+piece_str
            dupe_dict[str_list[1]] = piece_str
            # negated_dupe_dict[str_list[1]] = "negated"+name_str+" "+negated_piece_str
            negated_dupe_dict[str_list[1]] = "negated"+negated_piece_str            
            current_dupe_pieces_formating = []
            temp_dict = {str_list[1]: ["","","",""]}
            for value in removed_pieces:
                pieces_copy = ["Helm", "Chestplate", "Leggings", "Boots"]
                value_index = pieces_copy.index(value)
                temp_dict[str_list[1]][value_index] = str_list[1]
            formated_dupe_list.append(temp_dict)
        else:
            data_dict[str_list[1]] = [str_list[0]]

dupe_t1s = []
#gets all t1s to dupes
for hex,piece in data_dict.items():
    deltaScore = 1000.0
    low_hex = ""
    low_hex, unsed1, deltaScore, unsed2 = delta(hex[1:],piece[0],negated_dupe_dict)
    if deltaScore > 2.00:
        continue
    else:
        dupe_t1s.append([hex, piece[0], low_hex, deltaScore])

final_list = []
current_t1_comparison = ""
current_piece_type = ""
current_delta = 1000

for dupe in formated_dupe_list:
    lowest_scores: list[list[str,int]] = [10,10,10,10]

    cur_dupe_items = list(dupe.items())[0]
    for i in range(len(dupe_t1s)-1,-1,-1):
        y= ["VELVET_TOP_HAT", "CASHMERE_JACKET", "SATIN_TROUSERS", "OXFORD_SHOES"]
        if cur_dupe_items[0] == dupe_t1s[i][2]:
            current_piece_type = dupe_t1s[i][1]
            current_t1_hex = dupe_t1s[i][0]
            current_delta = dupe_t1s[i][3]
            current_t1_comparison = dupe_t1s[i][2]
            piece_index = y.index(current_piece_type)
            if len(cur_dupe_items[1][piece_index]) == 0:
                cur_dupe_items[1][piece_index] = current_t1_hex
                lowest_scores[piece_index] = current_delta
            else:
                if current_delta < lowest_scores[piece_index]:
                    lowest_scores[piece_index] = current_delta
                    cur_dupe_items[1][piece_index] = current_t1_hex
    final_list.append(cur_dupe_items[1])

print_list = []
for idx,(hex,pieces) in enumerate(dupe_dict.items()):
    printstr = ""
    completeness = 0
    for value in final_list[idx]:
        if len(value) == 0:
            printstr = printstr + "-,"
        else:
            printstr = printstr + f" {value},"
            completeness += 1
    printstr = printstr[:-1]
    pieces: str
    if len(pieces) == 6:
        pieces = pieces.replace("dupe H", "Dupe Helms").replace("dupe C", "Dupe Chestplates").replace("dupe L", "Dupe Legs").replace('dupe B', "Dupe Boots")
    else:
        pieces = pieces.replace("dupe H", "Dupe Helms|").replace("dupe B", "|Dupe Boots")
        if pieces.find("dupe") != 0:
            pieces = pieces.replace("dupe C", "|Dupe Chestplates").replace("dupe L", "|Dupe Legs")
        else:
            pieces = pieces.replace("dupe C", "Dupe Chestplates|").replace("dupe L", "Dupe Legs|")
    print_list.append(f"{hex}, {pieces}, {completeness}/4, {printstr}")
    
with open("dupedatabase.txt", "w") as fs:
    dbstr = ""
    for i in range(len(print_list)):
        dbstr = f"{dbstr}{print_list[i]}\n".upper()
    fs.write(dbstr)


if __name__ == "__main__":
    pass