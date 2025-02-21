class Node:
    def __init__(self):
        self.left=None
        self.data=0
        self.right=None

class Bst:
    def __init__(self):
        self.root=None
        print("an empty bst is created")

    def inorder(self,root):
        if self.root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
    def preorder(self,root):
        if self.root:
            print(root.data,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if self.root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=' ')            

    def add_node(self):
        data=int(input("enter data of the new node:"))
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        temp1=self.root
        temp2=None
        while temp1!=None:
            temp2=temp1
            if data<temp1.data:
                temp1=temp1.left
            else:
                temp1=temp1.right
        if data<temp2.data:
            temp2.left=node
        else:
            temp2.right=node
            
        

        
    def delete_node(self):
        if self.root is None:
            print("tree is empty")
            return
        data=int(input("enter data to be deleted:"))
        temp1=self.root
        temp2=None
        while temp1.data!=data:
            if data<temp1.data:
                temp1=temp1.left
            else:
                temp1=temp1.right
            temp2=temp1
        if temp1.left is None and temp1.right is None:
            del temp1.data

        elif temp.left is None:
            temp.root=temp.right
        elif temp.right is None:
            temp.root=temp.left
        else:

            
            
        print("data not found")
        
        
    
    
    def search(self):
        if self.root is None:
            print("tree is empty")
            return
        data=int(input("enter the data to be searched:"))
        temp=self.root
        level=1
        while temp!=None:
            if data==temp.data:
                print("data found at level ",level)
                return
            elif data<temp.data:
                temp=temp.left
            else:
                temp=temp.right
            level+=1
        print("data not found")

class Menu:
    def get_menu(self, bst):
        menu = {
            1 : bst.add_node,
            2 : bst.delete_node,
            3 : bst.inorder,
            4 : bst.preorder,
            5 : bst.postorder,
            6 : bst.search_node,
            7 : self.end_of_program
        }
        return menu
    
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def run_menu(self):
        bst = Bst()
        while True:
            choice = int(input('1:Add 2:Delete 3:InOrder 4:PreOrder 5:PostOrder 6:Search 7:Exit.  Your choice: '))
            menu = self.get_menu(bst)
            menu.get(choice, self.invalid_choice)()

def start_app():
    menu = Menu()
    menu.run_menu()

start_app()