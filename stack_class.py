# from mainClass import Main_Function

# class Stack:
#    max =8
#    a=""

#    def my_print():
#     Stack.a=Stack.a+ str("*"*10)
#     print(Stack.a)

# Stack.my_print()
   
class Stack:
   max =8
   a=""
   item=[10]
   item_index=0
   # stack_push=2


   def Traverse(print_data):
      print(print_data)

   def my_print():
    str_value=""
    for count in range(Stack.max):
        item_index= Stack.max-2-count
        if(item_index >= 0 and item_index <len(Stack.item) ):
      #   if(count >= (Stack.max - Stack.stack_push) and count < (Stack.max - Stack.stack_push)):
         #   str_value= str_value +"|"+ "  10  " +"|"+"\n"
           str_value= str_value +"|  "+ str(Stack.item[item_index]) +"  |"+"\n"
        elif(count == 7):
           str_value= str_value +"|"+ ("_"  * 6) +"|"+"\n"
        else:
            str_value= str_value+ "|" + (" "  * 6) + "|" +"\n"
   #  for count in range(Stack.max):
       
   #      if(count == 6):
   #         str_value= str_value +"|"+ "  10  " +"|"+"\n"
   #      elif(count == 7):
   #         str_value= str_value +"|"+ ("_"  * 6) +"|"+"\n"
   #      else:
   #          str_value= str_value+ "|" + (" "  * 6) + "|" +"\n" 
        # str_value=str_value+"\n"
    print(str_value)

   def data_push(item):
   #  print("----len(Stack.item)",Stack.item)
   #  print("----len(Stack.item)",len(Stack.item))
   #  if(int(len(Stack.item))>int(Stack.max)):
    if(int(len(Stack.item)+1)==int(Stack.max)):   
       print("\n------------------") 
       print("Stack overflow!!!")
       print("------------------\n")
       return
       
    Stack.item.append(item)

    Stack.my_print()
   #  str_value=""
   #  for count in range(Stack.max):
   #      item_index= Stack.max-2-count
   #      if(item_index >= 0 and item_index <len(Stack.item) ):
   #    #   if(count >= (Stack.max - Stack.stack_push) and count < (Stack.max - Stack.stack_push)):
   #       #   str_value= str_value +"|"+ "  10  " +"|"+"\n"
   #         str_value= str_value +"|  "+ str(Stack.item[item_index]) +"  |"+"\n"
   #      elif(count == 7):
   #         str_value= str_value +"|"+ ("_"  * 6) +"|"+"\n"
   #      else:
   #          str_value= str_value+ "|" + (" "  * 6) + "|" +"\n"
   #      # str_value=str_value+"\n"
   
   
   
   #  Stack.stack_push = Stack.stack_push+1 
   #  print(str_value)


   # def data_pop():
   #  print("Stack.item----",len(Stack.item))
   # #  if(len(Stack.item)<0):
   #  if(len(Stack.item)==0):    #because we are not using last index our list getting started from 1 index
   #      print("Stack underflow!!!")
   #      return
   # #  print(Stack.item)  
   # #  last_index = len(Stack.item)-1
   # #  print(last_index)
   # #  for new_data in range(last_index):
   # #     Stack.item[new_data]=Stack.item[new_data]
   # #  print(Stack.item)   
   # #  lastvalu=(len(Stack.item)-1)
  
   # #  Stack.item[len(Stack.item)-1]=""
   #   # KEY CHANGE: Decrease tracker by 1. The last item is now logically deleted.
   # #  Stack.item_index = Stack.item_index - 1

   
   #  # 1. Rebuild the list manually to be shorter by 1 element
   #  new_shorter_list = []
   #  last_valid_index = len(Stack.item) - 1
    
   #  for new_data in range(last_valid_index):
   #     new_shorter_list.append(Stack.item[new_data])
       
   #  # 2. Overwrite the original list with the shorter one
   #  Stack.item = new_shorter_list

   #  str_value=""
   #  for count in range(Stack.max): #8-2-
   #      item_index= Stack.max-2-count
   #      if(item_index >= 0 and item_index <len(Stack.item) ):
      
   #         str_value= str_value +"|  "+ str(Stack.item[item_index]) +"  |"+"\n"
   #      elif(count == 7):
   #         str_value= str_value +"|"+ ("_"  * 6) +"|"+"\n"
   #      else:
   #          str_value= str_value+ "|" + (" "  * 6) + "|" +"\n"

   #  print(str_value)

   def data_pop():
   #  print("Stack.item----",len(Stack.item))
   #  if(len(Stack.item)<0):
    if(len(Stack.item)==0):    #because we are not using last index our list getting started from 1 index
        print("\n------------------")
        print("Stack underflow!!!")
        print("------------------\n")
        return

    # 1. Rebuild the list manually to be shorter by 1 element
    new_shorter_list = []
    last_valid_index = len(Stack.item) - 1
    
    for new_data in range(last_valid_index):
       new_shorter_list.append(Stack.item[new_data])
       
    # 2. Overwrite the original list with the shorter one
    Stack.item = new_shorter_list

    Stack.my_print()




   # def data_reverse():

   
   #  # 1. Rebuild the list manually to be shorter by 1 element
   #  new_shorter_list = []
   #  last_valid_index = len(Stack.item) - 1
    
   #  for new_data in range(last_valid_index,-1,-1):
   #     new_shorter_list.append(Stack.item[new_data])
       
   #  # 2. Overwrite the original list with the shorter one
   #  Stack.item = new_shorter_list

   #  str_value=""
   #  for count in range(Stack.max): #8-2-
   #      item_index= Stack.max-2-count
   #      if(item_index >= 0 and item_index <len(Stack.item) ):
      
   #         str_value= str_value +"|  "+ str(Stack.item[item_index]) +"  |"+"\n"
   #      elif(count == 7):
   #         str_value= str_value +"|"+ ("_"  * 6) +"|"+"\n"
   #      else:
   #          str_value= str_value+ "|" + (" "  * 6) + "|" +"\n"

   #  print(str_value)

   def data_reverse():

   
    # 1. Rebuild the list manually to be shorter by 1 element
    new_shorter_list = []
    last_valid_index = len(Stack.item) - 1
    
    for new_data in range(last_valid_index,-1,-1):
       new_shorter_list.append(Stack.item[new_data])
       
    # 2. Overwrite the original list with the shorter one
    Stack.item = new_shorter_list

    Stack.my_print()


   # def data_sort(asc_dec):
    
   #  # FIX 1: Indent all sorting code so it belongs to this IF condition
   #  if(asc_dec == "1"):
   #      last_valid_index = len(Stack.item) - 1
        
   #      for new_data in range(last_valid_index):
   #          # FIX 2: Added "+ 1" to the stop bound so the last element is included
   #          for new_data1 in range(new_data + 1, last_valid_index + 1):
   #              if(int(Stack.item[new_data]) > int(Stack.item[new_data1])):
   #                  ref = Stack.item[new_data]
   #                  Stack.item[new_data] = Stack.item[new_data1]
   #                  Stack.item[new_data1] = ref
   #  else:
   #      last_valid_index = len(Stack.item) - 1
        
   #      for new_data in range(last_valid_index):
   #          # FIX 2: Added "+ 1" to the stop bound so the last element is included
   #          for new_data1 in range(new_data + 1, last_valid_index + 1):
   #              if(int(Stack.item[new_data]) < int(Stack.item[new_data1])):
   #                  ref = Stack.item[new_data]
   #                  Stack.item[new_data] = Stack.item[new_data1]
   #                  Stack.item[new_data1] = ref


   #  str_value = ""
   #  for count in range(Stack.max): 
   #      # FIX 3: Changed -2 to -1 so the top element of the stack shows up
   #      item_index = Stack.max - 1 - count
        
   #      if(item_index >= 0 and item_index < len(Stack.item)):
   #          str_value = str_value + "|  " + str(Stack.item[item_index]) + "  |" + "\n"
   #      elif(count == Stack.max - 1): # Made dynamic instead of hardcoded 7
   #          str_value = str_value + "|" + ("_" * 6) + "|" + "\n"
   #      else:
   #          str_value = str_value + "|" + (" " * 6) + "|" + "\n"

   #  print(str_value)


   def data_sort(asc_dec):
    
    # FIX 1: Indent all sorting code so it belongs to this IF condition
    if(asc_dec == "1"):
        last_valid_index = len(Stack.item) - 1
        
        for new_data in range(last_valid_index):
            # FIX 2: Added "+ 1" to the stop bound so the last element is included
            for new_data1 in range(new_data + 1, last_valid_index + 1):
                if(int(Stack.item[new_data]) > int(Stack.item[new_data1])):
                    ref = Stack.item[new_data]
                    Stack.item[new_data] = Stack.item[new_data1]
                    Stack.item[new_data1] = ref
    else:
        last_valid_index = len(Stack.item) - 1
        
        for new_data in range(last_valid_index):
            # FIX 2: Added "+ 1" to the stop bound so the last element is included
            for new_data1 in range(new_data + 1, last_valid_index + 1):
                if(int(Stack.item[new_data]) < int(Stack.item[new_data1])):
                    ref = Stack.item[new_data]
                    Stack.item[new_data] = Stack.item[new_data1]
                    Stack.item[new_data1] = ref
    
    Stack.my_print()





   # def data_search(search_value):
    
    
   #    last_valid_index = len(Stack.item) 
   #    find_value=0
   #    value_position=0
        
   #    for new_data in range(last_valid_index):
   #       if(int(Stack.item[new_data])== int(search_value)):
   #          find_value = 1
   #          value_position=new_data+1

            

           
   #    if(find_value == 1):
   #       print("Value present at position",value_position)
   #    else:
   #       print("value not present")   


   #    str_value = ""
   #    for count in range(Stack.max): 
   #      # FIX 3: Changed -2 to -1 so the top element of the stack shows up
   #      item_index = Stack.max - 1 - count
        
   #      if(item_index >= 0 and item_index < len(Stack.item)):
   #          str_value = str_value + "|  " + str(Stack.item[item_index]) + "  |" + "\n"
   #      elif(count == Stack.max - 1): # Made dynamic instead of hardcoded 7
   #          str_value = str_value + "|" + ("_" * 6) + "|" + "\n"
   #      else:
   #          str_value = str_value + "|" + (" " * 6) + "|" + "\n"

   #    print(str_value)

   def data_search(search_value):
    
    
      last_valid_index = len(Stack.item) 
      find_value=0
      value_position=0
        
      for new_data in range(last_valid_index):
         if(int(Stack.item[new_data])== int(search_value)):
            find_value = 1
            value_position=new_data+1
           
      if(find_value == 1):
         print("\n--------------------------------------")
         print("Value present at position",value_position)
         print("--------------------------------------\n")
      else:
         print("\n-----------------")
         print("value not present")   
         print("-----------------\n")

      Stack.my_print()


   # def data_peek():

   #    last_valid_index = len(Stack.item) -1
   #    peek_value = Stack.item[last_valid_index]

   #    print(f"peek value is :- {peek_value} , At position :-{last_valid_index+1}")

   #    str_value = ""
   #    for count in range(Stack.max): 
   #      # FIX 3: Changed -2 to -1 so the top element of the stack shows up
   #      item_index = Stack.max - 1 - count
        
   #      if(item_index >= 0 and item_index < len(Stack.item)):
   #          str_value = str_value + "|  " + str(Stack.item[item_index]) + "  |" + "\n"
   #      elif(count == Stack.max - 1): # Made dynamic instead of hardcoded 7
   #          str_value = str_value + "|" + ("_" * 6) + "|" + "\n"
   #      else:
   #          str_value = str_value + "|" + (" " * 6) + "|" + "\n"

   #    print(str_value)


   def data_peek():

      last_valid_index = len(Stack.item) -1
      peek_value = Stack.item[last_valid_index]

      print("\n----------------------------------------------------")
      print(f"peek value is :- {peek_value} , At position :-{last_valid_index+1}")
      print("-----------------------------------------------------\n")

      Stack.my_print()

   

   def data_display():
         Stack.Traverse("* Please Select Stack Operation Below :\n"
         " (1) Push\n" 
         " (2) pop\n"
         " (3) peek\n"
         " (4) search\n"
         " (5) sort\n"
         " (6) Reverse\n"
         " (7) Exit"
         )
         operation_choice=input("Please enter your operation:")
         # data_inset=input("Please enter your data:")
         if(operation_choice=="1"):
            data_inset=input("Please enter your data:")
            Stack.data_push(data_inset)
         elif(operation_choice=="2"):
            Stack.data_pop()   
         elif(operation_choice=="6"):
            Stack.data_reverse()      
         elif(operation_choice=="5"):
            data_asc_des=input("Sort by \n(1) Ascending\n(2) Descending :")
            Stack.data_sort(data_asc_des)
         elif(operation_choice=="4"):
            data_search_value=input("Data Search value :-")
            Stack.data_search(data_search_value)   
         elif(operation_choice=="3"):
            Stack.data_peek()     
         elif(operation_choice=="7"):
            return
            # Main_Function()   

         Stack.data_display()


   # def data_push(item):
   #  Stack.item.append(item)  # Adds the new item to our list
   #  str_value = ""
    
   #  for count in range(Stack.max):
   #      # Calculate index: Top of stack prints first, down to index 0 at the bottom
   #      item_index = Stack.max - 2 - count 
        
   #      if(count == 7):
   #         # Always print the base floor at the very bottom
   #         str_value = str_value + "|" + ("_"  * 6) + "|" + "\n"
   #      elif(item_index >= 0 and item_index < len(Stack.item)):
   #         # If a valid item exists at this index position, format and print it
   #       #   val_str = str(Stack.item[item_index]).center(6)
   #         str_value = str_value + "|  " + str(Stack.item[item_index]) + "  |" + "\n"
   #      else:
   #         # Otherwise, leave the space blank
   #         str_value = str_value + "|" + (" "  * 6) + "|" + "\n"
           
   #  print(str_value)


