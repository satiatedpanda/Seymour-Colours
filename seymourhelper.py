import math
import re
import math


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




if __name__ == "__main__":

    hexlist = ["SATIN_TROUSERS", "#E7CECE"]

