import math

VelvetS = input("Velvet Hat Hexcodes:\n")
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

def rgbd2(r1,g1,b1,r2,g2,b2):
            if ((r1+r2) * 0.5) < 128:
                distVelOx = math.sqrt((2 * pow(r1-r2, 2)) + (4 * pow(g1-g2, 2)) + (3 * pow(b1-b2, 2)))
            else:
                distVelOx = math.sqrt((3 * pow(r1-r2, 2)) + (4 * pow(g1-g2, 2)) + (2 * pow(b1-b2, 2)))   
            return distVelOx


def rgbDist(r1,g1,b1,r2,g2,b2,r3,g3,b3,r4,g4,b4):
    #hi
    
    dist12 = rgbd2(r1,g1,b1,r2,g2,b2)
    dist13 = rgbd2(r1,g1,b1,r3,g3,b3)
    dist14 = rgbd2(r1,g1,b1,r4,g4,b4)
    dist23 = rgbd2(r2,g2,b2,r3,g3,b3)
    dist24 = rgbd2(r2,g2,b2,r4,g4,b4)
    dist34 = rgbd2(r3,g3,b3,r4,g4,b4)
    return ((dist12+dist13+dist14+dist23+dist24+dist34)/6)

def MyKey(ScoreString):
    return float(ScoreString[32:])


def HexSetLowestScoresTot():
    LowScoreHexes = []
    for i in range(len(VelvetArray)):
        decVelValR = int(VelvetArray[i][0:2], 16)
        decVelValG = int(VelvetArray[i][2:4], 16)
        decVelValB = int(VelvetArray[i][4:6], 16)
        for j in range(len(CashmereArray)):
            decCasValR = int(CashmereArray[j][0:2], 16)
            decCasValG = int(CashmereArray[j][2:4], 16)
            decCasValB = int(CashmereArray[j][4:6], 16)
            for k in range(len(SatinArray)):
                decSatValR = int(SatinArray[k][0:2], 16)
                decSatValG = int(SatinArray[k][2:4], 16)
                decSatValB = int(SatinArray[k][4:6], 16)
                for l in range(len(OxfordArray)):
                    decOxValR = int(OxfordArray[l][0:2], 16)
                    decOxValG = int(OxfordArray[l][2:4], 16)
                    decOxValB = int(OxfordArray[l][4:6], 16)
                    if ((decVelValR+decCasValR) * 0.5) < 128:
                        distVelCas = math.sqrt((2 * pow(decVelValR-decCasValR, 2)) + (4 * pow(decVelValG-decCasValG, 2)) + (3 * pow(decVelValB-decCasValB, 2)))
                    else:
                        distVelCas = math.sqrt((3 * pow(decVelValR-decCasValR, 2)) + (4 * pow(decVelValG-decCasValG, 2)) + (2 * pow(decVelValB-decCasValB, 2)))
                    if ((decVelValR+decSatValR) * 0.5) < 128:
                        distVelSat = math.sqrt((2 * pow(decVelValR-decSatValR, 2)) + (4 * pow(decVelValG-decSatValG, 2)) + (3 * pow(decVelValB-decSatValB, 2)))
                    else:
                        distVelSat = math.sqrt((3 * pow(decVelValR-decSatValR, 2)) + (4 * pow(decVelValG-decSatValG, 2)) + (2 * pow(decVelValB-decSatValB, 2)))
                    if ((decVelValR+decOxValR) * 0.5) < 128:
                        distVelOx = math.sqrt((2 * pow(decVelValR-decOxValR, 2)) + (4 * pow(decVelValG-decOxValG, 2)) + (3 * pow(decVelValB-decOxValB, 2)))
                    else:
                        distVelOx = math.sqrt((3 * pow(decVelValR-decOxValR, 2)) + (4 * pow(decVelValG-decOxValG, 2)) + (2 * pow(decVelValB-decOxValB, 2)))


                    sumdist = (distVelCas + distVelSat + distVelOx)/3
                    if sumdist <= 45:
                        LowScoreHexes.append(f'{VelvetArray[i]}, {CashmereArray[j]}, {SatinArray[k]}, {OxfordArray[l]}, {sumdist}')

    for i in range(len(LowScoreHexes)):
        print(f'{LowScoreHexes[i]}')

