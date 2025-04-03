from narrata.rpg import Player

player_inventory = Player.Inventory()

# Define the categories and subcategories
categories = [
    ("weapons", ["melee", "ranged"]),
    ("potions", ["healing", "damaging"]),
]

# Loop through and create categories and subcategories
for category, subcategories in categories:
    player_inventory.new_category(category)  # Add top-level category
    for subcategory in subcategories:
        player_inventory.new_category(category, subcategory)  # Add subcategory

# Define the items data in a more structured format
items_data = [
    ("katana", {"damage": 12, "speed": 8}, "weapons", "melee", "blades"),
    ("longbow", {"damage": 15, "range": 20}, "weapons", "ranged"),
    ("broadsword", {"damage": 20, "speed": 4}, "weapons", "melee", "blades"),
    ("bow", {"damage": 10, "range": 15}, "weapons", "ranged"),
    ("spear", {"damage": 8, "speed": 6}, "weapons", "melee", "blades"),
    ("healing potion", {"healing": 10}, "potions", "healing"),
    ("damage potion", {"damage": 5}, "potions", "damaging"),
    ("poison potion", {"poison": 3, "damage": 2}, "potions", "damaging"),
    ("bat", {"damage": 10, "speed": 7}, "weapons", "melee", "other"),
    ("mace", {"damage": 15, "speed": 4}, "weapons", "melee", "other"),
]

# Loop through and add items to respective categories and subcategories
for item_name, attributes, category, subcategory, *extra in items_data:
    if extra:
        # If there is an extra subcategory, add that to the item
        player_inventory.add_item(item_name, attributes, category, subcategory, extra[0])
    else:
        # Otherwise, add the item without extra subcategory
        player_inventory.add_item(item_name, attributes, category, subcategory)

# Removing items
player_inventory.remove_item("katana", "weapons", "melee", "blades")
player_inventory.remove_item("longbow", "weapons", "ranged")
player_inventory.remove_item("shortbow", "weapons", "ranged") # This item doesn't exist
                                                              # Throws an error (print statement for flow)