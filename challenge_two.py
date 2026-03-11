# Challenge Two: The Shop Menu


"""
PROCEDURE shop_buy(inventoryMoney, inventoryPick, stockList) {
    keepShopping ← "y"
    
    REPEAT UNTIL (keepShopping ≠ "y" AND keepShopping ≠ "Y") {
        DISPLAY "--- Items for Sale ---"
        i ← 1
        FOR EACH item IN stockList {
            DISPLAY i + ". " + item[1] + " - $" + item[2]
            i ← i + 1
        }
        
        DISPLAY "Enter the number of the item you want to buy:"
        choice ← INPUT()
        
        IF (choice ≥ 1 AND choice ≤ LENGTH(stockList)) {
            selectedItem ← stockList[choice]
            itemName ← selectedItem[1]
            itemPrice ← selectedItem[2]
            
            IF (inventoryMoney ≥ itemPrice) {
                inventoryMoney ← inventoryMoney - itemPrice
                
                // Extract 3 characters starting at the 10th letter (1-based)
                IF (SUBSTRING(itemName, 10, 3) = "Enh") {
                    inventoryPick ← "good"
                }
                ELSE IF (SUBSTRING(itemName, 10, 3) = "Gre") {
                    inventoryPick ← "better"
                }
                ELSE IF (SUBSTRING(itemName, 10, 3) = "Sup") {
                    inventoryPick ← "best"
                }
                
                REMOVE(stockList, choice)
                DISPLAY "You bought the " + itemName + "!"
            }
            ELSE {
                DISPLAY "You can't afford that!"
            }
        }
        ELSE {
            DISPLAY "Sorry, we don't have that."
        }
        
        DISPLAY "Keep shopping? Y/N"
        keepShopping ← INPUT()
    }
    
    RETURN inventoryMoney
}
"""

def shop_buy(stock, inventory):
    # Write your translated Python code below this line!
    def shop_buy(inventoryMoney, inventoryPick, stockList):
    keepShopping = "y"

    while keepShopping == "y" or keepShopping == "Y":
        print("--- Items for Sale ---")

        for i, item in enumerate(stockList, start=1):
            print(f"{i}. {item[0]} - ${item[1]}")

        choice = input("Enter the number of the item you want to buy: ")

        if not choice.isdigit():
            print("Sorry, we don't have that.")
            keepShopping = input("Keep shopping? Y/N: ")
            continue

        choice = int(choice)

        if 1 <= choice <= len(stockList):
            selectedItem = stockList[choice - 1]

            itemName = selectedItem[0]
            itemPrice = selectedItem[1]

            if inventoryMoney >= itemPrice:
                inventoryMoney -= itemPrice

                substring = itemName[9:12]

                if substring == "Enh":
                    inventoryPick = "good"
                elif substring == "Gre":
                    inventoryPick = "better"
                elif substring == "Sup":
                    inventoryPick = "best"

                stockList.pop(choice - 1)

                print(f"You bought the {itemName}!")
            else:
                print("You can't afford that!")
        else:
            print("Sorry, we don't have that.")

        keepShopping = input("Keep shopping? Y/N: ")

    return inventoryMoney
