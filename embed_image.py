
import os

with open('index.html', 'r') as f:
    html_content = f.read()

with open('image_base64.txt', 'r') as f:
    base64_content = f.read().strip()

new_src = f'src="data:image/jpeg;base64,{base64_content}"'
new_html = html_content.replace('src="320x480-100.jpg"', new_src)

with open('index.html', 'w') as f:
    f.write(new_html)

print("Updated index.html with base64 image.")