# Stack.Traverse(".  Welcome to Data Structure.  ")
# Stack.Traverse("-------------------------------")
# Stack.Traverse("-------------------------------")
# Stack.Traverse("Please select Data Structure")
# Stack.Traverse("(1) Stack (2) Queue")
# enter_choice=input("Please enter your Choice:")
# # Stack.Traverse("Please enter your Choice:")

# if(enter_choice=="1"):
#    Stack.Traverse("Data Structure Chosen : Stack")
#    Stack.my_print()
#    Stack.data_display()
 






# Stack.Traverse("My All data")


# Stack.data_push(20)
# Stack.data_push(30)
# Stack.data_push(10)






# By this way we can also solve this
# class Stack:
#    max = 8
#    a = ""
#    item = [10]
#    item_index = 1 # Tracks how many active items are in the stack


#    def Traverse(print_data):
#       print(print_data)

#    def my_print():
#     str_value = ""
#     for count in range(Stack.max):
       
#         if(count == 6):
#            str_value = str_value + "|" + "  10  " + "|" + "\n"
#         elif(count == 7):
#            str_value = str_value + "|" + ("_" * 6) + "|" + "\n"
#         else:
#             str_value = str_value + "|" + (" " * 6) + "|" + "\n"
#     print(str_value)

#    def data_push(item):
#     Stack.item.append(item)
#     # KEY FIX 1: Advance the active pointer tracker since an item was added
#     Stack.item_index = Stack.item_index + 1 
    
