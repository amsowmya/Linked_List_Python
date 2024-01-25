from linked_list import LinkedList

my_linked_list = LinkedList()
my_linked_list.insert_node(8)
my_linked_list.insert_node(3)
my_linked_list.insert_node(6)
my_linked_list.insert_node(16)

print(my_linked_list.head.next.next.next.value)

my_linked_list.print_list_items()

node_count = my_linked_list.count_nodes()
print(node_count)

node_counts = my_linked_list.count_nodes_in_list()
print(node_counts)

print(my_linked_list.find_node(160))

print(my_linked_list.delete_node(6))
print(my_linked_list.delete_node(16))

my_linked_list.print_list_items()