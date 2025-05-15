import google.generativeai as genai
import os 
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("AIzaSyA9rLGjcPW3oPF_2Cwlljva-sVS2fBhx8Q")
genai.configure(api_key=api)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

isExit = False

while isExit != True :
    text=input("GDG ON CAMPUS :")
    if text == "exit":
        isExit = True
        print("Çıkış yapıldı!")
        break
    else: 
        response = model.generate_content(text)
        print(response.text)
    
