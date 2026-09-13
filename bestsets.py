from databaseExtractor import databaseExtract
from seymourhelper import CIEVals, quickSetDelta, distanceRGBaway, deltaECie, avgabsSet, find_many
from itertools import groupby


def abs_restrictor(hex1, hex2, hex3, hex4, restrictor=None):
    """Checks if any abs between the 4 hexes are over or equal to the restrictor value, defaults to 50

    Returns:
        bool: False for fail, True for sucess
    """

    if restrictor == None:
        restrictor = 40
    if distanceRGBaway(hex1,hex4)>= restrictor:
        return False
    if distanceRGBaway(hex2,hex4)>= restrictor:
        return False
    if distanceRGBaway(hex3,hex4)>= restrictor:
        return False
    return True

def string_splitter(text):
    ColorSetHexes: list[str] = []
    InputStringHexes = text
    InputStringHexes = InputStringHexes.replace('\t', '').replace(',', '').replace(" ", "").replace("|", "").replace("\n", "")
    InputStringHexes = InputStringHexes + "END"
    if InputStringHexes.startswith("SEYMOUREXPORT") or InputStringHexes.startswith("SEYMOURDATABASEEXPORT"):
        input_list = InputStringHexes.split("TOP:")
        for string in input_list:
            if string[-3:] == "END":
                break
            piece_substrings = ["VELVETTOPHAT", "CASHMEREJACKET", "SATINTROUSERS", "OXFORDSHOES"]
            index_str = find_many(string, *piece_substrings)
            if index_str == -1:
                print("error")
                exit()
            string = string[index_str:]
            hexesandpieces = string.split("#")
            hexesandpieces[0] = hexesandpieces[0].replace("VELVETTOPHAT", "VELVET_TOP_HAT").replace("CASHMEREJACKET", "CASHMERE_JACKET").replace("SATINTROUSERS","SATIN_TROUSERS").replace("OXFORDSHOES", "OXFORD_SHOES")
            current_hex = f"{hexesandpieces[0]} #{hexesandpieces[1]}"
            ColorSetHexes.append(current_hex)            
    else:
        while True:
            #this is for from spreadsheet
            if InputStringHexes.startswith("VELVET_TOP_HAT#"):
                typeHexinput = InputStringHexes[0:14]
                pieceHexinput = InputStringHexes[14:21]
                current_hex = f"{typeHexinput} {pieceHexinput}"
                ColorSetHexes.append(current_hex)
                InputStringHexes = InputStringHexes[21:]
            elif InputStringHexes.startswith("CASHMERE_JACKET#"):
                typeHexinput = InputStringHexes[0:15]
                pieceHexinput = InputStringHexes[15:22]
                current_hex = f"{typeHexinput} {pieceHexinput}"
                ColorSetHexes.append(current_hex)
                InputStringHexes = InputStringHexes[22:]
            elif InputStringHexes.startswith("SATIN_TROUSERS#"):
                typeHexinput = InputStringHexes[0:14]
                pieceHexinput = InputStringHexes[14:21]
                current_hex = f"{typeHexinput} {pieceHexinput}"
                ColorSetHexes.append(current_hex)
                InputStringHexes = InputStringHexes[21:]
            elif InputStringHexes.startswith("OXFORD_SHOES#"):
                typeHexinput = InputStringHexes[0:12]
                pieceHexinput = InputStringHexes[12:19]
                current_hex = f"{typeHexinput} {pieceHexinput}"
                ColorSetHexes.append(current_hex)
                InputStringHexes = InputStringHexes[19:]    
            elif InputStringHexes.startswith("END"):
                break
            else:
                print("Split String Error")
                raise SystemExit
    for idx, val in enumerate(ColorSetHexes):
        created_uuid = f"{idx:05}"
        ColorSetHexes[idx] = f"{created_uuid} {val}"
    return ColorSetHexes
  
