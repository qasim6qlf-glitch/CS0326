import os 
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()

api_key = os.environ ["GEMINI_API_KEY"]
client = genai.Client (api_key="GEMINI_API_KEY")

safety_settings = [    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
                       types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),    
                       types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),    
                       types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
]



while True:    
    domanda = input("Tu: ")    
    if domanda.lower() == "esci":        
        print("Arrivederci!")        
        break     
    response = client.models.generate_content(        
        model="gemini-2.5-flash",        
        contents=domanda,        
        config=types.GenerateContentConfig(safety_settings=safety_settings)
    )    
    print(f"AI: {response.text}\n")
