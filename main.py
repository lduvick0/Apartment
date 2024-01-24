
def apt_search1(city,max_rent,min_beds,pets_allowed):
    if pets_allowed:
        print("Welcome to CG Property Management! Looking up listings in " + city + " for " + str(
            min_beds) + " bedroom apartments that are allowed, all within a budget of " + str(
            max_rent) + " per month...")

    else:
        print("Welcome to CG Property Management! Looking up listings in " + city + " for " + str(
            min_beds) + " bedroom apartments, all within a budget of " + str(max_rent) + " per month...")


def apt_search2(city,max_rent,min_beds=1,pets_allowed=False):
    if pets_allowed:
        print("Welcome to CG Property Management! Looking up listings in " +city+" for "+str(min_beds)+" bedroom apartments that are allowed, all within a budget of "+str(max_rent)+" per month...")

    else:
        print(f"Welcome to CG Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of {max_rent} per month...")

apt_search1("San Francisco",1400,3, True )
apt_search2("Charlotte",1200)
apt_search2("San Francisco", 1100, 2)
apt_search2(city="San Francisco", max_rent=1000, pets_allowed=True)




addMode = lambda a : a + 10
exponentMode=lambda a : a ** 2
dashMode=lambda a : "-"+ a
divideMode= lambda a: a/3

print (addMode(5))
print (exponentMode(10))
print (dashMode("Taco"))
print(divideMode(6))