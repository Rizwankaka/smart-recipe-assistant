# 🌟 CulinaryGenius AI: Your Smart Kitchen Companion 🍳

> Transform your cooking experience with AI-powered recipe magic!

A modern, AI-powered recipe assistant that helps you discover, cook, and manage your favorite recipes with ease! Built with Streamlit and Google's Gemini AI.

## ✨ Features

- 🔍 **Smart Recipe Search**
  - Search recipes based on dietary restrictions
  - Filter by available ingredients
  - Specify cuisine preferences
  - Set maximum cooking time

- 👩‍🍳 **Detailed Cooking Instructions**
  - Step-by-step cooking guides
  - Serving size adjustments
  - Preparation and cooking time estimates
  - Pro cooking tips

- 📊 **Nutritional Information**
  - Calories per serving
  - Detailed macronutrients breakdown
  - Key vitamins and minerals
  - Dietary considerations

- 🔄 **Ingredient Substitutions**
  - Smart alternative suggestions
  - Conversion ratios
  - Impact on taste and texture
  - Nutritional differences

- ⭐ **Recipe Management**
  - Save favorite recipes
  - Rate and review recipes
  - Track cooking history
  - Personal recipe notes

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Gemini API key (Get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/smart-recipe-assistant.git
cd smart-recipe-assistant
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Set up environment variables
   - Create a `.env` file in the project root
   - Add your Gemini API key:
```env
GEMINI_API_KEY=your_api_key_here
```

### 🎮 Running the App

1. Start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## 📱 Usage Guide

1. **Recipe Search**
   - Navigate to "Recipe Search" tab
   - Enter your dietary restrictions
   - List available ingredients
   - Specify cuisine preference
   - Set maximum cooking time
   - Click "Get Recipes" for personalized suggestions

2. **Cooking Instructions**
   - Go to "Cooking Instructions" tab
   - Enter recipe name
   - Adjust serving size
   - Get detailed step-by-step instructions
   - View nutritional information
   - Save to favorites if desired

3. **Managing Favorites**
   - Access "Favorites" tab to view saved recipes
   - Expand recipes to view full details
   - Rate recipes after cooking
   - Track your cooking history

4. **Finding Substitutions**
   - Visit "Substitutions" tab
   - Enter ingredient name
   - Get healthy alternative options
   - View conversion ratios and impacts

## 📁 Project Structure

```
smart-recipe-assistant/
├── requirements.txt
├── .env
├── recipe_assistant.py
├── streamlit_app.py
├── favorites.json
└── cooking_history.csv
```

## 💾 Data Storage

- Favorite recipes are stored in `favorites.json`
- Cooking history is maintained in `cooking_history.csv`
- All data is stored locally on your machine

## 🛠️ Technologies Used

- **Streamlit**: For the web interface
- **Google Gemini AI**: For recipe suggestions and instructions
- **Python**: Core programming language
- **Pandas**: Data handling and storage

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for powering recipe suggestions
- Streamlit for the amazing web framework
- All contributors and users of this application

## 📧 Contact

For any queries or suggestions, please open an issue in the GitHub repository.

---
Made with ❤️ by Rizwan
```

This README.md provides:
- Clear feature overview with emojis
- Detailed installation instructions
- Usage guidelines
- Project structure
- Technical details
- Contributing guidelines

