# import ollma 
import ollama

while True:
    user = input('You: ')
    if user.lower() == 'bye':
        
        print('Goodbye!')
        break

    response = ollama.chat(model='llama3.1', messages=[
        {'role': 'user', 'content': user}
    ])
    print('Chatbot:', response['message']['content'])
