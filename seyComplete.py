
from databaseExtractor import databaseExtract, random_extract
from seymourhelper import find_many
from hexcodeClass import Hexcode


def hexcodestuff(list_var: list[Hexcode]):
    new_list = []
    print("test hello")
    list_var = sorted(list_var, key=lambda x: x.hexcode)
    for current_hex in list_var:
        iHex = current_hex.hexcode
        iType = current_hex.piecetype
        current_hex.assign_all_attributes()
        current_hex.rename_all_false()
        lowestHexHyp, lowestHexName, lowestscorestr, distance = current_hex.pdelta        
        deltastr = str(f"{lowestHexHyp}, {lowestHexName}, {lowestscorestr}, {distance}")        
        str_1 = f"{iType}, {iHex}, {deltastr}, {current_hex.major_digits}, {current_hex.grayness}, {current_hex.isPatternAxAxAx},"
        str_2 = f" {current_hex.inCollectionRange}, {current_hex.isPatternABCABC}, {current_hex.isPatternAABBCC}, {current_hex.isPalendrome}, {current_hex.isthreextwo_nums}, {current_hex.everthing_else}, {current_hex.num_same_digit}"
        str_to_append = str_1 + str_2
        new_list.append(str_to_append)
    return new_list

def json_file_hexcode_stuff(list_var: list[list[str]]):
    new_list = []
    file_dictionary = {}
    list_var = sorted(list_var, key=lambda x: x[2])
    current_main_file = -1
    current_sub_file = list(range(0,8))
    last_stopped_idx = None
    list_len = len(list_var)-1
    for idx, sublist in enumerate(list_var):
        hexcode = sublist[2]
        if len(hexcode) != 7:
            print(f"invalid hexcode len: {len(hexcode)}")
            exit()
        if current_main_file == -1:
            current_main_file = int(hexcode[1])
            if int(hexcode[2], 16) < 8:
                current_sub_file = list(range(0,8))
            else:
                current_sub_file = list(range(8,16))
        if idx == list_len: #checks if this is the last element
            name_str = f"{current_main_file}.{current_sub_file[0]}"
            if last_stopped_idx == None:
                file_dictionary[name_str] = list_var
        elif int(hexcode[1], 16) == current_main_file:
            if int(hexcode[2], 16) in current_sub_file:
                continue
            else: #case where 2nd digit is 8 or over
                name_str = f"{current_main_file}.{current_sub_file[0]}"
                if last_stopped_idx == None:
                    file_dictionary[name_str] = list_var[0:idx]
                    last_stopped_idx = idx
                else:
                    file_dictionary[name_str] = list_var[last_stopped_idx:idx]
        else:
            pass



    for i in list_var:
        iHex = i[2]
        iType = i[1]
        current_hex = Hexcode(iHex, iType)
        current_hex.assign_all_attributes()
        current_hex.rename_all_false()
        lowestHexHyp, lowestHexName, lowestscorestr, distance = current_hex.pdelta        
        deltastr = str(f"{lowestHexHyp}, {lowestHexName}, {lowestscorestr}, {distance}")        
        str_1 = f"{iType}, {iHex}, {deltastr}, {current_hex.major_digits}, {current_hex.grayness}, {current_hex.isPatternAxAxAx},"
        str_2 = f" {current_hex.inCollectionRange}, {current_hex.isPatternABCABC}, {current_hex.isPatternAABBCC}, {current_hex.isPalendrome}, {current_hex.isthreextwo_nums}, {current_hex.everthing_else}, {current_hex.num_same_digit}"
        str_to_append = str_1 + str_2
        res = str_to_append.replace("False", "")
        new_list.append(str_to_append)
    return new_list

