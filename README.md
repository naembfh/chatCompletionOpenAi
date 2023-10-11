# Chat Completion with OpenAI GPT-3 

This repository contains a Python script that uses the OpenAI API to perform chat completions using the GPT-3 model. Before running the script, please follow the instructions below to set up your environment and provide your API key.

## Prerequisites

- Python 3.0 or later installed
- Git installed
- An OpenAI API key (sign up at [OpenAI](https://beta.openai.com/signup/) if you don't have one)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/naembfh/chatCompletionOpenAi.git
2. Create a virtual environment (you can use a different name if you prefer):

    ```bash
    python -m venv venv
3. Activate the virtual environment (on Windows, use the following command; on other systems, adjust accordingly):

    ```bash
    venv\Scripts\activate
4. While the virtual environment is activated, install the `openai` package using `pip`:

    ```bash
    pip install openai
    ```

## Configure Your API Key

5. Create a Python script named `apiKey.py` in the project directory to securely store your OpenAI API key. The content should look like this:

    ```python
    # apiKey.py

    openAiApiKey = "your-api-key-goes-here"
    ```

    Replace `"your-api-key-goes-here"` with your actual OpenAI API key.

## Run the Chat Completion Script

6. Run the Python script to perform chat completions using OpenAI:

    ```bash
    python chat_with_openai.py
    ```

The script will use your API key from `apiKey.py` to interact with the OpenAI GPT-3 model and generate chat completions.

**Note**: Be sure to keep your API key confidential and do not share it publicly.

If you have any questions or run into issues, please refer to the [OpenAI API documentation](https://beta.openai.com/docs/) or the [OpenAI support](https://beta.openai.com/support/) for assistance.

Enjoy using chat completion with OpenAI GPT-3!
