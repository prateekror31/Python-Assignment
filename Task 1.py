def calculate_area(length, width):
    if length == width:
        print ("This is a square!")
    else:
        print ("the area of rect is",length*width)

l = int(input("Enter the length: "))
b = int(input("Enter the width: "))
    
calculate_area(l, b)