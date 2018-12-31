'''
Given a set of intervals L, find the min set of points
so that each inteval is covered at least once by 
a given point.

eg input: (1, 3), (2, 5), (3, 6)
output: 3

Algo:
    - sort intervals in increasing order
    - for interval in interval-set
        add interval endpoint to set of points
'''


def min_points(intervals):
    sorted_intvl = sorted(intervals, key=lambda x: x[1])

    points = [sorted_intvl[0][-1]]

    for interv in sorted_intvl:
        if not(points[-1] >= interv[0] and points[-1] <= interv[-1]):
            points.append(interv[-1])

    return points

pts = [[2, 5], [1, 3], [3, 6]] 
#print(min_points(pts))

pts = [[4, 7], [1, 3], [2, 5], [5, 6]]
#print(min_points(pts))



'''
Given an integer n, find maximum number of unique summands.

e.g: 
    input:n=8
    output: [1 + 2 + 5] = 3
'''
def max_summands(n):
    summands = []
    sum_summands = 0
    next_int = 1

    while sum_summands + next_int <= n:
        sum_summands += next_int
        summands.append(next_int)
        next_int += 1

    # show values
    print(n, summands)

    # calc number of summands in the list
    #summands[-1] += n - summands

    num_of_summands = len(summands)
    
    return num_of_summands

print(max_summands(8))

