#tamrin dovom
#dar in amrin bayad az karbar ta zamani ke addad manfi vared nakarde addad begire
#miangin in addad ro hesab kone
#majmo in addad ham bayad chap kone
Numbers_List = list()
Total = 0
while 1 == 1:
    Number = int(input("enter number \n"))
    if Number > 0:
        Numbers_List.append(Number)
    elif Number < 0:
        for i in range(0, len(Numbers_List)):
            Total += Numbers_List[i]
        print('Our list is  {}'.format(Numbers_List))
        print('The sum of our list is {}'.format(Total))
        Average = Total/len(Numbers_List)
        print("The Average of our list is {}".format(Average))
        break