def string_splitter():
    ColorSetHexes: list[list[str]] = []
    InputStringHexes = input("Colour Set Hex Codes, Right Click and paste as a single line:\n").upper()
    InputStringHexes = InputStringHexes.replace('\t', '').replace(',', '').replace(" ", "").replace("|", "").replace("\n", "")
    InputStringHexes = InputStringHexes + "END"
    if InputStringHexes.startswith("SEYMOUREXPORT"):
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
            current_hex = Hexcode("#"+hexesandpieces[1], hexesandpieces[0])
            ColorSetHexes.append(current_hex)            
    else:
        while True:
            #this is for from spreadsheet
            if InputStringHexes.startswith("VELVET_TOP_HAT#"):
                typeHexinput = InputStringHexes[0:14]
                pieceHexinput = InputStringHexes[14:21]
                current_hex = Hexcode(pieceHexinput, typeHexinput)
                ColorSetHexes.append(current_hex)
                InputStringHexes = InputStringHexes[21:]
            elif InputStringHexes.startswith("CASHMERE_JACKET#"):
                typeHexinput = InputStringHexes[0:15]
                pieceHexinput = InputStringHexes[15:22]
                current_hex = Hexcode(pieceHexinput, typeHexinput)
                ColorSetHexes.append(current_hex)
                InputStringHexes = InputStringHexes[22:]
            elif InputStringHexes.startswith("SATIN_TROUSERS#"):
                typeHexinput = InputStringHexes[0:14]
                pieceHexinput = InputStringHexes[14:21]
                current_hex = Hexcode(pieceHexinput, typeHexinput)
                ColorSetHexes.append(current_hex)
                InputStringHexes = InputStringHexes[21:]
            elif InputStringHexes.startswith("OXFORD_SHOES#"):
                typeHexinput = InputStringHexes[0:12]
                pieceHexinput = InputStringHexes[12:19]
                current_hex = Hexcode(pieceHexinput, typeHexinput)
                ColorSetHexes.append(current_hex)
                InputStringHexes = InputStringHexes[19:]    
            elif InputStringHexes.startswith("END"):
                break
            else:
                print("Split String Error")
                raise SystemExit
    return ColorSetHexes
  
def auto_yes():
    changed_list = []  
    with open("seymourdatabase.txt", "r") as fs:
        oldcolors = fs.read().split('\n')
        oldcolors.pop(-1)
        for idx,val in enumerate(oldcolors):
            oldcolors[idx] = val.split(" ")
    ColorSetHexes = databaseExtract()
    for i in range(len(ColorSetHexes)):
        ColorSetHexes[i] = ColorSetHexes[i].split(" ")
    removed_colors = []
    added_colors: list[list[str]] = []
    old_color_set = set()
    new_color_set = set()

    for i in range(len(oldcolors)):
        old_color_set.add(oldcolors[i][0].upper())
    for i in range(len(ColorSetHexes)):
        new_color_set.add(ColorSetHexes[i][0].upper())
    
    o_color_set = old_color_set.difference(new_color_set)
    n_color_set = new_color_set.difference(old_color_set)
    if len(o_color_set)>0:    
        for value in oldcolors:
            if value[0] in o_color_set:
                removed_colors.append(value)
        
    if len(n_color_set)>0:
        for value in ColorSetHexes:
            if value[0] in n_color_set:
                value = Hexcode(value[2], value[1], value[0])
                added_colors.append(value)

    if len(added_colors)+len(removed_colors) == 0:
        print("No changes made since last ran")
        exit()
    if len(removed_colors)>0:
        changed_list.append("\nRemoved Colors:")
        for i in range(len(removed_colors)):
            iHex = removed_colors[i][2]
            iType = removed_colors[i][1]
            appendval = Hexcode(iHex, iType)
            changed_list.append(appendval)
    if len(added_colors)>0:
        changed_list.append("\nAdded Colors:")
        added_list = hexcodestuff(added_colors)
        changed_list.extend(added_list)
    for idx, value in enumerate(ColorSetHexes):
        ColorSetHexes[idx] = Hexcode(value[2], value[1], value[0])
    return ColorSetHexes, changed_list

#main function, combinging them all
def MainFunction():
  #dictionaries
    ColorSetHexes: list[Hexcode] = []
    FinalPrintList = []
    changed_list = []    
    Auto = input("type '0' for manual, anything else for automatic\n")
    if Auto == "0":
        ColorSetHexes = string_splitter()
    else:
        ColorSetHexes, changed_list = auto_yes()
    FinalPrintList = hexcodestuff(ColorSetHexes)
    return FinalPrintList, changed_list, Auto



if __name__ == '__main__':
    
    piecedata, updatelist, append = MainFunction()
    if append != "0":
        if len(updatelist) < 300:
            for i in updatelist:
                print(i)
            print()
        else:
            print("Many things added/removed\n")
        with open("SheetsUploadDatabase.txt", "w") as fd:
                dbstr = ""
                for i in range(len(piecedata)):
                    dbstr = f"{piecedata[i]}\n"
                    fd.write(dbstr)
                print("Writing Done")

    else:
        for i in piecedata:
            print(i)
        WritetoFile = input("Do you want to append exported hexes the file? (\"0\" for yes, anything else for no)\n")
        if "0" in WritetoFile:
            with open("SheetsUploadDatabase.txt", "a") as fd:
                    dbstr = ""
                    for i in range(len(piecedata)):
                        dbstr = f"{piecedata[i]}\n"
                        fd.write(dbstr)
                    print("Writing Done")