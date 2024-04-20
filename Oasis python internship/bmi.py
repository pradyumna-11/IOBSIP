try :
    weight = float(input("Enter weight in kg : "))
    height = float(input("Enter height in meters : "))
    bmi = weight/height**2
    if(bmi<18.5):
        print("Underweight")
    elif(bmi>=18.5 and bmi<25):
        print("Normal weight")
    elif(bmi>=25 and bmi<30):
        print("Overweight")
    elif(bmi>=30):
        print("Obesity")
    else:
        print("Please enter valid input")
except ValueError:
    print("Please enter valid input")