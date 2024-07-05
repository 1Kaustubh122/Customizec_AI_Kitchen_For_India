# from flask import Flask, render_template, request
# import openai
# from openai.error import RateLimitError

# app = Flask(__name__)

# api_key = 'sk-proj-WXZXazvotDjg71dzNG8YT3BlbkFJw9qf3u7dTAszfG6Jq2Rb'


# openai.api_key = api_key

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chatbot', methods=['GET', 'POST'])
# def chatbot():
#     error_message = None
#     if request.method == 'POST':
#         user_input = request.form['user_input']
        
#         try:
#             response = generate_response(user_input)
#             print(response)
#         except RateLimitError:
#             error_message = "Rate limit exceeded. Please try again later."
#             response = None

#         return render_template('chatbot.html', user_input=user_input, response=response, error_message=error_message)
    
#     return render_template('chatbot.html')

# def generate_response(input_text):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5",  # Adjust model based on your needs
#             messages=[
#                 {"role": "user", "content": input_text}
#             ],
#             max_tokens=150
#         )
#         return response['choices'][0]['message']['content'].strip()
#     except RateLimitError:
#         raise RateLimitError("Rate limit exceeded. Please try again later.")

# if __name__ == '__main__':
#     app.run(port=2000, debug=True)








# from flask import Flask, render_template, request
# import requests

# app = Flask(__name__)

# import google.generativeai as genai

# API_KEY = 'AIzaSyCQmJPyQiNRa6wJQaodTkxt4eB_k9zxF34'
# genai.configure(
# api_key=API_KEY
# )
# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat (history=[])

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chatbot', methods=['GET', 'POST'])
# def chatbot():
#     error_message = None
#     response = None
#     if request.method == 'POST':
#         user_input = request.form['user_input']
        
#         response = chat.send_message(user_input)
        
#         return render_template('chatbot.html', user_input=user_input, response=response.text, error_message=error_message)
    
#     return render_template('chatbot.html')


# if __name__ == '__main__':
#     app.run(port=2000, debug=True)
















from flask import Flask, render_template, request, redirect, url_for
import os
import google.generativeai as genai
from ml import photo_pred


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

API_KEY = 'AIzaSyCQmJPyQiNRa6wJQaodTkxt4eB_k9zxF34'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/chatbot', methods=['GET', 'POST'])
# def chatbot():
#     error_message = None
#     response = "Hello"
#     food = ""
#     if request.method == 'POST':

#         if 'file' in request.files and request.files['file'].filename != '':
#             file = request.files['file']
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(filepath)
#             x = photo_pred(filepath)  # Pass the file path to your photo_pred function
#             response = f"File {file.filename} uploaded successfully. {x} detected"
#             print(f"\nresponse = {response}\n")
    #         response = chat.send_message(f"{x} recipe").text
    #     elif 'user_input' in request.form and request.form['user_input'].strip() != '':
    #         user_input = request.form['user_input']
    #         response = chat.send_message(user_input).text
    #     else:
    #         error_message = "No file selected or user input provided."
 
    # return render_template('chatbot.html', response=response, error_message=error_message, food=food)

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    response = ""
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        user_file = request.files.get('file')

        if user_input:
            user_input = request.form['user_input']
            response = chat.send_message(user_input).text

        elif user_file:
            file = request.files['file']
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            x = photo_pred()  
            response = chat.send_message(f"{x} recipe").text
        else:
            response = "No input received"
    return render_template('chatbot.html', response=response)

if __name__ == '__main__':
    app.run(port=2000, debug=True)
