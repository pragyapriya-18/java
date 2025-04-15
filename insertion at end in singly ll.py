def insert_end(self,data):
    new_node=Node(data)
    if self.head is None:
        self.head=new_node
        return
    last=self.head
    while(last.next):
        last=last.next
    last.next=new_node

    
