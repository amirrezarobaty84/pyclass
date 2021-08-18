#ostad in tamrin braye hesab kardan masahat mostatil ast ba vahed pishfarz metr

def area(length, Width, unit="m"):
    if unit == "mm":
        operation1 = (length * Width) / 1000
        print("rectangle's area is {} meter".format(operation1))
    elif unit == "cm":
        operation2 = (length * Width) / 100
        print("rectangle's area is {} meter".format(operation2))
    elif unit == "m":
        operation3 = length * Width
        print("rectangle's area is {} meter".format(operation3))
    else:
        print("i dont know what is it")

area(2, 20, "km")
