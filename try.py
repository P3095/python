userscore= []

max_score = 10
max_trial = 8


def question1():
   print ("Question 1")
   print ("What is the highest grossing movie of 2024?")
   answer = input()
   if answer == "Avatar":
        print ("Correct!")
        print ("The answer is Avatar: The Way of Water")
        userscore.append(answer)
        print (userscore)
        print ("Would you like to go to the next question?")
        #assume = input()
        #if assume == "yes":
         #question2()
      
   else:
        print ("Wrong")
        print ("Would you like to try again?")
        answer = input()
        if answer == "yes":
         print ("Question 1")
         print ("What is the highest grossing movie of 2024?")
         qews = input()
         if answer == "Avatar":
          print ("Correct!")
          print ("The answer is Avatar: The Way of Water")
        if answer == "no":
          print ("Game Over!")
            
def question2():
 print ("Question 2")
 print ("Who is the highest paid director of all time?")
 answer = input()
 if answer == "Quentin" or  "quentin":
    print ("Correct!")
    print ("The answer is Quentin Taratino")
    userscore.append(answer)
    print (userscore)
    print ("Would you like to go to the next question?")

 else:
     print ("Wrong")
     print ("Would you like to try again?")
     answer = input()
     if answer == "yes":
         print ("Question 2")
         print ("Who is the highest paid director of all time?")
         dcd = input()
         if answer == "no":
            print ("Game Over!")



def question3():
 print ("Question 3")
 print ("Which movie got a 100 on Rotten Tomatoes?")
 answer = input()
 if answer == "Supacell":
    print ("Correct!")
    print ("The answer is Supacell")
    print("Would you like to go the next question?")

 else:
     print ("Wrong")
     print ("Would you like to try again?")
     var = input()
     if var == "yes":
         print ("Question 2")
         print ("Who is the highest paid director of all time?")
         dcd = input()
         if var == "no":
            print ("Game Over!")


def startgame2():
   currenttrial = 1
   currentscore = 0
   currenttrial += 1
   print ("Welcome to the Movie quiz. You will be asked a series of question and if you can get 20 of it right, you win.")
   print ("You have only two chances on each question so use it wisely.")
   print ("Press Enter to begin")
   ten = input()
   question1()
   while True:
    currentscore += 2
    currenttrial += 1
    wen= input()
    if wen == 'yes':
     print ("Your score is " + str(currentscore))
    elif wen == 'no':
     print ("Your score is " + str(currentscore))
     print ("Game over")
     break
    question2()
    wen= input()
    if wen == 'yes':
     currentscore += 2
     currenttrial += 1
     print ("Your score is " + str(currentscore))
    elif wen == 'no':
     print ("Your score is " + str(currentscore))
     print ("Game over")
     break
    question3()
    wen= input()
    if wen == 'yes':
     currentscore += 2
     currenttrial += 1
     print ("Your score is " + str(currentscore))
    elif wen == 'no':
     print ("Your score is " + str(currentscore))
     print ("Game over")
     break

    if currentscore >= max_score:
     print ("hello")
     break

startgame2()