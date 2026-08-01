# a = 5
# b = 6

# a = a+b
# b = a-b
# a = a-b

# print(a,b)



# for i in range(1,51):
#     if(i%2 == 0):
#         print("even =>",i)
    # else :
    #     print("odd =>",i)


# for i in range(1,51):
#     if(i%2 != 0):
#         print("odd =>",i)    


# for i in range(0,7):
#     a=""
#     for j in range(0,7):
#         a=a+"*"
#     print(a)


# for i in range(0,7):
#     a=""
#     for j in range(0,i):
#         a=a+"*"
#     print(a)




# for i in range(0,7):
#     a=""
#     for j in range(0,i):
#         a=a+"*"
#     print(a)

# print("*"*10)



# must main

# for count in range(0,7):
    # print((" " * ( 8 - ( count + 1 ))) + ( "*" * ( count + 1 )))


# print("ankit")


# for count in range(0,7):
#     a=""
#     for count2 in range(0,7):
#       print(8-(count2+1))
#       if (8-(count2+1) > 0):
#         a=a+" "
#       else:    
#         a=a+"*"
#     a += "\n"
# print("a:",a)  


# -----------------
a=""        #
for count_1 in range(1,9):
    for count_2 in range(count_1,9):
        a=a+" "
    for count_3 in range(0,count_1):   
        a=a+"*"
    a+="\n"#


print(a)   #
      
'''
count_1(1-8)                1   2
count_2(count_1-8)          1   2   3   4   5   6   7   8
coun_3(0-count_1)           0   1
a                           _ _ _ _ _ _ _ _ *
                            _ _ _ _ _ _ _ * *
       *
      **
     ***
    ****
   *****
  ******
 *******
********


'''      




# for i in range(0,7):
#     a=""
#     for j in range(i,7):
#         a=a+" "
#     a=a+"*"    
#     print(a)    



a=''
for count in range(1,9):
    for count_1 in range(count,9):
        a=a+" "
    for count_2 in range(0,count):
        a=a+"* "
    a=a+'\n'        
print(a)    


a=''
for count in range(1,6):
    for count_1 in range(count*2,6):
        a=a+" "
    for count_2 in range(0,count):
        a=a+"* "
    a=a+'\n'        
print(a)    

'''
    *
   **
  ****
 ******
********
'''


# for count in range(1,8):
#     a=""
#     for count_1 in range(count,7):
#         a=a+" "
#     if(count==1):
#         a=a+"*"    
#     else:    
#         for count_2 in range(1,(count*2-1)):
#             a=a+"*"
#     print(a)



# for count in range(1,8):
#     a=""
#     if(count == 1 or count == 7):
#         for count_1 in range(1,7):
#             a=a+"*"
#     else:
#         a=a+"*"
#         for count_2 in range(1,5):
#             a=a+" "
#         a=a+"*" 

#     print(a)



# for count in range(1,8):
#     a=""
#     for count_1 in range(1,7):
#         a=a+"*"
#         if(count == 1 or count == 7):
#             pass
#         elif(count_1 > 1 and count_1 < 5):
#             a=a+" "
#         elif(count != 1 and count != 7 and count_1 == 6):
#             a=a+"*" 
#     print(a)




# print("HOLLOW")

# for count in range(1,8):
#     a=""
#     for count_1 in range(1,7):
#         # a=a+"*"
#         if(count == 1 or count == 7):
#             a=a+"*"
#         elif(count_1 > 1 and count_1 < 6):
#             a=a+" "
#         elif(count != 1 and count != 7 and (count_1 == 6 or count_1 == 1)):
#             a=a+"*"
#     print(a)


# print("HOLLOW")

print("Number Triangle")
a=''
for count in range(1,7):
    for count_1 in range(0,count):
        a=a+str(count)
    a=a+"\n"    
print(a)
print("Number Triangle")


print("Number Increasing Pyramid")
a=''
for count in range(1,7):
    for count_1 in range(1,(count+1)):
        a=a+str(count_1)
    a=a+"\n"    
print(a)
print("Number Increasing Pyramid")




print("Number Increasing Reverse Pyramid")
a=''
for count in range(7,0,-1):
    for count_1 in range(1,count):
        a=a+str(count_1)
    a=a+"\n"    
print(a)
print("Number Increasing Reverse Pyramid")




print("palindrome triangle pattern")
a=''
for count in range(1,7):
    for count_1 in range(count,0,-1):
        a=a+str(count_1)
    for count_2 in range(2,(count +1)):
        a=a+str(count_2)
    a=a+"\n"       
print(a)    
print("palindrome triangle pattern")




print("zero. one triangle pattern")
a=''
for count in range(1,8):
    for count_1 in range(count,0,-1):
        if((count_1)%2==0):
            a=a+str(0)
        else:
            a=a+str(1)        
    a=a+"\n"       
print(a)    
print("zero one triangle pattern")




# new_arr = [0] * len(arr)
# new_arr=[0,0,0,0,0]


def arr_fun(arr):
    new_arr=[]
    for count in range(len(arr)):

        if(arr[count]!= -1):
            # continue
            # if():else: we can use
            freq=1
            for count_1 in range(count+1,len(arr)):
                # if(arr[count] == arr[count_1] and arr[count]!= -1):
                if(arr[count] == arr[count_1]):
                    freq=freq+1
                    arr[count_1]=-1
           

            new_arr.append({arr[count]:freq})
    print(new_arr)    
    return new_arr;    





arr = [11,12,13,12,11,14,11,45,45]

print("Print Frequency of Array......")
arr_fun(arr)





print("REMOVE Duplicate From Array")


def remove_duplicate(Arr):
    new_Arr=[]
    for count in range(len(Arr)):
        if(Arr[count] != -1):
            for count_1 in range(count+1,len(Arr)):
                if(Arr[count] == Arr[count_1]):
                   Arr[count_1]=-1
            new_Arr.append(Arr[count])   
                    
    return new_Arr;                    

arr = [11,12,13,12,11,14,11,45,45,10]

print(remove_duplicate(arr))




