
# Wave Tales with Code

**Wave Tales with Code** is an interactive Python-based story generator that crafts personalized fictional stories for children based on their input text. Using natural language processing, the program detects key words to shape the theme, characters, and magical elements in the story.

---

## Features

- NLP-powered story element extraction (main character, themes)
- Fantasy-themed, kid-friendly story templates
- Randomized magical settings, artifacts, and creatures
- Text-based interaction and storytelling
- Outputs story to a readable `.txt` file

---

## Tech Stack

- **Python**
- **NLTK (Natural Language Toolkit)**
- `random`, `re`, and standard Python libraries
  
---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/AnkitaVekariya/Wave-Tales-With-Code.git
cd Wave-Tales-With-Code
````

### 2. Install dependencies

```bash
pip install nltk
```

### 3. Download NLTK data

Run the following in Python shell or include in a script:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## How to Run

In your terminal:

```bash
python story.py
```

Follow the prompts to enter a short inspirational text and enjoy your customized fairy tale!

---

## Sample Output

```
Enter some text: Maya was a fearless girl who loved adventures in the forest.

Here's your fictional story:
Once upon a time in a distant Forest, Maya the brave princess set out to rescue a friend...
```
