import nltk
import random
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you.', 'I\'m doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot.', 'You can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'Have a great day!', 'See you later.']),
    # Add more patterns and responses based on the conversations you want the bot to handle
]

# Create a chatbot using the patterns
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I'm a simple chatbot. Ask me something or say goodbye to end the conversation.")

# Keep the conversation going until the user says goodbye
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Bot:", response)
