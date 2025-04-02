import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "assets.json")

def _load_json():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def _save_json(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

class Player:

    class Bio:
        def __init__(self, name, **kwargs):
            self.name = name
            self.__dict__.update(kwargs)
            player_data = _load_json()
            player_data.setdefault("player", {})["bio"] = self.__dict__
            _save_json(player_data)

    class Stats:
        def __init__(self, health, **kwargs):
            self.health = health
            self.__dict__.update(kwargs)
            player_data = _load_json()
            player_data.setdefault("player", {})["stats"] = self.__dict__
            _save_json(player_data)

    class Inventory:
        def __init__(self, **kwargs):
            player_data = _load_json()
            self.inventory = player_data.setdefault("player", {}).setdefault("inventory", {})
            _save_json(player_data)

        def _get_nested_dict(self, keys):
            """Gets a nested dictionary structure, creating it if necessary."""
            player_data = _load_json()
            inventory = player_data.setdefault("player", {}).setdefault("inventory", {})

            current = inventory
            for key in keys:
                current = current.setdefault(key, {})

            _save_json(player_data)
            return player_data

        def new_category(self, *categories):
            """Creates a new category and subcategories."""
            self._get_nested_dict(categories)

        def add_item(self, item_name, item_data, *categories):
            """Adds an item to a specific category."""
            player_data = self._get_nested_dict(categories)
            inventory = player_data["player"]["inventory"]

            # Navigate to the correct category
            current = inventory
            for key in categories:
                current = current[key]

            current[item_name] = item_data
            _save_json(player_data)

        def remove_item(self, item_name, *categories):
            """Removes an item from a specific category."""
            player_data = _load_json()
            inventory = player_data.setdefault("player", {}).setdefault("inventory", {})

            current = inventory
            for key in categories:
                if key in current:
                    current = current[key]
                else:
                    print(f"Category {key} not found!")
                    return

            if item_name in current:
                del current[item_name]
                _save_json(player_data)
            else:
                print(f"Item {item_name} not found in {' -> '.join(categories)}!")