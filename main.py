
def apt_search1(city,max_rent,min_beds,pets_allowed):

    if pets_allowed:
        pets=" are allowed "
    else:
        pets=" are not allowed "

    print("Welcome to CG Property Management! Looking up listings in "+city+" for"+str(min_beds)+" bedroom apartments that" + pets +", all within a budget of "+str(max_rent)+" per month...")


def apt_search2(city,max_rent,min_beds,pets_allowed):
    min_beds = 1
    pets_allowed = False
    if pets_allowed:
        pets=" are allowed "
    else:
        pets="are not allowed "

    print("Welcome to CG Property Management! Looking up listings in " +city+" for"+str(min_beds)+" bedroom apartments that" + pets +", all within a budget of "+str(max_rent)+" per month...")

max_rent=int(input("What is your budget for rent?: "))
city=input("What city would you like to search for?: ")
min_beds=int(input("How many"))
pets_allowed=bool(input("Do you have any pets (True/False): "))
apt_search1(city,max_rent ,min_beds,pets_allowed)
apt_search2(city ,max_rent ,min_beds ,pets_allowed)

