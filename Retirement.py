class Retirement:

    def retireFunc():
        x = 1
        while x == 1:
            age = int(input("How old are you? "))
            salary = int(input("What is your current salary(no commas)? "))
            savings = float(input("How much would you like to save per year (Ex. 10 for 10%)? "))
            goal = float(input("How much money would you like to save in total? "))

            newSavings = savings / 100
        #print(newSavings)
            spy = salary * newSavings
            spy2 = spy * 1.35

##round up for age 
            numYears = goal/spy2
            goalAge = numYears + age
            newAge = round(goalAge, 0)
        #code for roungin age
        #goalAge2 = goalAge 
        #if goalAge <
            if newAge < 100:
                print("You will be", newAge, "years old when you are able to retire.")
    
            else:
                print("Sorry! Your savings goal will NOT be met. Try again with other values.")

        
            
