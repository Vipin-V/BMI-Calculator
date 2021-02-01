
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2

bmi_as_int = int(round(bmi))

if bmi_as_int < 18.5:
    print(f"Your BMI is {bmi_as_int}, you are underweight")
elif bmi_as_int < 23:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight")
elif bmi_as_int < 29:
    print(f"Your BMI is {bmi_as_int}, you are slightly overweight")
elif bmi_as_int < 34:
    print(f"Your BMI is {bmi_as_int}, you are obese")
else:
    print(f"Your BMI is {bmi_as_int}, you are clinically obese")