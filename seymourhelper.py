import math
import re

def rgb2cielab(rgbhex:str) -> list[float]:
    """Converts a rgb hexcode into CIElab

    Args:
        rgbhex (str): hexcode

    Returns:
        list[float]: list of CIE values of the hexcode
    """
    # sR, sG and sB (Standard RGB) input range = 0 ÷ 255
    # X, Y and Z output refer to a D65/2° standard illuminant.


    sR, sG, sB = rgbdecouple(rgbhex)
    
    sR = float(sR)
    sG = float(sG)
    sB = float(sB)


    var_R = ( sR / 255 )
    var_G = ( sG / 255 )
    var_B = ( sB / 255 )

    if ( var_R > 0.04045 ): 
        var_R = ((var_R + 0.055) / 1.055 )**2.4
    else:                   
        var_R = var_R / 12.92
    if ( var_G > 0.04045 ):
        var_G = ( ( var_G + 0.055 ) / 1.055 )**2.4
    else:                   
        var_G = var_G / 12.92
    if ( var_B > 0.04045 ):
        var_B = ( ( var_B + 0.055 ) / 1.055 )**2.4
    else:
        var_B = var_B / 12.92

    var_R = var_R * 100
    var_G = var_G * 100
    var_B = var_B * 100

    X = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
    Y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
    Z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505

    var_X = X / 95.047
    var_Y = Y / 100.000
    var_Z = Z / 108.883

    if ( var_X > 0.008856 ):
        var_X = var_X**( 1/3 )
    else:                    
        var_X = ( 7.787 * var_X ) + ( 16 / 116 )
    if ( var_Y > 0.008856 ):
        var_Y = var_Y**( 1/3 )
    else:
        var_Y = ( 7.787 * var_Y ) + ( 16 / 116 )
    if ( var_Z > 0.008856 ):
        var_Z = var_Z**( 1/3 )
    else:
        var_Z = ( 7.787 * var_Z ) + ( 16 / 116 )

    CIEL = ( 116 * var_Y ) - 16
    CIEa = 500 * ( var_X - var_Y )
    CIEb = 200 * ( var_Y - var_Z )
    return [CIEL, CIEa, CIEb]
  
def deltaEcielab(rgb1: str,rgb2: str) -> float:
    """Calculates the color differnce between two hexcodes

    Args:
        rgb1 (str): hex 1
        rgb2 (str): hex 2

    Returns:
        float: deltaE
    """
    CIElab1: list[float] = rgb2cielab(rgb1)
    CIElab2: list[float] = rgb2cielab(rgb2)
    deltaE: float = math.sqrt((CIElab2[0]-CIElab1[0])**2 + (CIElab2[1]-CIElab1[1])**2 + (CIElab2[2]-CIElab1[2])**2)
    return deltaE

def rgbDist(rgb1: str, rgb2: str, rgb3: str, rgb4: str) -> float:
    """Calculates average delta of 4 rgb pieces

    Args:
        rgb1 (str): hex1
        rgb2 (str): hex2
        rgb3 (str): hex3
        rgb4 (str): hex4

    Returns:
        float: average deltaE
    """
    dist12 = deltaEcielab(rgb1,rgb2)
    dist13 = deltaEcielab(rgb1,rgb3)
    dist14 = deltaEcielab(rgb1,rgb4)
    dist23 = deltaEcielab(rgb2,rgb3)
    dist24 = deltaEcielab(rgb2,rgb4)
    dist34 = deltaEcielab(rgb3,rgb4)
    return ((dist12+dist13+dist14+dist23+dist24+dist34)/6)

def distanceRGBaway(pieceHex: str, comparisonHex: str) -> int:
    """Calculates abs distance from two hexes in RGB

    Args:
        pieceHex (str): hex 1
        comparisonHex (str): hex 2

    Returns:
        int: abs distance
    """
    red: int
    green: int
    blue: int
    compared_red: int
    compared_green: int
    compared_blue: int
    red, green, blue = rgbdecouple(pieceHex)
    compared_red, compared_green, compared_blue = rgbdecouple(comparisonHex)
    totaldistance: int = abs(compared_red - red) + abs(compared_green - green) + abs(compared_blue - blue)
    return totaldistance

