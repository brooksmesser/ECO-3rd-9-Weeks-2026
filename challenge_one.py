# Challenge One: The Mining Engine


"""
PROCEDURE mining(inventoryPick, gem_inventory, gemstones, rarity) {
    DISPLAY "You head down to the mines..."
    
    IF (inventoryPick = "basic"){
        start_percent ← 30
    } ELSE IF (inventoryPick = "good"){
        start_percent ← 50
    } ELSE IF (inventoryPick = "better"){
        start_percent ← 70
    } ELSE {
        start_percent ← 90
    }
    
    DISPLAY "You swing your pick at the rock..."
    
    chance ← start_percent
    keepSwinging ← "y"
    
    REPEAT UNTIL (keepSwinging ≠ "y" AND keepSwinging ≠ "Y") {
        DISPLAY "Swing? Y/N"
        keepSwinging ← INPUT()
        
        IF (keepSwinging = "y" OR keepSwinging = "Y") {
            DISPLAY "You reveal a little more gemstone..."
            chance ← chance + 5
        }
        ELSE {
            roll ← RANDOM(1, 100)
            
            IF (roll ≤ chance) {
                // Pick a random gem and rarity using 1-based indexing
                gem_name ← gemstones[RANDOM(1, LENGTH(gemstones))]
                gem_rarity ← rarity[RANDOM(1, LENGTH(rarity))]
                
                DISPLAY "You carefully uncover a " + gem_name + "!"
                
                // Append as a list: [Name, Value, Rarity]
                newGem ← [gem_name, 0, gem_rarity] 
                APPEND(gem_inventory, newGem)
            }
            ELSE {
                DISPLAY "Unlucky! Your wild swings crack the gem. You'll have to return and try again."
            }
        }
    }
}
"""

import random

def mining(inventory, gem_inventory):
    gemstones = ["diamond", "ruby", "emerald", "topaz", "onyx", "opal", "turquoise", "lapis lazuli"]
    rarity = ["common", "uncommon", "rare", "unique", "fake"]
    #===========I dont know what this part is above I think its part of thre code and you just gave it to me ==============================================
    # Write your translated Python code below this line!
    import random

def mining(inventoryPick, gem_inventory, gemstones, rarity):
    print("You head down to the mines...")

    if inventoryPick == "basic":
        start_percent = 30
    elif inventoryPick == "good":
        start_percent = 50
    elif inventoryPick == "better":
        start_percent = 70
    else:
        start_percent = 90

    print("You swing your pick at the rock...")

    chance = start_percent
    keepSwinging = "y"

    while keepSwinging == "y" or keepSwinging == "Y":
        keepSwinging = input("Swing? Y/N: ")

        if keepSwinging == "y" or keepSwinging == "Y":
            print("You reveal a little more gemstone...")
            chance += 5
        else:
            roll = random.randint(1, 100)

            if roll <= chance:
                gem_name = random.choice(gemstones)
                gem_rarity = random.choice(rarity)

                print(f"You carefully uncover a {gem_name}!")

                newGem = [gem_name, 0, gem_rarity]
                gem_inventory.append(newGem)
            else:
                print("Unlucky! Your wild swings crack the gem. You'll have to return and try again.")
