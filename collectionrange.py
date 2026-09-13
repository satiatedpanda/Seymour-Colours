from hexcodeClass import Hexcode, DatabaseToHex
from seymourhelper import rgbDist

def is_special(silksong: Hexcode) -> int: 
    value = 0
    if silksong.num_same_digit > 3:
        value = 1
        if "True" in silksong.everthing_else:
            value = 6
            return value
    if silksong.isPatternAABBCC or silksong.isPatternABCABC:
        value = 4
        return value
    if silksong.isPalendrome:
        value = 6
        return value
    if silksong.grayness == "0.000":
        value = 10
        return value
    return value

def rank(delta) -> int:
    tier = 3
    if delta < 5.000:
        tier = 2
    if delta < 2.000:
        tier = 1
    if delta < 1.000:
        tier = 0
    if delta == 0.000:
        tier = -1
    return tier

database = DatabaseToHex()
collection_range_database: list[Hexcode] = []
for temphex in database:
    temphex.assign_all_attributes()
    if temphex.inCollectionRange:
        collection_range_database.append(temphex)
del database
del temphex
collection_range_database.sort(key=lambda x: x.major_digits)
current = ""
idx = 0
temp_list = []
data: dict[str, list[Hexcode]] = {}

for inex, i in enumerate(collection_range_database):
    if current == i.major_digits:
        temp_list.append(i)
        if inex == len(collection_range_database)-1:
            data[current] = temp_list
        continue
    elif current == "":
        current = i.major_digits
        temp_list.append(i)
        continue 
    tp = temp_list[:]
    data[current] = tp
    temp_list.clear()
    current = i.major_digits
    temp_list.append(i)


del current, tp, i, inex, idx, temp_list, collection_range_database
# {major_digit: list[Hexcode]}

# priority - t1 <- t2 <- good set
# coolness priority -- perfect gray <
# if multiple t1/t2, take lowest delta
# make best set out of above criteria
final_hexcodes: dict[str, list[Hexcode]] = {}
for major, pieces  in data.items():
    lowest_pieces = [None, None, None, None]
    comparison = ["VELVET_TOP_HAT", "CASHMERE_JACKET", "SATIN_TROUSERS", "OXFORD_SHOES"]
    for piece in pieces: #Gets best t2s and t1s
        sp = is_special(piece)
        current_delta = piece.pdelta[2]
        if (current_delta < 5.000) or (sp > 0):
            piece_idx = comparison.index(piece.piecetype)
            if lowest_pieces[piece_idx] is None:
                lowest_pieces[piece_idx] = piece
                continue
            ps = is_special(lowest_pieces[piece_idx])
            comparison_delta = lowest_pieces[piece_idx].pdelta[2]
            if current_delta < comparison_delta: #checks for lower deltas
                if (ps > sp) : # checks for special pieces
                    cur_tier = rank(current_delta)
                    comparison_tier = rank(comparison_delta)
                    if cur_tier < comparison_tier: #replaces if old special piece is higher tier
                        lowest_pieces[piece_idx] = piece
                    continue #else keeps old special piece
                lowest_pieces[piece_idx] = piece 
                continue
            if sp > ps: #delta will always be higher, but below 5
                cur_tier = rank(current_delta)
                comparison_tier = rank(comparison_delta)
                if cur_tier == comparison_tier:
                    lowest_pieces[piece_idx] = piece                

    leftovers: list[Hexcode] = []
    for piece in pieces: #finds all leftover t3s
        piece_idx = comparison.index(piece.piecetype)
        if lowest_pieces[piece_idx] is not None:
            continue
        leftovers.append(piece)
    if len(leftovers) != 0:
        #sorts and splits by piece type
        leftovers.sort(key=lambda x: x.piecetype)
        current = ""
        splt_idx = 0
        final_leftovers: list[list[Hexcode]] = []
        for idx, p in enumerate(leftovers):
            if idx == 0:
                current = p.piecetype
                continue
            if current != p.piecetype:
                final_leftovers.append(leftovers[splt_idx:idx])
                splt_idx = idx
                current = p.piecetype
        final_leftovers.append(leftovers[splt_idx:])

        lef_len = len(final_leftovers)
        lowest_delta = 100000
        best_pieces: list[Hexcode] = []
        only_pieces: list[Hexcode] = list(value for value in lowest_pieces if value is not None)
        if lef_len == 1:
            for piece in final_leftovers[0]:
                temp_delta = rgbDist(piece.hexcode, only_pieces[0].hexcode, only_pieces[1].hexcode, only_pieces[2].hexcode)
                if temp_delta < lowest_delta:
                    lowest_delta = temp_delta
                    best_pieces = [piece]
        elif lef_len == 2:
            for piece in final_leftovers[0]:
                for eciep in final_leftovers[1]:
                    temp_delta = rgbDist(piece.hexcode, eciep.hexcode, only_pieces[0].hexcode, only_pieces[1].hexcode)
                    if temp_delta < lowest_delta:
                        lowest_delta = temp_delta
                        best_pieces = [piece, eciep]
        elif lef_len == 3:
            for piece in final_leftovers[0]:
                for eciep in final_leftovers[1]:
                    for ec in final_leftovers[2]:
                        temp_delta = rgbDist(piece.hexcode, eciep.hexcode, ec.hexcode, only_pieces[0].hexcode)
                        if temp_delta < lowest_delta:
                            lowest_delta = temp_delta
                            best_pieces = [piece, eciep, ec]
        elif lef_len == 4:
            for piece in final_leftovers[0]:
                for eciep in final_leftovers[1]:
                    for ec in final_leftovers[2]:
                        for omgwhy in final_leftovers[3]:
                            temp_delta = rgbDist(piece.hexcode, eciep.hexcode, ec.hexcode, omgwhy.hexcode)
                            if temp_delta < lowest_delta:
                                lowest_delta = temp_delta
                                best_pieces = [piece, eciep, ec, omgwhy]
        else:
            print("how ---", lef_len)
            exit()
        
        for piece in best_pieces:
            piece_idx = comparison.index(piece.piecetype)
            lowest_pieces[piece_idx] = piece
    if None in lowest_pieces:
        print(lowest_pieces)
    temp_delta = rgbDist(lowest_pieces[0].hexcode, lowest_pieces[1].hexcode, lowest_pieces[2].hexcode, lowest_pieces[3].hexcode)
    temp_delta = f"{temp_delta:.3f}"
    temp_dict= {f"{major}+{temp_delta}": lowest_pieces[:]}
    final_hexcodes = final_hexcodes | temp_dict





#printing
for key, value in final_hexcodes.items():
    print(f"{key}:")
    for idx, val in enumerate(value):
        print(val.hexcode, end=" ")
    print()
    for idx, val in enumerate(value):
        print(val.hexcode, val.piecetype, val.pdelta)
    print("\n")
