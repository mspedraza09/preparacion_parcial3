class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_at_end(self, data): # Cambia el nombre para que sea claro
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        # NO cambies self.head aquí
    
    def display(self):
        if self.head is None:
            print("Empty list")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break
                                            
        print("(back to head)")
    
    def eliminar_descarte(self, k):
        current = self.head 
        i = 1
        while current != current.next:
            while i < k-1:
                current = current.next
                i += 1
            next_node = current.next 
            current.next = next_node.next 
            i = 1
            if next_node == self.head:
                self.head = next_node.next
            current = current.next
    
    def zigzag (self):
        current = self.head

        while current.next != None:
            next_node = current.next 
            current.next = next_node.next
            otro = next_node.next
            otro.next = next_node
            current = next_node
            


