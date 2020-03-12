
end_list = []
name = ""
def dead(age):
    print("###########################\nYOU ARE DEAD")
    if(age>0):
        print("You lived to age",age)
    else:
        end_list.append("\n"+name + " died peacefully of natural causes. (woo-hoo)")
    i =0;
    print("Your eulogy read...\n")
    while(i<len(end_list)):
        print(end_list[i], end = " ")
        i+=1

def q6():
    age=60
    print("###########################\nYou are 60 years old...")
    print("\nWoohoo, you lived to an early retirement! Will you spend you final years: \nA) The Hawiian Islands \nB) Florida \nC) The mountains of Colorado")
    choice = input()
    if (choice == "A" or choice == "a"):
        end_list.append("\nIn their later years, "+name+" was a warm loving person.")
        age=0
        dead(age)
    elif (choice == "B" or choice == "b"):
        end_list.append("\nIn their later years, "+name+" moved to Florida, where they were murdered by a psycho during a hurrican.")#change to death
        dead(age)
    elif (choice == "C" or choice == "c"):
        end_list.append("\nIn their later years, "+name+" was a calm, wise person.")
        age=0
        dead(age)

    else:
        print("Invalid input \n \n")
        q5()

def q5():
    age = 50
    print("###########################\nYou are 50 years old...")
    print("\nUh Oh....mid-life crisis! Will you:\nA) Purchase an exotic sports car?\nB) Take a soothing island vacation to find yourself? \nC) Go sky-diving?")
    choice = input()
    if (choice == "A" or choice == "a"):
        end_list.append("\nWhen crisis struck "+name+" handled it with impulsiveness.")
        q6()
    elif (choice == "B" or choice == "b"):
        end_list.append("\nWhen crisis struck "+name+" handled it with grace.")
        q6()
    elif (choice == "C" or choice == "c"):
        end_list.append("\nWhen crisis struck "+name+" went splat.")
        dead(age)

    else:
        print("Invalid input \n \n")
        q5()

def q4():
    age = 40
    print("###########################\nYou are 40 years old...")
    print("\nYou are in the grind will you:\nA) Cheat to get ahead in your career?\nB) Work honestly even if it goes unnoticed? \nC) Choose work over all?")
    choice = input()
    if (choice == "A" or choice == "a"):
        end_list.append(name+" was a fierce competitor and did whatever was necessary to ensure they were successful.")
        q5()
    elif (choice == "B" or choice == "b"):
        end_list.append(name+" worked with the utmost integrity.")
        q5()
    elif (choice == "C" or choice == "c"):
        end_list.append(name+" worked hard...too hard, work overtook their life and the stress caused an eventual heart-attack.")
        dead(age)

    else:
        print("Invalid input \n \n")
        q4()

def q3():
    print("###########################\nYou are 30 years old...")
    print("\nIt's time to choose, will you have children?\nA) Yes\nB) No")
    choice = input()
    if (choice == "A" or choice == "a"):
        end_list.append("\nA loving parent, ")
        q4()
    elif (choice == "B" or choice == "b"):
        end_list.append("\nA free spirit, ")
        q4()
    else:
        print("Invalide input \n \n")
        q3()

def q2():
    age = 20
    print("###########################\nYou are 20 years old...\n")
    print("It's time to choose a career will you:\nA) Go to college for engineering\nB) Pursue your career as an aspiring artist\nC) Get a job in your home-town as a mechanic")
    choice = input()
    if (choice == "A" or choice == "a"):
        end_list.append("engineer.")
        q3()
    elif (choice == "B" or choice == "b"):
        end_list.append("artist.")
        q3()

    elif (choice == "C" or choice == "c"):
        end_list.append("mechanic. \nUnfortunately a car fell on their head leading to an early retirement...from life.")
        dead(age)
    else:
        print("Invalide input \n \n")
        q2()

def q1():
    print("###########################\nYou are 10 years old")
    print("\nOn the playground you see some kids bullying another kid, do you:\nA) Step in\nB) Do not get involved\nC) Go find help")
    choice = input()
    if(choice == "A" or choice =="a"):
        end_list.append(name+" was a brave")
        q2()
    elif(choice == "B" or choice == "b"):
        end_list.append(name+" was a cowardly")
        q2()

    elif (choice == "C" or choice == "c"):
        end_list.append(name+" was a helpful")
        q2()
    else:
        print("Invalide input \n \n")
        q1()



if __name__ == "__main__":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n###########################\nWelcome to your life!\nYou are 0 years old, please enter your name: ")
    name = input()
    print("Hello",name)
    q1()