def main():
    all_sets = input("Do you want sets with or without overlap? Y for without overlap, n for all sets including overlap\nY/n: ")
    ColorSetHexes = databaseExtract()
    for i in range(len(ColorSetHexes)):
        temp = ColorSetHexes[i].split(" ")
        temp[2] = CIEVals(temp[2], uuid=temp[0])
        ColorSetHexes[i] = temp[1:]
    ColorSetHexes = [list(g) for k, g in groupby(sorted(ColorSetHexes, key=lambda item: item[0]), key=lambda x: x[0])]
    helm: list[CIEVals] = [x[1] for x in ColorSetHexes[3]]
    chest: list[CIEVals] = [x[1] for x in ColorSetHexes[0]]  
    legs: list[CIEVals] = [x[1] for x in ColorSetHexes[2]]  
    boots: list[CIEVals] = [x[1] for x in ColorSetHexes[1]]     
    del ColorSetHexes
    del i
    best_sorted = []
    restrictor = 5.000
    for hm in helm: #overall loop, TERRIBLY INEFFICENT
        best_set = ["", "", "", "", "", ""]
        restricted_chests: list[tuple[CIEVals, float]] = []
        restricted_legs: list[tuple[CIEVals, float]] = []
        restricted_boots: list[tuple[CIEVals, float]] = []
        ## Remove all hexes in these that do not match current helmet- will then just skip over them the next time it runs a loop
        for t in chest:
            delta = deltaECie(hm, t)
            if delta < restrictor:
                restricted_chests.append((t, delta))
        for t in legs:
            delta = deltaECie(hm, t)
            if delta < restrictor:
                restricted_legs.append((t, delta))        
        for t in boots:
            delta = deltaECie(hm, t)            
            if delta < restrictor:
                restricted_boots.append((t, delta))        


        for ch, cdelta in restricted_chests:      
            for lg, ldelta in restricted_legs: 
                cldelta = deltaECie(ch, lg)
                if cldelta < restrictor:                                          
                    for bt, bdelta in restricted_boots:
                        final_delta = (cdelta+ldelta+bdelta+cldelta+deltaECie(ch, bt)+deltaECie(lg, bt))/6
                        abs = avgabsSet(hm.hex, ch.hex, lg.hex, bt.hex)
                        if final_delta < 2.000:
                            best_set = [hm, ch, lg, bt, final_delta, abs]
                            best_sorted.append(best_set)
        print(f"{len(helm)-helm.index(hm)}        ", end="\r")


    if "Y" in all_sets[:5]:
        best_sorted = sorted(best_sorted, key=lambda x: x[4])    
        taken_uuids = []
        for val in best_sorted:
            skip = False
            temp_uuids = []
            for i in range(4):
                if val[i].uuid in taken_uuids:
                    skip = True
                else:
                    temp_uuids.append(val[i].uuid)
            if skip == False:
                taken_uuids = taken_uuids + temp_uuids
                print(val[0].hex, val[1].hex, val[2].hex, val[3].hex, val[4], val[5])
    elif "Z" in all_sets[:5]:
        best_sorted = sorted(best_sorted, key=lambda x: float(x[5]))    
        taken_uuids = []
        for val in best_sorted:
            skip = False
            temp_uuids = []
            for i in range(4):
                if val[i].uuid in taken_uuids:
                    skip = True
                else:
                    temp_uuids.append(val[i].uuid)
            if skip == False:
                taken_uuids = taken_uuids + temp_uuids
                print(val[0].hex, val[1].hex, val[2].hex, val[3].hex, val[4], val[5])                
    else:
        best_sorted = sorted(best_sorted, key=lambda x: x[4])
        with open("personal_databases\\BestSets.txt", "w") as fd:
                dbstr = ""
                for val in best_sorted:
                    dbstr = f"{val[0].hex}, {val[1].hex}, {val[2].hex}, {val[3].hex}, {val[4]}, {val[5]}\n"
                    fd.write(dbstr)
                print("Writing Done")      
        best_sorted = best_sorted[:5001]         
        for val in best_sorted:
            print(val[0].hex, val[1].hex, val[2].hex, val[3].hex, val[4], val[5])


