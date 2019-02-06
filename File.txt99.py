#write a program that copies contents of file:
f=open('File.txt','w')
f.writelines("Give me the power,\nI will give you freedom. \nWhen ever you treat me bad,\nThe reaction of mine is also bad.")
f.close()


#write a program that produces error on name length less than 3:
name=input("enter the Name:")
if name.isalpha() and len(name)<3:
    raise NameError("Name is not valid")
else:
    print("accepted")


#write a program that produces 3 diffrent error and write handler for that error:

try:
    age = int(input("Enter your age: "))
    print ("You must be {0} years old.".format(age))
except ValueError:
    print( "Your age must be numeric.")


#wap to correct the text:
from textblob import TextBlob
text=TextBlob('he is gret persan')
print(text.correct())

str="Hello-this-is-my-file"
print(str.replace('-',' '))