def HexSetLowestGroupByHat():
    LowScoreHexes = []
    for i in range(len(VelvetArray)):
        decVelValR = int(VelvetArray[i][0:2], 16)
        decVelValG = int(VelvetArray[i][2:4], 16)
        decVelValB = int(VelvetArray[i][4:6], 16)
        sumdistlow = 10000
        for j in range(len(CashmereArray)):
            decCasValR = int(CashmereArray[j][0:2], 16)
            decCasValG = int(CashmereArray[j][2:4], 16)
            decCasValB = int(CashmereArray[j][4:6], 16)
            for k in range(len(SatinArray)):
                decSatValR = int(SatinArray[k][0:2], 16)
                decSatValG = int(SatinArray[k][2:4], 16)
                decSatValB = int(SatinArray[k][4:6], 16)
                for l in range(len(OxfordArray)):
                    decOxValR = int(OxfordArray[l][0:2], 16)
                    decOxValG = int(OxfordArray[l][2:4], 16)
                    decOxValB = int(OxfordArray[l][4:6], 16)
                    if ((decVelValR+decCasValR) * 0.5) < 128:
                        distVelCas = math.sqrt((2 * pow(decVelValR-decCasValR, 2)) + (4 * pow(decVelValG-decCasValG, 2)) + (3 * pow(decVelValB-decCasValB, 2)))
                    else:
                        distVelCas = math.sqrt((3 * pow(decVelValR-decCasValR, 2)) + (4 * pow(decVelValG-decCasValG, 2)) + (2 * pow(decVelValB-decCasValB, 2)))
                    if ((decVelValR+decSatValR) * 0.5) < 128:
                        distVelSat = math.sqrt((2 * pow(decVelValR-decSatValR, 2)) + (4 * pow(decVelValG-decSatValG, 2)) + (3 * pow(decVelValB-decSatValB, 2)))
                    else:
                        distVelSat = math.sqrt((3 * pow(decVelValR-decSatValR, 2)) + (4 * pow(decVelValG-decSatValG, 2)) + (2 * pow(decVelValB-decSatValB, 2)))
                    if ((decVelValR+decOxValR) * 0.5) < 128:
                        distVelOx = math.sqrt((2 * pow(decVelValR-decOxValR, 2)) + (4 * pow(decVelValG-decOxValG, 2)) + (3 * pow(decVelValB-decOxValB, 2)))
                    else:
                        distVelOx = math.sqrt((3 * pow(decVelValR-decOxValR, 2)) + (4 * pow(decVelValG-decOxValG, 2)) + (2 * pow(decVelValB-decOxValB, 2)))


                    sumdist = (distVelCas + distVelSat + distVelOx)/3
                    if sumdist < sumdistlow:
                        if sumdistlow != 10000:
                            LowScoreHexes = LowScoreHexes[:-1]
                        LowScoreHexes.append(f'{VelvetArray[i]}, {CashmereArray[j]}, {SatinArray[k]}, {OxfordArray[l]}, {sumdist}')
                        sumdistlow = sumdist
                    

    for i in range(len(LowScoreHexes)):
        print(f'{LowScoreHexes[i]}')


