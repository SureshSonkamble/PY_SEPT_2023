from playsound import playsound
pwd=int(input("Enter your password"))
if(pwd==123):
    print("Welcome to system..")
else:
    print("Invalid password")
    playsound("danger.mp3")
