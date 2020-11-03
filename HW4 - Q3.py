import time
import matplotlib.pyplot as plt
import random

# Modified from: https://www.educative.io/edpresso/binary-trees-in-python
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

binary_tree = Node(None)
hash_table = {}

hash_times = []
tree_times = []
list_lengths = []

range_list = [1, 10, 100, 1000, 10000, 100000, 400000, 800000]

for i in range_list:
    num_items = i
    list_lengths.append(num_items)
    insertion_random = []
    merge_random = []
    tim_random = []

    # Inserting into hash table
    hash_table = {}
    # measure time for merge sort on this list
    start2 = time.perf_counter()
    # put random values into each list
    for i in range(0, num_items):
        n = random.randint(0, 10000)
        hash_table[n] = 1
    end2 = time.perf_counter()
    hash_time = end2 - start2
    hash_times.append(hash_time)

    binary_tree = Node(None)
    start1 = time.perf_counter()
    # put random values into each list
    for i in range(0, num_items):
        n = random.randint(0, 10000)
        binary_tree.insert(n)
    end1 = time.perf_counter()
    tree_time = end1 - start1
    tree_times.append(tree_time)

plt.plot(list_lengths, tree_times, color="blue", label="Insertion Sort")
plt.plot(list_lengths, hash_times, color="olive", label="Merge Sort")
plt.xlabel('List lengths')
plt.ylabel('Time (sec)')
plt.show()




