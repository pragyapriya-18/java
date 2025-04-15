def searching(self,value):
    position=0
    foound=0
    if self.head is None:
        print("the ll is notexists")
    else:
        temp=self.head
        while temp is not None:
            position=position+1
            if temp.value==value:
                print("element found at:",position)
                found=1
                temp=temp.next
            if found==0:
                print("element not found")