#dar in tamrin do addad ro be onvan vorodi migirim va check mikonim
#bebinim ke addad aval bar addad dovom bakhshpazir hast ya na
##man mesl tamrin ghabl in tamrin ham ba 2 ravash raftam .

#first method:

number1 = int(input("please enter your first number \n"))
number2 = int(input("please enter your second number \n"))
number3 = number1 % number2
if number3 == 0 :
    print("your first number is divisible by second number ")
else:
    print("your first number is not divisible by second number")
#second method:
number1 = int(input("please enter your first number \n"))
number2 = int(input("please enter your second number \n"))
if number1 % number2 == 0 :
    print('your first number is divisible by second number')
else:
    print("your first number is not divisible by second number")
