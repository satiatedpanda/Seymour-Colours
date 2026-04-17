import math
FOURpiecesets = dict([("00FF00", "Pure Green/Emerald/Cactus"),
("FFFF00", "Pure Yellow/Farm Suit"),
("FF0000", "Pure Red/Mushroom"),
("00FFFF", "Pure Cyan"),
("EDAA36", "Pumpkin"),
("FFFFFF", "Pure White/SnowSuit"),
("0000FF", "Pure Blue/Lapis"),
("7A7964", "Miners/Prospecting"),
("FFD700", "Farm Armour/Elanor's Set (Rift)"),
("00BE00", "Growth Armour"),
("B3B3B3", "Heat Armour"),
("000000", "Pure Black/Tara/BatP/ShadowAs/Wither"),
("FF9300", "Armour of Magma"),
("ADFF2F", "Bouncy"),
("E1EB34", "Skeleton Grunt"),
("FF6B0B", "Skeleton Master"),
("FFBC0B", "Skeleton Soldier"),
("D51230", "Zombie Comander"),
("D07F00", "Zombie Soldier"),
("E0FCF7", "Speedster Set/Mercenary Boots"),
("450101", "Crypt Witherlord"),
("993399", "Great Spook"),
("CBD2DB", "Rabbit Armour"),
("C83200", "Yog Armour"),
("FFCCE5", "Fairy Boots (Main)/OG Fairy+ Rest (FFCCE5)"),
("FF99CC", "Fairy Legs (Main)/Dyed Fairy Boots/OG Fairy+ Chest+Helm (FF99CC)"),
("FF66B2", "Fairy Chest (Main)/Dyed Fairy Legs+Boots/OG Fairy+ Helm (FF66B2)"),
("FF3399", "Fairy Helm (Main)/Dyed Fairy Rest (FF3399)"),
("FF007F", "Fairy Dyed (FF007F)"),
("CC0066", "OG Fariy+ boots/Fairy Dyed Rest (CC0066)"),
("99004C", "OG Fairy+ Legs+Boots/Fairy Dyed Helm+Chest (99004C)"),
("660033", "OG Fairy+ Chest+Legs+Boots/Fairy Dyed Helm (660033)"),
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
("CEB8AA", "Livid Dye"),
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
("D50808", "Sangria Dye"),
("7D7D7D", "Secret Dye"),
("324D6C", "Tentacle Dye"),
("FF43A4", "Strawberry Dye"),
("FCD12A", "Treasure Dye"),
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
("191919", "Exo pure black/EleTux Ches+bts/WizmanLegs")
])
fourPkeys = list(FOURpiecesets.keys())

FourpieceSeperate = dict([#Together Below
("9E7003", "Rotten Helm+Boots"),
("017D31", "Rotten Chestplate+Leggings"),
#
#Together Below
("E6E6E6", "Super Heavy Helm+Boots"),
("5A6464", "Super Heavy Chestplate+Leggings"),
#
#Together below
("FFFFFF", "Heavy Helm+Boots"),
("828282", "Heavy Chestplate+Leggings"),
#
#Together Below
("C13C0F", "Salmon Helm+Boots"),
("A82B76", "Salmon Chestplate+Leggings"),
#Together Below
("D48EF2", "Celeste Helm"),
("FF8EDE", "Celeste Chestplate"),
("FF8ECA", "Celeste Leggings"),
("FF8EB6", "Celeste Boots")
])
fourPSepkeys = list(FourpieceSeperate.keys())

THREEpiecesets = dict([("8B0000", "Arachne Armour"),
("4DCC4D", "Leaflet"),
("FFAC00", "Biohazard"),         
("37B042", "Goblin"),                  
("DF2E06", "Rampart"),             
("07031B", "Shimering Light"),                       
("F7DA33", "Blaze Armour"),
("03FCF8", "Glacite"),
("CCE5FF", "Mineral Armour"),
("0B004F", "Angler"),
("FFDC51", "Sponge"),
("606060", "Spooky Armour"),
("24DDE5", "Thunder"),
("A0DAEF", "Frozen Blaze"),
("5B0DAE", "Glossy Mineral Armour"),
("47D147", "Holy Dragon"),
("6F0F08", "Magma Lord"),
("F0E6AA", "Old Dragon"),
("99978B", "Protector Dragon"),
("1B1B1B", "Reaper Armour"),
("002CA6", "Shark Scale Armour"),
("B212E3", "Unstable Dragon"),
("1D1105", "Werewolf"),
("29F0E9", "Wise Dragon"),
("DDE4F0", "Young Dragon"),
("35530A", "Kuudra Follower"),
("BFBCB2", "Adaptive Armour (Outside Dungeon)"),
("E7413C", "Necron Dye"),
("268105", "Skeleton Lord"),
("9B01C1", "Zombie Lord"),
("899E20", "Melon Armour"),
("3588ff", "Vanguard"),
("918F89", "Skeletor"),
("A06540", "Bleached"),
("101555", "Hydra"),
("990D00", "Emperor"),
("10616E", "Sea Walker 3p"),
("586158", "Fallen Star 3p"),
("0E1736", "Primordial Armour 3p"),
("1C9759", "Figmail 3p"),
("0E666D", "Abyssal 3p")
])
threePkeys = list(THREEpiecesets.keys())

