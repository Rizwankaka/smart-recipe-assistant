import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

class RecipeAssistant:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.model = genai.GenerativeModel('gemini-pro')
        self.favorites_file = 'favorites.json'
        self.history_file = 'cooking_history.csv'
        
    def get_recipe_suggestions(self, preferences):
        prompt = f"""
        Suggest 3 recipes based on the following preferences:
        - Dietary restrictions: {preferences.get('dietary_restrictions', 'None')}
        - Available ingredients: {preferences.get('ingredients', [])}
        - Cuisine preference: {preferences.get('cuisine', 'Any')}
        - Cooking time: {preferences.get('cooking_time', 'Any')}
        
        For each recipe, provide:
        1. Name
        2. Ingredients list
        3. Cooking time
        4. Difficulty level
        """
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def get_cooking_instructions(self, recipe_name, servings=2):
        prompt = f"""
        Provide detailed step-by-step cooking instructions for {recipe_name} for {servings} servings.
        Include:
        1. Prep time
        2. Cooking time
        3. Detailed steps
        4. Tips for success
        """
        
        response = self.model.generate_content(prompt)
        return response.text 
    
    def get_nutritional_info(self, recipe_name):
        prompt = f"""
        Provide detailed nutritional information for {recipe_name}. Include:
        1. Calories per serving
        2. Macronutrients (protein, carbs, fats)
        3. Key vitamins and minerals
        4. Dietary considerations
        """
        response = self.model.generate_content(prompt)
        return response.text
    
    def get_ingredient_substitutions(self, ingredient):
        prompt = f"""
        Suggest healthy substitutions for {ingredient}. For each substitution, provide:
        1. Name of substitute
        2. Conversion ratio
        3. Impact on taste/texture
        4. Nutritional differences
        """
        response = self.model.generate_content(prompt)
        return response.text
    
    def save_to_favorites(self, recipe_data):
        try:
            if os.path.exists(self.favorites_file):
                with open(self.favorites_file, 'r') as f:
                    favorites = json.load(f)
            else:
                favorites = []
                
            favorites.append(recipe_data)
            
            with open(self.favorites_file, 'w') as f:
                json.dump(favorites, f)
            return True
        except Exception as e:
            print(f"Error saving to favorites: {e}")
            return False
    
    def get_favorites(self):
        if os.path.exists(self.favorites_file):
            with open(self.favorites_file, 'r') as f:
                return json.load(f)
        return []
    
    def log_cooking_activity(self, recipe_name, servings, rating):
        try:
            new_entry = {
                'date': datetime.now().strftime("%Y-%m-%d"),
                'recipe': recipe_name,
                'servings': servings,
                'rating': rating
            }
            
            if os.path.exists(self.history_file):
                df = pd.read_csv(self.history_file)
            else:
                df = pd.DataFrame(columns=['date', 'recipe', 'servings', 'rating'])
                
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            df.to_csv(self.history_file, index=False)
            return True
        except Exception as e:
            print(f"Error logging activity: {e}")
            return False 