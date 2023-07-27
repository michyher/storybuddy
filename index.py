import openai
import json
import random

# Load API key from JSON file
with open("config.json", "r") as file:
    config = json.load(file)

# Set your OpenAI API key
openai.api_key = config["api_key"]

# Rest of your code...



# Function to send a message and receive a response from ChatGPT
def send_message(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,  # Adjust the response length as per your needs
        temperature=0.7,  # Control the randomness of the response
    )

    generated_response = response.choices[0].text.strip()
    return generated_response

# # Example usage
# message = 'Hello, ChatGPT!'
# response = send_message(message)
# print('ChatGPT:', response)
# --------------------------------------------------------------------


# Prompt the user to choose a genre
print("Choose a genre:")
print("1. Adventure")
print("2. Fantasy")
print("3. Humor")

genre_choice = input("Enter your genre choice (1-3): ")

# Validate the genre_choice input
while genre_choice not in ["1", "2", "3"]:
    print("Invalid choice. Please enter a valid genre choice (1-3): ")
    genre_choice = input()

# Map the user's input to the actual genre name
genre_mapping = {
    "1": "Adventure",
    "2": "Fantasy",
    "3": "Humor"

}
chosen_genre = genre_mapping[genre_choice]


# Define the mad lib story templates for each genre
adventure_story_template = """Once upon a time, in a faraway land, there was a brave young explorer named {name}. One day, while {verb_ing} in the {adjective} {noun}, {name} discovered an ancient map hidden inside a {noun}.

The map showed the way to a mysterious island called "The Isle of {adjective} {noun}." Legend had it that the island was filled with {adjective} {noun} and guarded by a {adjective} {noun}.

Excited about the adventure ahead, {name} gathered their {number} most trusted companions, including a {noun}, {noun}, and {noun}. Together, they set sail on a grand {noun} named "The {adjective} {noun}."

As they sailed across the vast {noun}, the sky turned {adjective}, and a strong wind began to {verb}. But {name} and their crew faced the challenges {adverb} and never gave up.

Finally, after days of sailing, they spotted the shores of "The Isle of {adjective} {noun}." The island was covered in lush {noun}, and the air was filled with the scent of {noun}.

But to reach the hidden treasure, they had to solve three {adjective} {noun} puzzles. With wit and determination, they cracked each one and reached the heart of the island.

There, they found a magnificent {adjective} {noun} filled with sparkling {noun}. The sight was {adjective}, and they knew they had found the legendary treasure!

With hearts full of joy, they sailed back home, knowing that they would cherish this {adjective} {noun} forever. And so, the brave explorer {name} and their companions returned as heroes, having learned the power of teamwork and the joy of {verb_ing} on an incredible adventure.

The End.
"""
with open("word_options.json", "r") as file:
    word_options = json.load(file)

# Choose 4 options from each array in word_options
# Choose 4 random options from each array in word_options
chosen_word_options = {word_type: random.sample(options, 4) for word_type, options in word_options.items()}

# Define the word options for each blank in the story


# # Prompt the user to input their name
user_name = input("What is your name? ")

# Prompt the user to input their choices for each blank in the story
user_inputs = {}
for word_type, options in chosen_word_options.items():
    print(f"Choose a {word_type}:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    user_choice = input(f"Enter your {word_type} choice (1-{len(options)}): ")

    # Validate the user's input
    while user_choice not in [str(i) for i in range(1, len(options) + 1)]:
        print(f"Invalid choice. Please enter a valid {word_type} choice (1-{len(options)}): ")
        user_choice = input()

    # Map the user's input to the actual word
    user_inputs[word_type] = options[int(user_choice) - 1]

# Generate the story using the provided information
story = adventure_story_template.format(**user_inputs, name=user_name)
# response = openai.Completion.create(
#     engine='text-davinci-003',
#     prompt=prompt,
#     max_tokens=1000,  # Adjust the response length as per your needs
#     temperature=0.7  # Control the randomness of the response
# )

# story = response.choices[0].text.strip()

# Print the generated story
print("\nGenerated Story:")
print(story)
output_file = "generated_story.txt"
with open(output_file, "w") as file:
    file.write(story)

print(f"Story has been saved to {output_file}.")