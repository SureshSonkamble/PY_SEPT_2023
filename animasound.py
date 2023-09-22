from playsound import playsound
from PIL import Image
print("1.Lion")
print("2.Bird")
print("3.Cartoon")
print("4.Dog")
ch=int(input("Select Choice To Play Sound"))
if(ch==1):
    print("Lion")
    myImage = Image.open("l.jpg");
    myImage.show();
    playsound("l.wav")
elif(ch==2):
    print("Bird")
    playsound("b.wav")
elif(ch==3):
    print("Cartoon")
    playsound("c.wav")
elif(ch==4):
    print("Dog")
    playsound("d.wav")
else:exit()    