def for_other_peoples():
    all_sets = input("Do you want sets with or without overlap? Y for without overlap, n for all sets including overlap\nY/n: ")
    read_from_file = input("Do you want to read from a file?\nY/n: ")    

    inputstr_hexes = ""
    if "Y" in read_from_file[:5]:
        file_location = input("Paste file location: ")
        with open(file_location[1:-1]) as fd:
            inputstr_hexes = fd.read().upper()
    else:
        inputstr_hexes = input("Colour Set Hex Codes, Right Click and paste as a single line:\n").upper()

    ColorSetHexes = string_splitter(inputstr_hexes)
    for i in range(len(ColorSetHexes)):
        temp = ColorSetHexes[i].split(" ")
        temp[2] = CIEVals(temp[2], uuid=temp[0])
        ColorSetHexes[i] = temp[1:]
    ColorSetHexes = [list(g) for k, g in groupby(sorted(ColorSetHexes, key=lambda item: item[0]), key=lambda x: x[0])]
    helm: list[CIEVals] = [x[1] for x in ColorSetHexes[3]]
    chest: list[CIEVals] = [x[1] for x in ColorSetHexes[0]]  
    legs: list[CIEVals] = [x[1] for x in ColorSetHexes[2]]  
    boots: list[CIEVals] = [x[1] for x in ColorSetHexes[1]]     
    del ColorSetHexes
    del i
    best_sorted = []
    restrictor = 5.000
    for hm in helm: #overall loop
        best_set = ["", "", "", "", "", ""]
        restricted_chests: list[tuple[CIEVals, float]] = []
        restricted_legs: list[tuple[CIEVals, float]] = []
        restricted_boots: list[tuple[CIEVals, float]] = []
        ## Remove all hexes in these that do not match current helmet- will then just skip over them the next time it runs a loop
        for t in chest:
            delta = deltaECie(hm, t)
            if delta < restrictor:
                restricted_chests.append((t, delta))
        for t in legs:
            delta = deltaECie(hm, t)
            if delta < restrictor:
                restricted_legs.append((t, delta))        
        for t in boots:
            delta = deltaECie(hm, t)            
            if delta < restrictor:
                restricted_boots.append((t, delta))        


        for ch, cdelta in restricted_chests:      
            for lg, ldelta in restricted_legs: 
                cldelta = deltaECie(ch, lg)
                if cldelta < restrictor:                                          
                    for bt, bdelta in restricted_boots:
                        final_delta = (cdelta+ldelta+bdelta+cldelta+deltaECie(ch, bt)+deltaECie(lg, bt))/6
                        abs = avgabsSet(hm.hex, ch.hex, lg.hex, bt.hex)
                        if final_delta < 2.000:
                            best_set = [hm, ch, lg, bt, final_delta, abs]
                            best_sorted.append(best_set)
        print(f"{len(helm)-helm.index(hm)}        ", end="\r")


    if "Y" in all_sets[:5]:
        best_sorted = sorted(best_sorted, key=lambda x: x[4])    
        taken_uuids = []
        for val in best_sorted:
            skip = False
            temp_uuids = []
            for i in range(4):
                if val[i].uuid in taken_uuids:
                    skip = True
                else:
                    temp_uuids.append(val[i].uuid)
            if skip == False:
                taken_uuids = taken_uuids + temp_uuids
                print(val[0].hex, val[1].hex, val[2].hex, val[3].hex, val[4], val[5])
    elif "Z" in all_sets[:5]:
        best_sorted = sorted(best_sorted, key=lambda x: float(x[5]))    
        taken_uuids = []
        for val in best_sorted:
            skip = False
            temp_uuids = []
            for i in range(4):
                if val[i].uuid in taken_uuids:
                    skip = True
                else:
                    temp_uuids.append(val[i].uuid)
            if skip == False:
                taken_uuids = taken_uuids + temp_uuids
                print(val[0].hex, val[1].hex, val[2].hex, val[3].hex, val[4], val[5])                
    else:
        best_sorted = sorted(best_sorted, key=lambda x: x[4])      
        best_sorted = best_sorted[:5001]         
        for val in best_sorted:
            print(val[0].hex, val[1].hex, val[2].hex, val[3].hex, val[4], val[5])




                                 
if __name__ == '__main__':
    # main()
    # for_other_peoples()