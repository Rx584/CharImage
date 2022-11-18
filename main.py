from PIL import Image
import os
origin = input("原图片路径\n")
output_name = input("输出文件名称\n")
width = int(input("宽度\n"))
height = int(input("高度\n"))
img = Image.open(origin).convert("L").resize((width,height))
ASCII_HIGH = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
output = ""
for y in range(width):
    for x in range(height):
        pos=(x,y)
        gray=img.getpixel(pos)
        index=int(gray/256*70)
        output += ASCII_HIGH[index]+" "
    output += "\n"
os.system("cls")
print(output)
with open(output_name,mode = "w",encoding="utf-8")as f:
    f.write(output)
