class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next =next
       
    def append(self):
        curr = self.head

class linkedlist():
    def __init__(self):
        self.head =None
    def insert(self,data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next =newNode
        else:
            self.head = newNode
    def display(self):
        curr = self.head
        if curr:
            while curr:
                print(curr.data)
                curr = curr.next
        else:
            return -1
    # def delete(self):
    #     curr = self.head
    #     if curr:
    #         while curr:
    #             temp = curr
                
    def handle_request(self,data):
        self.insert(data)
        self.display()


if __name__ == "__main__":
    ll = linkedlist()
    result = ll.handle_request(18)
    print(result)