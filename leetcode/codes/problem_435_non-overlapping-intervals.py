#%%
import pandas as pd
import matplotlib.pyplot as plt

ax = plt.subplot()
intervals = [[1,2],[2,3],[3,4],[1,3]]
#intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,100],[11,22],[1,11],[2,12]]
intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]

intervals = sorted(intervals,key = lambda x: (x[1]))

intervals = [[i[0]+74,i[1]+74] for i in intervals]
print(intervals)
c = len(intervals)
for i,interval in enumerate(intervals):
    y = i+1
    ax.plot(interval,[y,y])
    ax.plot([interval[0],interval[0]],[0,c])
    ax.plot([interval[1],interval[1]],[0,c])
plt.show()
#%%
a_result = []
for i in range(0,len(intervals)):
    a,b = intervals[i]
    count = 0
    for j in range(i,len(intervals)):
        
        if i == j: continue
        
        a_new, b_new = intervals[j]

        if a_new < b:
            count+=1
    
    a_result.append(([a,b],count))
        
a_result


#%% - Solution


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals,key = lambda x: (x[1]))

        a,b = intervals[0]
        count_remove = 0
        for i in range(1,len(intervals)):
            a_new, b_new = intervals[i]

            if b > a_new:
                count_remove += 1
            else:
                b = b_new
                
        return count_remove


