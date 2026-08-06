
"""
 _______ ________            _______ ________            _______ ________       
|       |        |          |       |        |          |       |        |              
|   10  |        -------->  |   20  |        -------->  |   30  |        -------->Null
|_______|________|          |_______|________|          |_______|________|



"""




# class Node:
#     arr=[]
#     size=0
#     # arr=[0]
#     # size=1

#     def Traverse(print_data):
#         print(print_data)

#     # def display(self,value):
#     #     Node.arr.append(value)
#     def display():
#         # if(len(Node.arr) <= 1):
#     # FRONT always points to first node
#         # if Node.size > 0:
#         element_arrow = """      
#       FRONT
#         |
#         |
#         V"""
#         print(element_arrow)


#         element1 = " _______ ________           " * Node.size
#         element2 = "|       |        |          " * Node.size
#         # element1 = " _______ ________           " * len(Node.arr)
#         # element2 = "|       |        |          " * len(Node.arr)
#         element3=""
#         # for element in Node.arr:
#         for element in range(int(Node.size)):     
#              element3 += "|   "+str(Node.arr[element])+"  |        -------->  "
#             #  element3 += "|   "+str(element)+"  |        -------->  "

#         element3 +=   "NULL"



#         element4 = "|_______|________|          " * Node.size
#         # element4 = "|_______|________|          " * len(Node.arr)

#         if(len(Node.arr) == 0 ):
#             print("       "+ element3)
#         else:
#             print(element1)
#             print(element2)
#             print(element3)
#             print(element4)

#         Node.show_oper()


#     def show_oper():

#         Node.Traverse("operation have to perform : \n (1) insertion \n (2) deletion")

#         ope_value = input("please select opration :")

#         if(ope_value== "2"):
#             node = Node()
#             value = input("Enter a Value of node which have to delete: ")
#             node.link_delete(value)
#         else:
#             if(len(Node.arr)==0):
#                 node4 = Node()
#                 value = input("Enter a Value of node: ")
#                 node4.First_insertion(value)
#             elif(len(Node.arr)>2):    
#                 Node.Traverse("(1) first (2)end (3)position")
#                 p_value = input("please select opration :")
#             else:    
#                 Node.Traverse("(1) first (2)end")
#                 p_value = input("please select opration :")

#             # Node.Traverse("(1) first (2)end (3)position")
#             # p_value = input("please select opration :")


#             if p_value == "1":
#                 node4 = Node()
#                 value = input("Enter a Value of node: ")
#                 node4.First_insertion(value)
#             elif p_value == "2":
#                 node3 = Node()
#                 value = input("Enter a Value of node: ")
#                 node3.insertion(value)
#             elif  p_value == "3":
#                 value = input("Enter a Value of node :")
#                 pos_value = input("Enter a position: ")
#                 node.new_insertion(pos_value,value)




#     def insertion(self,value):
#         Node.arr.append(value)
#         Node.size+=1
#         Node.display()

#     def link_delete(self,value):
#         node_position = 0
#         # for count in range(len(Node.arr)):
#         for count in range(Node.size):
#             if Node.arr[count] == value:
#                 node_position = count
#                 break

#         # for count in range(node_position,(len(Node.arr)-1)):
#         for count in range(node_position,(Node.size-1)):    
#             Node.arr[count] = Node.arr[count+1] 

#         Node.size-=1    

#         Node.display()            

#     # Insert at first
#     def First_insertion(self, value):

#         Node.arr.append("")

#         # Right shift all values
#         for count in range(Node.size, 0, -1):
#             Node.arr[count] = Node.arr[count - 1]

#         Node.arr[0] = value

#         Node.size += 1

#         Node.display()





# #Right shift
#     def new_insertion(self,position,value):
#         # Node.arr.append("")
#         position = int(position)-1
#         for count in range(int(Node.size),int(position),-1):
#             Node.arr[count] = Node.arr[count-1]

#         Node.arr[int(position)]=value    
#         Node.size+=1
#         Node.display()   










# class Node:

