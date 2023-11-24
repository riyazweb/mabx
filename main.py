import keyboard
import requests
import json
import openai
from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap
import random
import os
import time

openai.api_key = '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'


def cat():
    with open("news.txt", "r") as file:
        news = file.read().strip()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"write a motivation line ON MONEY from great person except this: {news} just write a motivation line from great person"}
        ]
    )
    OP = response['choices'][0]['message']['content']
    OP = OP.replace('"', '')
    with open("news.txt", "r") as file:
        if OP in file.read():
            print("This line has already been added to the file.")
        else:
            with open("news.txt", "a") as file:
                file.write(OP + "\n")
                print("Added the following line to the file: " + OP)

            from io import BytesIO

# Make a request to the Unsplash API to get a random photo
            response = requests.get(
                'https://source.unsplash.com/random/600x600?rich')

            # Create an Image object with the downloaded image
            img = Image.open(BytesIO(response.content))

            # Resize the image to 600x600
            img = img.resize((600, 600))

            # Display the image

            # Create an Image object with the randomly chosen background color

            # Create a Draw object for drawing on the image
            draw = ImageDraw.Draw(img)
# Create a black layer with transparency of 30%
            alpha = 77  # 30% transparency
            black_layer = Image.new(
                'RGBA', (img.width, img.height), (0, 0, 0, alpha))
            # Choose a font and size for the text
            # reduced font size to 24
            font = ImageFont.truetype('Muroslant.otf', size=23)

            # Define the text to draw
            text = f"{OP}"

            # Wrap the text to fit within the image width
            wrapped_text = textwrap.wrap(text, width=50)

            # Calculate the position of the text in the center of the image
            x = (img.width - draw.textbbox((0, 0),
                 wrapped_text[0], font=font)[2]) // 2
            y = (img.height -
                 font.getsize(wrapped_text[0])[1] * len(wrapped_text)) // 2

            # Draw each line of wrapped text on the image
            for line in wrapped_text:
                draw.text((x, y), line, fill='white',
                          font=font, outline='black')
                # draw.text((x, y), line, fill='black', font=font, stroke_width=1, stroke_fill='white', align='center')
                y += draw.textsize(line, font=font)[1]

            # Get the news item's title
            title = "News Title"

            # Create a folder to store the images if it doesn't exist
            if not os.path.exists(title):
                os.makedirs(title)

            # Save the image with a unique filename
            i = 1
            while True:
                img_filename = f"{title}/image{i}.png"
                if not os.path.exists(img_filename):
                    break
                i += 1
            img.save(img_filename)
            print(f"Saved image as {img_filename}")


for i in range(20):
    print(f"Running cat() for the {i+1}th time")
    cat()
    time.sleep(1)
