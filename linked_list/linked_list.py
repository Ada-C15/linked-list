
# Defines a node in the singly linked list
from typing import Counter


class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head == None:
            return None

        return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def length(self):
        length = 0
        current = self.head
        while current is not None:
            length+=1
            current=current.next
        return length


    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def get_at_index(self, index):
        if self.length()<index:
            return None
        
        current = self.head
        current_index=0
        while current is not None:
            if current_index == index:
                return current.value
            current = current.next
            current_index += 1

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        Current = self.head
        if Current is None:
            return None

        while Current.next != None:
            Current = Current.next
        return Current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)
        current = self.head
        if not self.head:
            self.add_first(value)
        else:
            while current.next != None:
                current = current.next
            current.next=new_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current = self.head
        if current == None:
            return None
        max = self.head.value
        
        while current != None:
            if current.value>max:
                max=current.value
            current = current.next
        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def delete(self, value):
        if not self.head:
            return None
        elif self.head.value == value:
            self.head=self.head.next
        else:
            current = self.head
            while current.next and current.next.value != value:
                current = current.next
            current.next = current.next.next

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def reverse(self):
        new_list = LinkedList()
        new_list.head = self.pop_last_node()
        curr = new_list.head

        if curr is not None:
            next_node = self.pop_last_node()
            while next_node:
                curr.next = next_node
                curr = curr.next
                next_node = self.pop_last_node()

        self.head = new_list.head

    def pop_last_node(self):
        if self.head == None:
            return None

        elif self.head.next == None:
            last_node = self.head
            self.head = None
            return last_node

        else:
            curr = self.head

            while curr is not None:
                if curr.next is None:
                    return curr
                elif curr.next.next is None:
                    last_node = curr.next
                    curr.next = None
                    return last_node
                curr = curr.next

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        middle = self.length()//2
        return self.get_at_index(middle)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        if not self.head or n >= self.size:
            return None
        
        idx = self.length()-1-n
        return self.get_at_index(idx)
        
        

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        s = set()
        current = self.head
        while current:
            if current in s:
                return True

            s.add(current)
            current = current.next
 
        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
