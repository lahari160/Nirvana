import google.generativeai as genai

API_KEY = 'AIzaSyAlkfgfRyRgHVfMXN4o-xNN7OwE49_bblw'

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while(True):
    question = input("How may I assist you?:")

    if(question.strip() == ''):
        break

    response = chat.send_message(question)
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')

    