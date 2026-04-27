import math
from collections import Counter
from databaseExtractor import databaseExtract
from seymourhelper import delta, rgbdecouple, find_many

def threeMainVals(pieceHex):
    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    AxBxCx = f"{pieceHex[0]}{pieceHex[2]}{pieceHex[4]}"
    return f"{AxBxCx}"

def palendromepices(pieceHex):
    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    if (pieceHex[0] == pieceHex[5]) and (pieceHex[1] == pieceHex[4]) and (pieceHex[2] == pieceHex[3]):
        return "True"
    else:
        return ""

def sameThreeAAA(pieceHex):
    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    if pieceHex[0] == pieceHex[2] == pieceHex[4]:
        return "True"
    else:
        return ""
    
def sameThreeABC(pieceHex):
    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    if pieceHex[0:3] == pieceHex[3:6]:
        return "True"
    else:
        return ""
    
def sameAABBCC(pieceHex):
    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    if (pieceHex[0] == pieceHex[1]) and (pieceHex[2] == pieceHex[3]) and (pieceHex[4] == pieceHex[5]):
        return "True"
    else:
        return ""

def sameRGBval(pieceHex):
    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    if pieceHex[0:2] == pieceHex[2:4] == pieceHex[4:6]:
        return "True"
    else:
        return ""
    
def countofvals(pieceHex):
    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    
    mp = {}

    # to store length of string
    n = len(pieceHex)
    cnt = 0

    # traverse the string
    for i in range(n):
        # push element into dictionary and increase its frequency
        if pieceHex[i] in mp:
            mp[pieceHex[i]] += 1
        else:
            mp[pieceHex[i]] = 1

        # update answer and count
        if cnt < mp[pieceHex[i]]:
            cnt = mp[pieceHex[i]]

    return cnt

def threeTwoSameNums(pieceHex):
    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    a = list(pieceHex)
    x = Counter(a)
    x_values = list(x.values())
    if (len(x_values) == 3) and (x_values[0] == 2) and (x_values[1] == 2):
        return "True"
    else:
        return ""
            
def whiteness(piecehex):
    "parametric equation for line"
    'v = <1,1,1>'
    "p = (1,1,1)"
    red, green, blue = rgbdecouple(piecehex)
    rprod = green - blue
    gprod = blue - red
    bprod = red - green
    return f"{(math.sqrt((rprod**2) + (gprod**2) + (bprod**2))/1.7):.3f}"

def incollectionrange(pieceHex):
    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    lowval = ["0", "1", "2"]
    lowvalnum = 0
    highval = ["D", "E", "F"]
    highvalnum = 0
    for i in range(0,len(pieceHex), 2):
        if pieceHex[i] in lowval:
            lowvalnum += 1
        elif pieceHex[i] in highval:
            highvalnum += 1
        else: 
            return ""
    if 3 in {lowvalnum, highvalnum}:
        return "True"
    else:
        return ""
    
def allOther(pieceHex):

    if pieceHex[0] == "#":
        pieceHex = pieceHex[1:]
    #includes words, hexes with only 1 color, and whatever else I feel like adding
    wordlist = ["DECODE", "D1ED", "B00B", "C001", "FA11", "BEEF", "C0FFEE", "F1EA", "F1EE",
                "FE1F", "BEAD", "CEA1", "BA11", "DEAD", "DEED", "DECADE", "FADE", "4AC0B",
                "B1EED", "FACE", "F00D", "FEED", "FACADE", "D05E", "6969", "9696", "CAFE", "BA1D",
                "5EED", "5AFE", "CEA5E", "B0D1E5", "CA5E", "B033C1", "DEF1ED", "D1CE", "AC1D", "1EAF",
                "51DE", "BA5E", "BADD1E", "BA55", "EDD1E", "FEEB1E", "C0DE", "F01D", "BADA55", "007AC0", "1EAD"
                "C0C0", "DEAF", "A0D1AC", "CA5A", "1CED", "1DEA", "D7ED", "DEC1DE", "DEA1", "AD1DA5", "CA1C",
                "ABCDEF", "ABCDE", "ABCD", "D15C0"
                "C0DA", "2025", "2024", "2020", "2023", "2022", "2021", "2004", "2019", "ACAC1A", "CA551E"]
    
    if (len(pieceHex) - len(pieceHex.lstrip('0'))) > 2:
        if (len(pieceHex) - len(pieceHex.lstrip('0'))) == 3:
            return "3 length"
        if (len(pieceHex) - len(pieceHex.lstrip('0'))) == 4:
            return "2 length"        
        if (len(pieceHex) - len(pieceHex.lstrip('0'))) == 5:
            return "Single Length!"    
    
    for i in range(len(wordlist)):
        if wordlist[i] in pieceHex:
            return wordlist[i]


    if (int(countofvals(pieceHex)) == 3) and (len(list(set(pieceHex))) == 2):
        return "2L-repeaters"

    if int(countofvals(pieceHex)) > 3:
        char_lst = "0123456789ABCDEF"
        for char in char_lst:
            current_char = char * 4
            if current_char in pieceHex:
                return "True "+ char + "'s"
        return str(max(pieceHex, key=pieceHex.count)) + "'s"

    return ""
    

