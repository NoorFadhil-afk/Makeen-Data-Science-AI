#Counting Matches
string = "Welcome"
uppercase = 0
for char in string :
    if char.isupper() :
        uppercase = uppercase + 1
print("string:", uppercase)

#Counting Vowels
word = input("Enter a word: ")
vowels = 0
for char in word :
 if char.lower() in "aeiou" :
    vowels = vowels + 1
print("Enter of vowels:", vowels)

#Finding All Matches Example
sentence = input("Enter a sentence: ")
for i in range(len(sentence)) :
     if sentence[i].isupper() :
         print(i)
#First Example
found = False
position = 0
while not found and position < len(string) :
 if string[position].isdigit() :
     found = True
 else :
     position = position + 1
if found :
   print("First digit occurs at position", position)
else :
   print("The string does not contain a digit.")
#Finding the Last Match
found = False
position = len(string) - 1
while not found and position >= 0 :
 if string[position].isdigit() :
    found = True
 else :
    position = position - 1
#Validiting String
string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid = len(string) == 13
position = 0
while valid and position < len(string) :
 if position == 0:
     valid = string[position] == "("
 elif position == 4 :
     valid = string[position] == ")"
 elif position == 8 :
     valid = string[position] == "-"
 else:
     valid = string[position].isdigit()
 position = position + 1
if valid :
     print("The string contains a valid phone number.")
else:
     print("The string does not contain a valid phone number.")
#Validating a String (code)
string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid = len(string) == 13
position = 0
while valid and position < len(string) :
 valid = ((position == 0 and string[position] == "(") or
     (position == 4 and string[position] == ")") or
     (position == 8 and string[position] == "-") or
     (position != 0 and position != 4 and position != 8  and
     string[position].isdigit())) 
 position = position + 1
if valid :
 print("The string contains a valid phone number.")
else:
 print("The string does not contain a valid phone number.")
##Building a New String (code)
userInput = input("Enter a credit card number: ")
creditCardNumber = ""
for char in userInput :
 if char != " " and char != "-" :
    creditCardNumber = creditCardNumber + char
#Example: Grading Multiple Choice Exam multiplechoice.py
#  This program grades a multiple choice exam in which each question has four
#  possible choices: a, b, c, or d.
# Define a string containing the correct answers.
CORRECT_ANSWERS = "adbdcacbdac"
# Obtain the user's answers, and make sure enough answers are provided.
done = False
while not done :
   userAnswers = input("Enter your exam answers: ")
   if len(userAnswers) == len(CORRECT_ANSWERS) :
      done = True     
   else :
     print("Error: an incorrect number of answers given.")    
# Check the exam.
numQuestions = len(CORRECT_ANSWERS)
numCorrect = 0
results = ""
#Example: Grading Multiple Choice Exam multiplechoice.py (2)
for i in range(numQuestions) :
  if userAnswers[i] == CORRECT_ANSWERS[i] :
     numCorrect = numCorrect + 1
     results = results + userAnswers[i]
  else :
     results = results + "X"
# Grade the exam.
score = round(numCorrect / numQuestions * 100)
if score == 100 :
    print("Very Good!")
else :
    print("You missed %d questions: %s" % (numQuestions- numCorrect, results))
print("Your score is: %d percent" % score) 
#Random Numbers/Simulations
from random import randint
for i in range(10):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(d1,d2)
##The Monte Carlo Method
from random import randint
TRIES = 10000
hits = 0

for i in range(TRIES):
    r = random()
    x = -1 + 2 * r
    r = random()
    y = -1 + 2 * r
    if x * x * + y * y <= 1:
        hits = hits + 1
piEstimate = 4.0 * hits / TRIES
print("piEstimate for pi:", piEstimate)

#Guess Game: Guess number 1 -100
from random import randint
 #generate a random integer 1-100
r = randint(1,100)
done = False
while not done:
 #get user guess
 userGuess = int(input("Guess a number between 1 and 100: "))
 if userGuess <1 or userGuess >100 :
     print("Your guess is outside range 1-100!")
 else:
     if userGuess == r:
         print("Congratulation! You win.")
         done = True
     elif userGuess > r:
         print("Go lower")
     else:
         print("Go higher")

