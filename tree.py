# """
#     _ _ _ 
#    |     |
#     - - -
# """






# class Tree:
#     arr=[]
#     size=0
#     # arr=[0]
#     # size=1

#     def Traverse(print_data):
#         print(print_data)

#     # def display(self,value):
#     #     Node.arr.append(value)
#     def display():



#         element1 = " _______  " * Tree.size
#         element2 = "|       | " * Tree.size

#         element3=""
#         # for element in Node.arr:
#         for element in range(int(Tree.size)):     
#              element3 += "|   "+str(Tree.arr[element])+"   |"




#         element4 = "|_______|" * Tree.size


 
#         print(element1)
#         print(element2)
#         print(element3)
#         print(element4)


#     def insertion(value):

#         Tree.arr.append(value)
#         Tree.size += 1 
#         Tree.display()   



# while True:

#     value = input("Enter value (q to stop): ")

#     if value == "q":
#         break

#     Tree.insertion(value)

# # Tree.display()

# Tree.display()        



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# root = Node(10)        
# root.left = Node(20)
# root.right = Node(30)


# root.left.left = Node(40)
# root.left.right = Node(50)
# root.right.left = Node(60)




# class Node:

#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# class Tree:

#     def __init__(self):
#         self.root = None


#     def display(self):

#         if self.root is None:
#             print("Tree is Empty")
#             return

#         print()

#     # Root
#         print(" " * 10 + str(self.root.value))

#     # Branches
#         print(" " * 9 + "/" + " " * 2 + "\\")

#     # Level 2
#         left = " "
#         right = " "

#         if self.root.left:
#             left = str(self.root.left.value)

#         if self.root.right:
#             right = str(self.root.right.value)

#         print(" " * 7 + left + " " * 6 + right)

#     # Level 3
#         if self.root.left:

#             if self.root.left.left:
#                 print(" " * 6 + "/")


#         lleft = " "
#         lright = " "

#         if self.root.left.left:
#             lleft = str(self.root.left.left.value)

#         if self.root.left.right:
#             lright = str(self.root.left.right.value)

#         print(" " * 4 + lleft + " " * 6 + lright)    

#     # Find node by value
#     def search(self, root, parent_value):

#         if root is None:
#             return None

#         if root.value == parent_value:
#             return root

#         temp = self.search(root.left, parent_value)

#         if temp is not None:
#             return temp

#         return self.search(root.right, parent_value)

#     # Insert Node
#     def insert(self):

#         value = input("Enter Node Value : ")

#         # First Node
#         if self.root is None:
#             self.root = Node(value)
#             print("Root inserted.")
#             return

#         parent = input("Enter Parent Node Value : ")

#         parent_node = self.search(self.root, parent)

#         if parent_node is None:
#             print("Parent not found.")
#             return

#         print("1. Left")
#         print("2. Right")

#         choice = input("Select Position : ")

#         if choice == "1":

#             if parent_node.left is None:
#                 parent_node.left = Node(value)
#                 print("Left child inserted.")
#             else:
#                 print("Left child already exists.")

#         elif choice == "2":

#             if parent_node.right is None:
#                 parent_node.right = Node(value)
#                 print("Right child inserted.")
#             else:
#                 print("Right child already exists.")

#         else:
#             print("Invalid Choice")




# tree = Tree()

# while True:

#     print("\n1. Insert")
#     print("2. Exit")

#     choice = input("Enter Choice : ")

#     if choice == "1":
#         tree.insert()

#     else:
#         break


#tree must be balanced


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    # ---------------- SEARCH ----------------
    def search(self, root, parent_value):

        if root is None:
            return None

        if root.value == parent_value:
            return root

        temp = self.search(root.left, parent_value)

        if temp is not None:
            return temp

        return self.search(root.right, parent_value)

    # ---------------- INSERT ----------------
    # def insert(self):

    #     value = input("Enter Node Value : ")

    #     if self.root is None:
    #         self.root = Node(value)
    #         print("Root inserted.")
    #         return

    #     parent = input("Enter Parent Node Value : ")

    #     parent_node = self.search(self.root, parent)

    #     if parent_node is None:
    #         print("Parent not found.")
    #         return

    #     print("1. Left")
    #     print("2. Right")

    #     choice = input("Select Position : ")

    #     if choice == "1":

    #         if parent_node.left is None:
    #             parent_node.left = Node(value)
    #             print("Left child inserted.")
    #         else:
    #             print("Left child already exists.")

    #     elif choice == "2":

    #         if parent_node.right is None:
    #             parent_node.right = Node(value)
    #             print("Right child inserted.")
    #         else:
    #             print("Right child already exists.")

    #     else:
    #         print("Invalid Choice")

    def insert(self):
        value = input("pls Enter value : -")
        new_node = Node(value)

        #First Node
        if self.root is None:
            self.root = new_node
            print("root inserted")
            return

        temp = self.root

        while True:

            # Try LEFT
            if temp.left is None:
                temp.left = new_node
                print("inserted on left")
                return

            elif temp.right is None:
                temp.right = new_node
                print("inserted on right")
                return

            
            # Both are occupied
            # Move to next node
            else:
                temp = temp.left

            
    # ---------------- DISPLAY ----------------
    # def display(self):

    #     if self.root is None:
    #         print("Tree is Empty")
    #         return

    #     print("\n")

    #     # Root
    #     print(" " * 10 + str(self.root.value))

    #     # Root branches
    #     print(" " * 9 + "/" + " " * 2 + "\\")

    #     # Level 2
    #     left = " "
    #     right = " "

    #     if self.root.left:
    #         left = self.root.left.value

    #     if self.root.right:
    #         right = self.root.right.value

    #     print(" " * 7 + str(left) + " " * 6 + str(right))

    #     # Level 3
    #     if self.root.left:

    #         ll = " "
    #         lr = " "

    #         if self.root.left.left:
    #             ll = self.root.left.left.value

    #         if self.root.left.right:
    #             lr = self.root.left.right.value

    #         print(" " * 6 + "/" + " " * 2 + "\\")
    #         print(" " * 4 + str(ll) + " " * 6 + str(lr))

    #     if self.root.right:

    #         rl = " "
    #         rr = " "

    #         if self.root.right.left:
    #             rl = self.root.right.left.value

    #         if self.root.right.right:
    #             rr = self.root.right.right.value

    #         print(" " * 20 + "/" + " " * 2 + "\\")
    #         print(" " * 18 + str(rl) + " " * 6 + str(rr))

    # ---------------- DISPLAY ----------------

    def display(self):

        if self.root is None:
            print("Tree is Empty")
            return

        print("\n")

        print(" " * 10 + str(self.root.value))

        print(" " * 9 + "/" + " " * 2 + "\\")

        left = " "
        right = " "

        if self.root.left:
            left = self.root.left.value

        if self.root.right:
            right = self.root.right.value

        print(" " * 7 + str(left) + " " * 6 + str(right))

        if self.root.left:

            ll = " "
            lr = " "

            if self.root.left.left:
                ll = self.root.left.left.value

            if self.root.left.right:
                lr = self.root.left.right.value

            print(" " * 6 + "/" + " " * 2 + "\\")

            print(" " * 4 + str(ll) + " " * 6 + str(lr))





tree = Tree()

while True:

    print("\n1. Insert")
    print("2. Display")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        tree.insert()

    elif choice == "2":
        tree.display()

    elif choice == "3":
        break

    else:
        print("Invalid Choice")