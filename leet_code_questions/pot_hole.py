"""
You are given a task to fix potholes in a road. The road is described by a string S
consisting of N characters. Each character represents a single fragment of the road.
Character "." denotes a smooth surface and "X" denotes a pothole. For example, S =
"...xxx..xx" means that the road starts with three smooth fragments, followed by three
potholes, followed by two smooth fragments and ending with one pothole.

You can choose any number of consecutive potholes and fix all of them. Fixing a segment
consistiof K consecutive potholes costs K + 1. In the example above, fixing the first two
consecutive potholes costs 2 + 1 = 3 and fixing the last pothole costs 1 + 1 = 2. After
these fixes, the road would look like this: "......X...".

You are given a budget B. You can fix multiple segments containing potholes as long as
you fit in the budget. What is the maximum number of potholes you can fix?

Write a function:
class solution
1 public int solution(String S, int B) :
that, given the string S of length N and the integer B, returns the maximum number of
potholes that can be fixed.
Examples:
1. Given S = "...xxx..x....xxx" and B = 7, the function should return 5. You can start by fixing
the first three consecutive potholes for a cost of 4, obtaining the road: "........x....xxx". Then,
you can fix the last two potholes for a cost of 3, obtaining the road: "........x....x..."
The total cost is 7, which fits in the budget, and you fix 5 potholes in total.

2. Given S = "..xxxxx" and B = 4, the function should return 3. One way is to fix the middle
three potholes, which costs the whole budget and makes the road look as follows: "..x...x"
Alternatively, you could fix the first three potholes or the last three potholes.

3. Given S= "x.x.xxx...x" and B = 14, the function should return 6. You can fix all the
potholes, which costs 2 + 2 + 4 + 2 = 10, leaving you with the spare budget of 4. This fixes
the entire road.

4. Given S="..". and B = 5, the function should return 0. There are no potholes to fix.
"""

def solution(road, budget):
    l = len(road)
    consecutive_potholes = []

    i = 0
    while i < l:
        cnt = 0
        # count total potholes that occur in consecutive order
        while i < l and road[i] == 'X':
            cnt += 1  # count this pothole
            i += 1    # move to next 
        # if potholes are >= 0
        if cnt > 0:
            consecutive_potholes.append(cnt)
        if cnt == 0:
            i += 1
    print(consecutive_potholes)

    # sort in descending order
    consecutive_potholes = sorted(consecutive_potholes, reverse=True)

    print(consecutive_potholes)
    i = 0
    repaired = 0

    # iterate untill budget is over (we need budget to be at least 2 to repair 1 pothole)
    while budget > 1 and i < len(consecutive_potholes):
    # if all potholes are fixed then stop
        # if i == len(consecutive_potholes):
        #     break
        # find cost of repair for this patch of potholes
        cost = min(consecutive_potholes[i] + 1, budget)
        # update budget
        budget -= cost
        # total potholes repaired
        curr_repaired = (cost - 1)
        # add to total
        repaired += curr_repaired
        # update the potholes remaining
        consecutive_potholes[i] -= curr_repaired
        if consecutive_potholes[i] == 0:
            # move to next patch
            i += 1
  
    return repaired

roads = "..XXX.XX.XXX.XXX.XXXX"
budgets = 10

print(solution(roads, budgets))