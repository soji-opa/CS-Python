command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else: 
            started = True
            print ("Car started...")
        
    elif command ==  "stop":
        if stopped:
            print("Engine stopped already")
        else:
            stopped = True
            print ("Stop engine...")
    elif command == "help":
        print ("""
Start - To get the car running
Stop - To stop the car
Quit - To exit the program
help - To get help on features of the car
        """)
    elif command == "quit":
        break
    else:
        print("I do not understand that code")