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

try:
    x=input("enter the integer:")
    add=x+t
except NameError:
    print("t is not declared")
except:
    print("t is declared")


try:
    a=input("enter the value")
    if a<3:
        print("enter the value again")
    else:
        print("value",a)

except SyntaxError:
    print("SyntexError in line 34 & line 36")
except:
    print("the value of a is defined")



#wap to correct the text:
str="Hello-this-is-my-file"
print(str.replace('-',' '))


#extra questions
from textblob import TextBlob
text=TextBlob('he is gret persan')
print(text.correct())

