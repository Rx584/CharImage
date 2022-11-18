from PIL import Image
origin = input("原图片路径")
output_name = input("输出文件名称")
img = Image.open(origin).convert("L").resize((200,200))
width = img.width
height = img.height
ASCII_HIGH = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
output = ""
for y in range(width):
    for x in range(height):
        pos=(x,y)
        gray=img.getpixel(pos)
        index=int(gray/256*70)
        output += ASCII_HIGH[index]+" "
    output += "\n"
with open(output_name,mode = "w",encoding="utf-8")as f:
    f.write(output)