name= input('ENTER YOUR NAME: ')
height=float(input('ENTER YOUR HEIGHT IN CM: '))
weight=float(input('ENTER YOUR WIGHT IN KG: '))

bmi= weight/ (height/100)**2

if(bmi<=18.5):
    print("\n",name,',You are underweight')
elif(18.5<bmi<=24.9):
    print("\n",name,',Awesome! You are healthy')
elif(24.9<bmi<=29.9):
    print("\n",name,',You are overweight')
else:
    print("\n",name,',You are obese')