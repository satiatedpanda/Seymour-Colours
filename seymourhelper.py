import math
import re
import math



class CIEVals:
    def __init__(self, hex, *, cie = None, uuid = None):
        self.hex = hex
        if cie == None:
            self.cie = rgb2cielab(hex)
        else:
            self.cie = cie
        if uuid != None:
            self.uuid = uuid            

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.cie}"

def Hypixel_Dictionary() -> dict[str, str]:
    dictionary: dict[str, str] = dict([("0B004F", "Angler 3p"), #hypixel hexcodes
        ("00FF00", "Pure Green"),
        ("FFFF00", "Pure Yellow"),
        ("4DCC4D", "Leaflet 3p"),
        ("FF0000", "Pure Red"),
        ("EDAA36", "Pumpkin"),
        ("FFAC00", "Biohazard 3p"),
        ("0000FF", "Pure Blue"),
        ("7A7964", "Miners/Prospecting"),
        ("FFD700", "Haymaker 3p/Elanor's Set (Rift)"),
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
        ("E7413C", "Necron Dye/Chest"),
        ("E1EB34", "Skeleton Grunt"),
        ("268105", "Skeleton Lord 3p"),
        ("FF6B0B", "Skeleton Master"),
        ("FFBC0B", "Skeleton Soldier"),
        ("D51230", "Zombie Comander"),
        ("9B01C1", "Zombie Lord 3p"),
        ("D07F00", "Zombie Soldier"),
        ("E0FCF7", "Speedster Set/Mercenary Bts"),
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
        ("CC0066", "OG Fairy Dyed (CC0066)"),
        ("99004C", "OG Fairy Dyed (99004C)"),
        ("660033", "OG Fairy Dyed (660033)"),
        ("FFCCFF", "OG Fairy Dyed (FFCCFF)"),
        ("FF99FF", "OG Fairy Dyed (FF99FF)"),
        ("E5CCFF", "OG Fairy Dyed (E5CCFF)"),
        ("CC99FF", "OG Fairy Dyed (CC99FF)"),
        ("FF66FF", "OG Fairy Dyed (FF66FF)"),
        ("FF33FF", "OG Fairy Dyed (FF33FF)"),
        ("B266FF", "OG Fairy Dyed (B266FF)"),
        ("9933FF", "OG Fairy Dyed (9933FF)"),
        ("FF00FF", "Pure Pink/OG Fairy Dyed (FF00FF)"),
        ("CC00CC", "OG Fairy Dyed (CC00CC)"),
        ("7F00FF", "OG Fairy Dyed (7F00FF)"),
        ("6600CC", "OG Fairy Dyed (6600CC)"),
        ("990099", "OG Fairy Dyed (990099)"),
        ("660066", "OG Fairy Dyed (660066)"),
        ("4C0099", "OG Fairy Dyed (4C0099)"),
        ("330066", "OG Fairy Dyed (330066)"),
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
        ("F9FFFE", "1.12 White"),
        ("9D9D97", "1.12 Light Gray"),
        ("474F52", "1.12 Gray"),
        ("1D1D21", "1.12 Black"),
        ("835432", "1.12 Brown"),
        ("B02E26", "1.12 Red"),
        ("F9801D", "1.12 Orange"),      
        ("FED83D", "1.12 Yellow"),
        ("80C71F", "1.12 Lime"),
        ("5E7C16", "1.12 Green"),
        ("169C9C", "1.12 Cyan"),
        ("3AB3DA", "1.12 Light Blue"),
        ("3C44AA", "1.12 Blue"),
        ("8932B8", "1.12 Purple"),
        ("C74EBD", "1.12 Magenta"),    
        ("F38BAA", "1.12 Pink"), 
        ("E25A16", "Helix 3p"),   
        ("FF700A", "Thermodynamic 3p"),
        # ("9E00B2", "Great Spook - 9E00B2"),     
        # ("9700AA", "Great Spook - 9700AA"),
        # ("9000A3", "Great Spook - 9000A3"),
        # ("89009B", "Great Spook - 89009B"),
        # ("830093", "Great Spook - 830093"),
        # ("7C008B", "Great Spook - 7C008B"),
        # ("750084", "Great Spook - 750084"),
        # ("6E007C", "Great Spook - 6E007C"),
        # ("670074", "Great Spook - 670074"),
        # ("60006C", "Great Spook - 60006C"),
        # ("590065", "Great Spook - 590065"),
        # ("52005D", "Great Spook - 52005D"),          
        # ("4C0055", "Great Spook - 4C0055"),
        # ("45004D", "Great Spook - 45004D"),
        # ("3E0046", "Great Spook - 3E0046"),
        # ("37003E", "Great Spook - 37003E"),
        # ("300036", "Great Spook - 300036"),           
        # ("29002E", "Great Spook - 29002E"),
        # ("220027", "Great Spook - 220027"),
        # ("1B001F", "Great Spook - 1B001F"),
        # ("150017", "Great Spook - 150017"),
        # ("0E000F", "Great Spook - 0E000F"),
        # ("111111", "Black-White - 1s"),
        # ("222222", "Black-White - 2s"),
        # ("333333", "Black-White - 3s"),
        # ("444444", "Black-White - 4s"),
        # ("555555", "Black-White - 5s"),
        # ("666666", "Black-White - 6s"),
        # ("777777", "Black-White - 7s"),
        # ("888888", "Black-White - 8s"),
        # ("AAAAAA", "Black-White - As"),
        # ("BBBBBB", "Black-White - Bs"),
        # ("CCCCCC", "Black-White - Cs"),
        # ("DDDDDD", "Black-White - Ds"),
        # ("EEEEEE", "Black-White - Es"),
        


        # ("FCFCFC", "Ghostly Boots - FCFCFC"),
        # ("F5F5F5", "Ghostly Boots - F5F5F5"),
        # ("E9E9E9", "Ghostly Boots - E9E9E9"),
        # ("C6C6C6", "Ghostly Boots - C6C6C6"),
        # ("B0B0B0", "Ghostly Boots - B0B0B0"),
        # ("989898", "Ghostly Boots - 989898"),
        # ("686868", "Ghostly Boots - 686868"),
        # ("505050", "Ghostly Boots - 505050"),
        # ("3A3A3A", "Ghostly Boots - 3A3A3A"),
        # ("272727", "Ghostly Boots - 272727"),
        # ("171717", "Ghostly Boots - 171717"),
        # ("0B0B0B", "Ghostly Boots - 0B0B0B"),
        # ("040404", "Ghostly Boots - 040404"),
        # ("010101", "Ghostly Boots - 010101"),

        #all below this are specific
        ("35B73B", "Wyld Leggings (Rift)"),
        ("154918", "Wyld Boots (Rift)"),
        ("ED6612", "Flaming Chestplate"),
        ("CE2C2C", "Moogma Leggings"),
        ("276114", "Slug Boots"),
        ("117391", "Guardian Chestplate"),
        ("7AE82C", "Creeper Pants (Leggings)"),
        ("FFA33B", "Berserker Chestplate"),
        ("FFB727", "Berserker Leggings"),
        ("FFD427", "Berserker Boots"),
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
        ("017D31", "Backwater 3p/Rotten Cht+Lgs"),
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
        ("D9D9D9", "Stone-Metal-Steel Chestplate"),
        # ("D9D9D9", "Stone-Metal-Steel Chestplate+Ghostly Boots - D9D9D9"),        
        ("FF4600", "Orange Chestplate (Rift)"),
        ("FFF200", "Chicken Leggings (Rift)"),
        ("48FF00", "Femurgrowth Leggings (Rift)"),
        ("04CFD3", "Stereo Pants (Leggings)"),
        ("380024", "Exceedingly Comfy Sneakers (Rift) (Boots)"),
        ("CC5500", "Farmers Boots"),
        ("4F2886", "Gunthers Sneakers (Rift) (Boots)"),
        ("1A004C", "Snake-in-a-boot (Rift) (Boots)"),
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
        ("3333FF", "Ugly Boots (Rift)"),
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
        ("FFE501", "Helianthus Leggings"),
        ("FDE862", "Farmhand Helm"),
        ("EC041F", "Farmhand Chestplate"),
        ("4A4884", "Farmhand Leggings"),
        ("FFA73F", "Sprout Chestplate"),
        ("FF8E09", "Sprout Leggings"),
        ("AC3900", "Sprout Boots"),
        ("F8D086", "Tater Chestplate"),
        ("C8973A", "Tater Leggings"),
        ("9A5500", "Tater Boots")
        ])
    return dictionary

