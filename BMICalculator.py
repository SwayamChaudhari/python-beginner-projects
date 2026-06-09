# Height Reference
'''
| Imperial | Meters | Centimeters |
| :------- | :----- | :---------- |
| 5'0"     | 1.52 m | 152 cm      |
| 5'1"     | 1.55 m | 155 cm      |
| 5'2"     | 1.57 m | 157 cm      |
| 5'3"     | 1.60 m | 160 cm      |
| 5'4"     | 1.63 m | 163 cm      |
| 5'5"     | 1.65 m | 165 cm      |
| 5'6"     | 1.68 m | 168 cm      |
| 5'7"     | 1.70 m | 170 cm      |
| 5'8"     | 1.73 m | 173 cm      |
| 5'9"     | 1.75 m | 175 cm      |
| 5'10"    | 1.78 m | 178 cm      |
| 5'11"    | 1.80 m | 180 cm      |
| 6'0"     | 1.83 m | 183 cm      |
| 6'1"     | 1.85 m | 185 cm      |
| 6'2"     | 1.88 m | 188 cm      |
| 6'3"     | 1.91 m | 191 cm      |
| 6'4"     | 1.93 m | 193 cm      |
'''
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

bmi = weight / (height * height)
if bmi < 18.5:
    print(f"BMI: {bmi}")
    print("Category: Underweight")
elif bmi < 25:
    print(f"BMI: {bmi}")
    print("Category: Normal Weight")
elif bmi < 30:
    print(f"BMI: {bmi}")
    print("Category: Overweight")
else:
    print(f"BMI: {bmi}")
    print("Category: Obese")

print("Uploaded to GitHub successfully")






