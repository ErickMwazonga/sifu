
def get_ith_item(head, i):
    if i < 0:
        raise ValueError('No negatives!!! 🐱')

    current_node = head
    current_position = 0

    while current_node:
        if current_position == i:
            return current_node

        current_node = current_node.next
        current_position += 1

    raise ValueError('Not Found')