#main function, combinging them all
def MainFunction():
  #dictionaries
    dictOfHypixelHexColours = dict([("0B004F", "Angler 3p"),
    ("00FF00", "Pure Green"),
    ("FFFF00", "Pure Yellow"),
    ("4DCC4D", "Leaflet 3p"),
    ("FF0000", "Pure Red"),
    ("EDAA36", "Pumpkin"),
    ("FFAC00", "Biohazard 3p"),
    ("0000FF", "Pure Blue"),
    ("7A7964", "Miners/Prospecting"),
    ("FFD700", "Farm Armour/Elanor's Set (Rift)"),
    ("37B042", "Goblin 3p"),
    ("00BE00", "Growth Armour"),
    ("B3B3B3", "Heat Armour"),
    ("000000", "Pure Black"),
    ("DF2E06", "Rampart 3p"),
    ("07031B", "Shimmering Light 3p"),
    ("8B0000", "Arachne Armour 3p"),
    ("F7DA33", "Blaze Armour 3p"),
    ("03FCF8", "Glacite 3p"),
    ("FF9300", "Armour of Magma"),
    ("CCE5FF", "Mineral Armour 3p"),
    ("FFFFFF", "Pure White"),
    ("FFDC51", "Sponge 3p"),
    ("606060", "Spooky Armour 3p"),
    ("24DDE5", "Thunder 3p"),
    ("A0DAEF", "Frozen Blaze 3p"),
    ("5B0DAE", "Glossy Mineral Armour 3p"),
    ("47D147", "Holy Dragon 3p"),
    ("6F0F08", "Magma Lord 3p"),
    ("F0E6AA", "Old Dragon 3p"),
    ("99978B", "Protector Dragon 3p"),
    ("1B1B1B", "Reaper Armour 3p"),
    ("002CA6", "Shark Scale Armour 3p"),
    ("B212E3", "Unstable Dragon 3p"),
    ("1D1105", "Werewolf 3p"),
    ("29F0E9", "Wise Dragon 3p"),
    ("DDE4F0", "Young Dragon 3p"),
    ("35530A", "Kuudra Follower 3p"),
    ("BFBCB2", "Adaptive Armour (Outside Dungeon) 3p"),
    ("ADFF2F", "Bouncy"),
    ("E7413C", "Necron Dye/Chestplate"),
    ("E1EB34", "Skeleton Grunt"),
    ("268105", "Skeleton Lord 3p"),
    ("FF6B0B", "Skeleton Master"),
    ("FFBC0B", "Skeleton Soldier"),
    ("D51230", "Zombie Comander"),
    ("9B01C1", "Zombie Lord 3p"),
    ("D07F00", "Zombie Soldier"),
    ("E0FCF7", "Speedster Set/Mercenary Boots"),
    ("450101", "Crypt Witherlord"),
    ("993399", "Great Spook"),
    ("899E20", "Melon Armour 3p"),
    ("CBD2DB", "Rabbit Armour"),
    ("C83200", "Yog Armour"),
    ("FFCCE5", "Fairy Dyed (FFCCE5)"),
    ("FF99CC", "Fairy Dyed (FF99CC)"),
    ("FF66B2", "Fairy Dyed (FF66B2)"),
    ("FF3399", "Fairy Dyed (FF3399)"),
    ("FF007F", "Fairy Dyed (FF007F)"),
    ("CC0066", "OG Fariy Dyed (CC0066)"),
    ("99004C", "OG Fairy Dyed (99004C)"),
    ("660033", "OG Fairy Dyed (660033)"),
    ("FFCCFF", "OG Fairy Dyed (FFCCFF)"),
    ("FF99FF", "OG Fairy Dyed (FF99FF)"),
    ("E5CCFF", "Og Fairy Dyed (E5CCFF)"),
    ("CC99FF", "Og Fairy Dyed (CC99FF)"),
    ("FF66FF", "Og Fairy Dyed (FF66FF)"),
    ("FF33FF", "Og Fairy Dyed (FF33FF)"),
    ("B266FF", "Og Fairy Dyed (B266FF)"),
    ("9933FF", "Og Fairy Dyed (9933FF)"),
    ("FF00FF", "Pure Pink/Og Fairy Dyed (FF00FF)"),
    ("CC00CC", "Og Fairy Dyed (CC00CC)"),
    ("7F00FF", "Og Fairy Dyed (7F00FF)"),
    ("6600CC", "Og Fairy Dyed (6600CC)"),
    ("990099", "Og Fairy Dyed (990099)"),
    ("660066", "Og Fairy Dyed (660066)"),
    ("4C0099", "Og Fairy Dyed (4C0099)"),
    ("330066", "Og Fairy Dyed (330066)"),
    ("FCF3FF", "Crystal Armour Reg (FCF3FF)"),
    ("EFE1F5", "Crystal Dyed (EFE1F5)"),
    ("E5D1ED", "Crystal Dyed (E5D1ED)"),
    ("D9C1E3", "Crystal Dyed (D9C1E3)"),
    ("C6A3D4", "Crystal Dyed (C6A3D4)"),
    ("B88BC9", "Crystal Dyed (B88BC9)"),
    ("A875BD", "Crystal Dyed (A876BD)"),
    ("9C64B3", "Crystal Dyed (9C64B3)"),
    ("8E51A6", "Crystal Dyed (8E51A6)"),
    ("7E4196", "Crystal Dyed (7E4196)"),
    ("6A2C82", "Crystal Dyed (6A2C82)"),
    ("63237D", "Crystal Dyed (63237D)"),
    ("5D1C78", "Crystal Dyed (5D1C78)"),
    ("54146E", "Crystal Dyed (54146E)"),
    ("46085E", "Crystal Dyed (46085E)"),
    ("1F0030", "Crystal Dyed (1F0030)"),
    ("7FFFD4", "Aquamarine Dye"),
    ("B80036", "Archfiend Dye"),
    ("002FA7", "Bingo Blue Dye"),
    ("E3DAC9", "Bone Dye"),
    ("CB4154", "Brick Red Dye"),
    ("702963", "Byzantium Dye"),
    ("960018", "Carmine Dye"),
    ("ACE1AF", "Celadon Dye"),
    ("B2FFFF", "Celeste Dye"),
    ("7B3F00", "Chocolate Dye"),
    ("B87333", "Copper Dye"),
    ("F56FA1", "Cyclamen Dye"),
    ("301934", "Dark Purple Dye"),
    ("4F2A2A", "Dung Dye"),
    ("50C878", "Emerald Dye"),
    ("E25822", "Flame Dye"),
    ("866F12", "Fossil Dye"),
    ("09D8EB", "Frostbitten Dye"),
    ("3C6746", "Holly Dye"),
    ("71A6D2", "Iceberg Dye"),
    ("00A86B", "Jade Dye"),
    ("CEB7AA", "Livid Dye"),
    ("FDBE02", "Mango Dye"),
    ("74A12E", "Matcha Dye"),
    ("50216C", "Midnight Dye"),
    ("967969", "Mocha Dye"),
    ("F6ADC6", "Nadeshiko Dye"),
    ("E9FFDB", "Nyanza Dye"),
    ("115555", "Pearlescent Dye"),
    ("50414C", "Pelt Dye"),
    ("CCCCFF", "Periwinkle Dye"),
    ("0013FF", "Pure Blue Dye"),
    ("FFF700", "Pure Yellow Dye"),
    ("D40808", "Sangria Dye"),
    ("7D7D7D", "Secret Dye"),
    ("324D6C", "Tentacle Dye"),
    ("FF43A4", "Strawberry Dye"),
    ("993333", "Exo pure red"),
    ("D87F33", "Exo pure orange"),
    ("E5E533", "Exo pure yellow"),
    ("7FCC19", "Exo pure green"),
    ("667F33", "Exo pure dark green"),
    ("6699D8", "Exo pure light blue"),
    ("4C7F99", "Exo pure cyan"),
    ("334CB2", "Exo pure blue"),
    ("F27FA5", "Exo pure pink"),
    ("7F3FB2", "Exo pure purple"),
    ("B24CD8", "Exo pure magenta"),
    ("664C33", "Exo pure brown"),
    ("999999", "Exo pure light grey"),
    ("4C4C4C", "Exo pure grey"),
    ("191919", "Exo pure black"),
    ("FCD12A", "Treasure Dye"),
    ("00FFFF", "Pure Cyan"),
    ("A06540", "Bleached"),
    ("918F89", "Skeletor 3p"),
    ("101555", "Hydra 3p"),
    ("3588FF", "Vanguard 3p"),
    ("990D00", "Emperor 3p"),
    ("10616E", "Sea Walker 3p"),
    ("586158", "Fallen Star 3p"),
    ("0E1736", "Primordial Armour 3p"),
    ("1C9759", "Figmail 3p"),
    ("0E666D", "Abyssal 3p"),
    ("6F6F0C", "Mythological Dye"),


    #all below this are specific
    ("35B73B", "Wyld Leggings (Rift)"),
    ("154918", "Wyld Boots (Rift)"),
    ("ED6612", "Flaming Chestplate"),
    ("CE2C2C", "Moogma Leggings"),
    ("276114", "Slug Boots"),
    ("117391", "Guardian Chestplate"),
    ("7AE82C", "Creeper Pants (Leggings)"),
    ("FFA33B", "Beserker Chestplate"),
    ("FFB727", "Beserker Leggings"),
    ("FFD427", "Beserker Boots"),
    ("383838", "Cheap Tux Chestplate+Boots"),
    ("C7C7C7", "Cheap Tux Leggings"),
    ("DEBC15", "Rising Sun Leggings"),
    ("9F8609", "Rising Sun Boots"),
    ("FEFDFC", "Elegant Tux Leggings"),
    ("332A2A", "Fancy Tux Chestplate+Boots"),
    ("D4D4D4", "Fancy Tux Leggings"),
    ("0A0011", "Final Destination Chestplate+Boots"),
    ("FF75FF", "Final Destination Leggings"),
    ("D91E41", "Strong Dragon Chestplate"),
    ("E09419", "Strong Dragon Leggings"),
    ("F0D124", "Strong Dragon Boots"),
    ("F2DF11", "Superior Dragon Chestplate+Leggings"),
    ("F25D18", "Superior Dragon Boots"),
    ("FC2F3C", "Nutcracker Chestplate"),
    ("FFF9EB", "Nutcracker Leggings"),
    ("46343A", "Nutcracker Boots"),
    ("45413C", "Goldor Chestplate"),
    ("65605A", "Goldor Leggings"),
    ("88837E", "Goldor Boots"),
    ("828282", "Heavy Chestplate+Leggings"),
    ("4A14B7", "Maxor Chestplate"),
    ("5D2FB9", "Maxor Leggings"),
    ("8969C8", "Maxor Boots"),
    ("370147", "Necromancer Lord Leggings"),
    ("400352", "Necromancer Lord Boots"),
    ("E75C3C", "Necron Leggings"),
    ("E76E3C", "Necron Boots"),
    ("9E7003", "Rotten Helm+Boots"),
    ("017D31", "Rotten Chestplate+Leggings"),
    ("1793C4", "Storm Chestplate"),
    ("17A8C4", "Storm Leggings"),
    ("1CD4E4", "Storm Boots"),
    ("E6E6E6", "Super Heavy Helm+Boots"),
    ("5A6464", "Super Heavy Chestplate+Leggings"),
    ("2841F1", "Aurora Chestplate"),
    ("3F56FB", "Aurora Leggings"),
    ("6184FC", "Aurora Boots"),
    ("FF6F0C", "Crimson Chestplate"),
    ("E66105", "Crimson Leggings"),
    ("E65300", "Crimson Boots"),
    ("F04729", "Fervor Chestplate"),
    ("17BF89", "Fervor Leggings"),
    ("07A674", "Fervor Boots"),
    ("FFCB0D", "Hollow Chestplate"),
    ("FFF6A3", "Hollow Leggings"),
    ("E3FFFA", "Hollow Boots"),
    ("3E05AF", "Terror Chestplate"),
    ("5D23D1", "Terror Leggings"),
    ("7C44EC", "Terror Boots"),
    ("D9D9D9", "Stone+Metal+Steel Chestplate"),
    ("FF4600", "Orange Chestplate (Rift)"),
    ("FFF200", "Chicken Leggings (Rift)"),
    ("48FF00", "Femurgrowth Leggings (Rift)"),
    ("04CFD3", "Stereo Pants (Leggings)"),
    ("380024", "Exceedingly Comfy Sneakers (Rift) (Boots)"),
    ("CC5500", "Farmers Boots"),
    ("4F2886", "Gunthers Sneakers (Boots)"),
    ("1A004C", "Snake-in-a-boot (Boots)"),
    ("BFBFBF", "Spirit Boots"),
    ("0C0C96", "Burned Pants (Rift) (Leggings)"),
    ("545454", "Squire Boots"),
    ("D48EF2", "Celeste Helm"),
    ("FF8EDE", "Celeste Chestplate"),
    ("FF8ECA", "Celeste Leggings"),
    ("FF8EB6", "Celeste Boots"),
    ("D400FF", "Starlight Chestplate+Boots"),
    ("7A2900", "Cropie Chestplate"),
    ("94451F", "Cropie Leggings"),
    ("BB6535", "Cropie Boots"),
    ("03430E", "Squash Chestplate"),
    ("0C4A16", "Squash Leggings"),
    ("13561E", "Squash Boots"),
    ("58890C", "Fermento Chestplate"),
    ("6A9C1B", "Fermento Leggings"),
    ("83B03B", "Fermento Boots"),
    ("808080", "Ghostly Boots"),
    ("3333FF", "Ugly Boots"),
    ("C13C0F", "Salmon Helm+Boots"),
    ("A82B76", "Salmon Chestplate+Leggings"),
    ("FF0A0A", "Minos Hunter Chestplate+Leggings"),
    ("304B4E", "Minos Hunter Boots"),
    ("F6DE51", "Charlies Trousers (Leggings)"),
    ("8D3592", "Melodys Shoes (Boots)"),
    ("006633", "Canopy Chestplate"),
    ("006600", "Canopy Leggings"),
    ("331900", "Canopy Boots"),
    ("2A5B48", "Challenger's Leggings+Boots"),
    ("7C3756", "Mythos Leggings+Boots"),
    ("FFE501", "Helianthus Leggings")
    ])
    ColorSetHexes: list[list[str]] = []
    oldcolors: list[list[str]] = []
    Auto = input("type '0' for manual, anything else for automatic\n")
    if Auto == "0":
        InputStringHexes = input("Colour Set Hex Codes, Right Click and paste as a single line:\n").upper()
        InputStringHexes = InputStringHexes.replace('\t', '').replace(',', '').replace(" ", "").replace("|", "")
        InputStringHexes = InputStringHexes + "END"
        if InputStringHexes.startswith("SEYMOUREXPORT"):
            input_list = InputStringHexes.split("TOP:")
            print(input_list)
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
                ColorSetHexes.append([hexesandpieces[0],"#"+hexesandpieces[1]])
        else:
            while True:
                #this is for from spreadsheet
                if InputStringHexes.startswith("VELVET_TOP_HAT#"):
                    typeHexinput = InputStringHexes[0:14]
                    pieceHexinput = InputStringHexes[14:21]
                    appendPiece = [typeHexinput, pieceHexinput]
                    ColorSetHexes.append(appendPiece)
                    InputStringHexes = InputStringHexes[21:]
                elif InputStringHexes.startswith("CASHMERE_JACKET#"):
                    typeHexinput = InputStringHexes[0:15]
                    pieceHexinput = InputStringHexes[15:22]
                    appendPiece = [typeHexinput, pieceHexinput]
                    ColorSetHexes.append(appendPiece)
                    InputStringHexes = InputStringHexes[22:]
                elif InputStringHexes.startswith("SATIN_TROUSERS#"):
                    typeHexinput = InputStringHexes[0:14]
                    pieceHexinput = InputStringHexes[14:21]
                    appendPiece = [typeHexinput, pieceHexinput]
                    ColorSetHexes.append(appendPiece)
                    InputStringHexes = InputStringHexes[21:]
                elif InputStringHexes.startswith("OXFORD_SHOES#"):
                    typeHexinput = InputStringHexes[0:12]
                    pieceHexinput = InputStringHexes[12:19]
                    appendPiece = [typeHexinput, pieceHexinput]
                    ColorSetHexes.append(appendPiece)
                    InputStringHexes = InputStringHexes[19:]    
                elif InputStringHexes.startswith("END"):
                    break
                else:
                    print("Split String Error")
                    raise SystemExit
    else:
        with open("seymourdatabase.txt", "r") as fs:
            oldcolors = fs.read().split('\n')
            oldcolors.pop(-1)
            for idx,val in enumerate(oldcolors):
                oldcolors[idx] = val.split(" ")
        ColorSetHexes = databaseExtract()
        for i in range(len(ColorSetHexes)):
            ColorSetHexes[i] = ColorSetHexes[i].split(" ")
    removed_colors = []
    added_colors = []
    old_color_set = set()
    new_color_set = set()

    for i in range(len(oldcolors)):
        old_color_set.add(oldcolors[i][0].upper())
    for i in range(len(ColorSetHexes)):
        new_color_set.add(ColorSetHexes[i][0].upper())
    
    o_color_set = old_color_set.difference(new_color_set)
    n_color_set = new_color_set.difference(old_color_set)
    while len(o_color_set)>0:    
        for value in oldcolors:
            if value[0] in o_color_set:
                removed_colors.append(value)
        break
    while len(n_color_set)>0:
        for value in ColorSetHexes:
            if value[0] in n_color_set:
                added_colors.append(value)
        break




    FinalPrintList = []
    for i in ColorSetHexes:
        iHex = i[2]
        iType = i[1]
        lowestHexHyp, lowestHexName, lowestscorestr, distance = delta(iHex, iType, dictOfHypixelHexColours)
        deltastr = str(f"#{lowestHexHyp}, {lowestHexName}, {lowestscorestr}, {distance}")
        FinalPrintList.append(f"{iType}, {iHex}, {deltastr}, {threeMainVals(iHex)}, {whiteness(iHex)}, {sameThreeAAA(iHex)}, {incollectionrange(iHex)}, {sameThreeABC(iHex)}, {sameAABBCC(iHex)}, {palendromepices(iHex)}, {sameRGBval(iHex)}, {threeTwoSameNums(iHex)}, {allOther(iHex)}, {countofvals(iHex)}")
    changed_list = []
    if len(removed_colors)>0:
        changed_list.append("\nRemoved Colors:")
        for i in range(len(removed_colors)):
            iHex = removed_colors[i][2]
            iType = removed_colors[i][1]
            changed_list.append(f"{iType}, {iHex}")
    if len(added_colors)>0:
        changed_list.append("\nAdded Colors:")
        for i in range(len(added_colors)):
            iHex = added_colors[i][2]
            iType = added_colors[i][1]
            lowestHexHyp, lowestHexName, lowestscorestr, distance = delta(iHex, iType, dictOfHypixelHexColours)
            deltastr = str(f"#{lowestHexHyp}, {lowestHexName}, {lowestscorestr}, {distance}")
            changed_list.append(f"{iType}, {iHex}, {deltastr}, {threeMainVals(iHex)}, {whiteness(iHex)}, {sameThreeAAA(iHex)}, {incollectionrange(iHex)}, {sameThreeABC(iHex)}, {sameAABBCC(iHex)}, {palendromepices(iHex)}, {sameRGBval(iHex)}, {threeTwoSameNums(iHex)}, {allOther(iHex)}, {countofvals(iHex)}")

    return FinalPrintList, changed_list, Auto


if __name__ == '__main__':
    
    piecedata, updatelist, append = MainFunction()
    if append != "0":
        if len(updatelist) > 0:
            if len(updatelist) < 300:
                for i in updatelist:
                    print(i)
                print()
            else:
                print("Many things added/removed\n")
            with open("SheetsUploadDatabase.txt", "w") as fd:
                    dbstr = ""
                    for i in range(len(piecedata)):
                        dbstr = f"{dbstr}{piecedata[i]}\n"
                    fd.write(dbstr)
                    print("Writing Done")
        else:
            print("No changes made since last ran\n")

    else:
        for i in piecedata:
            print(i)
        WritetoFile = input("\nDo you want to append exported hexes the file? (\"0\" for yes, anything else for no)\n")
        if "0" in WritetoFile:
            with open("SheetsUploadDatabase.txt", "a") as fd:
                    dbstr = ""
                    for i in range(len(piecedata)):
                        dbstr = f"{dbstr}{piecedata[i]}\n"
                    fd.write(dbstr)
                    print("Writing Done")