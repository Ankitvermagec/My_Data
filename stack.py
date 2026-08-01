print("Welcome. to Data Structure")
print("--------------------------")
print("Please select Data Structure")

Value = """
   (1) Stack 
   (2) Queue"""

print(Value)

user= input("Enter a value:-")


if(user == "1"):
    a=""
    for count in range(1,9):
        if(count==7):
            a=a+"|"
            for count_1 in range(1,5):
                if(count_1 ==3):
                    a=a+"10"
                
                a=a+" "
            a=a+"|"
            a=a+"\n"

        elif(count != 8): 
            a=a+"|"
            for count_1 in range(1,7):
                a=a+" "
            a=a+"|"
            a=a+"\n"
        else:
            a=a+"|"
            for count_2 in range(1,7):
                a=a+"_"
            a=a+"|"
            a=a+"\n"
    print(a) 




Value = """

Please select. the operation to perform on Stack:

   (1) Push 
   (2) pop"""

print(Value)

user2 = input("Enter Operation :-")


if(user2 == "1"):
    a=""
    for count in range(1,9):
        if(count==6):
            a=a+"|"
            for count_1 in range(1,5):
                if(count_1 ==3):
                    a=a+"20"
                
                a=a+" "
            a=a+"|"
            a=a+"\n"
        elif(count==7):
            a=a+"|"
            for count_1 in range(1,5):
                if(count_1 ==3):
                    a=a+"10"
                
                a=a+" "
            a=a+"|"
            a=a+"\n"
        # if(count==6 or count==7):
        #     a=a+"|"
        #     for count_1 in range(1,5):
        #         if(count_1 ==3):
        #             a=a+"10"
                
        #         a=a+" "
        #     a=a+"|"
        #     a=a+"\n"

        elif(count != 8): 
            a=a+"|"
            for count_1 in range(1,7):
                a=a+" "
            a=a+"|"
            a=a+"\n"
        else:
            a=a+"|"
            for count_2 in range(1,7):
                a=a+"_"
            a=a+"|"
            a=a+"\n"
    print(a) 
elif(user2 == "2"):
    a=""
    for count in range(1,9):
    #     if(count==6 or count==7):
    #         a=a+"|"
    #         for count_1 in range(1,5):
    #             if(count_1 ==3):
    #                 a=a+"10"
                
    #             a=a+" "
    #         a=a+"|"
    #         a=a+"\n"

        if(count != 8): 
            a=a+"|"
            for count_1 in range(1,7):
                a=a+" "
            a=a+"|"
            a=a+"\n"
        else:
            a=a+"|"
            for count_2 in range(1,7):
                a=a+"_"
            a=a+"|"
            a=a+"\n"
    print(a) 
