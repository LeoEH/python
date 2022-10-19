Bodweight = float(input("what is yr weight in kg: "))
hight = float(input("what is yr hight in meters: "))


BMI = Bodweight / hight**2

print(int(BMI))


if BMI < 17.5:
  print( "u r underweight")
elif BMI > 17.5 and BMI < 25:
  print("your BMI is normal")
elif BMI > 25 and BMI < 30:
  print(" you are overweight")
else:
  print("you are obese")
  
  