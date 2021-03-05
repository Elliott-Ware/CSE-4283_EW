class BMI:

    def calculator():
        weight = int(input("What is your weight in pounds: "))
        height = int(input("What is your height in inches(12 inches per foot): "))

        
#Calculations for body mass index
        step1 = weight * .45
        step2 = height * .025
        newStep2 = step2 * step2
        newStep1 = step1 / newStep2
        newNewStep = round(newStep1)

#If statements to determine BMI category
        if newNewStep < 18.5:
            print("Your BMI is:",newNewStep,", and you are underweight.")

        if 18.5 <= newNewStep <= 24.9:
            print("Your BMI is",newNewStep,", and you are normalweight.")

        if 25 < newNewStep <= 29.9:
            print("Your BMI is:",newNewStep,",and you are oververweight.")

        if newNewStep >= 30:
            print("Your BMI is:",newNewStep,", and you are obese.")



