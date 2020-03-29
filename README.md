# Data-Structures-Algorithms-Nanodegree-Program
My repository for Data Structures &amp; Algorithms Nanodegree Program


## Project 0:
 		__Run time analysis (Worst-Case Big-O Notation)__



### Task0:

	O(1)

	Explanation:Because there is only one statement to print.Its a one time operation



### Task1:

	O(4n^2)

	Explanation:I used a for loop and inside it there is another search opereation in the If statement so it contributes to (n^2) and another If statement in the same loop so another(n^2).They add up to n^2 + n^2 = 2n^2.There is one more for loop with run time 2n^2.So total = 2n^2 + 2n^2 = 4n^2 = n(n+n) + n(n+n) =4n^2



### Task2:

	O(4n^2)

	Explanation:I used a for loop and inside it there is another search opereation in the If statement so it contributes to (n^2) and another 3 If statements in the same loop so another 3*(n^2).Total = n(n+n+n+n) = O(4n^2)



### Task3:

	Total=O(66n^2+nlog(n)+22n)
	

	Explanation:I used a for loop and inside it there is another search opereation with string search in the If statement so it contributes to (11n^2) and another 5 If statements in the same loop so another 5*(11*n^2).

			maximum lenth of number =11 or 10 ~= 11
		Part A:	n(11*n+11*n+11*n+11*n+11*n+11*n)+nlog(n)=O(66n^2+nlog(n))

		Part B: n(11+11)=O(22n)

### Task4:

	O(11n+n^2)

	Explanation:There is one for loop in the for iterating over lists and string search codition to check the string.So it contributes to n*max_len(string) => n*11.After that there is one more for loop and search in the loop so it contributes to n*n=n^2
		
		Total:	n*(11)+n*n=11n+n^2=O(11n+n^2)