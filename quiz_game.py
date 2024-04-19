print("Welcome to my computer quiz!") 

playing = input("Would you like to play a game? (yes/no): ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What does CPU stand for? (CPU): ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does GPU stand for? (GPU): ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? (RAM): ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does PSU stand for? (PSU): ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"That is {(score/4) * 100}% answered correctly!")