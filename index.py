import openai
import json


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


# Prompt the user to input their name
name = input("Input name: ")

# Prompt the user to choose a genre
print("Choose a genre:")
print("1. Fantasy")
print("2. Adventure")
print("3. Mystery")
print("4. Sci-fi")

genre_choice = input("Enter your genre choice (1-4): ")

# Prompt the user to choose a location
print("Choose a location:")
print("1. City")
print("2. Forest")
print("3. Beach")
print("4. Space")

location_choice = input("Enter your location choice (1-4): ")


# Generate a story using the provided information
prompt = f"In a {location_choice}, there was a {genre_choice} story about a character named {name}..."
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=100,  # Adjust the response length as per your needs
    temperature=0.7  # Control the randomness of the response
)

story = response.choices[0].text.strip()

# Print the generated story
print("Generated Story:")
print(story)