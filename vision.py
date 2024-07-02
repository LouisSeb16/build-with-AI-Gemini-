import os
import google.generativeai as genai
import PIL.Image

with open("api_key.txt", "r") as f:
  api_key = f.read().strip()

os.environ['GOOGLE_API_KEY'] = api_key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

vision_model = genai.GenerativeModel('gemini-pro-vision')

image = PIL.Image.open('download.jpeg')

response = vision_model.generate_content(["Explain this image", image])
print(response.text)