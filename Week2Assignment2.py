print("Welcome; this is a game where you have to guess our teacher's age while he was finishing college."
      "If you guess it right you will have some extra points. Goog Luck!")
guess = 0

while guess != 22:

 g = input("What was Matthew Loschiavo age? ")

 try:
     guess = int(g)
 except:
     print("Please enter a number")

 if guess == 22:
     print("You're right! Talk to the teacher about the extra point cause I made that up!")
 else:
    if guess > 22:
        print("Nope, was he that old?, try again")
    else:
        print("Nope, was he this young? try again")

print("See you around!!")