
class Queue:
   max =8
   a=""
   item=[10]
   item_index=0
   # Queue_push=2


   def Traverse(print_data):
      print(print_data)

   # def my_print():
   #  str_value=""
   #  for count in range(Queue.max):
   #      item_index= Queue.max-2-count
   #      if(item_index >= 0 and item_index <len(Queue.item) ):
   #         str_value= str_value +"|  "+ str(Queue.item[item_index]) +"  |"+"\n"
   #    #   if(count == 6):
   #       #   str_value= str_value +"|"+ "  10  " +"|"+"\n"
   #      elif(count == 7):
   #         str_value= str_value +"|"+ ("_"  * 6) +"|"+"\n"
   #      else:
   #          str_value= str_value+ "|" + (" "  * 6) + "|" +"\n"
   #      # str_value=str_value+"\n"
   #  print(str_value)

   def my_print():
      var1= "- "*Queue.max
      var2=""
      for item_index in range (len(Queue.item)):
            var2+=str(Queue.item[item_index])+" "
      var3= "- "*Queue.max

      print(var1)
      print(var2)
      print(var3)

   def data_push(item):
    if(int(len(Queue.item)+1)==int(Queue.max)):  
   #  if(len(Queue.item)>Queue.max):
       print("Queue overflow!!!")
       return
       
    Queue.item.append(item)
   #  str_value=""
   #  for count in range(Queue.max):
   #      item_index= Queue.max-2-count
   #      if(item_index >= 0 and item_index <len(Queue.item) ):
   #    #   if(count >= (Queue.max - Queue.Queue_push) and count < (Queue.max - Queue.Queue_push)):
   #       #   str_value= str_value +"|"+ "  10  " +"|"+"\n"
   #         str_value= str_value +"|  "+ str(Queue.item[item_index]) +"  |"+"\n"
   #      elif(count == 7):
   #         str_value= str_value +"|"+ ("_"  * 6) +"|"+"\n"
   #      else:
   #          str_value= str_value+ "|" + (" "  * 6) + "|" +"\n"
   #      # str_value=str_value+"\n"
   # #  Queue.Queue_push = Queue.Queue_push+1 
   #  print(str_value)
    Queue.my_print()


   def data_pop():
    if(len(Queue.item)<=0):
        print("Queue underflow!!!")
        return

   
    # 1. Rebuild the list manually to be shorter by 1 element
    new_shorter_list = []
    # last_valid_index = len(Queue.item) - 1
    last_valid_index = len(Queue.item)
    
    for new_data in range(1,last_valid_index):
       new_shorter_list.append(Queue.item[new_data])
       
    # 2. Overwrite the original list with the shorter one
    Queue.item = new_shorter_list

   #  str_value=""
   #  for count in range(Queue.max): #8-2-
   #      item_index= Queue.max-2-count
   #      if(item_index >= 0 and item_index <len(Queue.item) ):
      
   #         str_value= str_value +"|  "+ str(Queue.item[item_index]) +"  |"+"\n"
   #      elif(count == 7):
   #         str_value= str_value +"|"+ ("_"  * 6) +"|"+"\n"
   #      else:
   #          str_value= str_value+ "|" + (" "  * 6) + "|" +"\n"

   #  print(str_value)
    Queue.my_print()


   def data_reverse():

   
    # 1. Rebuild the list manually to be shorter by 1 element
    new_shorter_list = []
    last_valid_index = len(Queue.item) - 1
    
    for new_data in range(last_valid_index,-1,-1):
       new_shorter_list.append(Queue.item[new_data])
       
    # 2. Overwrite the original list with the shorter one
    Queue.item = new_shorter_list

   #  str_value=""
   #  for count in range(Queue.max): #8-2-
   #      item_index= Queue.max-2-count
   #      if(item_index >= 0 and item_index <len(Queue.item) ):
      
   #         str_value= str_value +"|  "+ str(Queue.item[item_index]) +"  |"+"\n"
   #      elif(count == 7):
   #         str_value= str_value +"|"+ ("_"  * 6) +"|"+"\n"
   #      else:
   #          str_value= str_value+ "|" + (" "  * 6) + "|" +"\n"

   #  print(str_value)
    Queue.my_print()

 
   def data_sort(asc_dec):
    
    # FIX 1: Indent all sorting code so it belongs to this IF condition
    if(asc_dec == "1"):
        last_valid_index = len(Queue.item) - 1
        
        for new_data in range(last_valid_index):
            # FIX 2: Added "+ 1" to the stop bound so the last element is included
            for new_data1 in range(new_data + 1, last_valid_index + 1):
                if(int(Queue.item[new_data]) > int(Queue.item[new_data1])):
                    ref = Queue.item[new_data]
                    Queue.item[new_data] = Queue.item[new_data1]
                    Queue.item[new_data1] = ref
    else:
        last_valid_index = len(Queue.item) - 1
        
        for new_data in range(last_valid_index):
            # FIX 2: Added "+ 1" to the stop bound so the last element is included
            for new_data1 in range(new_data + 1, last_valid_index + 1):
                if(int(Queue.item[new_data]) < int(Queue.item[new_data1])):
                    ref = Queue.item[new_data]
                    Queue.item[new_data] = Queue.item[new_data1]
                    Queue.item[new_data1] = ref


   #  str_value = ""
   #  for count in range(Queue.max): 
   #      # FIX 3: Changed -2 to -1 so the top element of the Queue shows up
   #      item_index = Queue.max - 1 - count
        
   #      if(item_index >= 0 and item_index < len(Queue.item)):
   #          str_value = str_value + "|  " + str(Queue.item[item_index]) + "  |" + "\n"
   #      elif(count == Queue.max - 1): # Made dynamic instead of hardcoded 7
   #          str_value = str_value + "|" + ("_" * 6) + "|" + "\n"
   #      else:
   #          str_value = str_value + "|" + (" " * 6) + "|" + "\n"

   #  print(str_value)
    Queue.my_print()



   def data_search(search_value):
    
    
      last_valid_index = len(Queue.item) 
      find_value=0
      value_position=0
        
      for new_data in range(last_valid_index):
         if(int(Queue.item[new_data])== int(search_value)):
            find_value = 1
            value_position=new_data+1

            

           
      if(find_value == 1):
         print("Value present at position",value_position)
      else:
         print("value not present")   


      # str_value = ""
      # for count in range(Queue.max): 
      #   # FIX 3: Changed -2 to -1 so the top element of the Queue shows up
      #   item_index = Queue.max - 1 - count
        
      #   if(item_index >= 0 and item_index < len(Queue.item)):
      #       str_value = str_value + "|  " + str(Queue.item[item_index]) + "  |" + "\n"
      #   elif(count == Queue.max - 1): # Made dynamic instead of hardcoded 7
      #       str_value = str_value + "|" + ("_" * 6) + "|" + "\n"
      #   else:
      #       str_value = str_value + "|" + (" " * 6) + "|" + "\n"

      # print(str_value)
      Queue.my_print()

   

   def data_peek():

      last_valid_index = len(Queue.item) -1
      peek_value = Queue.item[last_valid_index]

      print(f"peek value is :- {peek_value} , At position :-{last_valid_index+1}")

      # str_value = ""
      # for count in range(Queue.max): 
      #   # FIX 3: Changed -2 to -1 so the top element of the Queue shows up
      #   item_index = Queue.max - 1 - count
        
      #   if(item_index >= 0 and item_index < len(Queue.item)):
      #       str_value = str_value + "|  " + str(Queue.item[item_index]) + "  |" + "\n"
      #   elif(count == Queue.max - 1): # Made dynamic instead of hardcoded 7
      #       str_value = str_value + "|" + ("_" * 6) + "|" + "\n"
      #   else:
      #       str_value = str_value + "|" + (" " * 6) + "|" + "\n"

      # print(str_value)
      Queue.my_print()

   

   def data_display():
         Queue.Traverse("* Please Select Queue Operation Below :\n"
         "(1) enqueue\n" 
         "(2) dequeue\n"
         "(3) peek\n"
         "(4) search\n"
         "(5) sort\n"
         "(6) Reverse"
         )
         operation_choice=input("Please enter your operation:")
         # data_inset=input("Please enter your data:")
         if(operation_choice=="1"):
            data_inset=input("Please enter your data:")
            Queue.data_push(data_inset)
         elif(operation_choice=="2"):
            Queue.data_pop()   
         elif(operation_choice=="6"):
            Queue.data_reverse()      
         elif(operation_choice=="5"):
            data_asc_des=input("Sort by \n(1) Ascending\n(2) Descending :")
            Queue.data_sort(data_asc_des)
         elif(operation_choice=="4"):
            data_search_value=input("Data Search value :-")
            Queue.data_search(data_search_value)   
         elif(operation_choice=="3"):
            Queue.data_peek()     

         Queue.data_display()



# Queue.Traverse(".  Welcome to Data Structure.  ")
# Queue.Traverse("-------------------------------")
# Queue.Traverse("-------------------------------")
# Queue.Traverse("Please select Data Structure")
# Queue.Traverse("(1) Stack (2) Queue")
# enter_choice=input("Please enter your Choice:")
# # Queue.Traverse("Please enter your Choice:")

# if(enter_choice=="2"):
#    Queue.Traverse("Data Structure Chosen : Queue")
#    Queue.my_print()
#    Queue.data_display()