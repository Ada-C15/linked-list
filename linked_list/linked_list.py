# Defines a node in the singly linked list
class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value 
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1); head's always first or None
    # Space Complexity: O(1); no new data structures created
    def get_first(self):
        if self.head == None:
            return None
        return self.head.value

    # method to add a new node with the specific data value in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def add_first(self, value):
        new_first = Node(value)
        new_first.next = self.head 
        self.head = new_first 

    # method to find if the linked list contains a node with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1) ?
    def search(self, value):
        current = self.head

        if current == None:
            return False 
        
        while current != None: 
            if current.value == value: 
                return True 
            else:
                current = current.next 
        return False
    
    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        node_count = 0
        current = self.head

        while current != None:
            node_count += 1 
            current = current.next 
        return node_count

    # method that returns the value at a given index in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        current = self.head
        current_position = 0

        if not index:
            index == 0

        if index > (self.length() - 1):
            return None

        while current:
            if current_position == index:
                return current.value
            current_position += 1
            current = current.next 

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        current = self.head

        if not current:
            return None 

        while current:
            if current.next == None:
                return current.value
            current = current.next 

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n) ?
    def add_last(self, value):
        new_last = Node(value)
        if self.head == None:
            self.head = new_last
        else:
            current = self.head

            while current.next != None:
                current = current.next
            current.next = new_last

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        current = self.head 
        max_ct = 0 # max char count var
        
        if not current: 
            return None

        while current != None:
            if max_ct < current.value:
                max_ct = current.value
            current = current.next
        return max_ct

    # method to delete the first node found with specified value
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def delete(self, value):
        current = self.head

        if current != None:
            if current.value == value: 
                self.head = current.next 
                current = None 
                return

        while current != None: 
            if current.value == value: 
                break 
            prev = current
            current = current.next

        if current == None: 
            return

        prev.next = current.next 
        current = None

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self): # built by chris/ada
        helper_list = []
        current = self.head

        while current: 
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(n) ?
    def reverse(self): 
        previous = None 
        current = self.head

        while current != None: 
            next = current.next 
            current.next = previous
            previous = current 
            current = next
        self.head = previous


## Advanced/ Exercises
# returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        pointer_one = self.head
        pointer_two = self.head 

        if self.head != None:
            while pointer_two != None and pointer_two.next != None:
                pointer_two = pointer_two.next.next 
                pointer_one = pointer_one.next 
            return pointer_one.value
    
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