class stack:
    def __init__ (self,maxsize,top):
        self.maxsize=maxsize
        self.top=top
        self.list=[]

    def __str__ (self):
        values=self.list.reverse()
        values=[str(x)for x in self.list]
        return '\n'.join (values)
    
    def push(self,value):
        if self.top == self.maxsize:
            print("stack is full")
        else:
            self.list.append(value)
            self.top+=1
            print(value,"haas sbeen inserted")

    def pop (self):
        if self.top == -1:
            print("the stack is empty")
        else:
            print("popped item=",self.list.pop())
            self.top-=1

    def display(self):
        if self.top == -1:
            print("the stack is empty")
        else:
            print("contains of stack are:")
            print(self)

s = stack(4,-1)
s.push(10)
s.push(20)
s.display()
s.pop()
s.display()
 