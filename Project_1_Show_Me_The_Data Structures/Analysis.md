# Project1 - Show Me Data Structures

## Problem 1: LRU Cache
For the LRU_Cache problem, after thinking of using different approaches (included previous failures), it has been decided to use the `OrderedDict()`, specifically the use of the method `.popitem(last=False)`. It allows to remove the first added element, which is basic for the priority construction demanded.


In respects to the limitation of the cache, any hashing approach has been discarded, as the risk of collision, hence the necessity of adding a nested hash (reaching` O(n)`). Finally deciding for this approach that satisfies the `O(1)` requirement. As in therms of space complexity, the structure requires the usage of c, being c the desired LRU_Cache capacity; being it in the end assimilable to` O(n)`.

## Problem 2: File Recursion
For the Finding files problem , I decideed to use `recursion` .Using recursion here has a flexibiliy rather than any other.
Coming to the time complexity is dependns on the depth of the recursion(The leaf sub directory is d) and Number of files in each directory (n) then it is `O(nd)`.The space complexity is only the call stack nothing more than that. 


## Problem 3: Huffman Coding
This was a difficult problem. Luckily YouTube and some fellow students helped me with understanding the algorithms involved.

My solution was to use Python's heapq library. To encode a string, we first count the frequency of each letter. I then make a binary tree by pulling the two smallest values off of the heap, and adding back my newly made node to the heap.

I then make a mapping from the tree, where I recursively add a '0' or a '1' to the prefix, and put that as the value for the map, where the key is the label or character from the tree.

To get the final encoding, I simply iterate over each key (or character) in the string and get the binary value from the map, and join it all together.

For decoding, we simply iterate over each "bit" in the binary string and append the value (label) while traversing the tree.

For Big O we loop over all characters, we then loop over all frequencies to make the heap. We also recurse through the tree when making the map of characters to binary code. So I believe our performance is `O(3n)`. For space complexity we use a dictionary, a heap, and a recursive call in makeMap, giving us Big `O(3n log n)`

## Problem 4: Active Directory
This problem is a bit unclear. I wasn't sure if it was asking us to find a user if nested within a group. But I solved for that since that could use recursion. If the user is in the group we return True. Else, for every group in the group we call our function again and search through users.

Coming to time complexity is recursion depth(All the sub directories.Deepest subdirectory `d`) and sub groups in each each we take `n` so it is` O(nd)` and space complexity is only call stack and that is depends on the depth of the recursion` O(d)`

## Problem 5: Blockchain
Our Blockchain problem is really just a node and a linked list. Each node in the list points to the next, while also storing the hash of itself, and its previous hash.

Since we merely iterate through a linked list, and do some hashing functions, the Big O for time should be a simple `O(1)`. And Big O for space is 1 for our hash sha and 1 for our linked list: `O(2n)`. Big O Notation Time: `O(1)` Space: `O(n)`

##  Problem 6: Union and Intersection
For the Union & Intersection problem we have to find the union of two Linked List and Intersection of two linked lists. It is very simple traversing over the linked list and adding elements to another linked list.
Time complexity for the union function is `O(3n)` and for intersection function is `O(n^2)`.Space complexity for union function is` O(2n)` and for intersection function is `O(n)` 