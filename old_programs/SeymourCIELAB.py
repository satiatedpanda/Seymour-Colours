import math

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

def rgbDist(r1,g1,b1,r2,g2,b2,r3,g3,b3,r4,g4,b4):
    #hi
    
    dist12 = deltaEcielab(r1,g1,b1,r2,g2,b2)
    dist13 = deltaEcielab(r1,g1,b1,r3,g3,b3)
    dist14 = deltaEcielab(r1,g1,b1,r4,g4,b4)
    dist23 = deltaEcielab(r2,g2,b2,r3,g3,b3)
    dist24 = deltaEcielab(r2,g2,b2,r4,g4,b4)
    dist34 = deltaEcielab(r3,g3,b3,r4,g4,b4)
    return ((dist12+dist13+dist14+dist23+dist24+dist34)/6)

def MyKey(ScoreString):
    return float(ScoreString[32:])

def MyKey2(ScoreString):
    ScoreString = str(ScoreString)
    return int(ScoreString.count('#'))

def HexSortALL():
    LowScoreHexes = []
    for i in range(len(VelvetArray)):
        VelvR = int(VelvetArray[i][0:2], 16)
        VelvG = int(VelvetArray[i][2:4], 16)
        VelvB = int(VelvetArray[i][4:6], 16)
        sumdistlowC = 10000
        sumdistlowS = 10000
        sumdistlowO = 10000
        hexCashlow = ''
        hexSatlow = ''
        hexOxlow = ''
        for j in range(len(CashmereArray)):
            CasR = int(CashmereArray[j][0:2], 16)
            CasG = int(CashmereArray[j][2:4], 16)
            CasB = int(CashmereArray[j][4:6], 16)
            distVelCas = deltaEcielab(VelvR,VelvG,VelvB,CasR,CasG,CasB)
            if distVelCas < sumdistlowC:
                sumdistlowC = distVelCas
                hexCashlow = CashmereArray[j] 
        
        for k in range(len(SatinArray)):
            SatR = int(SatinArray[k][0:2], 16)
            SatG = int(SatinArray[k][2:4], 16)
            SatB = int(SatinArray[k][4:6], 16)
            distVelSat = deltaEcielab(VelvR,VelvG,VelvB,SatR,SatG,SatB)
            if distVelSat < sumdistlowS:
                sumdistlowS = distVelSat
                hexSatlow = SatinArray[k]
        
        
        for l in range(len(OxfordArray)):
            OxR = int(OxfordArray[l][0:2], 16)
            OxG = int(OxfordArray[l][2:4], 16)
            OxB = int(OxfordArray[l][4:6], 16)
            distVelOx = deltaEcielab(VelvR,VelvG,VelvB,OxR,OxG,OxB)
            if distVelOx < sumdistlowO:
                sumdistlowO = distVelOx
                hexOxlow = OxfordArray[l]

        sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                          int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
        sumdist = f"{sumdist:.4f}"
        LowScoreHexes.append(f'{VelvetArray[i]}, {hexCashlow}, {hexSatlow}, {hexOxlow}, {sumdist}')
    
    for i in range(len(CashmereArray)):
        VelvR = int(CashmereArray[i][0:2], 16)
        VelvG = int(CashmereArray[i][2:4], 16)
        VelvB = int(CashmereArray[i][4:6], 16)
        sumdistlowC = 10000
        sumdistlowS = 10000
        sumdistlowO = 10000
        hexCashlow = ''
        hexSatlow = ''
        hexOxlow = ''
        for j in range(len(VelvetArray)):
            CasR = int(VelvetArray[j][0:2], 16)
            CasG = int(VelvetArray[j][2:4], 16)
            CasB = int(VelvetArray[j][4:6], 16)
            distVelCas = deltaEcielab(VelvR,VelvG,VelvB,CasR,CasG,CasB)
            if distVelCas < sumdistlowC:
                sumdistlowC = distVelCas
                hexCashlow = VelvetArray[j] 
        
        for k in range(len(SatinArray)):
            SatR = int(SatinArray[k][0:2], 16)
            SatG = int(SatinArray[k][2:4], 16)
            SatB = int(SatinArray[k][4:6], 16)
            distVelSat = deltaEcielab(VelvR,VelvG,VelvB,SatR,SatG,SatB)
            if distVelSat < sumdistlowS:
                sumdistlowS = distVelSat
                hexSatlow = SatinArray[k]
        
        
        for l in range(len(OxfordArray)):
            OxR = int(OxfordArray[l][0:2], 16)
            OxG = int(OxfordArray[l][2:4], 16)
            OxB = int(OxfordArray[l][4:6], 16)
            distVelOx = deltaEcielab(VelvR,VelvG,VelvB,OxR,OxG,OxB)
            if distVelOx < sumdistlowO:
                sumdistlowO = distVelOx
                hexOxlow = OxfordArray[l]

        sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                          int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
        sumdist = f"{sumdist:.4f}"
        if f'{hexCashlow}, {CashmereArray[i]}, {hexSatlow}, {hexOxlow}, {sumdist}' not in LowScoreHexes:
            # InArray = False
            # for m in range(len(LowScoreHexes)-1, -1, -1):
            #     if CashmereArray[i] == LowScoreHexes[m][8:14]:
            #         if float(sumdist) < float(LowScoreHexes[m][32:]):
            #             del LowScoreHexes[m]
            #             LowScoreHexes.append(f'{hexCashlow}, {CashmereArray[i]}, {hexSatlow}, {hexOxlow}, {sumdist}')
            #             InArray = True
            # if InArray == False:
                LowScoreHexes.append(f'{hexCashlow}, {CashmereArray[i]}, {hexSatlow}, {hexOxlow}, {sumdist}')

    for i in range(len(SatinArray)):
        VelvR = int(SatinArray[i][0:2], 16)
        VelvG = int(SatinArray[i][2:4], 16)
        VelvB = int(SatinArray[i][4:6], 16)
        sumdistlowC = 10000
        sumdistlowS = 10000
        sumdistlowO = 10000
        hexCashlow = ''
        hexSatlow = ''
        hexOxlow = ''
        for j in range(len(VelvetArray)):
            CasR = int(VelvetArray[j][0:2], 16)
            CasG = int(VelvetArray[j][2:4], 16)
            CasB = int(VelvetArray[j][4:6], 16)
            distVelCas = deltaEcielab(VelvR,VelvG,VelvB,CasR,CasG,CasB)
            if distVelCas < sumdistlowC:
                sumdistlowC = distVelCas
                hexCashlow = VelvetArray[j] 
        
        for k in range(len(CashmereArray)):
            SatR = int(CashmereArray[k][0:2], 16)
            SatG = int(CashmereArray[k][2:4], 16)
            SatB = int(CashmereArray[k][4:6], 16)
            distVelSat = deltaEcielab(VelvR,VelvG,VelvB,SatR,SatG,SatB)
            if distVelSat < sumdistlowS:
                sumdistlowS = distVelSat
                hexSatlow = CashmereArray[k]
        
        
        for l in range(len(OxfordArray)):
            OxR = int(OxfordArray[l][0:2], 16)
            OxG = int(OxfordArray[l][2:4], 16)
            OxB = int(OxfordArray[l][4:6], 16)
            distVelOx = deltaEcielab(VelvR,VelvG,VelvB,OxR,OxG,OxB)
            if distVelOx < sumdistlowO:
                sumdistlowO = distVelOx
                hexOxlow = OxfordArray[l]

        sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                          int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
        sumdist = f"{sumdist:.4f}"        
        if f'{hexCashlow}, {hexSatlow}, {SatinArray[i]}, {hexOxlow}, {sumdist}' not in LowScoreHexes:
            LowScoreHexes.append(f'{hexCashlow}, {hexSatlow}, {SatinArray[i]}, {hexOxlow}, {sumdist}')

    for i in range(len(OxfordArray)):
        VelvR = int(OxfordArray[i][0:2], 16)
        VelvG = int(OxfordArray[i][2:4], 16)
        VelvB = int(OxfordArray[i][4:6], 16)
        sumdistlowC = 10000
        sumdistlowS = 10000
        sumdistlowO = 10000
        hexCashlow = ''
        hexSatlow = ''
        hexOxlow = ''
        for j in range(len(VelvetArray)):
            CasR = int(VelvetArray[j][0:2], 16)
            CasG = int(VelvetArray[j][2:4], 16)
            CasB = int(VelvetArray[j][4:6], 16)
            distVelCas = deltaEcielab(VelvR,VelvG,VelvB,CasR,CasG,CasB)
            if distVelCas < sumdistlowC:
                sumdistlowC = distVelCas
                hexCashlow = VelvetArray[j] 
        
        for k in range(len(CashmereArray)):
            SatR = int(CashmereArray[k][0:2], 16)
            SatG = int(CashmereArray[k][2:4], 16)
            SatB = int(CashmereArray[k][4:6], 16)
            distVelSat = deltaEcielab(VelvR,VelvG,VelvB,SatR,SatG,SatB)
            if distVelSat < sumdistlowS:
                sumdistlowS = distVelSat
                hexSatlow = CashmereArray[k]
        
        
        for l in range(len(SatinArray)):
            OxR = int(SatinArray[l][0:2], 16)
            OxG = int(SatinArray[l][2:4], 16)
            OxB = int(SatinArray[l][4:6], 16)
            distVelOx = deltaEcielab(VelvR,VelvG,VelvB,OxR,OxG,OxB)
            if distVelOx < sumdistlowO:
                sumdistlowO = distVelOx
                hexOxlow = SatinArray[l]

        sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                          int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
        sumdist = f"{sumdist:.4f}"
        if f'{hexCashlow}, {hexSatlow}, {hexOxlow}, {OxfordArray[i]}, {sumdist}' not in LowScoreHexes:
            LowScoreHexes.append(f'{hexCashlow}, {hexSatlow}, {hexOxlow}, {OxfordArray[i]}, {sumdist}')

    for i in range(len(LowScoreHexes)):
        LowScoreHexes.sort(key=MyKey)

    for i in range(len(LowScoreHexes)):
        print(f'{LowScoreHexes[i]}')

