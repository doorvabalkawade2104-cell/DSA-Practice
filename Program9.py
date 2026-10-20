class solution:
    def traverse(self,head):
        result=[]
        temp=head

        while temp:
            result.append(temp,val)
            temp =temp.next
        return result
    
    def insertAtPosition(self,head,value,position):
        new_node =ListNode(value)

        if position == 0:
            new_node.next=head
            return new_node

        temp=head
        index=0

        while temp and index<position-1:
            temp=temp.next
            index +=1

        if temp is none:
            return head
        
        new_node.next =temp.next
        temp.next=new_node

    def middlenode(self,head):
        slow =head
        fast =head 

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def deleteNode(self,head,value):
        if head is None:
            return None
        if head.val==value:
            return head.next
        temp = head

        while temp.next:
            if temp.next.val == value:
                temp.next.val==temp.next.next
                break
            temp=temp.next
        return head

    def reverseList(self,head):
        prev=None
        curr=head

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev

    def sumConsecutive(self,head):
        result =[]
        temp=head
        while temp and temp.next:
            result.append(temp.val +temp.next.val)
            temp = temp.next
        return result

        print(result)