import json
import os

def load_recipes(file_path):
    """Load recipes from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_recipes(data, file_path):
    """Save recipes to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_recipe(name, file_path):
    """Add a new recipe to the JSON file with dynamic ingredient input."""
    data = load_recipes(file_path)
    ingredients = {
        "bread": [],
        "protein": [],
        "veggie": [],
        "sauce_flavor": [],
        "cheese": []
    }

    print("Let's add the ingredients for the new recipe.")
    for category in ingredients.keys():
        while True:
            item = input(f"Enter an ingredient for {category} (or type 'done' to finish this category): ").strip()
            if item.lower() == 'done':
                break
            if item in data['ingredients'][category]:
                ingredients[category].append(item)
            else:
                print(f"{item} is not a valid ingredient in the {category} category. Please enter a valid ingredient.")
    
    new_recipe = {
        "name": name,
        "ingredients": ingredients
    }
    data["classicRecipes"].append(new_recipe)
    save_recipes(data, file_path)
    print(f"Recipe '{name}' added successfully with the following ingredients: {ingredients}")

def delete_recipe(name, file_path):
    """Delete a recipe from the JSON file."""
    data = load_recipes(file_path)
    data["classicRecipes"] = [recipe for recipe in data["classicRecipes"] if recipe["name"] != name]
    save_recipes(data, file_path)
    print(f"Recipe '{name}' deleted successfully.")

def display_available_ingredients(file_path):
    """Display available ingredients by category."""
    data = load_recipes(file_path)
    ingredients = data['ingredients']
    print("Available Ingredients by Category:")
    for category, items in ingredients.items():
        print(f"{category.capitalize()}: {', '.join(items)}")

def display_all_recipes(file_path):
    """Display all recipe names."""
    data = load_recipes(file_path)
    print("Existing Recipes:")
    for recipe in data["classicRecipes"]:
        print(f"- {recipe['name']}")

def search_recipe(name, file_path):
    """Search for a recipe by name. Offer to create it if not found."""
    data = load_recipes(file_path)
    found = any(recipe['name'] == name for recipe in data["classicRecipes"])
    if found:
        print(f"Recipe '{name}' found.")
    else:
        print(f"Recipe '{name}' not found. Would you like to create it? (yes/no)")
        answer = input().strip().lower()
        if answer == 'yes':
            # Prompt user for ingredients or implement a method to add them
            print("Please enter ingredients in the format 'category: ingredient1, ingredient2, ...'")
            ingredients = input("Ingredients: ").strip()  # Simplified, adjust as needed
            add_recipe(name, ingredients, file_path)
        else:
            print("No new recipe created.")

def main_menu(file_path):
    while True:
        print("\nRecipe Manager Menu:")
        print("1. Display available ingredients")
        print("2. Display all recipes")
        print("3. Add a recipe")
        print("4. Delete a recipe")
        print("5. Search for a recipe")
        print("6. Exit")
        choice = input("Please enter your choice (1-6): ").strip()

        if choice == '1':
            display_available_ingredients(file_path)
        elif choice == '2':
            display_all_recipes(file_path)
        elif choice == '3':
            name = input("Enter the name of the recipe: ").strip()
            add_recipe(name, file_path)
        elif choice == '4':
            name = input("Enter the name of the recipe to delete: ").strip()
            delete_recipe(name, file_path)
        elif choice == '5':
            name = input("Enter the name of the recipe to search for: ").strip()
            search_recipe(name, file_path)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the file
    file_path = os.path.join(script_dir, 'recipes.json')
    print("Welcome to the Recipe Manager!")
    main_menu(file_path)