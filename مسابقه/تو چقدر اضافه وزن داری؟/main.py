# nesbate BMI

n = int(input())  # vazn kg
m = float(input())  # ghad metr

bmi = n / (m * m)

print("%.2f" % bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi and bmi < 25:
    print("Normal")
elif 25 <= bmi and bmi < 30:
    print("Overweight")
elif bmi >= 30:
    print("Obese")
