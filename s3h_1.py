#ostad in tamrin bmi hastash ke be do ravesh anjam dadam
#yeki az karbar addad mighire
#yeki shoma behesh addad midin

#first_method
def BMI():
    weight = float(input("please enter your weight \n"))
    stature = float(input("please enter your stature \n"))
    operation =  weight / stature  ** 2
    print(operation)

BMI()

#second_method
def BMI(weight, stature):
    operation = weight / stature  ** 2
    print(operation)

BMI(123, 123)
