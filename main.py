from recipe_assistant import RecipeAssistant

def get_user_preferences():
    print("\n=== Recipe Preference Collection ===")
    
    dietary_restrictions = input("Enter any dietary restrictions (e.g., vegetarian, vegan, gluten-free): ")
    ingredients = input("Enter available ingredients (comma-separated): ").split(',')
    cuisine = input("Enter preferred cuisine (or 'any'): ")
    cooking_time = input("Enter maximum cooking time in minutes (or 'any'): ")
    
    return {
        'dietary_restrictions': dietary_restrictions,
        'ingredients': [i.strip() for i in ingredients],
        'cuisine': cuisine,
        'cooking_time': cooking_time
    }

def main():
    assistant = RecipeAssistant()
    
    while True:
        print("\n=== Recipe Assistant Menu ===")
        print("1. Get recipe suggestions")
        print("2. Get cooking instructions")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            preferences = get_user_preferences()
            suggestions = assistant.get_recipe_suggestions(preferences)
            print("\n=== Recipe Suggestions ===")
            print(suggestions)
            
        elif choice == '2':
            recipe_name = input("\nEnter the recipe name: ")
            servings = int(input("Enter number of servings: "))
            instructions = assistant.get_cooking_instructions(recipe_name, servings)
            print("\n=== Cooking Instructions ===")
            print(instructions)
            
        elif choice == '3':
            print("\nThank you for using Recipe Assistant!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 