threepieceSeperate = dict([#together below
("ED6612", "Flaming Chestplate"),
("CE2C2C", "Moogma Leggings"),
("276114", "Slug Boots"),
#
#together below
("117391", "Guardian Chestplate"),
("7AE82C", "Creeper Pants (Leggings)"),
("000000", "Tarantula Boots"),
#
#together below
("FFA33B", "Beserker Chestplate"),
("FFB727", "Beserker Leggings"),
("FFD427", "Beserker Boots"),
#
#together below
("D91E41", "Strong Dragon Chestplate"),
("E09419", "Strong Dragon Leggings"),
("F0D124", "Strong Dragon Boots"),
#
#together below
("FC2F3C", "Nutcraker Chestplate"),
("FFF9EB", "Nutcraker Leggings"),
("46343A", "Nutcraker Boots"),
#
#together below
("45413C", "Goldor Chestplate"),
("65605A", "Goldor Leggings"),
("88837E", "Goldor Boots"),
#
#together below
("4A14B7", "Maxor Chestplate"),
("5D2FB9", "Maxor Leggings"),
("8969C8", "Maxor Boots"),
#
#together below
("000001", "Necromancer Lord Chestplate"),
("370147", "Necromancer Lord Leggings"),
("400352", "Necromancer Lord Boots"),
#
#together below
("E7413C", "Necron Chestplate"),
("E75C3C", "Necron Leggings"),
("E76E3C", "Necron Boots"),
#
#together below
("1793C4", "Storm Chestplate"),
("17A8C4", "Storm Leggings"),
("1CD4E4", "Storm Boots"),
#
#together below
("2841F1", "Aurora Chestplate"),
("3F56FB", "Aurora Leggings"),
("6184FC", "Aurora Boots"),
#
#together below
("FF6F0C", "Crimson Chestplate"),
("E66105", "Crimson Leggings"),
("E65300", "Crimson Boots"),
#
#together below
("F04729", "Fervor Chestplate"),
("17BF89", "Fervor Leggings"),
("07A674", "Fervor Boots"),
#
#together below
("FFCB0D", "Hollow Chestplate"),
("FFF6A3", "Hollow Leggings"),
("E3FFFA", "Hollow Boots"),
#
#together below
("3E95AF", "Terror Chestplate"),
("5D23D1", "Terror Leggings"),
("7C44EC", "Terror Boots"),
#
#together below
("7A2900", "Cropie Chestplate"),
("94451F", "Cropie Leggings"),
("BB6535", "Cropie Boots"),
#
#together below
("03430E", "Squash Chestplate"),
("0C4A16", "Squash Leggings"),
("13561E", "Squash Boots"),
#
#together below
("58890C", "Fermento Chestplate"),
("6A9C1B", "Fermento Leggings"),
("83B03B", "Fermento Boots"),
#
#together below
("006633", "Canopy Chestplate"),
("006600", "Canopy Leggings"),
("331900", "Canopy Boots"),
#
#together below
("383838", "Cheap Tux Chestplate+Boots"),
("C7C7C7", "Cheap Tux Leggings"),
#
#together below
("191919", "Elegant Tux Chestplate+Boots/Wizardman Leggings"),
("FEFDFC", "Elegant Tux Leggings"),
#
#together below
("332A2A", "Fancy Tux Chestplate+Boots"),
("D4D4D4", "Fancy Tux Leggings"),
#
#together below
("0A0011", "Final Destination Chestplate+Boots"),
("FF75FF", "Final Destination Leggings"),
#
#together below
("F2DF11", "Superior Dragon Chestplate+Leggings"),
("F25D18", "Superior Dragon Boots")
])
threePSepkeys = list(threepieceSeperate.keys())

TWOpiecesets = dict([
#Together below
("35B73B", "Wyld Leggings (Rift)"),
("154918", "Wyld Boots (Rift)"),
#
#Together below
("DEBC15", "Rising Sun Leggings"),
("9F8609", "Rising Sun Boots"),
#
("D400FF", "Starlight Chestplate+Boots"),
#Together Below
("FFFFFF", "Pack Helm"),
("FF0000", "Pack Chestplate")
])
twoPkeys = list(TWOpiecesets.keys())

SinglePieceSets = dict([("D9D9D9", "Stone/Metal/Steel Chestplate"),
("FF4600", "Orange Chestplate (Rift)"),
("FFF200", "Chicken Leggings (Rift)"),
("48FF00", "Femurgrowth Leggings (Rift)"),
("993333", "Leggings of the Coven (Rift) (Base)"),
("04CFD3", "Stereo Pants (Leggings)"),
("0C0C96", "Burned Pants (Rift) (Leggings)"),
("F6DE51", "Charlies Trousers (Leggings)"),
("380024", "Exceedingly Comfy Sneakers (Rift) (Boots)"),
("CC5500", "Farmers Boots"),
("4F2886", "Gunthers Sneakers (Boots)"),
("1A004C", "Snake-in-a-boot (Boots)"),
("BFBFBF", "Spirit Boots"),
("545454", "Squire Boots"),
("808080", "Ghostly Boots"),
("3333FF", "Ugly Boots"),
("8D3592", "Melodys Shoes (Boots)")
])
onePkeys = list(SinglePieceSets.keys())

def rgb2cielab(sR,sG,sB):
    # sR, sG and sB (Standard RGB) input range = 0 ÷ 255
    # X, Y and Z output refer to a D65/2° standard illuminant.
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
    
def deltaEcielab(r1,g1,b1,r2,g2,b2):
    CIElab1 = rgb2cielab(r1,g1,b1)
    CIElab2 = rgb2cielab(r2,g2,b2)
    deltaE = math.sqrt((CIElab2[0]-CIElab1[0])**2 + (CIElab2[1]-CIElab1[1])**2 + (CIElab2[2]-CIElab1[2])**2)
    return deltaE


def MyKey(ScoreString):
    return float(ScoreString[-2:])


VelvetS = input("Vevlet Hat Hexcodes:\n")
CashmereS = input("Cashmere:\n")
SatinsS = input("Satin:\n")
OxfordsS = input("Oxfords:\n")
Velvetstr = VelvetS[1:]
Cashmerestr = CashmereS[1:]
Satinstr = SatinsS[1:]
Oxfordstr = OxfordsS[1:]

#Press Alt+Space, then right clikc to paste in text
VelvetArray = Velvetstr.split('#')
CashmereArray = Cashmerestr.split('#')
SatinArray = Satinstr.split('#')
OxfordArray = Oxfordstr.split('#')
finalList = []