def rgbdecouple(Hexcode: str, toInt: bool = True) -> tuple[str,str,str] | tuple[int,int,int]:
    """Decouples a hexcode into its subsequent R, G, and B values

    Args:
        Hexcode (str): hex to decouple
        toInt (bool, optional): Check if you want to convert decoupled hex to binary int. Defaults to True.

    Returns:
        tuple[str,str,str] | tuple[int,int,int]: returns tuple of str if toInt is false, else returns tuple of ints
    """
    if Hexcode.startswith("#"):
        Hexcode = Hexcode[1:]
    if toInt == True:
        red = int(Hexcode[0:2], 16)
        green = int(Hexcode[2:4], 16)
        blue = int(Hexcode[4:6], 16)
    else:
        red = Hexcode[0:2]
        green = Hexcode[2:4]
        blue = Hexcode[4:6]
    return red, green, blue

def lowestmatch(hex: str, hyphex: str,  current_hex_name: str, LHexName: str, LHexHyp: str,  lowscore: float) -> tuple[str,float,str]:
    """Helper to delta function, checks if new delta is lower than the old delta

    Args:
        hex (str): piece hex
        hyphex (str): hypixel hex for comparison
        current_hex_name (str): current hypixel hex name
        LHexName (str): lowest hex name
        LHexHyp (str): lowest hypixel hexcode
        lowscore (float): lowest delta

    Returns:
        tuple[str,float,str]: tuple in form: new lowest hexcode, new lowest hex name, new lowest delta, new lowest abs
    """
        
    iScore = deltaEcielab(hex, hyphex)
    if iScore < lowscore:
        LHexHyp = hyphex
        lowscore = iScore            
        LHexName = current_hex_name

    return LHexHyp, lowscore, LHexName

def delta(pieceHex: str, typeOfPiece, main_dict: dict[str,str]) -> tuple[str,str,float,int]:
    """Computes the lowest delta between a piece and a dictionary of hexes

    Args:
        pieceHex (_type_): hexcode to compare
        typeOfPiece (_type_): type of piece, Helm, Chest, Legs, or Boots
        main_dict (dict[str,str]): dictionary of hexes to compare

    Returns:
        tuple[str,str,str,int]: tuple in form: lowest hex, name of lowest hex, delta, abs distance
    """
    ArmorTypes = ["VELVET_TOP_HAT", "CASHMERE_JACKET", "SATIN_TROUSERS", "OXFORD_SHOES"]
    if typeOfPiece not in ArmorTypes:
        print(f"Armour Type given: {typeOfPiece}")
    lowestscore: float = 10000.0
    lowestHexHyp = "None"
    lowestHexName = "None"
    PieceTypes = ["Helm", "Chestplate", "Leggings", "Boots"]
    piecetype = PieceTypes[ArmorTypes.index(typeOfPiece)]
    for hyphex in main_dict:
        if piecetype in main_dict[hyphex] or "/" in main_dict[hyphex]: 
            lowestHexHyp, lowestscore, lowestHexName = lowestmatch(pieceHex, hyphex, main_dict[hyphex], lowestHexName, lowestHexHyp, lowestscore) 
            continue
        elif any(substring in main_dict[hyphex] for substring in PieceTypes):
            continue
        if ('3p' in main_dict[hyphex]) and (typeOfPiece == 'VELVET_TOP_HAT'):
            continue 
        else:
            lowestHexHyp, lowestscore, lowestHexName = lowestmatch(pieceHex, hyphex, main_dict[hyphex], lowestHexName, lowestHexHyp, lowestscore) 



    nm = 10
    lowestscorestr = str(lowestscore)
    while len(lowestscorestr) != nm:
        if len(lowestscorestr) > nm:
            lowestscorestr = lowestscorestr[:-1]
        if len(lowestscorestr) < nm:
            lowestscorestr = lowestscorestr + '0'
    if '3p' in lowestHexName:
        lowestHexName = lowestHexName[:-3]
    lowestscorestr = float(lowestscorestr)

    distance = distanceRGBaway(pieceHex, lowestHexHyp)
    return lowestHexHyp, lowestHexName, lowestscorestr, distance

def find_many(instring, *substrings):
    pat = re.compile('|'.join([re.escape(s) for s in substrings]))
    match = pat.search(instring)
    if match is None:
        return -1
    else:
        return match.start() 







if __name__ == "__main__":
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
        ("D9D9D9", "Stone/Metal/Steel Chestplate"),
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

    hexlist = ["SATIN_TROUSERS", "#E7CECE"]
    print(delta(hexlist[1][1:], hexlist[0], dictOfHypixelHexColours))