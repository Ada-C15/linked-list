
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
    def get_first(self):
        """
        Note: No reference changes here, since we're just getting the value of a node

        Time Complexity: O(1)
        Space Complexity:  O(1)
        """

        # this one is pretty obvious but just have to remember that the list head is always
        # the first node unless the list is empty, in which case head is None
        if self.head is None:
            return None
        return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    def add_first(self, value):
        """
        Note: This method always results in 2 reference changes

        Time Complexity: O(1)
        Space Complexity:  O(1)
        """

        # 1. First create the node to be added, using the passed in value and 
        # the original list head for its next attribute
        # 2. Then reroute the head reference to this new node
        self.head = Node(value, self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    def search(self, value):
        """
        Note: 

        Time Complexity:  O(n)
        Space Complexity:  O(1)
        """
        # 1. If the list is empty, then we auto return False
        if self.head is None:
            return False

        # 2. If the list is one node, we just check the head value
        if self.head.next is None:
            return (self.head.value == value)

        # 3. If there are some nodes, start traversing the list beginning with the first node
        this_node = self.head
        # this loop will end when this_node is None
        while this_node:
            # Check if the values match and bail if they do
            if this_node.value == value:
                return True
            # If not, the next code becomes the current node 
            # Note that if this_node.next is equal to None, then this_node is set to None! 
            # and therefore breaks the loop. COOL HUH
            this_node = this_node.next 
        return False 

    # method that returns the length of the singly linked list
    def length(self):
        """
        Note: 

        Time Complexity: O(n)
        Space Complexity:  O(1)
        """
        # 1. The length is 0 if there is no head
        if not self.head:
            return 0

        # 2. So we for sure have at least some nodes, and can
        # just count through the list - starting with the head and going until we've reached
        # the last node
        count = 1

        this_node = self.head
        while this_node.next:
            count += 1
            # make sure to keep going to the next node!
            this_node = this_node.next 
        return count 

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    def get_at_index(self, index):
        """
        Note: 

        Time Complexity: O(n)
        Space Complexity: O(1) 
        """
        # 1. Return None of there is no head 
        if not self.head:
            return None

        # 2. Get length of list using previous method, then compare that to index value
        # and only check index if length > index
        this_node = self.head
        if self.length() > index:
            for i in range(index):
                this_node = this_node.next
            # once we've reached index, return that value
            return this_node.value

        # 3. If we get here, length must be < index, so return None 
        return None


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    def get_last(self):
        """
        Note:  

        Time Complexity: O(n)
        Space Complexity: 0(1)
        """
        # 1. The linked list is empty if there is no head 
        if self.head is None:
            return
        # 2. Now we're kind of stuck with traversing the list to find the last node, 
        # but oh well - that's life. 
        # 3. So we start with the head and iterate until the current node's `next`
        # is empty (=None), indicating we've reached the end of the list
        this_node = self.head

        while this_node.next:
            this_node = this_node.next
        # 4. once we've reached the end of the list, return the current node's value
        return this_node.value

    # method that inserts a given value as a new last node in the linked list
    def add_last(self, value):
        """
        Note: this method requires traversing the whole list, but we're just doing
        reassignments each time

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        last_node = Node(value)
        # 1. If the list is empty, just make the head our new node and bail
        if not self.head:
            self.head = last_node
            return 

        # 2. Have to find the last node, which will just be the head if 
        # there is only 1 node 
        this_node = self.head
        while this_node.next:
            this_node = this_node.next 

        # 3. Then create the node we want and reassign the last node's `next` to our new
        # node
        this_node.next = last_node
    

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        """
        Note: 

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None:
            return 

        # 1. if there is only one node, can just return self.head.value
        if self.head.next is None:
            return self.head.value

        # 2. Need to traverse over all of the nodes. Weeeee! Use a counter
        # to track the max value. i'm too tired to dry this up
        this_node = self.head
        max_value = self.head.value
        while this_node.next:
            if this_node.next.value > this_node.value:
                max_value = this_node.next.value
            this_node = this_node.next 

        # 3. return the value at the end
        return max_value

    # method to delete the first node found with specified value
    def delete(self, value):
        """
        Note: Changing one or two references regardless of list length

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # 1. can't delete a node if list is empty 
        if self.head is None:
            return 

        # 2. Start by checking the first node
        if self.head.value == value:
            # if the head value matches the specified value, delete the head
            # by reassigning the head reference to the subsequent node 
            # and then the garbage collector gobbles up the original head node
            # yum yum
            self.head = self.head.next
            return 

        # 3. If there are some nodes, start traversing the list 
        # to find the PREVIOUS node of the node to be deleted
        this_node = self.head 
        while this_node:
            if this_node.value == value:
                break
            previous_node = this_node
            this_node = this_node.next 

        # 4. if we got through the loop and this_node is None, 
        # then we didn't fond any matches
        if this_node is None:
            return

        # 5. Change the next of the previous node to UNLINK 
        previous_node.next = this_node.next


    # method to print all the values in the linked list
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    def reverse(self):
        """
        Note: 

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        previous_node = None
        this_node = self.head
        while this_node:
            next_node = this_node.next
            this_node.next = previous_node
            previous_node = this_node
            this_node = next_node
        self.head = previous_node

  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        """
        Note: 

        Time Complexity:
        Space Complexity: 
        """

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        """
        Note: 

        Time Complexity:
        Space Complexity: 
        """

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        """
        Note: 

        Time Complexity:
        Space Complexity: 
        """

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
