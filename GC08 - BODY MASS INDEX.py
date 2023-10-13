weight = int(input("What is your weight in kg? "))
height = float(input("\nWhat is your height in meters? "))
BMI = weight / height ** 2
if BMI < 18.5:
  print("\nYour BMI is", BMI, "\n\nYou are underweight!")
elif 18.5 <= BMI < 25:
  print("\nYour BMI is", BMI, "\n\nYou have a normal weight :>")
elif 25 <= BMI < 30:
  print("\nYour BMI is", BMI, "\n\nYou are overweight!")
else:
  print("\nYour BMI is", BMI, "\n\nYou are obese!!")
