class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):

    in_any_of_one =set()

    head1=llist_1.head
    while head1:
        in_any_of_one.add(head1.value)
        head1=head1.next
    
    head2=llist_2.head
    while head2:
        in_any_of_one.add(head2.value)
        head2=head2.next
    in_any_of_one_ll=LinkedList()

    for val in in_any_of_one:
        in_any_of_one_ll.append(val)
    
    return in_any_of_one_ll

def intersection(llist_1, llist_2):

    in_both = LinkedList()
    head1=llist_1.head
    while head1:
        value1=head1.value
        head2=llist_2.head
        while head2:
            value2=head2.value
            if value1 == value2 :
                in_both.append(value1)
            head2=head2.next
        head1=head1.next

    return in_both


def test_union_intersection(element_1,element_2,ll_union,ll_intersection):
    set1 = set(element_1)
    set2 = set(element_2)

    set_union = set1.union(set2)
    set_intersection = set1.intersection(set2)

    if ll_union and set_union:
        head=ll_union.head
        while head:
            value=head.value
            if value not in set_union:
                return False
            head=head.next

    if ll_intersection and set_intersection:
        head=ll_intersection.head
        while head:
            value=head.value
            if value not in set_intersection:
                return False
            head=head.next
    return True

#-----------------------------------------------------------------------
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


ll_union = union(linked_list_1, linked_list_2)
ll_intersection = intersection(linked_list_1, linked_list_2)
print("\nTest Case 1")
print("    union", ll_union)
print("intersect", ll_intersection)

print("\nChecking against Python's union and intersection with sets...", end=" ")
print("Pass, yay!" if (test_union_intersection(element_1, element_2, ll_union, ll_intersection)) else "Fail, uh oh!")

#-----------------------------------------------------------------------
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

ll_union = union(linked_list_3, linked_list_4)
ll_intersection = intersection(linked_list_3, linked_list_4)
print("\nTest Case 1")
print("    union", ll_union)
print("intersect", ll_intersection)

print("\nChecking against Python's union and intersection with sets...", end=" ")
print("Pass, yay!" if (test_union_intersection(element_1, element_2, ll_union, ll_intersection)) else "Fail, uh oh!")


#-----------------------------------------------------------------------
# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [2, 4, 6, 8, 10]
element_2 = [1,3,5,7,9,11,13]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

ll_union = union(linked_list_5, linked_list_6)
ll_intersection = intersection(linked_list_5, linked_list_6)
print("\nTest Case 3")
print("    union", ll_union)
print("intersect", ll_intersection)

print("\nChecking against Python's union and intersection with sets...", end=" ")
print("Pass, yay!" if (test_union_intersection(element_1, element_2, ll_union, ll_intersection)) else "Fail, uh oh!")

#-----------------------------------------------------------------------
# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

ll_union = union(linked_list_7, linked_list_8)
ll_intersection = intersection(linked_list_7, linked_list_8)
print("\nTest Case 4")
print("    union", ll_union)
print("intersect", ll_intersection)

print("\nChecking against Python's union and intersection with sets...", end=" ")
print("Pass, yay!" if (test_union_intersection(element_1, element_2, ll_union, ll_intersection)) else "Fail, uh oh!")