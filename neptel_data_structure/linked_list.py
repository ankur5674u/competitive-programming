class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR 'Get' : Index out of range!")
            return None
        cur_node = self.head
        cur_id = 0
        while True:
            cur_node = cur_node.next
            if cur_id == index: return cur_node.data
            cur_id += 1

    def erase_index(self, index):
        if index >= self.length():
            print("ERROR 'Get' : Index out of range!")
            return None
        cur_node = self.head
        cur_id = 0
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_id == index:
                last_node.next = cur_node.next
                return
            cur_id += 1


if __name__ == '__main__':
    my_list = linked_list()
    my_list.display()
    my_list.append(1)
    my_list.append(2)
    my_list.length()
    my_list.get(1)
    my_list.erase_index(1)
