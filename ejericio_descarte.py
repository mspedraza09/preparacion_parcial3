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
            
    def reverseKGroup(head, k):
        dummy = Node(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # 1. verificar si hay k nodos
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next

            # 2. invertir grupo
            prev = group_next
            current = group_prev.next

            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # 3. reconectar
            temp = group_prev.next
            group_prev.next = prev
            group_prev = temp

    def Josephus_multiple4(self, k,m):
        current = self.head
        i = 1
        while current != current.next:
            while i < m:
                current = current.next 
                i += 1
            if current.next.data % k == 0:
                    multiplo_k = current.next
                    current.next = multiplo_k.next
                    current = current.next
                    i = 1
                    if multiplo_k == self.head:
                        self.head = multiplo_k.next
            else:
                    next_node = current.next
                    current.next = next_node.next
                    i = 1
                if next_node == self.head:
                    self.head = next_node.next
            
            
            