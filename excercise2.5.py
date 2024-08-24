print("Enter a mass in medieval units: ")
talents_str=input("Talents: ")
talents=float(talents_str)
print(f"= {talents*20*32*0.0133:.0f}  kilograms and {(talents*20*32*0.0133) % 1000:.2f}  grams")
pounds_str=input("Pounds: ")
pounds=float(pounds_str)
print(f"= {pounds*32*0.0133:.0f}  kilograms and {(pounds*32*0.0133) % 1000:.2f} grams")
lots_str=input("Lots: ")
lots=float(lots_str)
print(f"= {lots*0.0133:.0f}  kilograms and {(lots*0.0133) % 1000:.2f} grams")



