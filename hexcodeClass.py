from collections import Counter
from math import sqrt
from seymourhelper import rgbdecouple, distanceRGBaway, lowestmatch, Hypixel_Dictionary, readCIEvals, CIEVals, fastlowestmatch



def DatabaseToHex():
    database: list[Hexcode] = []
    with open("personal_databases\seymourdatabase.txt", "r") as fs:
        oldcolors = fs.read().split('\n')
        oldcolors.pop(-1)
        for val in oldcolors:
            temp = val.split(" ")
            database.append(Hexcode(temp[2], temp[1], temp[0]))
    return database




class Hexcode:
    def __init__(self, hexcode: str, piecetype: str = "NONE", uuid: str = None):
        self.hexcode = hexcode
        self.piecetype = piecetype
        self.uuid = uuid
        self.cie = CIEVals(self.hexcode)

    def assign_all_attributes(self, dictionary: dict | None = None):
        self.major_digits: str
        self.isPalendrome: bool
        self.isPatternAxAxAx: bool
        self.isPatternABCABC: bool    
        self.isPatternAABBCC: bool    
        self.num_same_digit: int     
        self.isthreextwo_nums: bool   
        self.grayness: str #float in type str
        self.inCollectionRange: bool
        self.everthing_else: str | bool
        self.pdelta: tuple[str,str,float,int]
        # self.delta() # CAN ADD SEPERATE DICTIONARY
        if dictionary == None:
            self.fastdelta()
        else:
            self.fastdelta(dictionary)
        self.threeMainVals()
        self.palendromepices()        
        self.sameThreeAAA()
        self.sameThreeABC()
        self.sameAABBCC()
        self.countofvals()
        self.threeTwoSameNums()
        self.whiteness()
        self.incollectionrange()
        self.allOther()

    def rename_all_false(self):
        lst = [self.isPalendrome, self.isPatternAxAxAx, self.isPatternABCABC, self.isPatternAABBCC, self.isthreextwo_nums, self.inCollectionRange, self.everthing_else]
        lstss = ["isPalendrome", "isPatternAxAxAx", "isPatternABCABC", "isPatternAABBCC", "isthreextwo_nums", "inCollectionRange", "everthing_else"]        
        for idx, attribute in enumerate(lst):
            if attribute == False:
                setattr(self, lstss[idx], "") 

    def __repr__(self):
        return str(self)

    def __str__(self):
        uuids = f" {self.uuid}" if self.uuid is not None else ""
        return f"{self.hexcode} {self.piecetype}{uuids}"

    def threeMainVals(self) -> None:
        pieceHex = self.hexcode
        if pieceHex[0] == "#":
            pieceHex = pieceHex[1:]
        AxBxCx = f"{pieceHex[0]}{pieceHex[2]}{pieceHex[4]}"
        self.major_digits =  f"{AxBxCx}"

    def palendromepices(self) -> None:
        pieceHex = self.hexcode
        if pieceHex[0] == "#":
            pieceHex = pieceHex[1:]
        if (pieceHex[0] == pieceHex[5]) and (pieceHex[1] == pieceHex[4]) and (pieceHex[2] == pieceHex[3]):
            self.isPalendrome = True
        else:
            self.isPalendrome = False

    def sameThreeAAA(self) -> None:
        pieceHex = self.hexcode
        if pieceHex[0] == "#":
            pieceHex = pieceHex[1:]
        if pieceHex[0] == pieceHex[2] == pieceHex[4]:
            self.isPatternAxAxAx = True
        else:
            self.isPatternAxAxAx = False
 
    def sameThreeABC(self) -> None:
        pieceHex = self.hexcode
        if pieceHex[0] == "#":
            pieceHex = pieceHex[1:]
        if pieceHex[0:3] == pieceHex[3:6]:
            self.isPatternABCABC = True
        else:
            self.isPatternABCABC = False
     
    def sameAABBCC(self) -> None:
        pieceHex = self.hexcode        
        if pieceHex[0] == "#":
            pieceHex = pieceHex[1:]
        if (pieceHex[0] == pieceHex[1]) and (pieceHex[2] == pieceHex[3]) and (pieceHex[4] == pieceHex[5]):
            self.isPatternAABBCC = True
        else:
            self.isPatternAABBCC = False
    
    def countofvals(self) -> None:
        pieceHex = self.hexcode
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

        self.num_same_digit = cnt

    def threeTwoSameNums(self) -> None:
        pieceHex = self.hexcode
        if pieceHex[0] == "#":
            pieceHex = pieceHex[1:]
        a = list(pieceHex)
        x = Counter(a)
        x_values = list(x.values())
        if (len(x_values) == 3) and (x_values[0] == 2) and (x_values[1] == 2):
            self.isthreextwo_nums = True
        else:
            self.isthreextwo_nums = False     

    def whiteness(self) -> None:
        piecehex = self.hexcode
        "parametric equation for line"
        'v = <1,1,1>'
        "p = (1,1,1)"
        red, green, blue = rgbdecouple(piecehex)
        rprod = green - blue
        gprod = blue - red
        bprod = red - green
        self.grayness = f"{(sqrt((rprod**2) + (gprod**2) + (bprod**2))/1.7):.3f}"

    def incollectionrange(self) -> None:
        pieceHex = self.hexcode
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
                self.inCollectionRange = False
        if 3 in {lowvalnum, highvalnum}:
            self.inCollectionRange = True
        else:
            self.inCollectionRange = False
     
    def allOther(self) -> None:
        pieceHex = self.hexcode
        if pieceHex[0] == "#":
            pieceHex = pieceHex[1:]
        self.everthing_else = False            
        #includes words, hexes with only 1 color, and whatever else I feel like adding
        wordlist = ["DECODE", "D1ED", "B00B", "BEEF", "C0FFEE",
                    "BEAD", "DEAD", "DEED", "DECADE", "FADE", "BA11",
                    "B1EED", "FACE", "F00D", "FEED", "FACADE", "6969", "9696", "CAFE",
                    "CEA5E", "B0D1E5", "CA5E", "B033C1", "DEF1ED", "D1CE", "AC1D",
                    "BADD1E", "EDD1E", "FEEB1E", "C0DE","BADA55", "007AC0",
                    "C0C0", "DEAF", "DEC1DE", "AD1DA5", "CA1C",
                    "ABCDEF", "ABCDE", "ABCD", "D15C0",
                    "C0DA", "2025", "2024", "2026", "ACAC1A", "CA551E"]     
        if (len(pieceHex) - len(pieceHex.lstrip('0'))) > 2:
            if (len(pieceHex) - len(pieceHex.lstrip('0'))) == 3:
                self.everthing_else = "3 length"
            if (len(pieceHex) - len(pieceHex.lstrip('0'))) == 4:
                self.everthing_else = "2 length"        
            if (len(pieceHex) - len(pieceHex.lstrip('0'))) == 5:
                self.everthing_else = "Single Length!"    
            return
        
        for i in range(len(wordlist)):
            if wordlist[i] in pieceHex:
                self.everthing_else = wordlist[i]
                return


        if (self.num_same_digit == 3) and (len(list(set(pieceHex))) == 2):
            self.everthing_else = "2L-repeaters"
            return

        if self.num_same_digit > 3:
            char_lst = "0123456789ABCDEF"
            for char in char_lst:
                current_char = char * 4
                if current_char in pieceHex:
                    self.everthing_else = "True "+ char + "'s"
                    return
            self.everthing_else = str(max(pieceHex, key=pieceHex.count)) + "'s"
            return

    def delta(self, main_dict: dict[str,str] | None = None) -> tuple:
        """Computes the lowest delta between a piece and a dictionary of hexes

        Args:
            main_dict (dict[str,str] | None): dictionary of hexes to compare. Defaults to None, and assigns to entire hypixel hexcodes
        """
        pieceHex = self.hexcode
        typeOfPiece = self.piecetype
        if main_dict == None:
            main_dict = Hypixel_Dictionary()
        ArmorTypes = ["VELVET_TOP_HAT", "CASHMERE_JACKET", "SATIN_TROUSERS", "OXFORD_SHOES", "NONE"]
        if typeOfPiece not in ArmorTypes:
            print(f"Armour Type given: {typeOfPiece}")
        lowestscore: float = 10000.0
        lowestHexHyp = "None"
        lowestHexName = "None"
        PieceTypes = ["Helm", "Chestplate", "Leggings", "Boots", "NONE"]
        piecetype = PieceTypes[ArmorTypes.index(typeOfPiece)]
        for hyphex in main_dict:
            if piecetype in main_dict[hyphex] or "/" in main_dict[hyphex]: 
                lowestHexHyp, lowestscore, lowestHexName = lowestmatch(pieceHex, hyphex, main_dict[hyphex], lowestHexName, lowestHexHyp, lowestscore) 
                continue
            elif (typeOfPiece != "NONE") and any(substring in main_dict[hyphex] for substring in PieceTypes):
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
        # if '3p' in lowestHexName:
        #     lowestHexName = lowestHexName[:-3]
        lowestscorestr = float(lowestscorestr)

        distance = distanceRGBaway(pieceHex, lowestHexHyp)
        lowestHexHyp = "#"+lowestHexHyp if lowestHexHyp.startswith("#") is not True else lowestHexHyp
        self.pdelta = lowestHexHyp, lowestHexName, lowestscorestr, distance
        return self.pdelta
 
    def fastdelta(self, insert_dict: dict[str,str] | None = None) -> tuple:
        """Computes the lowest delta between a piece and a dictionary of hexes

        Args:
            insert_dict (dict[str,str] | None): dictionary of hexes to compare. Defaults to None, and assigns to entire hypixel hexcodes.
        """
        main_dict: dict[str, tuple[str, float, float, float]]
        pieceHex = self.hexcode
        piCIE = CIEVals(pieceHex)        
        typeOfPiece = self.piecetype
        temp_dict = {}
        if insert_dict == None: #one off case where you only want to compute 1-2 deltas
            main_dict = readCIEvals()
        elif type(list(insert_dict.values())[0][0]) == str and type(list(insert_dict.values())[0][2]) == float: #checks if insterted dict fits main_dict structure
            main_dict = insert_dict
        else:
            for key, val in insert_dict.items():
                temp_cie = CIEVals(key)
                temp_dict[key] = (val, temp_cie.cie[0], temp_cie.cie[1], temp_cie.cie[2])
            main_dict = temp_dict
        ArmorTypes = ["VELVET_TOP_HAT", "CASHMERE_JACKET", "SATIN_TROUSERS", "OXFORD_SHOES", "NONE"]
        if typeOfPiece not in ArmorTypes:
            print(f"Armour Type given: {typeOfPiece}")
        lowestscore: float = 10000.0
        lowestHexHyp = "None"
        lowestHexName = "None"
        PieceTypes = ["Helm", "Chestplate", "Leggings", "Boots", "NONE"]
        piecetype = PieceTypes[ArmorTypes.index(typeOfPiece)]
        for hyphex, vals in main_dict.items():
            temp_piece_type = vals[0]
            hyCIE = CIEVals(hyphex, cie=(vals[1], vals[2], vals[3]))

            if piecetype in temp_piece_type or "/" in temp_piece_type: 
                lowestHexHyp, lowestscore, lowestHexName = fastlowestmatch(piCIE, hyCIE, temp_piece_type, lowestHexName, lowestHexHyp, lowestscore) 
                continue
            elif (typeOfPiece != "NONE") and any(substring in temp_piece_type for substring in PieceTypes):
                continue
            if ('3p' in temp_piece_type) and (typeOfPiece == 'VELVET_TOP_HAT'):
                continue 
            else:
                lowestHexHyp, lowestscore, lowestHexName = fastlowestmatch(piCIE, hyCIE, temp_piece_type, lowestHexName, lowestHexHyp, lowestscore) 



        nm = 10
        lowestscorestr = str(lowestscore)
        while len(lowestscorestr) != nm:
            if len(lowestscorestr) > nm:
                lowestscorestr = lowestscorestr[:-1]
            if len(lowestscorestr) < nm:
                lowestscorestr = lowestscorestr + '0'
        # if '3p' in lowestHexName:
        #     lowestHexName = lowestHexName[:-3]
        lowestscorestr = float(lowestscorestr)

        distance = distanceRGBaway(pieceHex, lowestHexHyp)
        lowestHexHyp = "#"+lowestHexHyp if lowestHexHyp.startswith("#") is not True else lowestHexHyp
        self.pdelta = lowestHexHyp, lowestHexName, lowestscorestr, distance
        return self.pdelta
 

    @staticmethod
    def sameRGBval(pieceHex: str) -> bool: # unused       
        if pieceHex[0] == "#":
            pieceHex = pieceHex[1:]
        if pieceHex[0:2] == pieceHex[2:4] == pieceHex[4:6]:
            return True
        else:
            return False







if __name__ == "__main__":
    # temp_hex = Hexcode("#232334")
    temp_hex = Hexcode("#CC0066", "CASHMERE_JACKET")
    temp_hex.assign_all_attributes()    
    print(temp_hex.pdelta)