def HexSortHatFast():
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
            distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
            if distVelCas < sumdistlowC:
                sumdistlowC = distVelCas
                hexCashlow = CashmereArray[j] 
        
        for k in range(len(SatinArray)):
            SatR = int(SatinArray[k][0:2], 16)
            SatG = int(SatinArray[k][2:4], 16)
            SatB = int(SatinArray[k][4:6], 16)
            distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
            if distVelSat < sumdistlowS:
                sumdistlowS = distVelSat
                hexSatlow = SatinArray[k]
        
        
        for l in range(len(OxfordArray)):
            OxR = int(OxfordArray[l][0:2], 16)
            OxG = int(OxfordArray[l][2:4], 16)
            OxB = int(OxfordArray[l][4:6], 16)
            distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
            if distVelOx < sumdistlowO:
                sumdistlowO = distVelOx
                hexOxlow = OxfordArray[l]

        sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                          int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
        LowScoreHexes.append(f'{VelvetArray[i]}, {hexCashlow}, {hexSatlow}, {hexOxlow}, {sumdist:.4f}')
                
                    

    for i in range(len(LowScoreHexes)):
        print(f'{LowScoreHexes[i]}')

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
            distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
            if distVelCas < sumdistlowC:
                sumdistlowC = distVelCas
                hexCashlow = CashmereArray[j] 
        
        for k in range(len(SatinArray)):
            SatR = int(SatinArray[k][0:2], 16)
            SatG = int(SatinArray[k][2:4], 16)
            SatB = int(SatinArray[k][4:6], 16)
            distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
            if distVelSat < sumdistlowS:
                sumdistlowS = distVelSat
                hexSatlow = SatinArray[k]
        
        
        for l in range(len(OxfordArray)):
            OxR = int(OxfordArray[l][0:2], 16)
            OxG = int(OxfordArray[l][2:4], 16)
            OxB = int(OxfordArray[l][4:6], 16)
            distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
            distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
            if distVelCas < sumdistlowC:
                sumdistlowC = distVelCas
                hexCashlow = VelvetArray[j] 
        
        for k in range(len(SatinArray)):
            SatR = int(SatinArray[k][0:2], 16)
            SatG = int(SatinArray[k][2:4], 16)
            SatB = int(SatinArray[k][4:6], 16)
            distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
            if distVelSat < sumdistlowS:
                sumdistlowS = distVelSat
                hexSatlow = SatinArray[k]
        
        
        for l in range(len(OxfordArray)):
            OxR = int(OxfordArray[l][0:2], 16)
            OxG = int(OxfordArray[l][2:4], 16)
            OxB = int(OxfordArray[l][4:6], 16)
            distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
            distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
            if distVelCas < sumdistlowC:
                sumdistlowC = distVelCas
                hexCashlow = VelvetArray[j] 
        
        for k in range(len(CashmereArray)):
            SatR = int(CashmereArray[k][0:2], 16)
            SatG = int(CashmereArray[k][2:4], 16)
            SatB = int(CashmereArray[k][4:6], 16)
            distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
            if distVelSat < sumdistlowS:
                sumdistlowS = distVelSat
                hexSatlow = CashmereArray[k]
        
        
        for l in range(len(OxfordArray)):
            OxR = int(OxfordArray[l][0:2], 16)
            OxG = int(OxfordArray[l][2:4], 16)
            OxB = int(OxfordArray[l][4:6], 16)
            distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
            distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
            if distVelCas < sumdistlowC:
                sumdistlowC = distVelCas
                hexCashlow = VelvetArray[j] 
        
        for k in range(len(CashmereArray)):
            SatR = int(CashmereArray[k][0:2], 16)
            SatG = int(CashmereArray[k][2:4], 16)
            SatB = int(CashmereArray[k][4:6], 16)
            distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
            if distVelSat < sumdistlowS:
                sumdistlowS = distVelSat
                hexSatlow = CashmereArray[k]
        
        
        for l in range(len(SatinArray)):
            OxR = int(SatinArray[l][0:2], 16)
            OxG = int(SatinArray[l][2:4], 16)
            OxB = int(SatinArray[l][4:6], 16)
            distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
                distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = CashmereArray[j] 

            for k in range(len(SatinArray)):
                SatR = int(SatinArray[k][0:2], 16)
                SatG = int(SatinArray[k][2:4], 16)
                SatB = int(SatinArray[k][4:6], 16)
                distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = SatinArray[k]
        
        
            for l in range(len(OxfordArray)):
                OxR = int(OxfordArray[l][0:2], 16)
                OxG = int(OxfordArray[l][2:4], 16)
                OxB = int(OxfordArray[l][4:6], 16)
                distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
                distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = VelvetArray[j] 
            
            for k in range(len(SatinArray)):
                SatR = int(SatinArray[k][0:2], 16)
                SatG = int(SatinArray[k][2:4], 16)
                SatB = int(SatinArray[k][4:6], 16)
                distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = SatinArray[k]
            
            
            for l in range(len(OxfordArray)):
                OxR = int(OxfordArray[l][0:2], 16)
                OxG = int(OxfordArray[l][2:4], 16)
                OxB = int(OxfordArray[l][4:6], 16)
                distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
                distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = VelvetArray[j] 
            
            for k in range(len(CashmereArray)):
                SatR = int(CashmereArray[k][0:2], 16)
                SatG = int(CashmereArray[k][2:4], 16)
                SatB = int(CashmereArray[k][4:6], 16)
                distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = CashmereArray[k]
            
            
            for l in range(len(OxfordArray)):
                OxR = int(OxfordArray[l][0:2], 16)
                OxG = int(OxfordArray[l][2:4], 16)
                OxB = int(OxfordArray[l][4:6], 16)
                distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
                distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = VelvetArray[j] 
            
            for k in range(len(CashmereArray)):
                SatR = int(CashmereArray[k][0:2], 16)
                SatG = int(CashmereArray[k][2:4], 16)
                SatB = int(CashmereArray[k][4:6], 16)
                distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = CashmereArray[k]
            
            
            for l in range(len(SatinArray)):
                OxR = int(SatinArray[l][0:2], 16)
                OxG = int(SatinArray[l][2:4], 16)
                OxB = int(SatinArray[l][4:6], 16)
                distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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



