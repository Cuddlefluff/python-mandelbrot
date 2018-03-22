from PIL import Image, ImageColor

width = 1920
height = 1080
destinationImage = Image.new("RGB", (width, height))

for px in range(0, width):
    for py in range(0, height):

        x0 = (((px / width ) * 3.5) - 2.5)
        y0 = (((py / height) * 2.0) - 1.0)
        x = 0.0
        y = 0.0
        iteration = 0

        while x*x + y*y < 4 and iteration < 1024:
            xtemp = x * x - y * y + x0
            y = 2 * x * y + y0
            x = xtemp
            iteration = iteration + 1
        
        if iteration > 0:
            color = ((iteration / 1024) * 255)
            destinationImage.putpixel((px, py), int(color))

destinationImage.save("output.png")