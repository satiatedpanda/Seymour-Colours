import json

databaselist = []

with open(r"c:\Users\flemi\AppData\Roaming\PrismLauncher\instances\1.21.11 Skyblock\minecraft\config\seymouranalyzer\collection.json", "r") as file:
    col: dict = json.load(file)
    colkeys = list(col.keys())


    for i in range(len(col)):
        curName: str = col[colkeys[i]]["pieceName"]
        curName = curName.replace(" ", "_")
        curName = curName.replace("Giant_", "")
        curHex = col[colkeys[i]]["hexcode"]
        databaselist.append(f"{curName} #{curHex}")


with open(r"C:\Users\flemi\Documents\SeymourStuf\seymourdatabase.txt", "w") as f:
    dbstr = ""
    for i in range(len(databaselist)):
        dbstr = f"{dbstr}{databaselist[i]}\n".upper()
    f.write(dbstr)

if __name__ == '__main__':
    for j in range(len(databaselist)):
        print(databaselist[j])