#     def __init__(self, value):
#         self.value = value
#         self.ref = None


# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def traverse(self, msg):
#         print(msg)

#     # ---------------- DISPLAY ----------------

#     def display(self):

#         print("\nFRONT")
#         print("  |")
#         print("  V")

#         if self.head is None:
#             print("NULL")
#             return

#         temp = self.head

#         while temp is not None:
#             print(" _______ ________ ", end="")
#             temp = temp.ref
#         print()

#         temp = self.head
#         while temp is not None:
#             print("|       |        |", end="")
#             temp = temp.ref
#         print()

#         temp = self.head
#         while temp is not None:
#             print(f"|  {temp.value:^4} | -----> ", end="")
#             temp = temp.ref

#         print("NULL")

#         temp = self.head
#         while temp is not None:
#             print("|_______|________|", end="")
#             temp = temp.ref
#         print()

#     # ---------------- INSERT AT END ----------------

#     def insert_end(self, value):

#         new_node = Node(value)

#         if self.head is None:
#             self.head = new_node
#             return

#         temp = self.head

#         while temp.ref is not None:
#             temp = temp.ref

#         temp.ref = new_node

#     # ---------------- INSERT AT FIRST ----------------

#     def insert_first(self, value):

#         new_node = Node(value)

#         new_node.ref = self.head

#         self.head = new_node

#     # ---------------- INSERT AT POSITION ----------------

#     def insert_position(self, position, value):

#         new_node = Node(value)

#         if position == 1:
#             new_node.ref = self.head
#             self.head = new_node
#             return

#         temp = self.head
#         count = 1

#         while temp is not None and count < position - 1:
#             temp = temp.ref
#             count += 1

#         if temp is None:
#             print("Invalid Position")
#             return

#         new_node.ref = temp.ref
#         temp.ref = new_node

#     # ---------------- DELETE ----------------

#     def delete(self, value):

#         if self.head is None:
#             print("Linked List Empty")
#             return

#         if self.head.value == value:
#             self.head = self.head.ref
#             return

#         prev = self.head
#         curr = self.head.ref

#         while curr is not None:

#             if curr.value == value:
#                 prev.ref = curr.ref
#                 return

#             prev = curr
#             curr = curr.ref

#         print("Value Not Found")

#     # ---------------- MENU ----------------

#     def menu(self):

#         while True:

#             self.display()

#             print("\n1. Insert")
#             print("2. Delete")
#             print("3. Exit")

#             choice = input("Enter Choice : ")

#             if choice == "1":

#                 print("\n1. First")
#                 print("2. End")
#                 print("3. Position")

#                 op = input("Enter Choice : ")

#                 value = input("Enter Value : ")

#                 if op == "1":
#                     self.insert_first(value)

#                 elif op == "2":
#                     self.insert_end(value)

#                 elif op == "3":

#                     position = int(input("Enter Position : "))
#                     self.insert_position(position, value)

#                 else:
#                     print("Invalid Choice")

#             elif choice == "2":

#                 value = input("Enter Value to Delete : ")
#                 self.delete(value)

#             elif choice == "3":
#                 print("Program End")
#                 break

#             else:
#                 print("Invalid Choice")


# # ---------------- MAIN ----------------

# ll = LinkedList()
# ll.menu()


class Node:

    def __init__(self,value):
        self.value = value
        self.ref = None



