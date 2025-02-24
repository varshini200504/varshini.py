class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.start
            self.start = new_node
            return
        temp = self.start
        for _ in range(position - 1):
            if temp is None:
                raise IndexError("Position out of bounds")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_position(self, position):
        if self.start is None:
            raise IndexError("Position out of bounds")
        if position == 0:
            self.start = self.start.next
            return
        temp = self.start
        for _ in range(position - 1):
            if temp.next is None:
                raise IndexError("Position out of bounds")
            temp = temp.next
        if temp.next is None:
            raise IndexError("Position out of bounds")
        temp.next = temp.next.next

    def reverse(self):
        prev = None
        current = self.start
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.start = prev

    def print_list(self):
        temp = self.start
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    @staticmethod
    def merge(list1, list2):
        dummy = Node(0)
        tail = dummy
        p1 = list1.start
        p2 = list2.start
        while p1 is not None and p2 is not None:
            if p1.data < p2.data:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        tail.next = p1 if p1 is not None else p2
        merged_list = LinkedList()
        merged_list.start = dummy.next
        return merged_list

# Example usage:
ll = LinkedList()
ll.insert_at_position(3, 0)
ll.insert_at_position(1, 0)
ll.insert_at_position(2, 1)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None
ll.delete_at_position(1)
ll.print_list()  # Output: 1 -> 3 -> None
ll.reverse()
ll.print_list()  # Output: 3 -> 1 -> None

# Merging two lists
ll1 = LinkedList()
ll1.insert_at_position(1, 0)
ll1.insert_at_position(3, 1)
ll1.insert_at_position(5, 2)

ll2 = LinkedList()
ll2.insert_at_position(2, 0)
ll2.insert_at_position(4, 1)
ll2.insert_at_position(6, 2)

merged_ll = LinkedList.merge(ll1, ll2)
merged_ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
