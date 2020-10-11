def addTwoNumbers(ListNode l1, ListNode l2):
    result_list = None
    head = None

    carry = 0

    while(l1 or l2):
        # Find the sum at that index
        _sum = 0
        if(l1 != None):
            _sum += l1.val
            l1 = l1.next
       
        if(l2 != None):
            _sum += l2.val
            l2 = l2.next
       
        _sum += carry

        # Create node with the remainder
        value  = _sum % 10
        carry = _sum // 10
        node = ListNode(value)

        # Add the newly created node in the result_list Linkedlist
        if(result_list is not None):
            result_list.next = node
            result_list = result_list.next
        else:
            result_list = head = node
        
    if carry > 0:
        result.next = ListNode(carry)

    return head