#     str_value = ""
#     for count in range(Stack.max):
#         item_index = Stack.max - 2 - count
#         # KEY FIX 2: Check against Stack.item_index instead of len(Stack.item)
#         if(item_index >= 0 and item_index < Stack.item_index):
#            str_value = str_value + "|  " + str(Stack.item[item_index]) + "  |" + "\n"
#         elif(count == 7):
#            str_value = str_value + "|" + ("_" * 6) + "|" + "\n"
#         else:
#             str_value = str_value + "|" + (" " * 6) + "|" + "\n"
#     print(str_value)


#    def data_pop():
#     if Stack.item_index == 0:
#         print("Stack Underflow! No items to pop.")
#         return

#     # Decrease tracker by 1. The last item is now logically deleted.
#     Stack.item_index = Stack.item_index - 1
    
#     str_value = ""
#     for count in range(Stack.max): 
#         item_index = Stack.max - 2 - count
#         # KEY FIX 3: Check against Stack.item_index instead of len(Stack.item)
#         if(item_index >= 0 and item_index < Stack.item_index):
#            str_value = str_value + "|  " + str(Stack.item[item_index]) + "  |" + "\n"
#         elif(count == 7):
#            str_value = str_value + "|" + ("_" * 6) + "|" + "\n"
#         else:
#             str_value = str_value + "|" + (" " * 6) + "|" + "\n"

#     print(str_value)




#    def data_display():
#          Stack.Traverse("Operation have to perform :\n"
#          "(1) Push\n" 
#          "(2) pop\n"
#          "(3) peek\n"
#          "(4) search\n"
#          "(5) sort\n"
#          "(6) Reverse"
#          )
#          operation_choice = input("Please enter your operation:")
         
#          if(operation_choice == "1"):
#             data_inset = input("Please enter your data:")
#             Stack.data_push(data_inset)
#          elif(operation_choice == "2"):
#             Stack.data_pop()   
#          Stack.data_display()


# Stack.Traverse(".  Welcome to Data Structure.  ")
# Stack.Traverse("-------------------------------")
# Stack.Traverse("-------------------------------")
# Stack.Traverse("Please select Data Structure")
# Stack.Traverse("(1) Stack (2) Queue")
# enter_choice = input("Please enter your Choice:")

# if(enter_choice == "1"):
#    Stack.Traverse("Data Structure Chosen : Stack")
#    Stack.my_print()
#    Stack.data_display()