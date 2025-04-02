from narrata.rpg import Player

player_inventory = Player.Inventory()

player_inventory.new_category("weapons")
player_inventory.new_category("weapons", "melee")
player_inventory.new_category("weapons", "ranged")
player_inventory.new_category("potions", "healing")
player_inventory.new_category("potions", "damaging")

# Adding items
player_inventory.add_item("katana", {"damage": 12, "speed": 8}, "weapons", "melee", "swords")
player_inventory.add_item("longbow", {"damage": 15, "range": 20}, "weapons", "ranged")
player_inventory.add_item("broadsword", {"damage": 20, "speed": 4}, "weapons", "melee", "swords")
player_inventory.add_item("bow", {"damage": 10, "range": 15}, "weapons", "ranged")
player_inventory.add_item("spear", {"damage": 8, "speed": 6}, "weapons", "melee", "swords") 
player_inventory.add_item("healing potion", {"healing": 10}, "potions", "healing")
player_inventory.add_item("damage potion", {"damage": 5}, "potions", "damaging")
player_inventory.add_item("poison potion", {"poison": 3, "damage": 2}, "potions", "damaging")

# Removing an item
player_inventory.remove_item("katana", "weapons", "melee", "swords")
player_inventory.remove_item("longbow", "weapons", "ranged")