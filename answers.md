# CMPS 2200 Assignment 3
## Answers

**Name:**________Joshua Sasson__________


Place all written answers from `assignment-03.md` here for easier grading.
1a.
start with the highest power of 2 coin that will allow one coin to be used, then move to the next highest and use the max amount of coins without going over
repeat until the total is the amount you need.

1b. 
greedy choice: use the highest coin value allowable the most amount of times possible is in the optimal solution
optimal substructure: Breaking a change amount down into smaller problems following the greedy choice 
and adding them together will create the optimal solution
Proof that the greedy choice can create optimal substructure by example
if I have to give change for 25 I can break it into two problems giving change for 16 (highest power of two) and 9 
then I can break 9 into two problems (8 highest power of 2 ) and 1
solving each of these individually and then combining them will give me the optimal answer.

1c.
work O(lg(k)) have to do a constant amount of work each iteration and the max amount of iterations is lg(k) where k is the lowest power of two that is greater than or equal to the amount of change  
Span O(lg(k)) same as work since I am doing it by an iterative process

2a. 
If I have to have change for 11 cents and I have the arbirary coins 7, 5, and 1
if I used the same greedy algorithm as before I would use one 7 and 4 ones leading to a total of 5 coins
The optimal solution is actually two 5 coins and one 1 coin for a total of 3 coins

2b. the optimal substructure property is that 
if I break down the problem into smaller problems and then solve those for the optimal solution the combined
results will be the optimal solution. 
For example breaking 11 into 6 and 5 leads to two results of 5,1 and 5 which is three coins and the optimal solution 

2c. 
The optimal solution is the minimum number of coins 
min(OPT(coin set, number of coins))
iterate through the coin set calling OPT(coin set -1, number of coins) untilt the lowest coin is reached
For the work, notice that the number of distinct subproblems is nk, and each minimization on the right hand side requires  𝑂(1)  work. This results in an overall work and span of O(nk) .
