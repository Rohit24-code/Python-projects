print("Welcome to the day of the dead")
user=input("Do You Want To Play ? ");

print()

count=0;

if(user.lower()=="yes"):
    print("Hurray Let's start then --->>>> ");
else:
    print("ok let's play later");
    quit();
print()
print()

q1=input("1. What is the full form of cpu ? ");
if(q1.lower()=="central processing unit"):
    count+=1;
    print("Correct !! \U0001F600");
else:
    print("Better luck next time \U0001F622");

print()
print()
print()

q2=input("2. What is full form of gpu ? ");
if(q2.lower()=="graphical user interface"):
        count+=1;
        print("Correct !! \U0001F600");
else:
    print("Better luck next time \U0001F622");


print()
print()
print()

q3=input("3. What is full form of ram ? ");
if(q3.lower()=="random access memory"):
        count+=1;
        print("Correct !! \U0001F600");
else:
    print("Better luck next time \U0001F622");


print()
print()
print()

q4=input("4. What is full form of psu ? ");
if(q4.lower()=="power supply"):
        count+=1;
        print("Correct !! \U0001F600");
else:
    print("Better luck next time \U0001F622");

print()
print()
print()

print("{j} you got {q} question correct out of 4".format(q=count,j="\U0001F600" if count > 2 else "\U0001F622"))


