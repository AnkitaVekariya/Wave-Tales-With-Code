import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re

def read_story_templates(file_path):
    with open(file_path, 'r') as file:
        templates = file.readlines()
    return [template.strip() for template in templates]

def preprocess_text(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words]
    words = [word for word in words if word.isalpha()]
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    return words

def generate_story_elements(text):
    words = preprocess_text(text)
    freq_dist = FreqDist(words)
    main_character = freq_dist.most_common(1)[0][0]
    return main_character

def generate_fictional_story(template, main_character, setting, goal, obstacle, action, friend, artifact, place, animal):
    story = template.format(
        name=main_character.capitalize(),
        character="princess", 
        setting=setting.capitalize(),
        goal=goal,
        obstacle=obstacle,
        action=action,
        friend=friend,
        artifact=artifact,
        place=place,
        animal=animal
    )
    return story

def generate_story_with_preferences(template):
    print("Welcome to the Kids' Fictional Story Generator!")
    print("Please provide some text to inspire your story.")
    user_text = input("Enter some text: ")
    main_character = generate_story_elements(user_text)
    setting = random.choice(user_text)
    goal = random.choice(["rescue a friend", "find a hidden treasure", "save the kingdom", "solve a magical mystery"])
    obstacle = random.choice(["a fierce dragon", "an evil sorcerer", "a dark curse", "a treacherous maze"])
    action = random.choice(["brave the dangers", "use magic spells", "solve riddles", "make new friends"])
    friend = random.choice(["wizard", "fairy", "elf", "dragon"])
    artifact = random.choice(["crystal", "amulet", "wand", "book"])
    place = random.choice(["cave", "ruins", "castle", "forest"])
    animal = random.choice(["dragon", "unicorn", "griffin", "phoenix"])
    story = generate_fictional_story(template, main_character, setting, goal, obstacle, action, friend, artifact, place, animal)
    print("\nHere's your fictional story:")
    print(story)
    return story

def main():
    story_templates = read_story_templates('story_templates.txt')
    selected_template = random.choice(story_templates)
    generated_story = generate_story_with_preferences(selected_template)

    # Write the generated story to a file
    with open('generated_story.txt', 'w') as file:
        file.write(generated_story)

if __name__ == "__main__":
    main()
