def askForInput():
    print("Error")

try:
    number = int(input("Enter number: "))
    #result = number/0
    #open a file
except ValueError:
    print("Your input is not Correct!")
except ZeroDivisionError:
    print("you are dividing by 0!")
except:
    print("something happened I dont know!")
finally:
    print("im always executed NO MATTER WHAT!")
#     result = number/0
# except:
#     print("whoopsies, thats not right. try again?")
