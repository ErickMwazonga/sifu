class Node:
    '''Node in linked list'''

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
    
    def display(self):
        current_node = self
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

def size(head):
    if not head:
        return 0
    return  1 + size(head.next)
    
def get_tail(head):
    current_node = head

    while(current_node.next):
        current_node = current_node.next
    return current_node


def get_nth(head, idx):
    num_of_nodes = 1
    current_node = head

    while(current_node):
        if num_of_nodes == idx:
            break
        current_node = current_node.next
        num_of_nodes += 1

    # while(num_of_nodes < 3):
    #     current_node = current_node.next
    #     num_of_nodes += 1
    
    return current_node

def insert_nth(head, index, data):
    num_of_nodes = 1
    current_node = head

    # Insert to empty list
    if not head:
        return Node(data)

    # Prepend node - Set new head 
    if index == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node

    while(current_node):
        if num_of_nodes == index:
            inserted_node = Node(data)
            inserted_node.next = current_node.next 
            current_node.next = inserted_node
            break

        current_node = current_node.next 
        num_of_nodes += 1

    if not current_node:
        raise Exception()

    return head

def delete_nth(head, index):
    if index == 0:
        new_head = head.next
        head.next = None
        return new_head

    num_of_nodes = 1
    current_node = head
    
    while(current_node):
        if num_of_nodes == index:
            to_delete = current_node.next
            current_node.next = to_delete.next

            # if to_delete:
            #     current_node.next = to_delete.next
            # else:
            #     current_node.next = None
            break

        current_node = current_node.next 
        num_of_nodes += 1
    
    return head


node1 = Node(4)
node2 = Node(7)
node3 = Node(5)
node4 = Node(10)
node5 = Node(12)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# print('3rd nde', insert_nth(node1, 3, 10))
# print(insert_nth(node1, 2, 20))
# insert_nth(node1, 13, 20)
# print(node1.display())

# tail = get_tail(node1)
# print(tail)

# a = delete_nth(node1, 4)
# print(a.display())

print(size(node1))