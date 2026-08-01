# class Node:
#     value = ""
#     # ref = ""
#     # ref = "n"
#     ref = None
#     # str=""
#     # def show_linke(value,ref):
#     # def show_linke(self):
#     #     for count in range(1,4):
#     #         Node.str=Node.str+"|"
#     #         for count_1 in range(1,8):
#     #             if(count==2 and count_1 ==2):
#     #                 Node.str=Node.str+self.value
#     #                 # LinkedList.str=LinkedList.str+"2"
#     #             elif(count==2 and count_1 ==6):
#     #                 if(self.ref is not None):
#     #                 # if(self.ref != None):
#     #                     Node.str=Node.str+str(self.ref.value)
#     #                 else:      
#     #                     Node.str=Node.str+str(self.ref)  
#     #             # elif(count==2 and count_1 ==6):
#     #             #     Node.str=Node.str+str(self.ref)
#     #             #     # Node.str=Node.str+self.ref
#     #             #     # LinkedList.str=LinkedList.str+"n"
#     #             elif(count_1 == 4):
#     #                 Node.str=Node.str+"|"
#     #             elif(count == 1 or count == 3):
#     #                 Node.str=Node.str+"-"
#     #             else:
#     #                 Node.str=Node.str+" "  
 
#     #         Node.str=Node.str+"|\n"
#     #     # LinkedList.str=LinkedList.str+" "    
#     #     print(Node.str)  


#     def show_linke(self):
#         output_str=""
#         for count in range(1,4):
#             output_str=output_str+"|"
#             for count_1 in range(1,8):
#                 if(count==2 and count_1 ==2):
#                     output_str=output_str+self.value
#                     # LinkedList.str=LinkedList.str+"2"
#                 # elif(count==2 and count_1 ==6):
#                 #     if(self.ref is not None):
#                 #     # if(self.ref != None):
#                 #         output_str=output_str+str(self.ref.value)
#                 #     else:      
#                 #         output_str=output_str+str(self.ref)  
#                 elif(count==2 and count_1 ==6):
#                     if(self.ref == None):
#                         output_str=output_str+str(None)
#                     else:
#                         output_str=output_str+" "

#                     # Node.str=Node.str+str(self.ref)
#                     # Node.str=Node.str+self.ref
#                     # LinkedList.str=LinkedList.str+"n"
#                 elif(count_1 == 4):
#                     output_str=output_str+"|"
#                 elif(count == 1 or count == 3):
#                     output_str=output_str+"-"
#                 else:
#                     output_str=output_str+" "  
 
#             output_str=output_str+"|\n"
#         # LinkedList.str=LinkedList.str+" "    

#         print(output_str)  

#         # output_str=output_str+"---->>"






# # class LinkedList:




# print(" ----- Linked list ----")

# node = Node()
# node.value = input("Enter a Value of node: ")

# # node.ref = input("Enter a Reference of node: ")
# # node.show_linke()

# node1 = Node()
# node1.value = input("Enter a Value of node: ")
# node.ref=node1
# # node.ref=node1.ref.value

# print("----- Next Ref",node.ref)
# print("----- Next Ref value",node.ref.value)
# # node.ref = input("Enter a Reference of node: ")
# # node1.show_linke()

# node2 = Node()
# node2.value = input("Enter a Value of node: ")
# node1.ref=node2
# node2.ref = None
# # # node.ref = input("Enter a Reference of node: ")
# # node2.show_linke()


# # node.ref = node1
# # node.show_linke()


# print("Node")
# node.show_linke()

# print("Node1")
# node1.show_linke()

# print("Node2")
# node2.show_linke()


"""
 _______ ________            _______ ________            _______ ________       
|       |        |          |       |        |          |       |        |              
|   10  |        -------->  |   20  |        -------->  |   30  |        -------->Null
|_______|________|          |_______|________|          |_______|________|



"""


# arr=[10,20,30]
# element1 = " _______ ________           " * 3
# element2 = "|       |        |          " * 3

# # element3 = "|   10  |        -------->"

# element3=""
# for element in arr:
#     element3 += "|   "+str(element)+"  |        -------->  "

# element3 +=   "NULL"

# element4 = "|_______|________|          " * 3




# print(element1)
# print(element2)
# print(element3)
# print(element4)