for i in range(len(FOURpiecesets)):
    dicthex = fourPkeys[i]
    HexRed = int(dicthex[0:2], 16)
    HexGreen = int(dicthex[2:4], 16)
    HexBlue = int(dicthex[4:6], 16)
    Vlowestscore = 100000
    VlowestHex = ''
    VTier = ''
    Clowestscore = 100000
    ClowestHex = ''
    CTier = ''
    Slowestscore = 100000
    SlowestHex = ''
    STier = ''
    Xlowestscore = 100000
    XlowestHex = ''  
    XTier = ''  
    for j in range(len(VelvetArray)):     
            pieceHex = VelvetArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Vlowestscore:
                VlowestHex = f'#{pieceHex}'
                Vlowestscore = iScore            
    for j in range(len(CashmereArray)):     
            pieceHex = CashmereArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Clowestscore:
                ClowestHex = f"#{pieceHex}"
                Clowestscore = iScore              
    for j in range(len(SatinArray)):     
            pieceHex = SatinArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Slowestscore:
                SlowestHex = f'#{pieceHex}'
                Slowestscore = iScore    
    for j in range(len(OxfordArray)):     
            pieceHex = OxfordArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Xlowestscore:
                XlowestHex = f'#{pieceHex}'
                Xlowestscore = iScore        
    
    completeness = 12
    Vlowestscoreint = str(Vlowestscore)
    while len(Vlowestscoreint) != 4:
        if len(Vlowestscoreint) > 4:
            Vlowestscoreint = Vlowestscoreint[:-1]
        if len(Vlowestscoreint) < 4:
            Vlowestscoreint = Vlowestscoreint + "0"
    if Vlowestscore < 0.001:
         VTier = f'T0 ({Vlowestscoreint})'
    elif Vlowestscore < 2:
         VTier = f'T1 ({Vlowestscoreint})'
    elif Vlowestscore < 5:
         VTier = f'T2 ({Vlowestscoreint})'
    else:
         VTier = '-'
         completeness -= 3
    if VTier == '-':
        VlowestHex = '-'
    Clowestscoreint = str(Clowestscore)
    while len(Clowestscoreint) != 4:
        if len(Clowestscoreint) > 4:
            Clowestscoreint = Clowestscoreint[:-1]
        if len(Clowestscoreint) < 4:
            Clowestscoreint = Clowestscoreint + "0"
    if Clowestscore < 0.001:
         CTier = f'T0 ({Clowestscoreint})'
    elif Clowestscore < 2:
         CTier = f'T1 ({Clowestscoreint})'
    elif Clowestscore < 5:
         CTier = f'T2 ({Clowestscoreint})'
    else:
         CTier = '-'
         completeness -= 3
    if CTier == '-':
        ClowestHex = '-'
    Slowestscoreint = str(Slowestscore)
    while len(Slowestscoreint) != 4:
        if len(Slowestscoreint) > 4:
            Slowestscoreint = Slowestscoreint[:-1]
        if len(Slowestscoreint) < 4:
            Slowestscoreint = Slowestscoreint + "0"
    if Slowestscore < 0.001:
         STier = f'T0 ({Slowestscoreint})'
    elif Slowestscore < 2:
         STier = f'T1 ({Slowestscoreint})'
    elif Slowestscore < 5:
         STier = f'T2 ({Slowestscoreint})'
    else:
         STier = '-'
         completeness -= 3
    if STier == '-':
        SlowestHex = '-'       
    Xlowestscoreint = str(Xlowestscore)
    while len(Xlowestscoreint) != 4:
        if len(Xlowestscoreint) > 4:
            Xlowestscoreint = Xlowestscoreint[:-1]
        if len(Xlowestscoreint) < 4:
            Xlowestscoreint = Xlowestscoreint + "0"
    if Xlowestscore < 0.001:
         XTier = f'T0 ({Xlowestscoreint})'
    elif Xlowestscore < 2:
         XTier = f'T1 ({Xlowestscoreint})'
    elif Xlowestscore < 5:
         XTier = f'T2 ({Xlowestscoreint})'
    else:
         XTier = '-'
         completeness -= 3
    if XTier == '-':
        XlowestHex = '-'
    if len(str(completeness)) < 2:
        completeness = "0" + str(completeness)        
    finalList.append(f"{FOURpiecesets[dicthex]}, {VTier}, {VlowestHex}, {CTier}, {ClowestHex}, {STier}, {SlowestHex}, {XTier}, {XlowestHex}, {completeness}")

