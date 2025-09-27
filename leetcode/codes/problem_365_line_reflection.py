class Solution:
    def isSymmetric(self,points):
        
        points = sorted(points,key=lambda x:x[0])
        #print(points)
        
        l = 0
        r = len(points)-1    
        while l < r:
            point_l = points[l]
            point_r = points[r]
            if not (point_l[1] == point_r[1] or point_l[0] - point_r[0] == 0):
                return False
            
            l +=1
            r -= 1
            
        return True
    
points = [
  [1, 2], [0, -3], [-1, 2], [5, 2],
  [2, 0], [4, -3], [3, 2],
]
s = Solution()
print(s.isSymmetric(points))


points = [
  [1,1],
  [-1,1],
]
s = Solution()
print(s.isSymmetric(points))


points = [
  [1,1],
  [-1,-1],
]
s = Solution()
print(s.isSymmetric(points))