class Node:
    arr=[]
    size=0
    # arr=[0]
    # size=1

    def Traverse(print_data):
        print(print_data)

    # def display(self,value):
    #     Node.arr.append(value)
    def display():
        # if(len(Node.arr) <= 1):
    # FRONT always points to first node
        # if Node.size > 0:
        element_arrow = """      
      FRONT
        |
        |
        V"""
        print(element_arrow)


        element1 = " _______ ________           " * Node.size
        element2 = "|       |        |          " * Node.size
        # element1 = " _______ ________           " * len(Node.arr)
        # element2 = "|       |        |          " * len(Node.arr)
        element3=""
        # for element in Node.arr:
        for element in range(int(Node.size)):     
             element3 += "|   "+str(Node.arr[element])+"  |        -------->  "
            #  element3 += "|   "+str(element)+"  |        -------->  "

        element3 +=   "NULL"

        # if(len(Node.arr) == 0 ):       #only for spacing we use this
        #     element3 += "      " +   "NULL" 
        # else:
        #     element3 +=   "NULL"



        element4 = "|_______|________|          " * Node.size
        # element4 = "|_______|________|          " * len(Node.arr)

        if(len(Node.arr) == 0 ):
            print("       "+ element3)
        else:
            print(element1)
            print(element2)
            print(element3)
            print(element4)

        Node.show_oper()


    def show_oper():

        Node.Traverse("operation have to perform : \n (1) insertion \n (2) deletion")

        ope_value = input("please select opration :")

        if(ope_value== "2"):
            node = Node()
            value = input("Enter a Value of node which have to delete: ")
            node.link_delete(value)
        else:
            if(len(Node.arr)==0):
                node4 = Node()
                value = input("Enter a Value of node: ")
                node4.First_insertion(value)
            elif(len(Node.arr)>2):    
                Node.Traverse("(1) first (2)end (3)position")
                p_value = input("please select opration :")
            else:    
                Node.Traverse("(1) first (2)end")
                p_value = input("please select opration :")

            # Node.Traverse("(1) first (2)end (3)position")
            # p_value = input("please select opration :")


            if p_value == "1":
                node4 = Node()
                value = input("Enter a Value of node: ")
                node4.First_insertion(value)
            elif p_value == "2":
                node3 = Node()
                value = input("Enter a Value of node: ")
                node3.insertion(value)
            elif  p_value == "3":
                value = input("Enter a Value of node :")
                pos_value = input("Enter a position: ")
                node.new_insertion(pos_value,value)




    def insertion(self,value):
        Node.arr.append(value)
        Node.size+=1
        Node.display()

    def link_delete(self,value):
        node_position = 0
        # for count in range(len(Node.arr)):
        for count in range(Node.size):
            if Node.arr[count] == value:
                node_position = count
                break

        # for count in range(node_position,(len(Node.arr)-1)):
        for count in range(node_position,(Node.size-1)):    
            Node.arr[count] = Node.arr[count+1] 

        Node.size-=1    

        Node.display()            


        # for node_val in Node.arr:    
        #     if node_val == value:

    #     #Right shift
    # def First_insertion(self,value):
    #     Node.arr.append("")
    #     # position = int(position)-1
    #     for count in range(1,(int(Node.size)+1)):
    #         Node.arr[count] = Node.arr[count+1]

    #     Node.arr[0]=value    
    #     Node.size+=1
    #     Node.display()   


    # Insert at first
    def First_insertion(self, value):

        Node.arr.append("")

        # Right shift all values
        for count in range(Node.size, 0, -1):
            Node.arr[count] = Node.arr[count - 1]

        Node.arr[0] = value

        Node.size += 1

        Node.display()





#Right shift
    def new_insertion(self,position,value):
        # Node.arr.append("")
        position = int(position)-1
        for count in range(int(Node.size),int(position),-1):
            Node.arr[count] = Node.arr[count-1]

        Node.arr[int(position)]=value    
        Node.size+=1
        Node.display()   



# Node.display()        
# Node.show_oper()


# node = Node()
# value = input("Enter a Value of node: ")
# node.insertion(value)

# node1 = Node()
# value = input("Enter a Value of node: ")
# node.insertion(value)


# node = Node()



# Node.Traverse("operation have to perform : \n (1) insertion \n (2) deletion")

# ope_value = input("please select opration :")

# if(ope_value== "2"):
#     value = input("Enter a Value of node which have to delete: ")
#     node.link_delete(value)
# else:
#     Node.Traverse("(1) first (2)end (3)position")
#     p_value = input("please select opration :")


#     if p_value == "1":
#         node4 = Node()
#         value = input("Enter a Value of node: ")
#         node4.First_insertion(value)
#     elif p_value == "2":
#         node3 = Node()
#         value = input("Enter a Value of node: ")
#         node3.insertion(value)
#     elif  p_value == "3":
#         value = input("Enter a Value of node :")
#         pos_value = input("Enter a position: ")
#         node.new_insertion(pos_value,value)





