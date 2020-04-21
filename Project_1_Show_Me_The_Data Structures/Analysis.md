# Project1 - Show Me Data Structures

## Problem 1: LRU Cache
For the LRU_Cache problem, after thinking of using different approaches (included previous failures), it has been decided to use the `OrderedDict()`, specifically the use of the method `.popitem(last=False)`. It allows to remove the first added element, which is basic for the priority construction demanded.


In respects to the limitation of the cache, any hashing approach has been discarded, as the risk of collision, hence the necessity of adding a nested hash (reaching` O(n)`). Finally deciding for this approach that satisfies the `O(1)` requirement. As in therms of space complexity, the structure requires the usage of c, being c the desired LRU_Cache capacity; being it in the end assimilable to` O(n)`.

## Problem 2: File Recursion
For the Finding files problem , I decideed to use `recursion` .Using recursion here has a flexibiliy rather than any other.
Coming to the time complexity is dependns on the depth of the recursion(The leaf sub directory is d) and Number of files in each directory (n) then it is `O(nd)`.The space complexity is only the call stack nothing more than that. 


## Problem 3: Huffman Coding

The implementation of the Huffmann Algorithm, has consisted as pseudo code tasks were resolved, in the construction of several classes, being:

    Node
    Queue
    Tree
    HuffmanEncoder

This has allowed to have a more encapsulated development, as well as, providing the project with a more consistent structure. The compresing algorithm has shown, for the tested example a reduction of almost 50% of its size.


In respects to the study of the time complexity, would be O(Ln), being L the maximum length of a codeword; If I had not used a built it function for sorting the input that takes `O(n*log(n))`; ending up the time complexity being `O(n*log(n))`. In respects to the space complexity, it is directly related to the size of the employed alphabet, in this case k, resulting in `O(k)`.


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