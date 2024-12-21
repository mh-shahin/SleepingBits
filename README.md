Challenge 1:
Here’s a sample README text you can use for your GitHub project. You can adjust the content according to your project details:

---

# Bengali Transliteration Model

This repository contains a Bengali transliteration model that converts **Banglish** (Romanized Bengali) to **Bengali** text. The model is built using the Hugging Face Transformers library and fine-tuned on a custom dataset of Bengali transliterations.

## Project Overview

The goal of this project is to create a model that can convert text written in the Roman alphabet (Banglish) back to the Bengali script. This can be useful for a wide variety of applications, including improving text input for Bengali language users and building tools that aid in language localization.

## Dataset

The model is fine-tuned on the **SKNahin/bengali-transliteration-data** dataset, which contains pairs of Banglish and Bengali text. The dataset is split into training and validation sets.

### Dataset Structure:
- `bn`: Bengali text
- `rm`: Romanized Bengali (Banglish) text

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/bengali-transliteration.git
cd bengali-transliteration
pip install -r requirements.txt
```

## Usage

To train the model, run the following Python script:

```bash
python train.py
```

This will train the model using the provided dataset and save the trained model to the `./results` directory.

## Evaluation

The model's performance is evaluated using the **SacreBLEU** metric, which is used to measure the quality of machine-generated translations by comparing them to reference translations.

```python
import evaluate
metric = evaluate.load("sacrebleu")
```

## Training Arguments

The model training can be configured via the `training_args` parameter in the `train.py` script. For example:

- `output_dir`: Directory to save model checkpoints
- `evaluation_strategy`: Strategy for evaluating the model during training
- `per_device_train_batch_size`: Batch size for training
- `num_train_epochs`: Number of training epochs

## Model Architecture

The model uses the **mBART** architecture (`facebook/mbart-large-50`) from Hugging Face, which is suitable for multilingual tasks. The model is fine-tuned specifically for the Bengali transliteration task.

Challenge 2:
# Mofa's Kitchen Buddy

Mofa's Kitchen Buddy is a backend system that helps manage ingredients and suggests recipes based on available ingredients at home. It also integrates a chatbot to recommend recipes based on preferences like craving something sweet or specific dishes. This project consists of APIs for ingredient management, recipe retrieval, and chatbot integration.

---

## Table of Contents
- [Database Design](#database-design)
- [Ingredient Management API](#ingredient-management-api)
- [Recipe Retrieval](#recipe-retrieval)
- [Chatbot Integration](#chatbot-integration)
- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [Folder Structure](#folder-structure)
- [Additional Considerations](#additional-considerations)

---

## Database Design
A SQLite database schema is used to store the following:

- **Ingredients Table**
  - `id` (Integer, Primary Key): Unique ID for each ingredient.
  - `name` (String): Name of the ingredient.
  - `quantity` (Float): Quantity available.
  - `unit` (String): Unit of the ingredient (e.g., pcs, kg).

---

## Ingredient Management API
The backend provides APIs to input, retrieve, and update available ingredients after shopping or cooking.

---

## Recipe Retrieval
- Parses and stores recipe details from saved recipe texts/images into a combined `my_fav_recipes.txt` file.
- Provides APIs to input new favorite recipes.

---

## Chatbot Integration
A Large Language Model (LLM)-powered chatbot is integrated to:
- Understand user preferences (e.g., "I want something sweet today").
- Suggest recipes by processing `my_fav_recipes.txt` and checking available ingredients.

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd Challenge2
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the app:**
   - Use the public URL provided by **ngrok** to access the APIs.

---

## API Documentation

### 1. Add Ingredient
**Route:** `/ingredients`  
**Method:** `POST`  
**Payload:**
```json
{
  "name": "Tomato",
  "quantity": 5,
  "unit": "pcs"
}
```
**Response:**
```json
{
  "message": "Ingredient added successfully"
}
```

---

### 2. Get All Ingredients
**Route:** `/ingredients`  
**Method:** `GET`  
**Response:**
```json
[
  {
    "id": 1,
    "name": "Tomato",
    "quantity": 5,
    "unit": "pcs"
  },
  {
    "id": 2,
    "name": "Onion",
    "quantity": 2,
    "unit": "kg"
  }
]
```

---

### 3. Update Ingredient
**Route:** `/ingredients/<id>`  
**Method:** `PUT`  
**Payload:**
```json
{
  "quantity": 10,
  "unit": "pcs"
}
```
**Response:**
```json
{
  "message": "Ingredient updated successfully"
}
```

---

### 4. Add Recipe Text
**Route:** `/recipes/text`  
**Method:** `POST`  
**Payload:**
```json
{
  "recipe_text": "Recipe: Tomato Soup\nIngredients: Tomato, Onion, Garlic, Salt, Pepper\nTaste: Savory\nReviews: 4.5/5\nCuisine: Italian\nPreparation Time: 30 minutes"
}
```
**Response:**
```json
{
  "message": "Recipe added successfully"
}
```

---

## Folder Structure
```
Challenge2/
|-- app.py            # Main Flask application
|-- requirements.txt  # Dependencies
|-- my_fav_recipes.txt # Combined recipe text file
|-- database/         # SQLite database file
```

---

## Additional Considerations

1. **Elegant API Design:**
   - APIs are simple and intuitive for easy integration.

2. **Handle Large Recipe Files:**
   - Efficient parsing and storage of large `my_fav_recipes.txt` files.

3. **Chatbot Details:**
   - Uses an LLM to process user preferences and recommend recipes based on available ingredients.

4. **Optional Enhancements:**
   - Add OCR functionality to extract text from recipe images.

---

## Hosted Model
- Public URL: `<ngrok_public_url>`

---

### Contributors
Rakesh Biswas
MD Shahin Hossain


