# Data-Structures-Algorithms-Nanodegree-Program
My repository for Data Structures &amp; Algorithms Nanodegree Program


## Project 0:
 		__Run time analysis (Worst-Case Big-O Notation)__



### Task0:

	O(1)

	Explanation:Because there is only one statement to print.Its a one time operation



### Task1:

	O(2n)

	Explanation:I used a for loop for each record and inside it there are 2 set update operations.So for loop has O(n) and set update has O(1).There is another Loop for calls with the same time complexity.So total = O(n+1) + O(n+1) = O(2n) 



### Task2:

	O(4n^2)

	Explanation:I used a for loop and inside it there is another search opereation in the If statement so it contributes to (n^2) and another 3 If statements in the same loop so another 3*(n^2).Total = n(n+n+n+n) = O(4n^2)



### Task3:

	Total=O(2n)
	

	Explanation:

		Part A:	I used a for loop and inside it there is another search opereation with string search to find the wheather its starting with banglore area code or not.But they wont contribute much and doesnt grow the input as they are fixed length.Inside If statement there are 3 more if statements and as said they too wont contibute to time complexity.

		Part B:  There is one for and if condition inside so the time complexity is O(n) for this block.

			
		Part A:	O(n)

		Part B: O(n)
### Task4:
	O(2n)

	Explanation:There is one for loop in the for iterating over lists so O(n).and some set add operations so they are O(1) and ignore them. and in the second block there is one for loop and if condition inside.		
		Total:	O(n)+O(n)=O(2n)

