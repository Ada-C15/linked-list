
# Defines a node in the singly linked list
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node
#___________________________________________________
# Defines the singly linked list
# ___________________________________________________ 
class LinkedList:
    # Initialize (self)
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class
# ___________________________________________________
    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
# ___________________________________________________ 
    def get_first(self):  
        if self.head != None:
            return self.head.value
# ___________________________________________________        
    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: ? O(1)
    # Space Complexity: ? O(1)
# ___________________________________________________ 
    def add_first(self, value):  # OK - passed
        # it's a node with value
        first_node = Node(value)
        # points the node's next property to whatever the head is (which is none right now)
        first_node.next = self.head
        # this makes it the head to have that value, next becomes none as of right now 
        self.head  = first_node
        return first_node
# ___________________________________________________ 
    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    ## Time Complexity: O(n)
    ## Space Complexity: O(1)
# ___________________________________________________ 
    def search(self, value): # OK - passed
        current = self.head
        while current !=None:
            if current.value == value:
                return True
            current = current.next
        return False
# ___________________________________________________ 
    # method that returns the length of the singly linked list
    # Time Complexity:  O(n)
    # Space Complexity: ??? O(1) 
# ___________________________________________________ 
    def length(self): # OK - passed
        if self.head == None:
            return 0

        current = self.head
        count = 0
        while current !=None:
            count  +=1
            current = current.next
        return count
# ___________________________________________________ 
    # method returns value at a given index in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
# ___________________________________________________ 
    def get_at_index(self, index):  # OK - passed
        # if list is empty
        if not self.head:
            return None

        current = self.head
        current_i = 0

        # while node is not empty and while index hasn't reached the end of the list with index 
        while current and current_i < index:

            # and if index doesn't match the  current  
            if index != current_i:
                # go to next node and move index to that node
                current_i +=1
                current = current.next

        return current.value
# ___________________________________________________ 
    # method returns value of last node in linked list
    # returns None if linked list is empty
    # Time Complexity: O(n) - O(1)
    # Space Complexity: O(1)?
# ___________________________________________________ 
    def get_last(self): # OK - passed
        if self.head == None:
            return None
        current = self.head
        while current.next != None:
            current = current.next
        return current.value
# ___________________________________________________ 
    # method - inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    #  trying add last
# ___________________________________________________ 
    def add_last(self, value): # OK - passed

        last_node = Node(value)
        
        # if list is empty, add and node becomes head (can I call add first, if so how?)
        if self.head == None:
            # last_node = Node(value)
            last_node.next = self.head
            self.head = last_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = last_node
# ___________________________________________________         
    # method to return the max value in the linked list
    # returns the data value and not the node
# ___________________________________________________ 
    def find_max(self): # OK - passed
        # traverse the list until I find the max value
            # compare all nodes with first value 
            # if next node is bigger than previous, found current max
            # when finish comparing with all values in list, found max
        # if list is empty
        if self.head == None:
            return None

        # there is at least a first element in the list
        current_node = self.head
        max_value = current_node.value # assign that element as the max
        
        # while we haven't traversed throughout whole list
        while current_node != None: # there is something to compare with in the list with current element
            # compare max with current value 
            if max_value < current_node.value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
# ___________________________________________________ 
    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
# ___________________________________________________ 
    def delete(self, value): # OK - passed
        if not self.head:
            return
        current = self.head
        next_node = current.next

        # if value is at the head
        if current.value == value:
            self.head = next_node
            # garbage collector deletes hanging un - attached node
            return 
        
        # if value is from second node to end
        while next_node !=None:
            if next_node.value == value:
                # do the magic
                current.next = next_node.next
            # move to the next node
            current = current.next
            next_node = next_node.next
        return
# ___________________________________________________ 
    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
# ___________________________________________________ 
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))
# ___________________________________________________ 
    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?
# ___________________________________________________ 
    def reverse(self):
        if self.head == None:
            return None

        last = None
        current = self.head
        next_node = current.next

        while next_node !=None:
            current.next = last # last = none

            last = current
            current = next_node
            next_node = next_node.next

        # connect last node to previous node
        current.next = last # last = none
        # point head to last node (now the head)
        self.head = current
        
        return
# ___________________________________________________ 

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
# ___________________________________________________ 
    def find_middle_value(self):
        pass
# ___________________________________________________ 
    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
# ____________`_______________________________________ 
    def find_nth_from_end(self, n):
        pass
# ___________________________________________________ 
    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
# ___________________________________________________ 
    def has_cycle(self):
        pass
# ___________________________________________________ 

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
# ___________________________________________________ 
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
