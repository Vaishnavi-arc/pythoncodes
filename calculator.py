print("Calculator")
choose=input("CHOOSE THE OPERATION: 1.Addition  2.Sustraction  3.Multiplication 4.Division 5.Remainder   (choose 1-5 integer)")
value1=float(input("Enter first value : "))
value2=float(input("Enter second value : "))
if choose == '1' :
    res=value1 + value2
    print("Addition is  ",res)
elif choose == '2' :
    res=value1 - value2
    print("substraction is  ",res)     
elif choose == '3' :
    res=value1 * value2
    print("multiplication is  ",res)    
elif choose == '4' :
    res=value1 / value2
    print("Division is  ",res)
else :
    res=value1 % value2
    print("Remainder is  ",res) 
    
