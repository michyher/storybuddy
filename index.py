import openai

# Set your OpenAI API key
openai.api_key = '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'

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

# Example usage
message = 'Hello, ChatGPT!'
response = send_message(message)
print('ChatGPT:', response)
