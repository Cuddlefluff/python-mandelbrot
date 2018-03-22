from PIL import Image, ImageColor
maxIterations = 60
width = 400
height = 400
destinationImage = Image.new("RGBA", (width, height))
donepercent = 0
for px in range(0, width):
    for py in range(0, height):

        x0 = (((px / width ) * 2.5) - 1.5)
        y0 = (((py / height) * 2.0) - 1.0)
        x = 0.0
        y = 0.0
        iteration = 0

        while x*x + y*y < 4 and iteration < maxIterations:
            xtemp = x * x - y * y + x0
            y = 2 * x * y + y0
            x = xtemp
            iteration = iteration + 1
        
        if iteration > 0:
            color = int((iteration / maxIterations) * 255)
            color = 0 | int(color / 2) << 8 | color << 16 | color << 24
            destinationImage.putpixel((px, py), int(color))

    newdonepercent = int((px / width) * 100)
    if(newdonepercent != donepercent):
        print ("{}% ferdig".format(newdonepercent))
        donepercent = newdonepercent

destinationImage.save("output.png")