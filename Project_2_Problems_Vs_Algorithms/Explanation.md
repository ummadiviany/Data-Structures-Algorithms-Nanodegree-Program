# Project-2 Problems Vs Algorithms

## Problem 1: Square Root of an Integer
The principle of this algorithm is to implement a variance of the binary search, due to the required time complexity.I started checking from `number//2` onwards if it is greater than required and again reducit it to ``//2`` until is less than the required value.then I have retured the value.Although I gone few more iterations to go that number by incrementing `+1` that is very small number so time complexity is  `O(log(n))` and space complexity is constant `O(1)`

## Problem 2: Search in a Rotated Sorted Array
The principle employed in this algorithms is based directly in the binary search algorithms, differently, to this implementations, in its structure, it has been decided to be employed a `more divide approach`, rather than computationally expensive on previous levels to spare some division; e.g. when the lists are of size 2, both values could have been checked (though this would have increased our time complexity).
The time complexity being an algorithm based on binary search is `O(log(n))`. The number of iterations we perform, i.e. recursive depth, follows the rule of `recursive_depth^2 = n`. Thus if we isolate the number of iterations in relation to the `input space (n)`, we obtain `log(n) = recursive_depth`. As for the space complexity is also `O(log(n))` because it uses the call stack to store the returned values.
## Problem 3: Rearrange Array Digits

To rearrange a list of digits into two large numbers I first reverse `merge sort` the list. Merge sort time complexity is `O(n log(n))` and puts the largest number at the front of the list. Then I simply iterate through the numbers, and add it to `first_num` or `second_num` and converting them into `ints`.

The time complexity is `O(2n log(n))` because we iterate through the list after it's merged, which simplifies to `O(n log(n))`. The space complexity of merge sort is `O(n)` with two lists created again after merging for a total of `O(3n)`, simplified to `O(n)`.
## Problem 4: Dutch National Flag Problem
The `Sort 012` is a fun algorithm. Space complexity is `O(1)` since only a few variables are used to keep track of indexes, and sorting is done in place. Time complexity is `O(n)` since we must iterate through each item of the array to determine whether to send a 0 to the front or a 2 to the back.

The way this algorithm works is by incrementing a front index (next_0) for found 0 integers, decrementing a rear index (next_2) for found 2 integers, and leaving 1 integers in place by incrementing the traversing index. Then you simply traverse the array, swapping numbers when applicable.

## Problem 5: Autocomplete with Tries
This problem is focused on the development of the of a `trie` a data structure derived from a tree, suited for a good ratio between time and space complexity.


For the `trie`, time complexity of searching and inserting from a trie depends on the length of the word `a` that’s being searched for, inserted, and the number of total words, `n`, making the runtime of these operations `O(a*n)`. Looking into the space complexity of a trie, the worst case, would be when we have a word (or words), with no common characters between them, hence having, a node for each letter. Resulting in a space complexity of `O(n)`.
## Problem 6: Unsorted Integer Array
Traversing the array of ints has a time complexity of O(n) and a space complexity of O(1). We iterate through each number in a list of integers, and we set two variables, min and max, which we will update as check the min and max of each number. If the current number is larger than the max, it becomes the new max. Similarly, if the current number is less than the min, it becomes the new min.
## Problem 7: Request Routing in a Web Server with a Trie
The RouteTrieNode and RouteTrie are similar to a regular TrieNode and Trie respectively. The main difference is the addition of a handler to the TrieNode. In the main Router, we initialize our routes with a RouteTrie, adding a "/" root route and our default `not found`  route handler. To add a handler or lookup a route, we simply call on the familiar functions of RouteTrie `insert` and `find` passing a list of paths already split by the backslash ("/").

The time and space complexity is depends on the length of the given ,we need to iterate over the paths to `insert` or  `find`.So the time complexity would be `O(n)`. Our `add_handler` splits a route by its words ("/") and simply traverses the node's children for any matches before inserting the new path. The `lookup` function also splits the route into a list of paths, using each path to traverse the node children in search of a match.

Therefore the space complexity depends on the No. of unique paths we store in the RouteTrie .So in the worst case it is also linear `O(n)` 