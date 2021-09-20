# Defines a node in the singly linked list
class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value # details of node
        self.next = next_node # reference to next node (but not the details of that node themselves)
        #self.previous = previous_node # add this for doubly LLs # ""

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        # list starts off as empty
        self.head = None # keep the head private. Not accessible outside this class
        #self.tail = None # adding a tail to make get_last faster

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
        print('before: ', self.head)
        new_first = Node(value) # create new node
        new_first.next = self.head # but the new node's pointer on the orig first node
        self.head = new_first # afterwards, reassign the head value with the new node
        print('after: ', self.head.value) # no return statement if just adding, stop here for proof

    # method to find if the linked list contains a node with specified value
    def search(self, value):
        # traverse list looking for the node value
        # if you find it return it, otherwise return None
        # time complexity: O(N)
        # space complexity: O(1) no new data structures created
        current = self.head # start at first node
        if current == None:
            return False # empty list means return False, not None (tests)
        
        while current != None: # while current exists
            if current.value == value: # the the current node's value equals the one we're looking for
                return True #current
            else:
                current = current.next # move to the next one to check; right value?
        return False # if you get through the entire list and it's not there, return none (...False for tests..)
    
    # method that returns the length of the singly linked list
    def length(self):
        node_count = 0
        current = self.head

        while current != None:
            node_count += 1 # shasta pointer
            current = current.next # right logic? self.head.next?
            #node_count += 1 #>> up the counter here or above? doesnt seem to change the result
        print('length of ll: ', node_count)
        return node_count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    def get_at_index(self, index):
        current = self.head
        current_position = 0

        if not index:
            index == 0 # default value set to 0

        if index > (self.length() - 1): # DUPE MSG HERE
            print('None')
            return None

        while current:
            if current_position == index:
                print('current nodes value: ', current.value)
                return current.value
            print("NEXT:")
            current_position += 1
            current = current.next 
            print(">>>", current.value)

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: ?
    def get_last(self):
        current = self.head

        if not current:
            print('None')
            return None 

        while current:
            if current.next == None:
                print(current.value)
                return current.value
            print('Next! ')
            current = current.next 

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: ?
    def add_last(self, value):
        new_last = Node(value)
        if self.head == None:
            self.head = new_last
        #return 
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_last

    # method to return the max value in the linked list
    # returns the data value and not the node
    # LC NOTE: assuming "max" value means value with the longest number of chars...
    def find_max(self):
        current = self.head 
        max_ct = 0 # max char count var
        
        if not current: 
            return None

        while current != None:
            if max_ct < current.value:
                print('length of word: ', current.value)
                max_ct = current.value
            current = current.next
        print('for return: ', max_ct)
        return max_ct

    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    def delete(self, value):
        current = self.head

        if current != None:
            if current.value == value: # if the first node has the val we're looking for
                self.head = current.next # delete by first setting the 'head' to the 2nd node
                current = None # and secondly setting the old 'head' to None
                return # and break out of the func

        while current != None: # if we have to look through the rest of the list for this node
            if current.value == value: # compare each node's val to the target
                break # and break out if we find theyre equal
            prev = current # set prev var to the matching node
            current = current.next # move to the node following the matching node..........

    # if key was not present in linked list
        if current == None: 
            return # break out of the loop

        # ..........and unlink the node from list
        prev.next = current.next # by setting the node that followed the matching node to the new 'next val'
        current = None # and by setting the matching node to none

    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def visit(self): # built by chris/ada
        helper_list = [] # hold all node values for return
        current = self.head

        while current: 
            helper_list.append(str(current.value)) # append stringified node val to the other list
            current = current.next # move to the next node, lopping still we hit a None/list is traversed
        
        print(", ".join(helper_list)) # display finished product

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?
    def reverse(self): # hold var vals before switching
        previous = None # var to hold values as traversing begins
        current = self.head

        while current != None: 
            next = current.next # next set to current node's next node addr, to hold it
            current.next = previous # reassign actual current node's next node addr w None val (and then other node vals when traversing )
            previous = current # reassign previous var with current node value
            current = next # reassign current var with next node value 
        self.head = previous


## Advanced/ Exercises

# returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        pointer_one = self.head
        pointer_two = self.head 

        if self.head != None:
            while pointer_two != None and pointer_two.next != None:
                pointer_two = pointer_two.next.next # search node after next
                pointer_one = pointer_one.next # search next; functions as 'previous'
            print("Mid elem: ", pointer_one.value)
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