class LinkedList:

    def __init__(self):
        self.front = None

    def insert(self,value):
        # node_obj = Node(value)      #everytime it will create new node
        # node_obj.ref= self.front    #new node object on which we are storing data
        # self.front = node_obj
        if self.front == None:
            node_obj = Node(value)
            self.front = node_obj
        else:
            node_obj = Node(value)
            node_obj.ref= self.front
            self.front = node_obj


        # else :
        #     temp = self.front
        #     while True:
        #         if(temp.ref is None): 
        #             node_obj = Node(value)
        #             self.front = node_obj
        #             break
        #         temp=temp.ref    

        # self.display()    


         # ---------------- Insert End ----------------

    def insert_end(self, value):

        new_node = Node(value)

        if self.front is None:
            self.front = new_node
            return

        temp = self.front

        while temp.ref is not None:
            temp = temp.ref

        temp.ref = new_node   


         # ---------------- Insert End ----------------

    # def insert_position(self, value,pos):

    #     new_node = Node(value)

    #     if self.front is None:
    #         self.front = new_node
    #         return

    #     temp = self.front
    #     a=1

    #     while (temp.ref is not None and a<int(pos)):
    #         temp = temp.ref
    #         a+=1

    #     temp.ref = new_node   
    #     new_node.ref = temp


    def insert_position(self, value, pos):

        pos = int(pos)

        new_node = Node(value)

    # Insert at first
        if pos == 1:
            new_node.ref = self.front
            self.front = new_node
            return

        temp = self.front
        count = 1

        while temp is not None and count < pos - 1:
            temp = temp.ref
            count += 1

        if temp is None:
            print("Invalid Position")
            return

        new_node.ref = temp.ref
        temp.ref = new_node



    def Node_Delete(self,value):

        # Empty list
        if self.front is None:
            print("Linked List is Empty")
            return

         # Delete first node
        if self.front.value == value:
            self.front = self.front.ref

        prev = self.front
        curr = self.front.ref

        while curr is not None:
            if curr.value == value:
                prev.ref = curr.ref
                return

            prev = curr
            curr = curr.ref

        print("Value not found")








    def display(self):

        element_arrow = """      
      FRONT
        |
        |
        V"""
        print(element_arrow)

        element1 = ""
        element2 = ""
        temp = self.front
        while temp is not None:
            # element1 = " _______ ________           "
            # element2 = "|       |        |          "
            element1 += " _______ ________           "
            element2 += "|       |        |          "
            temp = temp.ref

        element3=""

        temp = self.front
        while temp is not None:
            # element3 += "|   "+str(temp.value)+"  |        -------->  "
            element3 += f"| {str(temp.value):^4}  |        -------->  "
        
            temp = temp.ref
   
        element3 +=   "NULL"

        element4=""         #otherwise it will orverwrite by while loop
        temp = self.front
        while temp is not None:
            element4 += "|_______|________|          "
            temp = temp.ref

        # if(len(Node.arr) == 0 ):
        if(self.front == None ):
            print("       "+ element3)
        else:
            print(element1)
            print(element2)
            print(element3)
            print(element4)

        # Node.show_oper()


    # def display(self):

    #     print("\nFRONT")
    #     print("  |")
    #     print("  V")

    #     if self.front is None:
    #         print("NULL")
    #         return

    #     temp = self.front

    #     while temp is not None:
    #         print(" _______ ________ ", end="")
    #         temp = temp.ref
    #     print()

    #     temp = self.front
    #     while temp is not None:
    #         print("|       |        |", end="")
    #         temp = temp.ref
    #     print()

    #     temp = self.front
    #     while temp is not None:
    #         print(f"|  {temp.value:^4} | -----> ", end="")
    #         temp = temp.ref

    #     print("NULL")

    #     temp = self.front
    #     while temp is not None:
    #         print("|_______|________|", end="")
    #         temp = temp.ref
    #     print()

    #     # ---------------- MENU ----------------

    def menu(self):

        while True:

            self.display()

            print("\n1. Insert")
            print("2. Delete")
            print("3. Exit")

            choice = input("Enter Choice : ")

            if choice == "1":

                print("\n1. First")
                print("2. End")
                print("3. Position")

                op = input("Enter Choice : ")

                value = input("Enter Value : ")

                if op == "1":
                    self.insert(value)

                if op == "2":
                    self.insert_end(value)     

                if op == "3":
                    position = input("Enter Positon : ")
                    self.insert_position(value,position)       

                else:
                    print("Invalid Choice")
            elif choice == "2":
                va_lue = input("Enter node value which have to delete : ")
                
                self.Node_Delete(va_lue)
            else:
                print("Invalid Choice")





l1 = LinkedList()
l1.menu()