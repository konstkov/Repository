gender=input("Enter your gender")
hemoglobin=int(input("Enter your hemoglobin level"))
if gender == " Male" and 134 < hemoglobin < 167 or gender == " Female" and 117 < hemoglobin < 155:
    print("Your hemoglobin level is normal")
elif gender == " Male" and hemoglobin < 134 or gender == " Female" and hemoglobin < 117:
    print("Your hemoglobin level is too low")
else: print("Your hemoglobin level is too high")