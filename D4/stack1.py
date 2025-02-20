import sys
class Stack:
    def __init__(self,size=5):
        self.stk=[]
        self.size=size
        print('empty stack is created')
    def push(self):
        if len(self.stk)==self.size:
            print("stack overflow")
        else:
            element=input("enter the element to b pushed:")
            self.stk.insert(0,element)
    def pop(self):
        if not self.stk:
            print("stack is empty")
        else:
            print("popped element is",self.stk[0])
            del self.stk[0]
#isempty isfull top element do these operations
    def display(self):
        if not self.stk:
            print("stack is empty")
        else:
            print('the stack is:',self.stk)
class Menu:
    def get_menu(self,stack):
        menu={
            1:stack.push,
            2:stack.pop,
            3:stack.display,
            4:self.end_of_program
        }
        return menu
    def invalid_choice(self):
        print("invalid choice entered")
    def end_of_program(self):
        sys.exit('end of program')
    def run_menu(self):
        stack=Stack()
        while True:
            choice=int(input("1.push 2.pop 3.display 4.exit your choice:"))
            menu=self.get_menu(stack)
            menu.get(choice,self.invalid_choice)()
menu=Menu()
menu.run_menu()
#do stack end,queue front and end
