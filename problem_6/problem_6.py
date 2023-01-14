class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, init=[]):
        self.head = None
        self.length = 0
        if init:
            self.append_iter(init)

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append_iter(self, list_values):
        for value in list_values:
            self.append(value)

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.length += 1
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        self.length += 1

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # This can be accomplished with Python sets and its union method assuming
    # our Linked List implememnts the __iter__ method. I opted for a more explicit
    # approach just in case this wasn't in the spirit of the challenge:
    # ans = set(llist_1).union(llist_2)
    # return LinkedList(ans)
    seen = set()
    ans = LinkedList()
    for element in llist_1:
        ans.append(element)
        seen.add(element)
    for element in llist_2:
        if element in seen:
            pass
        else:
            ans.append(element)
    return ans


def intersection(llist_1, llist_2):
    # This can be accomplished with Python sets and its intersection method assuming
    # our Linked List implememnts the __iter__ method. I opted for a more explicit
    # approach just in case this wasn't in the spirit of the challenge:
    # ans = set(llist_1).intersection(llist_2)
    # return LinkedList(ans)
    seen = set()
    ans = LinkedList()
    for element in llist_1:
        seen.add(element)
    for element in llist_2:
        if element in seen:
            ans.append(element)
    return ans


def union_test():
    a_llist = LinkedList([1, 2, 3])
    b_llist = LinkedList([2, 4, 5])
    expected = [1, 2, 3, 4, 5]
    ans = union(a_llist, b_llist)
    print(f"The union of {a_llist} and {b_llist} is: \n{ans}")
    return sorted(list(ans)) == sorted(expected)


def intersection_test():
    a_llist = LinkedList([1, 2, 3])
    b_llist = LinkedList([2, 4, 5])
    expected = [2]
    ans = intersection(a_llist, b_llist)
    print(f"The intersection of {a_llist} and {b_llist} is: \n{ans}")
    return sorted(list(ans)) == sorted(expected)


def union_and_intersection_of_equal_lists():
    a_llist = LinkedList([1, 2, 3])
    b_llist = LinkedList([1, 2, 3])
    expected = [1, 2, 3]
    u_ans = union(a_llist, b_llist)
    i_ans = intersection(a_llist, b_llist)
    print(f"The union of {a_llist} and {b_llist} is: \n{u_ans}")
    print(f"The intersection of {a_llist} and {b_llist} is: \n{i_ans}")
    return sorted(expected) == sorted(u_ans) and sorted(expected) == sorted(i_ans)


def intersection_with_an_empty_list():
    a_llist = LinkedList([1])
    b_llist = LinkedList()
    expected = []
    ans = intersection(a_llist, b_llist)
    print(f"The intersection of {a_llist} and {b_llist} is: \n{ans}")
    return sorted(expected) == sorted(list(ans))


def union_with_an_empty_list():
    a_llist = LinkedList([1, 2])
    b_llist = LinkedList()
    expected = [1, 2]
    ans = union(a_llist, b_llist)
    print(f"The union of {a_llist} and {b_llist} is: \n{ans}")
    return sorted(expected) == sorted(list(ans))


if __name__ == "__main__":
    print(union_test(), '\n')
    # The union of 1 -> 2 -> 3 ->  and 2 -> 4 -> 5 ->  is:
    # 1 -> 2 -> 3 -> 4 -> 5 ->
    # True
    print(intersection_test(), '\n')
    # The intersection of 1 -> 2 -> 3 ->  and 2 -> 4 -> 5 ->  is:
    # 2 ->
    # True
    print(union_and_intersection_of_equal_lists(), '\n')
    # The union of 1 -> 2 -> 3 ->  and 1 -> 2 -> 3 ->  is:
    # 1 -> 2 -> 3 ->
    # The intersection of 1 -> 2 -> 3 ->  and 1 -> 2 -> 3 ->  is:
    # 1 -> 2 -> 3 ->
    # True
    print(intersection_with_an_empty_list(), '\n')
    # The intersection of 1 ->  and  is:
    #
    # True
    print(union_with_an_empty_list(), '\n')
    # The union of 1 -> 2 ->  and  is:
    # 1 -> 2 ->
    # True
