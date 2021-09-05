
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
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        self.head = Node(value, self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head

        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        i = 0 
        current = self.head
        while current != None:
            current = current.next
            i += 1
        return i 

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if self.length() < index:
            return None
        
        current = self.head
        current_index = 0 
        while current != None:
            if current_index == index:
                return current.value
            current = current.next
            current_index += 1 

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head == None:
            return None

        current = self.head
        while current.next != None:
            current = current.next
        
        return current.value


    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return self.head.value
        
        current = self.head
        while current.next != None:
            current = current.next
        
        current.next = new_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    #time : O(n)
    #Space : O(1)
    def find_max(self):
        if self.head == None:
            return None

        max_val = self.head.value
        current = self.head.next

        while current != None:
            if max_val < current.value:
                max_val = current.value
            current = current.value
        
        return max_val

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.head == None:
            return None
        
        if self.head.value == value:
            self.head = self.head.next
            return
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    return
            current = current.next

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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.head == None:
            return None
        
        current = self.head
        previous = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        self.head = previous
        return self.head
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def find_middle_value(self):
        ll_length = self.length()
        mid_index = int(ll_length/2)
        mid_value = self.get_at_index(mid_index)
        return mid_value


    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

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