def rgb2cielab(rgbhex:str) -> tuple[float, float, float]:
    """Converts a rgb hexcode into CIElab

    Args:
        rgbhex (str): hexcode

    Returns:
        tuple[float, float, float]: tuple of CIE values of the hexcode
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

    X = var_R * 0.4124564 + var_G * 0.3575761 + var_B * 0.1804375
    Y = var_R * 0.2126729 + var_G * 0.7151522 + var_B * 0.0721750
    Z = var_R * 0.0193339 + var_G * 0.1191920 + var_B * 0.9503041

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
    return (CIEL, CIEa, CIEb)
  
def deltaEcielab(rgb1: str,rgb2: str) -> float:
    """Calculates the color differnce between two hexcodes

    Args:
        rgb1 (str): hex 1
        rgb2 (str): hex 2

    Returns:
        float: deltaE
    """
    CIElab1: tuple[float, float, float] = rgb2cielab(rgb1)
    CIElab2: tuple[float, float, float] = rgb2cielab(rgb2)
    deltaE: float = math.sqrt((CIElab2[0]-CIElab1[0])**2 + (CIElab2[1]-CIElab1[1])**2 + (CIElab2[2]-CIElab1[2])**2)
    return deltaE

def rgbDist(rgb1: str, rgb2: str, rgb3: str, rgb4: str) -> float: # THIS IS HORRIBLE
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

def find_many(instring, *substrings):
    pat = re.compile('|'.join([re.escape(s) for s in substrings]))
    match = pat.search(instring)
    if match is None:
        return -1
    else:
        return match.start() 
 
def int_to_rgb(integer: int, desired_length: int = 6):
    hexcode ="#" + hex(integer)[2:].rjust(desired_length,"0")
    if len(hexcode) != desired_length + 1:
        print("error, hex length does not match desired length")
        print(hexcode)
        print(desired_length, "length")
        exit()
    return hexcode.upper()

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

def assignCieHyphexes() -> None: #this writes to file. only run when adding new hexes
    d = list(Hypixel_Dictionary().items())
    f = []
    for i in d:
        temp_name = i[1].replace(" ", "_")
        tem_hex = i[0]
        cie = rgb2cielab(tem_hex)
        f.append(f"{temp_name} {tem_hex} {cie[0]} {cie[1]} {cie[2]}")
    

    with open("personal_databases\HypixelDictionaryCIE.txt", "w") as fd:
        dbstr = ""
        for i in range(len(f)):
            dbstr = f"{f[i]}\n"
            fd.write(dbstr)
        print("Writing Done")

def readCIEvals() -> dict[str, tuple[str, float, float, float]]:
    """Reads and Returns list of hypixel hexes' cie vals

    Returns:
        dict: dict[str, tuple[str, float, float, float]]
    """
    dict_list: list
    hyp_dict = {}
    with open("personal_databases\HypixelDictionaryCIE.txt", "r") as fd:
        dict_list = fd.read().split("\n")
        dict_list.pop()
    for idx, i in enumerate(dict_list):
        temp_list = i.split()
        temp_tuple = (temp_list[0].replace("_", " "), float(temp_list[2]), float(temp_list[3]), float(temp_list[4]))
        i = [temp_list[0].replace("_", " "), temp_list[1], temp_tuple]
        dict_list[idx] = i
        hyp_dict[temp_list[1]] = temp_tuple
    return hyp_dict

def avgabsSet(hex1, hex2, hex3, hex4): #ABS SET
    dist12 = distanceRGBaway(hex1,hex2)
    dist13 = distanceRGBaway(hex1,hex3)
    dist14 = distanceRGBaway(hex1,hex4)
    dist23 = distanceRGBaway(hex2,hex3)
    dist24 = distanceRGBaway(hex2,hex4)
    dist34 = distanceRGBaway(hex3,hex4)
    avg = (dist12+dist13+dist14+dist23+dist24+dist34)/6
    return (f"{avg:.3f}")

def avgdeltaESets(hex1: CIEVals, hex2: CIEVals, hex3: CIEVals, hex4: CIEVals):

    """Calculates average delta of 4 hexcode pieces

    Returns:
        _type_: avg deltaE
    """
    dist12 = deltaECie(hex1,hex2)
    dist13 = deltaECie(hex1,hex3)
    dist14 = deltaECie(hex1,hex4)
    dist23 = deltaECie(hex2,hex3)
    dist24 = deltaECie(hex2,hex4)
    dist34 = deltaECie(hex3,hex4)
    return ((dist12+dist13+dist14+dist23+dist24+dist34)/6)

def deltaECie(hex1: CIEVals, hex2: CIEVals):

    CIElab1 = hex1.cie
    CIElab2 = hex2.cie
    deltaE: float = math.sqrt((CIElab2[0]-CIElab1[0])**2 + (CIElab2[1]-CIElab1[1])**2 + (CIElab2[2]-CIElab1[2])**2)
    return deltaE

def fastlowestmatch(hex: CIEVals, hyphex: CIEVals,  current_hex_name: str, LHexName: str, LHexHyp: str,  lowscore: float) -> tuple[str,float,str]:
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
        
    iScore = deltaECie(hex, hyphex)
    if iScore < lowscore:
        LHexHyp = hyphex.hex
        lowscore = iScore            
        LHexName = current_hex_name

    return LHexHyp, lowscore, LHexName




def quickSetDelta(hex1: CIEVals, hex2: CIEVals, hex3: CIEVals, hex4: CIEVals): #DELTA SET, CIE76
    avg = avgdeltaESets(hex1, hex2, hex3, hex4)
    avgABS = avgabsSet(hex1.hex, hex2.hex, hex3.hex, hex4.hex)
    # print(f"Average delta of [{hex1.hexcode}, {hex2.hex}, {hex3.hex}, {hex4.hex}] is:\n{avg:.5f} and {avgABS} abs")  
    return (avg, avgABS)


if __name__ == "__main__":

    hexlist = ["SATIN_TROUSERS", "#E7CECE"]
    # print(rgbDist("#d6d1ed", "#d2d0ed", "#d3d0ed", "#d5d1ee"))
    # print(readCIEvals())
    assignCieHyphexes()
    # print(type(Hypixel_Dictionary()))