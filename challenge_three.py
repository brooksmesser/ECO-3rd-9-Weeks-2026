# Challenge Three: The Appraisal Engine


"""
PROCEDURE shop_sell(inventoryMoney, gem_inventory) {
    DISPLAY "What have you got to sell?"
    
    IF (LENGTH(gem_inventory) = 0) {
        DISPLAY "If ya ain't got nothing to sell, why ya bothering me?"
        RETURN inventoryMoney
    }
    
    DISPLAY "--- Your Gems ---"
    i ← 1
    FOR EACH gem IN gem_inventory {
        // If the value (index 2) is 0, hide the rarity
        IF (gem[2] = 0) {
            DISPLAY i + ". Unappraised " + gem[1]
        } ELSE {
            DISPLAY i + ". " + gem[3] + " " + gem[1] + " (Value: $" + gem[2] + ")"
        }
        i ← i + 1
    }
    
    DISPLAY "Enter the number of the gem you want to sell:"
    choice ← INPUT()
    
    IF (choice < 1 OR choice > LENGTH(gem_inventory)) {
        DISPLAY "You don't have that gem! Stop wasting my time!"
        RETURN inventoryMoney
    }
    
    selectedGem ← gem_inventory[choice]
    gemName ← selectedGem[1]
    gemValue ← selectedGem[2]
    gemRarity ← selectedGem[3]
    
    IF (gemRarity = "appraised_fake") {
        DISPLAY "Now look here, I ain't in the business of buying fakes."
        RETURN inventoryMoney
    }
    
    IF (gemValue = 0) {
        DISPLAY "Looks like this hasn't been appraised yet. Let me see..."
        
        IF (gemRarity = "common") {
            gemValue ← RANDOM(2, 5)
        } ELSE IF (gemRarity = "uncommon") {
            gemValue ← RANDOM(7, 10)
        } ELSE IF (gemRarity = "rare") {
            gemValue ← RANDOM(12, 20)
        } ELSE IF (gemRarity = "unique") {
            gemValue ← RANDOM(25, 50)
        } ELSE {
            gemValue ← 0
            gemRarity ← "appraised_fake"
        }
        
        selectedGem[2] ← gemValue
        selectedGem[3] ← gemRarity
        gem_inventory[choice] ← selectedGem
    }
    
    IF (gemRarity ≠ "appraised_fake") {
        DISPLAY "Ah yes. I'd be willing to offer you $" + gemValue + " for that."
        DISPLAY "Interested? Y/N"
        accept ← INPUT()
        
        IF (accept = "y" OR accept = "Y") {
            inventoryMoney ← inventoryMoney + gemValue
            REMOVE(gem_inventory, choice)
            DISPLAY "Transaction complete!"
        }
    } ELSE {
        DISPLAY "Now look here, I ain't in the business of buying fakes."
    }
    
    RETURN inventoryMoney
}
"""

import random

def shop_sell(inventory, gem_inventory):
    # Write your translated Python code below this line!
    pass