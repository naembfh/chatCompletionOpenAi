import openai
import json
from apiKey import openAiApiKey

openai.api_key = openAiApiKey

def chat_with_gpt():
    print("Welcome to Chat Completion with OpenAi! Type 'exit' to end chat \n")
    while True:
        userInput = input("You: ")
        if userInput.lower() == "exit":
            print("Bye! Thanks for using Chat Completion with OpenAi")
            break
        # response = openai.Completion.create(
        #     engine="davinci",
        #     prompt=f"You: {userInput}\n",
        #     max_tokens=500
        # )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": userInput}
            ]
        )

       
        print("AI: " + response['choices'][0]['message']['content'])

        userChoice = input("Do you want to continue? type 'yes' to continue, any key else to exit:\n")
        if userChoice.lower() != "yes":
            print("Bye! Thanks for using chat completion with OpenAi")
            break

if __name__ == "__main__":
    chat_with_gpt()
