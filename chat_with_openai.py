import openai
import json
import time
from apiKey import openAiApiKey

openai.api_key = openAiApiKey

# for smoothly show
# def typeSmoothly(text, delay=0.03):
#     for char in text:
#         print(char, end="", flush=True)
#         time.sleep(delay)

def chat_with_gpt():
    print("Welcome to Chat Completion with OpenAi! Type 'exit' to end chat \n")
    while True:
        userInput = input("You: ")
        if userInput.lower() == "exit":
            print("Bye! Thanks for using Chat Completion with OpenAi")
            break
        
        conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": userInput}
        ]
        
        startTime = time.time()
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = conversation
        )
        
        endTime = time.time()
        responseTime = abs(startTime - endTime)
        responseContent = response['choices'][0]['message']['content']
        
        print("AI is typing...\n", end="", flush=True)
        print("\nAI: " + responseContent)
        # typeSmoothly(responseContent)
        print("\nResponse time: {:.2f} seconds".format(responseTime))
        
        userChoice = input("Do you want to continue? type 'yes' to continue, any key else to exit:\n")
        if userChoice.lower() != "yes":
            print("Bye! Thanks for using chat completion with OpenAi")
            break

if __name__ == "__main__":
    chat_with_gpt()
