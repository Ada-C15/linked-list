import math


# Defines a node in the singly linked list
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
        else:
            return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value, next_node=self.head)
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        length = 0
        current_node = self.head
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if self.head == None:
            return None

        current_index = 0
        current_node = self.head

        while current_index < index:
            if current_node.next == None:
                return None
            else:
                current_node = current_node.next
                current_index += 1

        return current_node.value

    # helper method
    def get_last_node(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        return current_node


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head == None:
            return None
        else:
            last_node = self.get_last_node()
            return last_node.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            last_node = self.get_last_node()
            last_node.next = Node(value)


    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time complexity: O(n)
    # Space complexity: O(1)
    def find_max(self):
        if self.head == None:
            return None
        else:
            max_value = self.head.value
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
                if current_node.value > max_value:
                    max_value = current_node.value
            return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.head == None:
            return None
        current_node = self.head

        # to delete first value
        if current_node.value == value:
            self.head = current_node.next
            return

        # to delete value in remainder of linked list
        while current_node.next != None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        return None


    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.length() < 2:
            return

        current_node = self.head
        while current_node.next != None:
            self.add_first(current_node.next.value)
            if current_node.next.next:
                current_node.next = current_node.next.next
            else:
                current_node.next = None
            

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        if self.head == None:
            return None
        else:
            length = self.length()
            middle = math.floor(length / 2)
            return self.get_at_index(middle)


    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        if self.head == None:
            return None

        length = self.length()
            
        if n > length - 1:
            return None

        nth_from_end = length - 1 - n
        return self.get_at_index(nth_from_end)


    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def has_cycle(self):
        if self.head == None:
            return False
        current_node = self.head
        nodes_checked = set()
        while current_node.next != None:
            if current_node in nodes_checked:
                return True
            nodes_checked.add(current_node)
            current_node = current_node.next
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
