import random





count=0;



while True:
 user_input=input("Please Guess A Number !!!! ")
 random_number = random.randint(1, 10)
 print(user_input,"user_input")
 print(random_number,"Random Number")
 if user_input.isdigit():
    user_input=int(user_input)
    count+=1;
    if user_input==random_number:
        print("hurray you got it right the number is ", user_input);
        break;
    else:
        print("please try again");



