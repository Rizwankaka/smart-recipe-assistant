import streamlit as st
import pandas as pd
from recipe_assistant import RecipeAssistant

def init_session_state():
    if 'assistant' not in st.session_state:
        st.session_state.assistant = RecipeAssistant()
    if 'current_recipe' not in st.session_state:
        st.session_state.current_recipe = None

def render_recipe_search():
    st.header("Recipe Search")
    
    with st.form("recipe_preferences"):
        dietary_restrictions = st.text_input("Dietary Restrictions", placeholder="e.g., vegetarian, vegan, gluten-free")
        ingredients = st.text_input("Available Ingredients", placeholder="Enter ingredients, separated by commas")
        cuisine = st.text_input("Preferred Cuisine", placeholder="Any")
        cooking_time = st.text_input("Maximum Cooking Time (minutes)", placeholder="Any")
        
        submit = st.form_submit_button("Get Recipes")
        
        if submit:
            preferences = {
                'dietary_restrictions': dietary_restrictions,
                'ingredients': [i.strip() for i in ingredients.split(',')],
                'cuisine': cuisine,
                'cooking_time': cooking_time
            }
            
            suggestions = st.session_state.assistant.get_recipe_suggestions(preferences)
            st.session_state.current_recipe = suggestions
            st.markdown("### Recipe Suggestions")
            st.write(suggestions)

def render_cooking_instructions():
    st.header("Cooking Instructions")
    
    recipe_name = st.text_input("Recipe Name")
    servings = st.number_input("Number of Servings", min_value=1, value=2)
    
    if st.button("Get Instructions"):
        instructions = st.session_state.assistant.get_cooking_instructions(recipe_name, servings)
        st.markdown("### Cooking Instructions")
        st.write(instructions)
        
        # Additional features
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Get Nutritional Info"):
                nutrition = st.session_state.assistant.get_nutritional_info(recipe_name)
                st.markdown("### Nutritional Information")
                st.write(nutrition)
        
        with col2:
            if st.button("Save to Favorites"):
                recipe_data = {
                    'name': recipe_name,
                    'servings': servings,
                    'instructions': instructions,
                    'date_saved': pd.Timestamp.now().strftime("%Y-%m-%d")
                }
                if st.session_state.assistant.save_to_favorites(recipe_data):
                    st.success("Recipe saved to favorites!")
                else:
                    st.error("Error saving recipe")
        
        # Rating and logging
        rating = st.slider("Rate this recipe", 1, 5, 3)
        if st.button("Submit Rating"):
            if st.session_state.assistant.log_cooking_activity(recipe_name, servings, rating):
                st.success("Rating saved!")
            else:
                st.error("Error saving rating")

def render_favorites():
    st.header("Favorite Recipes")
    favorites = st.session_state.assistant.get_favorites()
    
    if not favorites:
        st.info("No favorite recipes saved yet!")
        return
    
    for recipe in favorites:
        with st.expander(f"{recipe['name']} ({recipe['date_saved']})"):
            st.write(f"Servings: {recipe['servings']}")
            st.write("Instructions:")
            st.write(recipe['instructions'])

def render_substitutions():
    st.header("Ingredient Substitutions")
    ingredient = st.text_input("Enter ingredient to find substitutions")
    
    if st.button("Find Substitutions"):
        substitutions = st.session_state.assistant.get_ingredient_substitutions(ingredient)
        st.write(substitutions)

def main():
    st.set_page_config(page_title="Recipe Assistant", layout="wide")
    st.title("🍳 Smart Recipe Assistant")
    
    init_session_state()
    
    tabs = ["Recipe Search", "Cooking Instructions", "Favorites", "Substitutions"]
    selected_tab = st.sidebar.radio("Navigation", tabs)
    
    if selected_tab == "Recipe Search":
        render_recipe_search()
    elif selected_tab == "Cooking Instructions":
        render_cooking_instructions()
    elif selected_tab == "Favorites":
        render_favorites()
    elif selected_tab == "Substitutions":
        render_substitutions()

if __name__ == "__main__":
    main() 