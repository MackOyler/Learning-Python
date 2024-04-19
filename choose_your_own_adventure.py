name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has dark forests on either side. The road comes to an T, you can go left or right. Which direction do you want to go? ").lower()


if answer == "left": 
    answer = input("You come to a river, you can try to walk around it or swim accross. Walk or Swim (walk/swim)? ").lower()

    if answer == "swim":
        print("You swam accross the river, and were eaten by alligators on the opposite shore. You are dead, and you lose.")
    elif answer == "walk":
        print("You walked for many miles, were consumed by the forest, and die of dehydration. You lose.")
    else:
        print("Not a valid option. You lose. Follow directions next time. ")     

elif answer == "right": 
    answer = input("You come to a bridge, it looks wobbly, do you cross the bridge or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back to main road. You are going in circles. You lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them, Yes or No (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stranger, and they hand you a hefty bag filled with gold, a map, a compass, and water. You WIN!")

        elif answer == "no":
            print("You ignore the stranger, and they disappear in the darkness, offended you didn't speak to them. You lose.")

        else:
            print("Not a valid option. You lose. Follow directions next time. ")    

    else:
        print("Not a valid option. You lose. Follow directions next time. ")

else: 
    print("Not a valid option. You lose. Follow directions next time. ")

    print("Thank you for playing", name, "!")