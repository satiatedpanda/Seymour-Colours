from private_functions.opendatabase import opendatabase
import csv

def databaseExtract():
    databaselist: list[str] = []

    col: dict = opendatabase() #This returns a dict from the json object. Done this way to not dox myself :D
    colkeys = list(col.keys())
    for i in range(len(col)):
        curName: str = col[colkeys[i]]["pieceName"]
        curName = curName.replace(" ", "_")
        curName = curName.replace("Giant_", "") # replace all reforges with adding on more replace statements when necessary
        curHex = col[colkeys[i]]["hexcode"]
        databaselist.append(f"{colkeys[i]} {curName} #{curHex}".upper())


    with open(r"seymourdatabase.txt", "w") as f:
        dbstr = ""
        for i in range(len(databaselist)):
            dbstr = f"{databaselist[i]}\n".upper()
            f.write(dbstr)
    return databaselist

def random_extract():
    collection: list[list[str]] = []
    databaselist: list[str] = []
    with open(r"C:\Users\flemi\Downloads\seymourDB\seymourDB.csv") as fp:
        reader = csv.reader(fp, delimiter=",")
        collection = [row for row in reader]
    for sublist in collection:
        name = sublist[1]
        ArmorTypes = ["VELVET_TOP_HAT", "CASHMERE_JACKET", "SATIN_TROUSERS", "OXFORD_SHOES"]   
        if name not in ArmorTypes:     
            bad = True
            for string in ArmorTypes:
                if string in name:
                    name = string
                    bad = False
            if bad == True:
                print(f"incorrect armour type: {name}")
                exit()
            
        databaselist.append(f"{sublist[3]} {name} #{sublist[0]}".upper())


    with open(r"katzedatabase.txt", "w") as f:
        dbstr = ""
        for i in range(len(databaselist)):
            dbstr = f"{databaselist[i]}\n".upper()
            f.write(dbstr)
            if i%500 == 0:
                print(i)
    return databaselist

def openfile():
    with open("seymourdatabase.txt", "r") as fd:
        database = fd.read().split("\n")
        database.pop()
    return database


if __name__ == '__main__':
    databaselist =databaseExtract()
    for j in range(len(databaselist)):
        print(databaselist[j])