from private_functions.opendatabase import opendatabase


def databaseExtract():
    databaselist = []

    col: dict = opendatabase() #This returns a dict from the json object. Done this way to not dox myself :D
    colkeys = list(col.keys())
    for i in range(len(col)):
        curName: str = col[colkeys[i]]["pieceName"]
        curName = curName.replace(" ", "_")
        curName = curName.replace("Giant_", "") # replace all reforges with adding on more replace statements when necessary
        curHex = col[colkeys[i]]["hexcode"]
        databaselist.append(f"{curName} #{curHex}")


    with open(r"seymourdatabase.txt", "w") as f:
        dbstr = ""
        for i in range(len(databaselist)):
            dbstr = f"{dbstr}{databaselist[i]}\n".upper()
        f.write(dbstr)
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