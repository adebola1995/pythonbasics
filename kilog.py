weight= float(input("enter your weight in kg:"))
height= float(input("enter your height in m:"))
BMI_CAT= weight/height
if BMI_CAT>=40:
    print("Obese class III")
elif BMI_CAT>=35.0 and BMI_CAT<=39.9:
    print("Obese class II")
elif BMI_CAT>=30.0 and BMI_CAT<=34.9:
    print("Obese class I")
elif BMI_CAT>=25.0 and BMI_CAT<=29.9:
    print("overweight")
elif BMI_CAT>=18.5 and BMI_CAT<=24.9:
    print("normal weight")
else:
    if BMI_CAT<18.5:
        print("underweight")