def LowestSetScoresOpt():
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
                distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = CashmereArray[j] 

            for k in range(len(SatinArray)):
                SatR = int(SatinArray[k][0:2], 16)
                SatG = int(SatinArray[k][2:4], 16)
                SatB = int(SatinArray[k][4:6], 16)
                distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = SatinArray[k]
        
        
            for l in range(len(OxfordArray)):
                OxR = int(OxfordArray[l][0:2], 16)
                OxG = int(OxfordArray[l][2:4], 16)
                OxB = int(OxfordArray[l][4:6], 16)
                distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
                distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = VelvetArray[j] 
            
            for k in range(len(SatinArray)):
                SatR = int(SatinArray[k][0:2], 16)
                SatG = int(SatinArray[k][2:4], 16)
                SatB = int(SatinArray[k][4:6], 16)
                distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = SatinArray[k]
            
            
            for l in range(len(OxfordArray)):
                OxR = int(OxfordArray[l][0:2], 16)
                OxG = int(OxfordArray[l][2:4], 16)
                OxB = int(OxfordArray[l][4:6], 16)
                distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
                distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = VelvetArray[j] 
            
            for k in range(len(CashmereArray)):
                SatR = int(CashmereArray[k][0:2], 16)
                SatG = int(CashmereArray[k][2:4], 16)
                SatB = int(CashmereArray[k][4:6], 16)
                distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = CashmereArray[k]
            
            
            for l in range(len(OxfordArray)):
                OxR = int(OxfordArray[l][0:2], 16)
                OxG = int(OxfordArray[l][2:4], 16)
                OxB = int(OxfordArray[l][4:6], 16)
                distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
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
                distVelCas = rgbd2(VelvR,VelvG,VelvB,CasR,CasG,CasB)
                if distVelCas < sumdistlowC:
                    sumdistlowC = distVelCas
                    hexCashlow = VelvetArray[j] 
            
            for k in range(len(CashmereArray)):
                SatR = int(CashmereArray[k][0:2], 16)
                SatG = int(CashmereArray[k][2:4], 16)
                SatB = int(CashmereArray[k][4:6], 16)
                distVelSat = rgbd2(VelvR,VelvG,VelvB,SatR,SatG,SatB)
                if distVelSat < sumdistlowS:
                    sumdistlowS = distVelSat
                    hexSatlow = CashmereArray[k]
            
            
            for l in range(len(SatinArray)):
                OxR = int(SatinArray[l][0:2], 16)
                OxG = int(SatinArray[l][2:4], 16)
                OxB = int(SatinArray[l][4:6], 16)
                distVelOx = rgbd2(VelvR,VelvG,VelvB,OxR,OxG,OxB)
                if distVelOx < sumdistlowO:
                    sumdistlowO = distVelOx
                    hexOxlow = SatinArray[l]

            sumdist = rgbDist(VelvR,VelvG,VelvB,int(hexCashlow[0:2], 16),int(hexCashlow[2:4], 16),int(hexCashlow[4:6], 16),
                            int(hexSatlow[0:2], 16),int(hexSatlow[2:4], 16),int(hexSatlow[4:6], 16),int(hexOxlow[0:2], 16),int(hexOxlow[2:4], 16),int(hexOxlow[4:6], 16))
            sumdist = f"{sumdist:.4f}"
            if f'{hexCashlow}, {hexSatlow}, {hexOxlow}, {OxfordArray[i]}, {sumdist}' not in LowScoreHexes:
                LowScoreHexes.append(f'{hexCashlow}, {hexSatlow}, {hexOxlow}, {OxfordArray[i]}, {sumdist}')
        LowScoreHexes.sort(reverse=True, key=MyKey)

        for m in range(len(LowScoreHexes)-1, -1, -1):
            # check velvet first
            if ((LowScoreHexes[m][0:6] not in VelvetArrayOut) and (LowScoreHexes[m][8:14] not in CashmereArrayOut) and (LowScoreHexes[m][16:22] not in SatinArrayOut) and
                        (LowScoreHexes[m][24:30] not in OxfordArrayOut)):
                            LowScoreHexesFinal.append(LowScoreHexes[m])
                            VelvetArrayOut.append(LowScoreHexes[m][0:6])
                            VelvetArray.remove(LowScoreHexes[m][0:6])
                            CashmereArrayOut.append(LowScoreHexes[m][8:14])
                            CashmereArray.remove(LowScoreHexes[m][8:14])
                            SatinArrayOut.append(LowScoreHexes[m][16:22])
                            SatinArray.remove(LowScoreHexes[m][16:22])
                            OxfordArrayOut.append(LowScoreHexes[m][24:30])
                            OxfordArray.remove(LowScoreHexes[m][24:30])
                            shortestPiece = shortestPiece - 1                            
    LowScoreHexesFinal.sort(key=MyKey)    
    for i in range(len(LowScoreHexesFinal)):
        print(LowScoreHexesFinal[i])











if __name__ == '__main__':
    #HexSetLowestGroupByHat()
    #HexSetLowestScoresTot()
    #HexSortHatFast()
    
    #Best functions below here
    
    #HexSortALL()
    #LowestSetScores()
    LowestSetScoresOpt()




