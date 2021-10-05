print("Welcome to Class 8 General Science Quiz")
print()

wanna_play = (input("Do you want to play? ").lower())

print()

if wanna_play != "yes":
    print("The game has ended. See you soon! :)")
    quit()

print("Ok then, Let's Play!")
print()

score = 0

print("READ THE INSTRUCTIONS CAREFULLY")
print()

ins = """Instructions:
1. There are 10 questions in this Quiz.
2. After typing the answer press Enter.
3. Don't write the answers in sentences, instead write in words.
4. Make sure you write the correct spelling otherwise your answer may be wrong.
5. Write the answers which have numbers in digits instead of words."""
print(ins)
print()

ans = input("1. ________ is called force per unit area. ")
if ans.lower() == "pressure":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print('Pressure')

print()

ans = input("2. Due to which force does an apple fall from a tree? ")
if ans.lower() == "gravitational force":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print('Gravitational Force')

print()

ans = input("3. Is electrostatic force a contact force? ")
if ans.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("It is a non-contact force.")

print()

ans = int(input("4. How many zones are there in a flame? "))
if ans == 3:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("3")

print()

ans = input("5. What is the Full Form of LPG? (MIND YOUR SPELLING) ")
if ans.lower() == "liquefied petroleum gas":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("Liquefied Petroleum Gas")

print()

ans = input("6. The lowest temperature at which a substance catches fire is called? ")
if ans.lower() == "ignition temperature":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("Ignition Temperature")

print()

ans = input("7. Is water a lubricant? ")
if ans.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("No, it is not.")

print()

ans = input("8. The Frictional Force exerted by fluids is called? ")
if ans.lower() == "drag":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("Drag")

print()

ans = input("9. Is Paramecium a multicellular organism? ")
if ans.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("It is unicellular and has a single cell.")

print()

ans = int(input("10. White light consists of how many colours? "))
if ans == 7:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    print("7")

print()
input("Press Enter To View Your Score")

print()

print("You got " + str(score) + " answer correct!!" )
print("Your Percentage Of Correct Answers is : " + str((score/10)*100) + "%" )

print()