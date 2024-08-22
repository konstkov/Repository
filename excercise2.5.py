print("Enter a mass in medieval units: ")
talents_str=input("Talents: ")
talents=float(talents_str)
pounds_str=input("Pounds: ")
pounds=float(pounds_str)
lots_str=input("Lots: ")
lots=float(lots_str)
print(f"Based on the mass you provided in talents, it would be {(talents/20/32)*0.0133:.2f} in kilograms")
print(f"Based on the mass you provided in pounds, it would be {(pounds/32)*0.0133:.2f} in kilograms")
print(f"Based on the mass you provided in lots, it would be {lots*0.0133:.2f} in kilograms")


