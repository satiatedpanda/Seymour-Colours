from random import randrange
import math
from time import time


bountydictionary = {
    "T1 Pure Black": [("Helm+Legs+Boots", 400),("Any", 350)],
    "T1 Exo Pure Black": [("Any", 500)],
    "T1 Reaper": [("Any", 250)],
    "T1 Final Destination": [("Chest+Boots", 65)],
    "T1 Final Destination Legs": [("Legs", 70)],
    "T1 Shimmering Light": [("Legs+0x0x1x", 125),("Any", 60)],
    "T1 Werewolf": [("Boots+1x1x0x", 110),("Any", 50)],

    "T2 Pure White": [("Chest+Legs", 85),("Any", 70)],
    "T1 FCF3FF": [("Any", 120)],
    "T1 E5D1ED": [("Any", 50)],
    "T1 EFE1F5": [("Helm+Chest+ExExFx", 100),("Any", 75)],
    "T1 Nutcracker": [("Legs", 80)],
    "T1 Nyanza Dye": [("Helm", 100), ("Any", 55)],
    "T1 Speedster": [("Boots+ExFxFx", 110), ("Any", 60)],
    
    "T1 Young Drag": [("Chest+DxExFx", 100),("Any", 50)],
    "T1 Protector": [("Legs", 230)],
    "T1 Old": [("Any", 50)],
    "T1 Superior Boots": [("Boots", 50)],
    "T1 Strong Legs": [("Legs", 45)],
   
    "T1 1F0030": [("Helm+Chest", 150)],
    "T1 Bone Dye": [("Helm", 80)],
    "T1 Dark Purple Dye": [("Helm", 150)],
    "T1 Exo Pure Light Blue": [("Boots", 50)],
    "T1 Exceedingly Comfy Sneakers": [("Boots", 100)]
}
bountykeys = list(bountydictionary.keys())

bounties = ""
secbounties = ""
curtime = math.floor(time())+86400

randbounty = bountykeys[randrange(len(bountykeys))]
randbountyprices = bountydictionary[randbounty]

firstval, firstprice = randbountyprices[0]
bounties = bounties + f"Today: {randbounty} {firstval}! {firstprice}m -> {firstprice+50}m"

if len(randbountyprices)>1:
    secval, secprice = randbountyprices[1]
    secbounties = secbounties + f"\n-# or {secval} for {secprice}m -> {secprice+50}m"

print("\nBounty of the day! (each day I increase a random bounty from my list by *50m*)")
print("All of my bounties - https://discord.com/channels/1075968098626179174/1356070137840537621/1356070137840537621")
print(f"{bounties}{secbounties}")
print(f"Ends <t:{curtime}:R>\n")