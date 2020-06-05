from random import randint
import sys
sys.argv                                                         # Remember the first input([0]) is the file name so start with index 1
Answer = randint(int(sys.argv[1]), int(sys.argv[2]))             # Inputs should be converted into integer in sys.argv form with index
while True :
    try:
         # print(Answer)
         Guess = int(input(f"Guess a Number Between {sys.argv[1]} to {sys.argv[2]} = "))
         if 0 <= Guess <= 10 :
             if Guess == Answer:
                 print("You are a Genius !!!")
                 break
             else :
                 print("Please try again. Better Luck Next Time.")
                 continue
         else:
             print("ERROR : Please Enter a number Between 0 to 10")
             continue
    except ValueError :
        print("ERROR : Please Enter a Numeric value ")
        continue

