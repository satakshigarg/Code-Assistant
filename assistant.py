import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def code_assist(code_snippet):
    prompt = f"Assist with the following code:\n```python\n{code_snippet}\n```"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None
    )

    return response['choices'][0]['text'].strip()

def main():
    print("Welcome to the Text-based Code Assistant!")
    
    while True:
        code_input = input("Enter your Python code (or 'exit' to quit):\n")
        
        if code_input.lower() == 'exit':
            break
        
        assistance = code_assist(code_input)
        print("Assistant's suggestion:")
        print(assistance)

if __name__ == "__main__":
    main()
