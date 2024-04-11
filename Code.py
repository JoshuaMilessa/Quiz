print("Welcome to my quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")
score = 0

# Questions
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "Graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does IT stand for? ")
if answer.lower() == "information technology":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")  

answer = input("What does WWW stand for? ")
if answer.lower() == "World Wide Web":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does HTML stand for? ")
if answer.lower() == "Hyper Text Markup Language":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does CSS stand for? ")
if answer.lower() == "Cascading Style Sheets":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does SQL stand for? ")
if answer.lower() == "Structured Query Language":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 10) * 100) + "%.")
