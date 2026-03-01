from challenge_one import mining
from challenge_two import shop_buy
from challenge_three import shop_sell


# INVENTORY AND STOCK FOR SHOPS
inventory = {
    "money":0,
    "pick":"basic"
}

stock = [
    ["Canteen",5],
    ["Pickaxe (Enhanced)",25],
    ["Pickaxe (Greater)",50], 
    ["Pickaxe (Superior)",100]
]

gem_inventory = [
    ["diamond",0,"uncommon"]
]
    
print("Welcome to the curio shop!")
print("Hope you find what you're looking for...")
while True:
    print("What are you looking to do?")
    choice = input("Buy/Sell/Mine\n")
    if choice.lower() == "buy":
        shop_buy(stock, inventory)
    elif choice.lower() == "sell":
        shop_sell(inventory, gem_inventory)
    elif choice.lower() == "mine":
        mining(inventory,gem_inventory)
    elif choice.lower() == "inventory":
        print(f"Money: ${inventory['money']} | Pickaxe: {inventory['pick']}")
        print("Gem Inventory:")
        if len(gem_inventory) == 0:
            print("  - Empty")
        else:
            for gem in gem_inventory:
                if gem[1] == 0:
                    print(f"  - Unappraised {gem[0].title()}")
                else:
                    print(f"  - {gem[2].title()} {gem[0].title()} (Value: ${gem[1]})")
    elif choice.lower() == "exit":
        break