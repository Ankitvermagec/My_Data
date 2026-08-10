from stack_class import Stack
from queue import Queue
# from linklist import Node



# Stack.Traverse("- - - - - - - - - - - - - - - - - - -")
# Stack.Traverse("      Welcome to Data Structures     ")
# Stack.Traverse("- - - - - - - - - - - - - - - - - - -")
# # Stack.Traverse("-------------------------------------")
# Stack.Traverse("                                       ")
# Stack.Traverse(" * Please select Data Structure Below :")
# Stack.Traverse("                                       ")
# Stack.Traverse(" (1) Stack\n (2) Queue\n (3) LinkedList")
# Stack.Traverse("                                       ")
# enter_choice=input(" Please enter your Choice:")
# Stack.Traverse("                                   ")
# # Stack.Traverse("Please enter your Choice:")

# if(enter_choice=="1"):
#    Stack.Traverse("- - - - - * * * * * * * - - - - - -")
#    Stack.Traverse("  Welcome to STACK Data Structure  ")
#    Stack.Traverse("- - - - - * * * * * * * - - - - - -")
#    Stack.Traverse("                                   ")
#    Stack.my_print()
#    Stack.data_display()
# elif(enter_choice=="2"):
#    Stack.Traverse("- - - - - * * * * * * * - - - - - -")
#    Stack.Traverse("  Welcome to QUEUE Data Structure  ")
#    Stack.Traverse("- - - - - * * * * * * * - - - - - -")
#    Stack.Traverse("                                   ")
#    Queue.my_print()
#    Queue.data_display()   

# elif(enter_choice=="3"):
#    Node.Traverse("- - - - - * * * * * * * * *  - - - - - -")
#    Node.Traverse("  Welcome to LINKEDLIST Data Structure  ")
#    Node.Traverse("- - - - - * * * * * * * * *  - - - - - -")
#    Node.Traverse("                                        ")
#    Node.display()     
#    print()   #for spacing
#    Node.show_oper()
         





class MainClass:

   #  @staticmethod
    def main_function(self):

        Stack.Traverse("- - - - - - - - - - - - - - - - - - -")
        Stack.Traverse("      Welcome to Data Structures     ")
        Stack.Traverse("- - - - - - - - - - - - - - - - - - -")

        Stack.Traverse("")
        Stack.Traverse(" * Please select Data Structure Below :")
        Stack.Traverse("")
        Stack.Traverse(" (1) Stack\n (2) Queue\n (3) LinkedList")
        Stack.Traverse("")

        enter_choice = input(" Please enter your Choice: ")

        if enter_choice == "1":

            Stack.Traverse("- - - - - * * * * * * * - - - - - -")
            Stack.Traverse("  Welcome to STACK Data Structure  ")
            Stack.Traverse("- - - - - * * * * * * * - - - - - -")
            Stack.Traverse("")

            Stack.my_print()
            Stack.data_display()

        elif enter_choice == "2":

            Stack.Traverse("- - - - - * * * * * * * - - - - - -")
            Stack.Traverse("  Welcome to QUEUE Data Structure  ")
            Stack.Traverse("- - - - - * * * * * * * - - - - - -")
            Stack.Traverse("")

            Queue.my_print()
            Queue.data_display()

        elif enter_choice == "3":

            Node.Traverse("- - - - - * * * * * * * * * - - - - - -")
            Node.Traverse("  Welcome to LINKED LIST Data Structure  ")
            Node.Traverse("- - - - - * * * * * * * * * - - - - - -")
            Node.Traverse("")

            node = Node()
            node.display()
            print()
            node.show_oper()

        else:
            print("Invalid Choice")


# if __name__ == "__main__":
#     MainClass.main_function()

# Program starts here
# if __name__ == "__main__":
# obj = MainClass()
# obj.main_function()