def LowestSetScores():
    LowScoreHexesFinal = []
    VelvetArrayOut = []
    CashmereArrayOut = []
    SatinArrayOut = []
    OxfordArrayOut = []
    shortestPiece = len(min(VelvetArray, CashmereArray, SatinArray, OxfordArray, key=len))
    while shortestPiece > 0:
        LowScoreHexes = []
        for i in range(len(VelvetArray)):
            VelvR = int(VelvetArray[i][0:2], 16)
            VelvG = int(VelvetArray[i][2:4], 16)
            VelvB = int(VelvetArray[i][4:6], 16)
            sumdistlowC = 10000
            sumdistlowS = 10000
            sumdistlowO = 10000
            hexCashlow = ''
            hexSatlow = ''
            hexOxlow = ''
            for j in range(len(CashmereArray)):
                CasR = int(CashmereArray[j][0:2], 16)
                CasG = int(CashmereArray[j][2:4], 16)
                CasB = int(CashmereArray[j][4:6], 16)
                distVelCas = deltaEcielab(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = CashmereArray[j] 

            for k in range(len(SatinArray)):
                SatR = int(SatinArray[k][0:2], 16)
                SatG = int(SatinArray[k][2:4], 16)
                SatB = int(SatinArray[k][4:6], 16)
                distVelSat = deltaEcielab(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = SatinArray[k]
        
        
            for l in range(len(OxfordArray)):
                OxR = int(OxfordArray[l][0:2], 16)
                OxG = int(OxfordArray[l][2:4], 16)
                OxB = int(OxfordArray[l][4:6], 16)
                distVelOx = deltaEcielab(VelvR,VelvG,VelvB,OxR,OxG,OxB)
                if distVelOx < sumdistlowO:
                    sumdistlowO = distVelOx
                    hexOxlow = OxfordArray[l]

            sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                          int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
            sumdist = f"{sumdist:.4f}"
            LowScoreHexes.append(f'{VelvetArray[i]}, {hexCashlow}, {hexSatlow}, {hexOxlow}, {sumdist}')
    
        for i in range(len(CashmereArray)):
            VelvR = int(CashmereArray[i][0:2], 16)
            VelvG = int(CashmereArray[i][2:4], 16)
            VelvB = int(CashmereArray[i][4:6], 16)
            sumdistlowC = 10000
            sumdistlowS = 10000
            sumdistlowO = 10000
            hexCashlow = ''
            hexSatlow = ''
            hexOxlow = ''
            for j in range(len(VelvetArray)):
                CasR = int(VelvetArray[j][0:2], 16)
                CasG = int(VelvetArray[j][2:4], 16)
                CasB = int(VelvetArray[j][4:6], 16)
                distVelCas = deltaEcielab(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = VelvetArray[j] 
            
            for k in range(len(SatinArray)):
                SatR = int(SatinArray[k][0:2], 16)
                SatG = int(SatinArray[k][2:4], 16)
                SatB = int(SatinArray[k][4:6], 16)
                distVelSat = deltaEcielab(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = SatinArray[k]
            
            
            for l in range(len(OxfordArray)):
                OxR = int(OxfordArray[l][0:2], 16)
                OxG = int(OxfordArray[l][2:4], 16)
                OxB = int(OxfordArray[l][4:6], 16)
                distVelOx = deltaEcielab(VelvR,VelvG,VelvB,OxR,OxG,OxB)
                if distVelOx < sumdistlowO:
                    sumdistlowO = distVelOx
                    hexOxlow = OxfordArray[l]

            sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                            int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
            sumdist = f"{sumdist:.4f}"
            if f'{hexCashlow}, {CashmereArray[i]}, {hexSatlow}, {hexOxlow}, {sumdist}' not in LowScoreHexes:
                    LowScoreHexes.append(f'{hexCashlow}, {CashmereArray[i]}, {hexSatlow}, {hexOxlow}, {sumdist}')

        for i in range(len(SatinArray)):
            VelvR = int(SatinArray[i][0:2], 16)
            VelvG = int(SatinArray[i][2:4], 16)
            VelvB = int(SatinArray[i][4:6], 16)
            sumdistlowC = 10000
            sumdistlowS = 10000
            sumdistlowO = 10000
            hexCashlow = ''
            hexSatlow = ''
            hexOxlow = ''
            for j in range(len(VelvetArray)):
                CasR = int(VelvetArray[j][0:2], 16)
                CasG = int(VelvetArray[j][2:4], 16)
                CasB = int(VelvetArray[j][4:6], 16)
                distVelCas = deltaEcielab(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = VelvetArray[j] 
            
            for k in range(len(CashmereArray)):
                SatR = int(CashmereArray[k][0:2], 16)
                SatG = int(CashmereArray[k][2:4], 16)
                SatB = int(CashmereArray[k][4:6], 16)
                distVelSat = deltaEcielab(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = CashmereArray[k]
            
            
            for l in range(len(OxfordArray)):
                OxR = int(OxfordArray[l][0:2], 16)
                OxG = int(OxfordArray[l][2:4], 16)
                OxB = int(OxfordArray[l][4:6], 16)
                distVelOx = deltaEcielab(VelvR,VelvG,VelvB,OxR,OxG,OxB)
                if distVelOx < sumdistlowO:
                    sumdistlowO = distVelOx
                    hexOxlow = OxfordArray[l]

            sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                            int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
            sumdist = f"{sumdist:.4f}"        
            if f'{hexCashlow}, {hexSatlow}, {SatinArray[i]}, {hexOxlow}, {sumdist}' not in LowScoreHexes:
                LowScoreHexes.append(f'{hexCashlow}, {hexSatlow}, {SatinArray[i]}, {hexOxlow}, {sumdist}')

        for i in range(len(OxfordArray)):
            VelvR = int(OxfordArray[i][0:2], 16)
            VelvG = int(OxfordArray[i][2:4], 16)
            VelvB = int(OxfordArray[i][4:6], 16)
            sumdistlowC = 10000
            sumdistlowS = 10000
            sumdistlowO = 10000
            hexCashlow = ''
            hexSatlow = ''
            hexOxlow = ''
            for j in range(len(VelvetArray)):
                CasR = int(VelvetArray[j][0:2], 16)
                CasG = int(VelvetArray[j][2:4], 16)
                CasB = int(VelvetArray[j][4:6], 16)
                distVelCas = deltaEcielab(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = VelvetArray[j] 
            
            for k in range(len(CashmereArray)):
                SatR = int(CashmereArray[k][0:2], 16)
                SatG = int(CashmereArray[k][2:4], 16)
                SatB = int(CashmereArray[k][4:6], 16)
                distVelSat = deltaEcielab(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = CashmereArray[k]
            
            
            for l in range(len(SatinArray)):
                OxR = int(SatinArray[l][0:2], 16)
                OxG = int(SatinArray[l][2:4], 16)
                OxB = int(SatinArray[l][4:6], 16)
                distVelOx = deltaEcielab(VelvR,VelvG,VelvB,OxR,OxG,OxB)
                if distVelOx < sumdistlowO:
                    sumdistlowO = distVelOx
                    hexOxlow = SatinArray[l]

            sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                            int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
            sumdist = f"{sumdist:.4f}"
            if f'{hexCashlow}, {hexSatlow}, {hexOxlow}, {OxfordArray[i]}, {sumdist}' not in LowScoreHexes:
                LowScoreHexes.append(f'{hexCashlow}, {hexSatlow}, {hexOxlow}, {OxfordArray[i]}, {sumdist}')
        LowScoreHexes.sort(reverse=True, key=MyKey)
        LowScoreHexesFinal.append(LowScoreHexes[-1])
        VelvetArrayOut.append(LowScoreHexes[-1][0:6])
        VelvetArray.remove(LowScoreHexes[-1][0:6])
        CashmereArrayOut.append(LowScoreHexes[-1][8:14])
        CashmereArray.remove(LowScoreHexes[-1][8:14])
        SatinArrayOut.append(LowScoreHexes[-1][16:22])
        SatinArray.remove(LowScoreHexes[-1][16:22])
        OxfordArrayOut.append(LowScoreHexes[-1][24:30])
        OxfordArray.remove(LowScoreHexes[-1][24:30])
        shortestPiece = shortestPiece - 1
        print(LowScoreHexesFinal[-1])
        # for i in range(len(LowScoreHexes)-1, -1, -1):
        #     if (LowScoreHexes[i][0:6] not in SatinArrayOut) == True:
        #         if (LowScoreHexes[i][8:14] not in CashmereArrayOut) == True:
        #             if (LowScoreHexes[i][16:22] not in SatinArrayOut) == True:
        #                 if (LowScoreHexes[i][24:30] not in OxfordArrayOut) == True:
        #                     LowScoreHexesFinal.append(LowScoreHexes[i])
        #                     SatinArrayOut.append(LowScoreHexes[i][0:6])
        #                     SatinArray.remove(LowScoreHexes[i][0:6])
        #                     CashmereArrayOut.append(LowScoreHexes[i][8:14])
        #                     CashmereArray.remove(LowScoreHexes[i][8:14])
        #                     SatinArrayOut.append(LowScoreHexes[i][16:22])
        #                     SatinArray.remove(LowScoreHexes[i][16:22])
        #                     OxfordArrayOut.append(LowScoreHexes[i][24:30])
        #                     OxfordArray.remove(LowScoreHexes[i][24:30])
        #                     shortestPiece = shortestPiece - 1




    # LowScoreHexesFinal.sort(key=MyKey)
    # for i in range(len(LowScoreHexesFinal)):
    #     print(f'{LowScoreHexesFinal[i]}')

def Matching3hex():
    
    dictMatchHexVelv = {}
    dictMatchHexCash = {}
    dictMatchHexSat = {}
    dictMatchHexOxf = {}
    sortedhex3list = []


    for i in range(len(VelvetArray)):
        dictMatchHexVelv.update({str(VelvetArray[i][0:6:2]): "#"+str(VelvetArray[i])})
        VelvetArray[i] = f'({VelvetArray[i][0:6:2]}, 00V)'
    for i in range(len(VelvetArray)):
        if VelvetArray[i] != 'GGGGGGGGGGGGGGGGG':
            for j in range(len(VelvetArray)):
                if VelvetArray[j] != 'GGGGGGGGGGGGGGGGG':
                    if i != j:
                        if VelvetArray[i][1:-6] == VelvetArray[j][1:-6]:
                            VelvetArray[j] = 'GGGGGGGGGGGGGGGGG'
                            VelvetArray[i] = VelvetArray[i][:6] + str(int(VelvetArray[i][6:-2]) + 1).zfill(len(VelvetArray[i][6:-2])) + VelvetArray[i][-2:]
    finalVelvetArray = sorted(set(VelvetArray), key=lambda x:VelvetArray.index(x))
    if 'GGGGGGGGGGGGGGGGG' in finalVelvetArray:
        finalVelvetArray.remove('GGGGGGGGGGGGGGGGG')
    
    for i in range(len(CashmereArray)):
        dictMatchHexCash.update({str(CashmereArray[i][0:6:2]): "#"+str(CashmereArray[i])})
        CashmereArray[i] = f'({CashmereArray[i][0:6:2]}, 00C)'
    for i in range(len(CashmereArray)):
        if CashmereArray[i] != 'GGGGGGGGGGGGGGGGG':
            for j in range(len(CashmereArray)):
                if CashmereArray[j] != 'GGGGGGGGGGGGGGGGG':
                    if i != j:
                        if CashmereArray[i][1:-6] == CashmereArray[j][1:-6]:
                            CashmereArray[j] = 'GGGGGGGGGGGGGGGGG'
                            CashmereArray[i] = CashmereArray[i][:6] + str(int(CashmereArray[i][6:-2]) + 1).zfill(len(CashmereArray[i][6:-2])) + CashmereArray[i][-2:]
    finalCashmereArray = sorted(set(CashmereArray), key=lambda x:CashmereArray.index(x))
    if 'GGGGGGGGGGGGGGGGG' in finalCashmereArray:
        finalCashmereArray.remove('GGGGGGGGGGGGGGGGG')

    for i in range(len(SatinArray)):
        dictMatchHexSat.update({str(SatinArray[i][0:6:2]): "#"+str(SatinArray[i])})
        SatinArray[i] = f'({SatinArray[i][0:6:2]}, 00S)'
    for i in range(len(SatinArray)):
        if SatinArray[i] != 'GGGGGGGGGGGGGGGGG':
            for j in range(len(SatinArray)):
                if SatinArray[j] != 'GGGGGGGGGGGGGGGGG':
                    if i != j:
                        if SatinArray[i][1:-6] == SatinArray[j][1:-6]:
                            SatinArray[j] = 'GGGGGGGGGGGGGGGGG'
                            SatinArray[i] = SatinArray[i][:6] + str(int(SatinArray[i][6:-2]) + 1).zfill(len(SatinArray[i][6:-2])) + SatinArray[i][-2:]
    finalSatinArray = sorted(set(SatinArray), key=lambda x:SatinArray.index(x))
    if 'GGGGGGGGGGGGGGGGG' in finalSatinArray:
        finalSatinArray.remove('GGGGGGGGGGGGGGGGG')   

    for i in range(len(OxfordArray)):
        dictMatchHexOxf.update({str(OxfordArray[i][0:6:2]): "#"+str(OxfordArray[i])})
        OxfordArray[i] = f'({OxfordArray[i][0:6:2]}, 00F)'
    for i in range(len(OxfordArray)):
        if OxfordArray[i] != 'GGGGGGGGGGGGGGGGG':
            for j in range(len(OxfordArray)):
                if OxfordArray[j] != 'GGGGGGGGGGGGGGGGG':
                    if i != j:
                        if OxfordArray[i][1:-6] == OxfordArray[j][1:-6]:
                            OxfordArray[j] = 'GGGGGGGGGGGGGGGGG'
                            OxfordArray[i] = OxfordArray[i][:6] + str(int(OxfordArray[i][6:-2]) + 1).zfill(len(OxfordArray[i][6:-2])) + OxfordArray[i][-2:]
    finalOxfordArray = sorted(set(OxfordArray), key=lambda x:OxfordArray.index(x))
    if 'GGGGGGGGGGGGGGGGG' in finalOxfordArray:
        finalOxfordArray.remove('GGGGGGGGGGGGGGGGG')      
   
    # Where sorting happens

    while len(finalVelvetArray) > 0:
        for i in range(len(finalVelvetArray)-1, -1, -1):
            dupevalues = ''
            currenthexinfo = f'{finalVelvetArray[i][1]}x{finalVelvetArray[i][2]}x{finalVelvetArray[i][3]}x, {dictMatchHexVelv.get(finalVelvetArray[i][1:4])}, '
            if finalVelvetArray[i][6:-1] != '00V':
                dupevalues = f'{finalVelvetArray[i][6:-1]}'
            cashmatch = 0
            cashmatchvals = 0
            satmatch = 0
            satmatchvals = 0
            oxfmatch = 0
            oxfmatchvals = 0
            for j in range(len(finalCashmereArray)-1, -1, -1):
                if finalVelvetArray[i][1:4] == finalCashmereArray[j][1:4]:
                    currenthexinfo = currenthexinfo + f'{dictMatchHexCash.get(finalCashmereArray[j][1:4])}, '
                    if finalCashmereArray[j][6:-1] != '00C':
                        dupevalues = dupevalues + f'{finalCashmereArray[j][6:-1]}'
                    cashmatchvals = j
                    cashmatch = 1
            if cashmatch != 1:
                currenthexinfo = currenthexinfo + '-, '
            else:
                finalCashmereArray.pop(cashmatchvals)
            for k in range(len(finalSatinArray)-1, -1, -1):
                if finalVelvetArray[i][1:4] == finalSatinArray[k][1:4]:
                    currenthexinfo = currenthexinfo + f'{dictMatchHexSat.get(finalSatinArray[k][1:4])}, '
                    if finalSatinArray[k][6:-1] != '00S':
                        dupevalues = dupevalues + f'{finalSatinArray[k][6:-1]}'
                    satmatchvals = k
                    satmatch = 1
            if satmatch != 1:
                currenthexinfo = currenthexinfo + '-, '     
            else:
                finalSatinArray.pop(satmatchvals)                       
            for l in range(len(finalOxfordArray)-1, -1, -1):    
                if finalVelvetArray[i][1:4] == finalOxfordArray[l][1:4]:
                    currenthexinfo = currenthexinfo + f'{dictMatchHexOxf.get(finalOxfordArray[l][1:4])}, '
                    if finalOxfordArray[l][6:-1] != '00F':
                        dupevalues = dupevalues + f'{finalOxfordArray[l][6:-1]}'
                    oxfmatchvals = l
                    oxfmatch = 1
            if oxfmatch != 1:
                currenthexinfo = currenthexinfo + '-, '
            else:
                finalOxfordArray.pop(oxfmatchvals)                
            if len(dupevalues) > 0:
                currenthexinfo = currenthexinfo + f'{dupevalues}'
            sortedhex3list.append(currenthexinfo)
            finalVelvetArray.pop(i)

    while len(finalCashmereArray) > 0:
        for i in range(len(finalCashmereArray)-1, -1, -1):
            dupevalues = ''
            currenthexinfo = f'{finalCashmereArray[i][1]}x{finalCashmereArray[i][2]}x{finalCashmereArray[i][3]}x, -, {dictMatchHexCash.get(finalCashmereArray[i][1:4])}, '
            if finalCashmereArray[i][6:-1] != '00C':            
                dupevalues = f'{finalCashmereArray[i][6:-1]}'
            satmatch = 0
            satmatchvals = 0
            oxfmatch = 0
            oxfmatchvals = 0   
            for k in range(len(finalSatinArray)-1, -1, -1):
                if finalCashmereArray[i][1:4] == finalSatinArray[k][1:4]:
                    currenthexinfo = currenthexinfo + f'{dictMatchHexSat.get(finalSatinArray[k][1:4])}, '
                    if finalSatinArray[k][6:-1] != '00S':                    
                        dupevalues = dupevalues + f'{finalSatinArray[k][6:-1]}'
                    satmatchvals = k
                    satmatch = 1
            if satmatch != 1:
                currenthexinfo = currenthexinfo + '-, '        
            else:
                finalSatinArray.pop(satmatchvals)                         
            for l in range(len(finalOxfordArray)-1, -1, -1):    
                if finalCashmereArray[i][1:4] == finalOxfordArray[l][1:4]:
                    currenthexinfo = currenthexinfo + f'{dictMatchHexOxf.get(finalOxfordArray[l][1:4])}, '
                    if finalOxfordArray[l][6:-1] != '00F':                    
                        dupevalues = dupevalues + f'{finalOxfordArray[l][6:-1]}'
                    oxfmatchvals = l
                    oxfmatch = 1
            if oxfmatch != 1:
                currenthexinfo = currenthexinfo + '-, '
            else:
                finalOxfordArray.pop(oxfmatchvals)          
            if len(dupevalues) > 0:    
                currenthexinfo = currenthexinfo + f'{dupevalues}'
            sortedhex3list.append(currenthexinfo)
            finalCashmereArray.pop(i)

    while len(finalSatinArray) > 0:
        for i in range(len(finalSatinArray)-1, -1, -1):
            dupevalues = ''
            currenthexinfo = f'{finalSatinArray[i][1]}x{finalSatinArray[i][2]}x{finalSatinArray[i][3]}x, -, -, {dictMatchHexSat.get(finalSatinArray[i][1:4])}, '
            if finalSatinArray[i][6:-1] != '00S':     
                dupevalues = f'{finalSatinArray[i][6:-1]}'
            oxfmatch = 0
            oxfmatchvals = 0   
            for l in range(len(finalOxfordArray)-1, -1, -1):    
                if finalSatinArray[i][1:4] == finalOxfordArray[l][1:4]:
                    currenthexinfo = currenthexinfo + f'{dictMatchHexOxf.get(finalOxfordArray[l][1:4])}, '
                    if finalOxfordArray[l][6:-1] != '00F':                        
                        dupevalues = dupevalues + f'{finalOxfordArray[l][6:-1]}'
                    oxfmatchvals = l
                    oxfmatch = 1
            if oxfmatch != 1:
                currenthexinfo = currenthexinfo + '-, '
            else:
                finalOxfordArray.pop(oxfmatchvals)          
            if len(dupevalues) > 0:    
                currenthexinfo = currenthexinfo + f'{dupevalues}'
            sortedhex3list.append(currenthexinfo)
            finalSatinArray.pop(i)

    while len(finalOxfordArray) > 0:
        for i in range(len(finalOxfordArray)-1, -1, -1):
            currenthexinfo = f'{finalOxfordArray[i][1]}x{finalOxfordArray[i][2]}x{finalOxfordArray[i][3]}x, -, -, -, {dictMatchHexOxf.get(finalOxfordArray[i][1:4])}'
            if finalOxfordArray[i][6:-1] != '00F':      
                currenthexinfo = currenthexinfo + f', {finalOxfordArray[i][6:-1]}'      
            sortedhex3list.append(currenthexinfo)
            finalOxfordArray.pop(i)

    
    #printing
    for i in range(len(sortedhex3list)):
        sortedhex3list.sort(key=len, reverse=True)
    for i in range(len(sortedhex3list)):
        sortedhex3list.sort(key=MyKey2, reverse=True)


    for i in range(len(sortedhex3list)):
        print(f'{sortedhex3list[i]}')




if __name__ == '__main__':
    
    #HexSortALL()
    LowestSetScores()
    #Matching3hex()