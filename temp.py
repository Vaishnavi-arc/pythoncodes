
p=input("Enter the system to you have to convert temperature Farenheit/ Degree celcius:")
   
if (p=="Farenheit"):
   a=float(input("Temperature in Degree celcius :"))
   F=(a*(9/5))+32
   print("Temperature in Farenheit:",F)
else :
   a=float(input("Temperature in  Farenheit:"))
   F=(a-32)*(5/9)
   print("Temperature in Degree celcius:",F)



