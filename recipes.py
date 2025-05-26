import json
import os

class RecipeManager:
    def __init__(self, data_file="recipes.json"):
        self.data_file = data_file
        self.recipes = self.load_recipes()

    def load_recipes(self):
        if not os.path.exists(self.data_file):
            return []
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading recipes: {e}")
            return []

    def save_recipes(self):
        try:
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump(self.recipes, f, indent=4)
        except Exception as e:
            print(f"Error saving recipes: {e}")

    def add_recipe(self, title, ingredients, instructions):
        recipe = {
            "title": title.strip(),
            "ingredients": ingredients.strip(),
            "instructions": instructions.strip()
        }
        self.recipes.append(recipe)
        self.save_recipes()

    def delete_recipe(self, index):
        if 0 <= index < len(self.recipes):
            self.recipes.pop(index)
            self.save_recipes()

    def edit_recipe(self, index, title, ingredients, instructions):
        if 0 <= index < len(self.recipes):
            self.recipes[index] = {
                "title": title.strip(),
                "ingredients": ingredients.strip(),
                "instructions": instructions.strip()
            }
            self.save_recipes()

    def get_recipe_titles(self):
        return [r["title"] for r in self.recipes]

    def get_recipe(self, index):
        if 0 <= index < len(self.recipes):
            return self.recipes[index]
        return None

    def clear_all(self):
        self.recipes = []
        self.save_recipes()
