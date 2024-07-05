# apikey = 'AIzaSyCQmJPyQiNRa6wJQaodTkxt4eB_k9zxF34'




import google.generativeai as genai

API_KEY = 'AIzaSyCQmJPyQiNRa6wJQaodTkxt4eB_k9zxF34'

genai.configure(
api_key=API_KEY
)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat (history=[])
while(True):
    question = input("You: ")
    if (question.strip() == ''):
        break
    response = chat.send_message(question)
    print('\n')
    print (f" Bot: {response.text}")
    print('\n')