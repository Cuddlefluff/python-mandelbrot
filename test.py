
for px in range(0, 10):
    for py in range(0, 10):

        x0 = ((px / 10.0) * 3.5) - 2.5
        y0 = ((py / 10.0) * 2.0) - 1.0
        x = 0.0
        y = 0.0
        iteration = 0

        while x*x + y*y < 4 and iteration < 1000:
            xtemp = x * x - y * y + x0
            y = 2 * x * y + y0
            x = xtemp
            iteration = iteration + 1
        
        if iteration > 0:
            color = iteration
            print(color)