#BMI Calculator
weight=int(input("enter the weight:"))
height=int(input("enter the height:"))
BMI=weight/height**2
print(BMI)
if BMI<18.5:
    print("Under weight")
elif(18.5<BMI<25):
    print("normal")
elif(25<BMI<30):
    print("over weight")
else:
    print("Obese")
