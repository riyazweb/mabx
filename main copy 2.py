import keyboard
import requests
import json
import openai
from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap
import random
import os
import time
from bing_image_downloader import downloader

openai.api_key = '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'


top = input("enter:")
num = int(input("num:"))
# Replace spaces in title with hyphens
dog = top.replace(" ", "-")

# Download images of dogs
downloader.download(f"{dog}", limit=num, output_dir="images",
                    adult_filter_off=True, force_replace=False)

for i in range(1, num+1):
    with open("news.txt", "r") as file:
        news = file.read().strip()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"write a motivation line ON  {top.upper()} except this: {news} just write a motivation line from great person"}
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

    # Make a request to the Unsplash API to get a random photo

                image_dir = f"images/{dog}/image_{i}.jpg"

                # Create an Image object with the local image file
                img = Image.open(image_dir)

                # Resize the image to 600x600
                img = img.resize((600, 600))
 # Load the overlay image
                overlay = Image.open('tranf.png')
                overlay = overlay.convert("RGBA")

                # Paste the overlay image onto the main image
                img.paste(overlay, (0, 0), overlay)
                # Display the image

                # Create an Image object with the randomly chosen background color

                # Create a Draw object for drawing on the image
                draw = ImageDraw.Draw(img)
            # Create a black layer with transparency of 30%
                
                # reduced font size to 24
                font = ImageFont.truetype('Turpis-GOgVm.ttf', size=23)

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
                title = f"{top}"

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
