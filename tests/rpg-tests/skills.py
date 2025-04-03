from narrata.rpg import Player

player_skills = Player.Skills()

# Define the top-level categories and subcategories
categories = [
    ("attacks", ["melee", "ranged"]),
    ("abilities", ["support", "status"]),
    ("magic", ["elemental", "dark", "light"]),
]

# Loop through and create categories and subcategories
for category, subcategories in categories:
    player_skills.new_category(category)  # Add top-level category
    for subcategory in subcategories:
        player_skills.new_category(category, subcategory)  # Add subcategory

# Define the skills data in a more structured format
skills_data = [
    ("slash", {"damage": 15, "stamina": 5}, "attacks", "melee"),
    ("bite", {"damage": 8, "stamina": 3}, "attacks", "melee"),
    ("long shot", {"damage": 12, "range": 20}, "attacks", "ranged"),
    ("fireball", {"damage": 30, "mana": 10}, "magic", "elemental"),
    ("lightning bolt", {"damage": 25, "mana": 8}, "magic", "elemental"),
    ("dark pulse", {"damage": 40, "mana": 12, "lifesteal": 5}, "magic", "dark"),
    ("divine light", {"healing": 25, "mana": 15}, "magic", "light"),
    ("heal", {"healing": 20, "mana": 15}, "abilities", "support"),
    ("poison touch", {"poison": 5, "stamina": 4}, "abilities", "status")
]

# Loop through and add skills to respective categories and subcategories
for skill_name, attributes, category, subcategory in skills_data:
    player_skills.add_skill(skill_name, attributes, category, subcategory)

# Removing skills
player_skills.remove_skill("fireball", "magic", "elemental")
player_skills.remove_skill("boom", "attacks", "ranged", "long")  # This skill does not exist
                                                                 # Throws an error (print statement for flow)