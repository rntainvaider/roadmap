class Node:
    def __init__(self, new_val) -> None:
        self.val = new_val
        self.next_node = None


class LinkedList:
    def __init__(self) -> None:
        self.count_elem = 0
        self.head = None  # Node(new_val=1)

    def __str__(self) -> str:
        if self.head:
            info = "|"
            cur_node = self.head
            while True:
                info += f" {cur_node.val},"
                if not cur_node.next_node:
                    break
                cur_node = cur_node.next_node

            return info[:-1] + " |"
        else:
            return "||"

    def append(self, obj) -> None:
        if not self.head:
            self.head = Node(new_val=obj)
        else:
            cur_node = self.head
            while True:
                if not cur_node.next_node:
                    cur_node.next_node = Node(new_val=obj)
                    break
                cur_node = cur_node.next_node
        self.count_elem += 1

    def pop(self) -> None:
        pass


n = Node(1)

my_list = LinkedList()
print(my_list)
my_list.append(22)
my_list.append(2)
my_list.append(3)
print(my_list)
