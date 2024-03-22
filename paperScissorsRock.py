import random;

options=["paper","rock","scissors"];
user_count=0;
system_count=0;

while True:
    user_input = input("Please choose paper scissors rock or q to quit! ");

    if user_input=="q":
        break;

    if user_input not in options:
        continue;
    random_number=random.randint(0,2);
    system_input = options[random_number];
   
    print(f"computer choose {system_input}")
   
    if user_input == "rock" and system_input == "paper":
        user_count+=1
        print("user wins");
    elif user_input == "scissors" and system_input == "paper":
        user_count+=1
        print("user wins");
    elif user_input == "scissors" and system_input == "rock":
        user_count+=1
        print("user wins");
    else:
        system_count+=1;
        print("computer wins");

print(f"you won {user_count} and computer won {system_count}")

    
         
