# Project1 - Show Me Data Structures

## Problem 1: LRU Cache
For the LRU_Cache problem, after thinking of using different approaches (included previous failures), it has been decided to use the `OrderedDict()`, specifically the use of the method `.popitem(last=False)`. It allows to remove the first added element, which is basic for the priority construction demanded.


In respects to the limitation of the cache, any hashing approach has been discarded, as the risk of collision, hence the necessity of adding a nested hash (reaching` O(n)`). Finally deciding for this approach that satisfies the `O(1)` requirement. As in therms of space complexity, the structure requires the usage of c, being c the desired LRU_Cache capacity; being it in the end assimilable to` O(n)`.

## Problem 2: File Recursion
For the Finding files problem , I decideed to use `recursion` .Using recursion here has a flexibiliy rather than any other.
Coming to the time complexity is dependns on the depth of the recursion(The leaf sub directory is d) and Number of files in each directory (n) then it is `O(nd)`.The space complexity is only the call stack nothing more than that. 


## Problem 3: Huffman Coding

For this Huffman Coding problem I decided to use a min heap to allow for easy merging of the frequency nodes. I used Pythons heapq library to make the addition and removal of nodes easier.

The time complexity of encode() is `O(nlogn)` Reason: make_frequency_dict takes` O(n)` time, min_heapify_dict takes `O(n)` time, merge_nodes takes `O(logn)`, make_codes takes `O(n)`, get_encoded_text takes `O(n)`. These all result in a complexity of nlogn

The space complexity of encode() is `O(n)` Reason: n is the size of the string. There is a linear space complexity.

The time complexity of decode() is `O(n)` Reason: There is a for loop going through each character in the encoded_text

The space complexity of decode() is `O(1)` Reason: Only one variable is allocated


## Problem 4: Active Directory
This problem is a bit unclear. I wasn't sure if it was asking us to find a user if nested within a group. But I solved for that since that could use recursion. If the user is in the group we return True. Else, for every group in the group we call our function again and search through users.

Coming to time complexity is recursion depth(All the sub directories.Deepest subdirectory `d`) and sub groups in each each we take `n` so it is` O(nd)` and space complexity is only call stack and that is depends on the depth of the recursion` O(d)`

## Problem 5: Blockchain
Our Blockchain problem is really just a node and a linked list. Each node in the list points to the next, while also storing the hash of itself, and its previous hash.

Since we merely iterate through a linked list, and do some hashing functions, the Big O for time should be a simple `O(1)`. And Big O for space is 1 for our hash sha and 1 for our linked list: `O(2n)`. Big O Notation Time: `O(1)` Space: `O(n)` .So the `n` is here no of blocks in blockchain.

##  Problem 6: Union and Intersection
For the Union & Intersection problem we have to find the union of two Linked List and Intersection of two linked lists. It is very simple traversing over the linked list and adding elements to another linked list.
Lets assume If Linked List 1 has n elements,Lets assume If Linked List 2 has m elements,

Time complexity for the union function is `O(n+m+max(n,m))` and for intersection function is `O(n*m)`.Space complexity for union function is` O(max(n,m))` and for intersection function is `O(min(n,m))` 