fourPtwofers = ["Rotton", "Super Heavy", "Heavy", "Salmon"]
for i in range(0,8,2):
    rottenVXhex = fourPSepkeys[i]
    rottenCShex = fourPSepkeys[i+1]
    HexRed = int(rottenVXhex[0:2], 16)
    HexGreen = int(rottenVXhex[2:4], 16)
    HexBlue = int(rottenVXhex[4:6], 16)
    XHexRed = int(rottenCShex[0:2], 16)
    XHexGreen = int(rottenCShex[2:4], 16)
    XHexBlue = int(rottenCShex[4:6], 16)
    Vlowestscore = 100000
    VlowestHex = ''
    VTier = ''
    Clowestscore = 100000
    ClowestHex = ''
    CTier = ''
    Slowestscore = 100000
    SlowestHex = ''
    STier = ''
    Xlowestscore = 100000
    XlowestHex = ''  
    XTier = ''  
    for j in range(len(VelvetArray)):     
            pieceHex = VelvetArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Vlowestscore:
                VlowestHex = f'#{pieceHex}'
                Vlowestscore = iScore            
    for j in range(len(CashmereArray)):     
            pieceHex = CashmereArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(XHexRed, XHexGreen, XHexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Clowestscore:
                ClowestHex = f"#{pieceHex}"
                Clowestscore = iScore              
    for j in range(len(SatinArray)):     
            pieceHex = SatinArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(XHexRed, XHexGreen, XHexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Slowestscore:
                SlowestHex = f'#{pieceHex}'
                Slowestscore = iScore    
    for j in range(len(OxfordArray)):     
            pieceHex = OxfordArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Xlowestscore:
                XlowestHex = f'#{pieceHex}'
                Xlowestscore = iScore        

    completeness = 12
    Vlowestscoreint = str(Vlowestscore)
    while len(Vlowestscoreint) != 4:
        if len(Vlowestscoreint) > 4:
            Vlowestscoreint = Vlowestscoreint[:-1]
        if len(Vlowestscoreint) < 4:
            Vlowestscoreint = Vlowestscoreint + "0"
    if Vlowestscore < 0.001:
            VTier = f'T0 ({Vlowestscoreint})'
    elif Vlowestscore < 2:
            VTier = f'T1 ({Vlowestscoreint})'
    elif Vlowestscore < 5:
            VTier = f'T2 ({Vlowestscoreint})'
    else:
            VTier = '-'
            completeness -= 3
    if VTier == '-':
        VlowestHex = '-'
    Clowestscoreint = str(Clowestscore)
    while len(Clowestscoreint) != 4:
        if len(Clowestscoreint) > 4:
            Clowestscoreint = Clowestscoreint[:-1]
        if len(Clowestscoreint) < 4:
            Clowestscoreint = Clowestscoreint + "0"
    if Clowestscore < 0.001:
            CTier = f'T0 ({Clowestscoreint})'
    elif Clowestscore < 2:
            CTier = f'T1 ({Clowestscoreint})'
    elif Clowestscore < 5:
            CTier = f'T2 ({Clowestscoreint})'
    else:
            CTier = '-'
            completeness -= 3
    if CTier == '-':
        ClowestHex = '-'
    Slowestscoreint = str(Slowestscore)
    while len(Slowestscoreint) != 4:
        if len(Slowestscoreint) > 4:
            Slowestscoreint = Slowestscoreint[:-1]
        if len(Slowestscoreint) < 4:
            Slowestscoreint = Slowestscoreint + "0"
    if Slowestscore < 0.001:
            STier = f'T0 ({Slowestscoreint})'
    elif Slowestscore < 2:
            STier = f'T1 ({Slowestscoreint})'
    elif Slowestscore < 5:
            STier = f'T2 ({Slowestscoreint})'
    else:
            STier = '-'
            completeness -= 3
    if STier == '-':
        SlowestHex = '-'       
    Xlowestscoreint = str(Xlowestscore)
    while len(Xlowestscoreint) != 4:
        if len(Xlowestscoreint) > 4:
            Xlowestscoreint = Xlowestscoreint[:-1]
        if len(Xlowestscoreint) < 4:
            Xlowestscoreint = Xlowestscoreint + "0"
    if Xlowestscore < 0.001:
            XTier = f'T0 ({Xlowestscoreint})'
    elif Xlowestscore < 2:
            XTier = f'T1 ({Xlowestscoreint})'
    elif Xlowestscore < 5:
            XTier = f'T2 ({Xlowestscoreint})'
    else:
            XTier = '-'
            completeness -= 3
    if XTier == '-':
        XlowestHex = '-'
    if len(str(completeness)) < 2:
        completeness = "0" + str(completeness) 
    idxn = int(i/2)       
    finalList.append(f"{fourPtwofers[idxn]}, {VTier}, {VlowestHex}, {CTier}, {ClowestHex}, {STier}, {SlowestHex}, {XTier}, {XlowestHex}, {completeness}")

    #end



for i in range(len(THREEpiecesets)):
    dicthex = threePkeys[i]
    HexRed = int(dicthex[0:2], 16)
    HexGreen = int(dicthex[2:4], 16)
    HexBlue = int(dicthex[4:6], 16)
    Clowestscore = 100000
    ClowestHex = ''
    CTier = ''
    Slowestscore = 100000
    SlowestHex = ''
    STier = ''
    Xlowestscore = 100000
    XlowestHex = ''  
    XTier = ''       
    for j in range(len(CashmereArray)):     
            pieceHex = CashmereArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Clowestscore:
                ClowestHex = f"#{pieceHex}"
                Clowestscore = iScore              
    for j in range(len(SatinArray)):     
            pieceHex = SatinArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Slowestscore:
                SlowestHex = f'#{pieceHex}'
                Slowestscore = iScore    
    for j in range(len(OxfordArray)):     
            pieceHex = OxfordArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Xlowestscore:
                XlowestHex = f'#{pieceHex}'
                Xlowestscore = iScore        
    
    completeness = 12
    Clowestscoreint = str(Clowestscore)
    while len(Clowestscoreint) != 4:
        if len(Clowestscoreint) > 4:
            Clowestscoreint = Clowestscoreint[:-1]
        if len(Clowestscoreint) < 4:
            Clowestscoreint = Clowestscoreint + "0"
    if Clowestscore < 0.001:
         CTier = f'T0 ({Clowestscoreint})'
    elif Clowestscore < 2:
         CTier = f'T1 ({Clowestscoreint})'
    elif Clowestscore < 5:
         CTier = f'T2 ({Clowestscoreint})'
    else:
         CTier = '-'
         completeness -= 4
    if CTier == '-':
        ClowestHex = '-'
    Slowestscoreint = str(Slowestscore)
    while len(Slowestscoreint) != 4:
        if len(Slowestscoreint) > 4:
            Slowestscoreint = Slowestscoreint[:-1]
        if len(Slowestscoreint) < 4:
            Slowestscoreint = Slowestscoreint + "0"
    if Slowestscore < 0.001:
         STier = f'T0 ({Slowestscoreint})'
    elif Slowestscore < 2:
         STier = f'T1 ({Slowestscoreint})'
    elif Slowestscore < 5:
         STier = f'T2 ({Slowestscoreint})'
    else:
         STier = '-'
         completeness -= 4
    if STier == '-':
        SlowestHex = '-'       
    Xlowestscoreint = str(Xlowestscore)
    while len(Xlowestscoreint) != 4:
        if len(Xlowestscoreint) > 4:
            Xlowestscoreint = Xlowestscoreint[:-1]
        if len(Xlowestscoreint) < 4:
            Xlowestscoreint = Xlowestscoreint + "0"
    if Xlowestscore < 0.001:
         XTier = f'T0 ({Xlowestscoreint})'
    elif Xlowestscore < 2:
         XTier = f'T1 ({Xlowestscoreint})'
    elif Xlowestscore < 5:
         XTier = f'T2 ({Xlowestscoreint})'
    else:
         XTier = '-'
         completeness -= 4
    if XTier == '-':
        XlowestHex = '-'
    if len(str(completeness)) < 2:
        completeness = "0" + str(completeness)    
    finalList.append(f"{THREEpiecesets[dicthex]}, n/a, n/a, {CTier}, {ClowestHex}, {STier}, {SlowestHex}, {XTier}, {XlowestHex}, {completeness}")


threePtwofers = ["Lava SC", "Monster Hunter", "Beserker", "Strong Dragon", "Nutcracker", 
                 "Goldor", "Maxor", "Necromancer", "Necron", "Storm", "Aurora", "Crimson",
                 "Fervor", "Hollow", "Terror", "Cropie", "Squash", "Fermento", "Canopy"]
for i in range(0,57,3):
    Chex = threePSepkeys[i]
    Shex = threePSepkeys[i+1]
    Xhex = threePSepkeys[i+2]    
    HexRed = int(Chex[0:2], 16)
    HexGreen = int(Chex[2:4], 16)
    HexBlue = int(Chex[4:6], 16)
    XHexRed = int(Shex[0:2], 16)
    XHexGreen = int(Shex[2:4], 16)
    XHexBlue = int(Shex[4:6], 16)
    ZHexRed = int(Xhex[0:2], 16)
    ZHexGreen = int(Xhex[2:4], 16)
    ZHexBlue = int(Xhex[4:6], 16)    
    Clowestscore = 100000
    ClowestHex = ''
    CTier = ''
    Slowestscore = 100000
    SlowestHex = ''
    STier = ''
    Xlowestscore = 100000
    XlowestHex = ''  
    XTier = ''         
    for j in range(len(CashmereArray)):     
            pieceHex = CashmereArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Clowestscore:
                ClowestHex = f"#{pieceHex}"
                Clowestscore = iScore              
    for j in range(len(SatinArray)):     
            pieceHex = SatinArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(XHexRed, XHexGreen, XHexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Slowestscore:
                SlowestHex = f'#{pieceHex}'
                Slowestscore = iScore    
    for j in range(len(OxfordArray)):     
            pieceHex = OxfordArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(ZHexRed, ZHexGreen, ZHexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Xlowestscore:
                XlowestHex = f'#{pieceHex}'
                Xlowestscore = iScore        

    completeness = 12
    Clowestscoreint = str(Clowestscore)
    while len(Clowestscoreint) != 4:
        if len(Clowestscoreint) > 4:
            Clowestscoreint = Clowestscoreint[:-1]
        if len(Clowestscoreint) < 4:
            Clowestscoreint = Clowestscoreint + "0"
    if Clowestscore < 0.001:
            CTier = f'T0 ({Clowestscoreint})'
    elif Clowestscore < 2:
            CTier = f'T1 ({Clowestscoreint})'
    elif Clowestscore < 5:
            CTier = f'T2 ({Clowestscoreint})'
    else:
            CTier = '-'
            completeness -= 4
    if CTier == '-':
        ClowestHex = '-'
    Slowestscoreint = str(Slowestscore)
    while len(Slowestscoreint) != 4:
        if len(Slowestscoreint) > 4:
            Slowestscoreint = Slowestscoreint[:-1]
        if len(Slowestscoreint) < 4:
            Slowestscoreint = Slowestscoreint + "0"
    if Slowestscore < 0.001:
            STier = f'T0 ({Slowestscoreint})'
    elif Slowestscore < 2:
            STier = f'T1 ({Slowestscoreint})'
    elif Slowestscore < 5:
            STier = f'T2 ({Slowestscoreint})'
    else:
            STier = '-'
            completeness -= 4
    if STier == '-':
        SlowestHex = '-'       
    Xlowestscoreint = str(Xlowestscore)
    while len(Xlowestscoreint) != 4:
        if len(Xlowestscoreint) > 4:
            Xlowestscoreint = Xlowestscoreint[:-1]
        if len(Xlowestscoreint) < 4:
            Xlowestscoreint = Xlowestscoreint + "0"
    if Xlowestscore < 0.001:
            XTier = f'T0 ({Xlowestscoreint})'
    elif Xlowestscore < 2:
            XTier = f'T1 ({Xlowestscoreint})'
    elif Xlowestscore < 5:
            XTier = f'T2 ({Xlowestscoreint})'
    else:
            XTier = '-'
            completeness -= 4
    if XTier == '-':
        XlowestHex = '-'
    if len(str(completeness)) < 2:
        completeness = "0" + str(completeness)      
    idxn = int(i/3)  
    finalList.append(f"{threePtwofers[idxn]}, n/a, n/a, {CTier}, {ClowestHex}, {STier}, {SlowestHex}, {XTier}, {XlowestHex}, {completeness}")

    #end

threePChleg = ["Cheap Tux", "Elegant Tux", "Fancy Tux", "Final Destination"]
for i in range(0,8,2):
    rottenVXhex = threePSepkeys[i+57]
    rottenCShex = threePSepkeys[i+58]
    HexRed = int(rottenVXhex[0:2], 16)
    HexGreen = int(rottenVXhex[2:4], 16)
    HexBlue = int(rottenVXhex[4:6], 16)
    XHexRed = int(rottenCShex[0:2], 16)
    XHexGreen = int(rottenCShex[2:4], 16)
    XHexBlue = int(rottenCShex[4:6], 16)
    Clowestscore = 100000
    ClowestHex = ''
    CTier = ''
    Slowestscore = 100000
    SlowestHex = ''
    STier = ''
    Xlowestscore = 100000
    XlowestHex = ''  
    XTier = ''           
    for j in range(len(CashmereArray)):     
            pieceHex = CashmereArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Clowestscore:
                ClowestHex = f"#{pieceHex}"
                Clowestscore = iScore              
    for j in range(len(SatinArray)):     
            pieceHex = SatinArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(XHexRed, XHexGreen, XHexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Slowestscore:
                SlowestHex = f'#{pieceHex}'
                Slowestscore = iScore    
    for j in range(len(OxfordArray)):     
            pieceHex = OxfordArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Xlowestscore:
                XlowestHex = f'#{pieceHex}'
                Xlowestscore = iScore        

    completeness = 12
    Clowestscoreint = str(Clowestscore)
    while len(Clowestscoreint) != 4:
        if len(Clowestscoreint) > 4:
            Clowestscoreint = Clowestscoreint[:-1]
        if len(Clowestscoreint) < 4:
            Clowestscoreint = Clowestscoreint + "0"
    if Clowestscore < 0.001:
            CTier = f'T0 ({Clowestscoreint})'
    elif Clowestscore < 2:
            CTier = f'T1 ({Clowestscoreint})'
    elif Clowestscore < 5:
            CTier = f'T2 ({Clowestscoreint})'
    else:
            CTier = '-'
            completeness -= 4
    if CTier == '-':
        ClowestHex = '-'
    Slowestscoreint = str(Slowestscore)
    while len(Slowestscoreint) != 4:
        if len(Slowestscoreint) > 4:
            Slowestscoreint = Slowestscoreint[:-1]
        if len(Slowestscoreint) < 4:
            Slowestscoreint = Slowestscoreint + "0"
    if Slowestscore < 0.001:
            STier = f'T0 ({Slowestscoreint})'
    elif Slowestscore < 2:
            STier = f'T1 ({Slowestscoreint})'
    elif Slowestscore < 5:
            STier = f'T2 ({Slowestscoreint})'
    else:
            STier = '-'
            completeness -= 4
    if STier == '-':
        SlowestHex = '-'       
    Xlowestscoreint = str(Xlowestscore)
    while len(Xlowestscoreint) != 4:
        if len(Xlowestscoreint) > 4:
            Xlowestscoreint = Xlowestscoreint[:-1]
        if len(Xlowestscoreint) < 4:
            Xlowestscoreint = Xlowestscoreint + "0"
    if Xlowestscore < 0.001:
            XTier = f'T0 ({Xlowestscoreint})'
    elif Xlowestscore < 2:
            XTier = f'T1 ({Xlowestscoreint})'
    elif Xlowestscore < 5:
            XTier = f'T2 ({Xlowestscoreint})'
    else:
            XTier = '-'
            completeness -= 4
    if XTier == '-':
        XlowestHex = '-'
    if len(str(completeness)) < 2:
        completeness = "0" + str(completeness) 
    idxn = int(i/2)       
    finalList.append(f"{threePChleg[idxn]}, n/a, n/a, {CTier}, {ClowestHex}, {STier}, {SlowestHex}, {XTier}, {XlowestHex}, {completeness}")

    #end

twoP = ["Wyld", "Rising Sun"]
for i in range(0,4,2):
    rottenVXhex = twoPkeys[i]
    rottenCShex = twoPkeys[i+1]
    HexRed = int(rottenVXhex[0:2], 16)
    HexGreen = int(rottenVXhex[2:4], 16)
    HexBlue = int(rottenVXhex[4:6], 16)
    XHexRed = int(rottenCShex[0:2], 16)
    XHexGreen = int(rottenCShex[2:4], 16)
    XHexBlue = int(rottenCShex[4:6], 16)
    Slowestscore = 100000
    SlowestHex = ''
    STier = ''
    Xlowestscore = 100000
    XlowestHex = ''  
    XTier = ''                     
    for j in range(len(SatinArray)):     
            pieceHex = SatinArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Slowestscore:
                SlowestHex = f'#{pieceHex}'
                Slowestscore = iScore    
    for j in range(len(OxfordArray)):     
            pieceHex = OxfordArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(XHexRed, XHexGreen, XHexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < Xlowestscore:
                XlowestHex = f'#{pieceHex}'
                Xlowestscore = iScore        

    completeness = 10
    Slowestscoreint = str(Slowestscore)
    while len(Slowestscoreint) != 4:
        if len(Slowestscoreint) > 4:
            Slowestscoreint = Slowestscoreint[:-1]
        if len(Slowestscoreint) < 4:
            Slowestscoreint = Slowestscoreint + "0"
    if Slowestscore < 0.001:
            STier = f'T0 ({Slowestscoreint})'
    elif Slowestscore < 2:
            STier = f'T1 ({Slowestscoreint})'
    elif Slowestscore < 5:
            STier = f'T2 ({Slowestscoreint})'
    else:
            STier = '-'
            completeness -= 5
    if STier == '-':
        SlowestHex = '-'       
    Xlowestscoreint = str(Xlowestscore)
    while len(Xlowestscoreint) != 4:
        if len(Xlowestscoreint) > 4:
            Xlowestscoreint = Xlowestscoreint[:-1]
        if len(Xlowestscoreint) < 4:
            Xlowestscoreint = Xlowestscoreint + "0"
    if Xlowestscore < 0.001:
            XTier = f'T0 ({Xlowestscoreint})'
    elif Xlowestscore < 2:
            XTier = f'T1 ({Xlowestscoreint})'
    elif Xlowestscore < 5:
            XTier = f'T2 ({Xlowestscoreint})'
    else:
            XTier = '-'
            completeness -= 5
    if XTier == '-':
        XlowestHex = '-'
    if len(str(completeness)) < 2:
        completeness = "0" + str(completeness) 
    idxn = int(i/2)       
    finalList.append(f"{twoP[idxn]}, n/a, n/a, n/a, n/a, {STier}, {SlowestHex}, {XTier}, {XlowestHex}, {completeness}")

    #end

for i in range(len(SinglePieceSets)):
    rottenVXhex = onePkeys[i]
    HexRed = int(rottenVXhex[0:2], 16)
    HexGreen = int(rottenVXhex[2:4], 16)
    HexBlue = int(rottenVXhex[4:6], 16)
    if (i == 0) or (i == 1):
        lowestscore = 100000
        lowestHex = ''  
        Tier = ''                     
        for j in range(len(CashmereArray)):     
            pieceHex = CashmereArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < lowestscore:
                lowestHex = f'#{pieceHex}'
                lowestscore = iScore    
        completeness = 10
        lowestscoreint = str(lowestscore)
        while len(lowestscoreint) != 4:
            if len(lowestscoreint) > 4:
                lowestscoreint = lowestscoreint[:-1]
            if len(lowestscoreint) < 4:
                lowestscoreint = lowestscoreint + "0"
        if lowestscore < 0.001:
                Tier = f'T0 ({lowestscoreint})'
        elif lowestscore < 2:
                Tier = f'T1 ({lowestscoreint})'
        elif lowestscore < 5:
                Tier = f'T2 ({lowestscoreint})'
        else:
                Tier = '-'
                completeness -= 10
        if Tier == '-':
            lowestHex = '-'     
        if len(str(completeness)) < 2:
            completeness = "0" + str(completeness) 
        finalList.append(f"{SinglePieceSets[rottenVXhex]}, n/a, n/a, {Tier}, {lowestHex}, n/a, n/a, n/a, n/a, {completeness}")
    if (i > 1) and (i < 7):
        lowestscore = 100000
        lowestHex = ''  
        Tier = ''                     
        for j in range(len(SatinArray)):     
            pieceHex = SatinArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < lowestscore:
                lowestHex = f'#{pieceHex}'
                lowestscore = iScore    
        completeness = 10
        lowestscoreint = str(lowestscore)
        while len(lowestscoreint) != 4:
            if len(lowestscoreint) > 4:
                lowestscoreint = lowestscoreint[:-1]
            if len(lowestscoreint) < 4:
                lowestscoreint = lowestscoreint + "0"
        if lowestscore < 0.001:
                Tier = f'T0 ({lowestscoreint})'
        elif lowestscore < 2:
                Tier = f'T1 ({lowestscoreint})'
        elif lowestscore < 5:
                Tier = f'T2 ({lowestscoreint})'
        else:
                Tier = '-'
                completeness -= 10
        if Tier == '-':
            lowestHex = '-'     
        if len(str(completeness)) < 2:
            completeness = "0" + str(completeness) 
        finalList.append(f"{SinglePieceSets[rottenVXhex]}, n/a, n/a, n/a, n/a, {Tier}, {lowestHex}, n/a, n/a, {completeness}")          
    if i >= 7:
        lowestscore = 100000
        lowestHex = ''  
        Tier = ''                     
        for j in range(len(OxfordArray)):     
            pieceHex = OxfordArray[j]
            pHexRed = int(pieceHex[0:2], 16)
            pHexGreen = int(pieceHex[2:4], 16)
            pHexBlue = int(pieceHex[4:6], 16)
            iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
            if iScore < lowestscore:
                lowestHex = f'#{pieceHex}'
                lowestscore = iScore    
        completeness = 10
        lowestscoreint = str(lowestscore)
        while len(lowestscoreint) != 4:
            if len(lowestscoreint) > 4:
                lowestscoreint = lowestscoreint[:-1]
            if len(lowestscoreint) < 4:
                lowestscoreint = lowestscoreint + "0"
        if lowestscore < 0.001:
                Tier = f'T0 ({lowestscoreint})'
        elif lowestscore < 2:
                Tier = f'T1 ({lowestscoreint})'
        elif lowestscore < 5:
                Tier = f'T2 ({lowestscoreint})'
        else:
                Tier = '-'
                completeness -= 10
        if Tier == '-':
            lowestHex = '-'     
        if len(str(completeness)) < 2:
            completeness = "0" + str(completeness) 
        finalList.append(f"{SinglePieceSets[rottenVXhex]}, n/a, n/a, n/a, n/a, n/a, n/a, {Tier}, {lowestHex}, {completeness}")       

#Minos hunter needs to be implimented
#Starlight
rottenVXhex = twoPkeys[4]
HexRed = int(rottenVXhex[0:2], 16)
HexGreen = int(rottenVXhex[2:4], 16)
HexBlue = int(rottenVXhex[4:6], 16)
Slowestscore = 100000
SlowestHex = ''
STier = ''
Xlowestscore = 100000
XlowestHex = ''  
XTier = ''                     
for j in range(len(CashmereArray)):     
        pieceHex = CashmereArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Slowestscore:
            SlowestHex = f'#{pieceHex}'
            Slowestscore = iScore    
for j in range(len(OxfordArray)):     
        pieceHex = OxfordArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Xlowestscore:
            XlowestHex = f'#{pieceHex}'
            Xlowestscore = iScore        

completeness = 10
Slowestscoreint = str(Slowestscore)
while len(Slowestscoreint) != 4:
    if len(Slowestscoreint) > 4:
        Slowestscoreint = Slowestscoreint[:-1]
    if len(Slowestscoreint) < 4:
        Slowestscoreint = Slowestscoreint + "0"
if Slowestscore < 0.001:
        STier = f'T0 ({Slowestscoreint})'
elif Slowestscore < 2:
        STier = f'T1 ({Slowestscoreint})'
elif Slowestscore < 5:
        STier = f'T2 ({Slowestscoreint})'
else:
        STier = '-'
        completeness -= 5
if STier == '-':
    SlowestHex = '-'       
Xlowestscoreint = str(Xlowestscore)
while len(Xlowestscoreint) != 4:
    if len(Xlowestscoreint) > 4:
        Xlowestscoreint = Xlowestscoreint[:-1]
    if len(Xlowestscoreint) < 4:
        Xlowestscoreint = Xlowestscoreint + "0"
if Xlowestscore < 0.001:
        XTier = f'T0 ({Xlowestscoreint})'
elif Xlowestscore < 2:
        XTier = f'T1 ({Xlowestscoreint})'
elif Xlowestscore < 5:
        XTier = f'T2 ({Xlowestscoreint})'
else:
        XTier = '-'
        completeness -= 5
if XTier == '-':
    XlowestHex = '-'
if len(str(completeness)) < 2:
    completeness = "0" + str(completeness)        
finalList.append(f"Starlight, n/a, n/a, {STier}, {SlowestHex}, n/a, n/a, {XTier}, {XlowestHex}, {completeness}")

rottenVXhex = twoPkeys[-2]
rottenCShex = twoPkeys[-1]
HexRed = int(rottenVXhex[0:2], 16)
HexGreen = int(rottenVXhex[2:4], 16)
HexBlue = int(rottenVXhex[4:6], 16)
XHexRed = int(rottenCShex[0:2], 16)
XHexGreen = int(rottenCShex[2:4], 16)
XHexBlue = int(rottenCShex[4:6], 16)
Slowestscore = 100000
SlowestHex = ''
STier = ''
Xlowestscore = 100000
XlowestHex = ''  
XTier = ''                     
for j in range(len(VelvetArray)):     
        pieceHex = VelvetArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Slowestscore:
            SlowestHex = f'#{pieceHex}'
            Slowestscore = iScore    
for j in range(len(CashmereArray)):     
        pieceHex = CashmereArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(XHexRed, XHexGreen, XHexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Xlowestscore:
            XlowestHex = f'#{pieceHex}'
            Xlowestscore = iScore        

completeness = 10
Slowestscoreint = str(Slowestscore)
while len(Slowestscoreint) != 4:
    if len(Slowestscoreint) > 4:
        Slowestscoreint = Slowestscoreint[:-1]
    if len(Slowestscoreint) < 4:
        Slowestscoreint = Slowestscoreint + "0"
if Slowestscore < 0.001:
        STier = f'T0 ({Slowestscoreint})'
elif Slowestscore < 2:
        STier = f'T1 ({Slowestscoreint})'
elif Slowestscore < 5:
        STier = f'T2 ({Slowestscoreint})'
else:
        STier = '-'
        completeness -= 5
if STier == '-':
    SlowestHex = '-'       
Xlowestscoreint = str(Xlowestscore)
while len(Xlowestscoreint) != 4:
    if len(Xlowestscoreint) > 4:
        Xlowestscoreint = Xlowestscoreint[:-1]
    if len(Xlowestscoreint) < 4:
        Xlowestscoreint = Xlowestscoreint + "0"
if Xlowestscore < 0.001:
        XTier = f'T0 ({Xlowestscoreint})'
elif Xlowestscore < 2:
        XTier = f'T1 ({Xlowestscoreint})'
elif Xlowestscore < 5:
        XTier = f'T2 ({Xlowestscoreint})'
else:
        XTier = '-'
        completeness -= 5
if XTier == '-':
    XlowestHex = '-'
if len(str(completeness)) < 2:
    completeness = "0" + str(completeness)       
finalList.append(f"Pack, {STier}, {SlowestHex}, {XTier}, {XlowestHex}, n/a, n/a, n/a, n/a, {completeness}")

#superior
rottenVXhex = threePSepkeys[-2]
rottenCShex = threePSepkeys[-1]
HexRed = int(rottenVXhex[0:2], 16)
HexGreen = int(rottenVXhex[2:4], 16)
HexBlue = int(rottenVXhex[4:6], 16)
XHexRed = int(rottenCShex[0:2], 16)
XHexGreen = int(rottenCShex[2:4], 16)
XHexBlue = int(rottenCShex[4:6], 16)
Clowestscore = 100000
ClowestHex = ''
CTier = ''
Slowestscore = 100000
SlowestHex = ''
STier = ''
Xlowestscore = 100000
XlowestHex = ''  
XTier = ''           
for j in range(len(CashmereArray)):     
        pieceHex = CashmereArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Clowestscore:
            ClowestHex = f"#{pieceHex}"
            Clowestscore = iScore              
for j in range(len(SatinArray)):     
        pieceHex = SatinArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Slowestscore:
            SlowestHex = f'#{pieceHex}'
            Slowestscore = iScore    
for j in range(len(OxfordArray)):     
        pieceHex = OxfordArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(XHexRed, XHexGreen, XHexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Xlowestscore:
            XlowestHex = f'#{pieceHex}'
            Xlowestscore = iScore        

completeness = 12
Clowestscoreint = str(Clowestscore)
while len(Clowestscoreint) != 4:
    if len(Clowestscoreint) > 4:
        Clowestscoreint = Clowestscoreint[:-1]
    if len(Clowestscoreint) < 4:
        Clowestscoreint = Clowestscoreint + "0"
if Clowestscore < 0.001:
        CTier = f'T0 ({Clowestscoreint})'
elif Clowestscore < 2:
        CTier = f'T1 ({Clowestscoreint})'
elif Clowestscore < 5:
        CTier = f'T2 ({Clowestscoreint})'
else:
        CTier = '-'
        completeness -= 4
if CTier == '-':
    ClowestHex = '-'
Slowestscoreint = str(Slowestscore)
while len(Slowestscoreint) != 4:
    if len(Slowestscoreint) > 4:
        Slowestscoreint = Slowestscoreint[:-1]
    if len(Slowestscoreint) < 4:
        Slowestscoreint = Slowestscoreint + "0"
if Slowestscore < 0.001:
        STier = f'T0 ({Slowestscoreint})'
elif Slowestscore < 2:
        STier = f'T1 ({Slowestscoreint})'
elif Slowestscore < 5:
        STier = f'T2 ({Slowestscoreint})'
else:
        STier = '-'
        completeness -= 4
if STier == '-':
    SlowestHex = '-'       
Xlowestscoreint = str(Xlowestscore)
while len(Xlowestscoreint) != 4:
    if len(Xlowestscoreint) > 4:
        Xlowestscoreint = Xlowestscoreint[:-1]
    if len(Xlowestscoreint) < 4:
        Xlowestscoreint = Xlowestscoreint + "0"
if Xlowestscore < 0.001:
        XTier = f'T0 ({Xlowestscoreint})'
elif Xlowestscore < 2:
        XTier = f'T1 ({Xlowestscoreint})'
elif Xlowestscore < 5:
        XTier = f'T2 ({Xlowestscoreint})'
else:
        XTier = '-'
        completeness -= 4
if XTier == '-':
    XlowestHex = '-'
if len(str(completeness)) < 2:
    completeness = "0" + str(completeness)       
finalList.append(f"Superior dragon, n/a, n/a, {CTier}, {ClowestHex}, {STier}, {SlowestHex}, {XTier}, {XlowestHex}, {completeness}")

#end
#celeste
celesteVhex = fourPSepkeys[8]
celesteChex = fourPSepkeys[9]
celesteShex = fourPSepkeys[10]
celesteXhex = fourPSepkeys[11]
HexRed = int(celesteVhex[0:2], 16)
HexGreen = int(celesteVhex[2:4], 16)
HexBlue = int(celesteVhex[4:6], 16)
CHexRed = int(celesteChex[0:2], 16)
CHexGreen = int(celesteChex[2:4], 16)
CHexBlue = int(celesteChex[4:6], 16)
SHexRed = int(celesteShex[0:2], 16)
SHexGreen = int(celesteShex[2:4], 16)
SHexBlue = int(celesteShex[4:6], 16)
XHexRed = int(celesteXhex[0:2], 16)
XHexGreen = int(celesteXhex[2:4], 16)
XHexBlue = int(celesteXhex[4:6], 16)
Vlowestscore = 100000
VlowestHex = ''
VTier = ''
Clowestscore = 100000
ClowestHex = ''
CTier = ''
Slowestscore = 100000
SlowestHex = ''
STier = ''
Xlowestscore = 100000
XlowestHex = ''  
XTier = ''  
for j in range(len(VelvetArray)):     
        pieceHex = VelvetArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(HexRed, HexGreen, HexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Vlowestscore:
            VlowestHex = f'#{pieceHex}'
            Vlowestscore = iScore            
for j in range(len(CashmereArray)):     
        pieceHex = CashmereArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(CHexRed, CHexGreen, CHexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Clowestscore:
            ClowestHex = f"#{pieceHex}"
            Clowestscore = iScore              
for j in range(len(SatinArray)):     
        pieceHex = SatinArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(SHexRed, SHexGreen, SHexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Slowestscore:
            SlowestHex = f'#{pieceHex}'
            Slowestscore = iScore    
for j in range(len(OxfordArray)):     
        pieceHex = OxfordArray[j]
        pHexRed = int(pieceHex[0:2], 16)
        pHexGreen = int(pieceHex[2:4], 16)
        pHexBlue = int(pieceHex[4:6], 16)
        iScore = deltaEcielab(XHexRed, XHexGreen, XHexBlue, pHexRed, pHexGreen, pHexBlue)
        if iScore < Xlowestscore:
            XlowestHex = f'#{pieceHex}'
            Xlowestscore = iScore        

completeness = 12
Vlowestscoreint = str(Vlowestscore)
while len(Vlowestscoreint) != 4:
    if len(Vlowestscoreint) > 4:
        Vlowestscoreint = Vlowestscoreint[:-1]
    if len(Vlowestscoreint) < 4:
        Vlowestscoreint = Vlowestscoreint + "0"
if Vlowestscore < 0.001:
        VTier = f'T0 ({Vlowestscoreint})'
elif Vlowestscore < 2:
        VTier = f'T1 ({Vlowestscoreint})'
elif Vlowestscore < 5:
        VTier = f'T2 ({Vlowestscoreint})'
else:
        VTier = '-'
        completeness -= 3
if VTier == '-':
    VlowestHex = '-'
Clowestscoreint = str(Clowestscore)
while len(Clowestscoreint) != 4:
    if len(Clowestscoreint) > 4:
        Clowestscoreint = Clowestscoreint[:-1]
    if len(Clowestscoreint) < 4:
        Clowestscoreint = Clowestscoreint + "0"
if Clowestscore < 0.001:
        CTier = f'T0 ({Clowestscoreint})'
elif Clowestscore < 2:
        CTier = f'T1 ({Clowestscoreint})'
elif Clowestscore < 5:
        CTier = f'T2 ({Clowestscoreint})'
else:
        CTier = '-'
        completeness -= 3
if CTier == '-':
    ClowestHex = '-'
Slowestscoreint = str(Slowestscore)
while len(Slowestscoreint) != 4:
    if len(Slowestscoreint) > 4:
        Slowestscoreint = Slowestscoreint[:-1]
    if len(Slowestscoreint) < 4:
        Slowestscoreint = Slowestscoreint + "0"
if Slowestscore < 0.001:
        STier = f'T0 ({Slowestscoreint})'
elif Slowestscore < 2:
        STier = f'T1 ({Slowestscoreint})'
elif Slowestscore < 5:
        STier = f'T2 ({Slowestscoreint})'
else:
        STier = '-'
        completeness -= 3
if STier == '-':
    SlowestHex = '-'       
Xlowestscoreint = str(Xlowestscore)
while len(Xlowestscoreint) != 4:
    if len(Xlowestscoreint) > 4:
        Xlowestscoreint = Xlowestscoreint[:-1]
    if len(Xlowestscoreint) < 4:
        Xlowestscoreint = Xlowestscoreint + "0"
if Xlowestscore < 0.001:
        XTier = f'T0 ({Xlowestscoreint})'
elif Xlowestscore < 2:
        XTier = f'T1 ({Xlowestscoreint})'
elif Xlowestscore < 5:
        XTier = f'T2 ({Xlowestscoreint})'
else:
        XTier = '-'
        completeness -= 3
if XTier == '-':
    XlowestHex = '-'
if len(str(completeness)) < 2:
    completeness = "0" + str(completeness)        
finalList.append(f"Celeste, {VTier}, {VlowestHex}, {CTier}, {ClowestHex}, {STier}, {SlowestHex}, {XTier}, {XlowestHex}, {completeness}")








for i in range(len(finalList)):
    finalList.sort(key=MyKey, reverse=True)
for i in range(len(finalList)):
     print(finalList[i])