#Write a program for fetching and storing airport data.
# The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit.
# If the user chooses to enter a new airport, the program asks the user
# to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead, the program
# asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends. The user can choose
# a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport.
# For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)
airports={}
while True:
    options=int(input("Choose between the following options: \n "
    "Press 1 if you would like to enter a new airport. \n"  
    "Press 2 if you would like to fetch the information \n"
    "of an existing airport. \n"
    "Press 3 if you would like to quit."))
    if options==1:
        icao=input("Please enter the ICAO code of the airport")
        name=input("Please enter the name of the airport")
        airports[icao]=name
    if options==2:
        icao=input("Please enter the ICAO code of the airport")
        if icao in airports:
            print(f"the airport you are looking for is {airports[icao]}")
        else:
            print(
            "Error: the airport data you are trying to retrieve doesn't exist,\n ""please complete the step 1 and enter ICAO code and name of the airport")

    elif options==3:
        print("Bye bye")
        break
    else:
        print("C'mon dude")




