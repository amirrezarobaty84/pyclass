#tamrin aval
#ma dar in tamrin bayad do ta addad be onvan vorodi begirim 
#va az addad bozorge be kochike print konim

Number1 = int(input("enter your number : "))
Number2 = int(input("enter your second number : "))

if Number1 < Number2:
    Elder = Number2
    Lesser = Number1
elif Number2 < Number1 :
    Elder = Number1
    Lesser = Number2

while Lesser <= Elder:
    print(Elder)
    Elder -= 1
