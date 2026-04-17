import random


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
dictkeys = list(dictOfHypixelHexColours.keys())


random_guess = -1
count = 0

def find_one_random_hex():
    while True:
        try:
            hex_input = input("type a valid 6 letter hexcode, or '-1' for random\n")
            if hex_input == "-1":
                int_hex = random.randint(0,16777216)
                hex_input = hex(int_hex)[2:].upper()
                break
            if len(hex_input) != 6:
                raise ValueError
            correctval_str = "0123456789ABCDEF"
            for char in hex_input:
                if char not in correctval_str:
                    raise ValueError
            int_hex = int(hex_input, 16)    
            break
        except ValueError:
            print("not a valid hexcode\n")

    while random_guess != int_hex:
        random_guess = random.randint(0,16777216)
        count += 1
        if count%1000000 == 0:
            print(f"{count//1000000}m rolls")
    formatted_count = format(count, ",")

    print(f"\nTook {formatted_count} rolls to roll hex #{hex_input}")

def find_one_random_1to1():
    UPPER_BOUND = 16777216 - len(dictOfHypixelHexColours)
    count = 0

    while True:
        random_guess = -1
        piece_types = ["Helm", "Chestplate", "Leggings", "Boots"]
        random_piece = piece_types[random.randint(0,3)]
        while random_guess < UPPER_BOUND:
            random_guess = random.randint(0,16777216)
            count += 1
            if count%1000000 == 0:
                print(f"{count//1000000}m rolls")
        formatted_hex = dictkeys[random_guess-UPPER_BOUND-1]
        dict_hex_name = dictOfHypixelHexColours[formatted_hex]
        if random_piece in dict_hex_name or "/" in dict_hex_name:
            break
        elif any(substring in dict_hex_name for substring in piece_types):
            continue
        if ('3p' in dict_hex_name) and (random_piece == 'Helm'):
            continue
        else:
            break

    formatted_count = format(count, ",")
    print(f"\nTook {formatted_count} rolls to roll {dict_hex_name} {random_piece}, hex {formatted_hex}")

def find_highest_lowest():
    UPPER_BOUND = 16777216 - len(dictOfHypixelHexColours)
    lowest_count = [100000000000, "", ""]
    highest_count = [0, "", ""]    
    average = 0
    random_guess = -1
    try:
        n: int = 100000
        print("starting...\n")
        for i in range(n):
            if i%500 == 0 and i != 0:
                print(f"{i} loops")
            count = 0
            while True:
                random_guess = -1
                piece_types = ["Helm", "Chestplate", "Leggings", "Boots"]
                random_piece = piece_types[random.randint(0,3)]
                while random_guess < UPPER_BOUND:
                    random_guess = random.randint(0,16777216)
                    count += 1
                    if count%1000000 == 0:
                        print(f"{count//1000000}m rolls")
                formatted_hex = dictkeys[random_guess-UPPER_BOUND-1]
                dict_hex_name = dictOfHypixelHexColours[formatted_hex]
                if random_piece in dict_hex_name or "/" in dict_hex_name:
                    break
                elif any(substring in dict_hex_name for substring in piece_types):
                    continue
                if ('3p' in dict_hex_name) and (random_piece == 'Helm'):
                    continue
                else:
                    break
            if lowest_count[0] > count:
                lowest_count = [count, dict_hex_name, random_piece]
            if highest_count[0] < count:
                highest_count = [count, dict_hex_name, random_piece]  
            average = (average*(i)+count)/(i+1)      
        placement_str = format(n, ",")
        print(f"Finding random 1:1 in {placement_str} iterations")
        placement_str = format(int(lowest_count[0]), ",")
        print(f"Lowest count was: {placement_str}. Matched: {lowest_count[1]} {lowest_count[2]}")
        placement_str = format(int(highest_count[0]), ",")
        print(f"Highest count was: {placement_str}. Matched: {highest_count[1]} {highest_count[2]}")
        placement_str = format(int(average), ",")
        print(f"Average count is: {placement_str}")
    except IndexError as e:
        print(e)
        print(len(dictkeys), f"{random_guess-UPPER_BOUND=}")

if __name__ == "__main__":
    find_highest_lowest()
    # find_one_random_1to1()
    # find_one_random_hex()