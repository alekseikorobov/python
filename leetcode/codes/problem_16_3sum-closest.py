
import types
from typing import List




class Solution:

    def get_middle_index(self, nums: List[int], target: int):        
        mid = 0
        print(f'{len(nums)=}')
        min_diff = abs(nums[0] - target)
        #print(f'{nums[0]=}, {target=}, {min_diff=}')
        for i in range(1,len(nums)):
            v = nums[i]
            min_diff_new = abs(v - target)
            #print(f'{v=}, {target=}, {min_diff_new=}')
            if min_diff_new < min_diff:
                min_diff = min_diff_new
                mid = i
        return mid

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        N = len(nums)        
        sum_res = float('inf')
        min_diff = abs(sum_res - target)
        for num1idx in range(0,N):
            num2idx = num1idx + 1
            num3idx = N - 1
            while num2idx < num3idx:
                sum_part = sum([nums[num1idx],nums[num2idx],nums[num3idx]])
                if sum_part == target:
                    return sum_part                
                min_diff_new = abs(sum_part - target)
                if min_diff_new < min_diff:
                    min_diff = min_diff_new
                    sum_res = sum_part
                elif sum_part > target:
                    num3idx -= 1
                else:
                    num2idx += 1
        return sum_res

                


    def threeSumClosest_2(self, nums: List[int], target: int) -> int:
        min_diff = -1
        res = -1
        complex = 0
        nums = sorted(nums, reverse=False)
        for a in range(0,len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(b+1,len(nums)):
                    complex += 1
                    s = sum([nums[a],nums[b],nums[c]])                    
                    #print(s)
                    if s == target:
                        return s
                    min_diff_new = abs(target - s)
                    if min_diff == -1:                       
                        res = s
                        min_diff = min_diff_new
                        print(min_diff,s)
                    elif min_diff_new < min_diff:
                        res = s
                        min_diff = min_diff_new
                        print(min_diff,s)
        print(f'{complex=}')
        return res

    def threeSumClosest_2(self, nums: List[int], target: int) -> int:
        min_diff = -1
        res = -1
        complex = 0
        nums = sorted(nums, reverse=False)
        for a in range(0,len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(b+1,len(nums)):
                    complex += 1
                    s = sum([nums[a],nums[b],nums[c]])                    
                    #print(s)
                    if s == target:
                        return s
                    min_diff_new = abs(target - s)
                    if min_diff == -1:                       
                        res = s
                        min_diff = min_diff_new
                        print(min_diff,s)
                    elif min_diff_new < min_diff:
                        res = s
                        min_diff = min_diff_new
                        print(min_diff,s)
        print(f'{complex=}')
        return res

    def threeSumClosest_1(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        min_diff = -1
        res = -1
        complex = 0
        for a in range(0,len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(b+1,len(nums)):
                    complex += 1
                    s = sum([nums[a],nums[b],nums[c]])
                    min_diff_new = abs(target - s)
                    if min_diff == -1:                        
                        res = s
                        min_diff = min_diff_new
                    elif min_diff_new < min_diff:
                        print(f'{a=} {b=} {c=} ({nums[a]=} {nums[b]=} {nums[c]=})')
                        res = s
                        min_diff = min_diff_new
        print(f'{complex=}')
        return res


s = Solution()

# print(s.threeSumClosest([-1,2,1,-4],1),2)
# print(s.threeSumClosest([0,0,0],1),0)
# print(s.threeSumClosest([-191,381,-998,-789,-658,-633,-250,-490,939,819,567,655,244,303,247,-639,-567,-777,180,-549,-580,-576,-40,-32,667,995,545,-817,836,686,-247,690,-210,517,-700,-403,-461,-610,-572,-736,-253,-455,-683,570,432,814,573,8,-987,818,-689,199,323,272,-638,212,115,480,586,-215,-320,596,-374,-366,539,-268,884,72,912,-726,455,-615,925,-861,983,-586,-269,-524,-753,384,-988,0,803,-233,296,-315,472,675,-595,-647,-810,92,-760,-573,431,181,174,93,5,288,10,-201,298,746,824,-767,994,640,-298,-163,185,352,-599,837,812,215,112,-804,-437,186,126,15,-248,-568,637,716,851,749,176,313,758,700,-249,715,666,423,987,-177,-21,687,594,-761,561,-221,25,-329,-336,475,-42,-155,-183,-160,-165,575,-487,773,-909,-926,75,-834,372,931,-129,171,-596,-635,727,786,-472,-350,516,48,595,-303,257,236,136,-229,-52,-41,657,-410,-811,-1,-31,59,555,-513,748,-855,875,-466,344,-153,770,-693,38,427,347,753,-731,892,326,466,-87,-80,-180,-357,-597,-363,-423,-646,530,-471,57,916,330,-408,-712,-975,904,54,328,-529,153]
# ,4549),2976)

# print(s.threeSumClosest([800,-56,-525,950,637,303,-960,-965,-915,686,566,-169,188,-286,-800,-753,-191,-473,317,368,-9,168,-193,340,-337,-668,-185,-138,-96,-995,-179,-8,-557,-168,-299,-438,311,208,-558,-734,-841,90,-508,531,-58,-666,803,836,-470,329,481,170,105,404,-737,160,990,540,865,-881,458,-630,-708,7,-857,23,539,871,479,-422,472,533,987,-502,-794,607,113,-843,365,-311,811,-768,-13,-905,-141,-512,-60,-722,847,-718,348,-342,936,-443,121,687,582,834,781,396,622,401,446,-528,-322,-878,-951,690,497,-556,525,-222,718,181,-587,-613,-706,984,-851,981,-118,841,165,835,-973,-241,-334,-457,-880,454,-214,971,443,-450,427,-497,-166,-358,184,-375,197,-352,-215,-147,-622,-590,-301,-724,-798,-79,934,-809,-149,532,722,868,-419,-67,-180,720,-712,307,813,621,-262,-68,-64,-914,576,604,-950,814,210,951,314,-789,-276,-779,-728,-409,-480,-440,-61,948,466,789,736,994,-546,812,327,-713,630,-201,691,692,-733,-785,301,-136,153,-403,155,-146,753,158,-730,-206,-836,-174,271]
# ,-5717),-2933)

#print(s.threeSumClosest([1,1,1,0],-100),2)

# print(s.threeSumClosest([13,252,-87,-431,-148,387,-290,572,-311,-721,222,673,538,919,483,-128,-518,7,-36,-840,233,-184,-541,522,-162,127,-935,-397,761,903,-217,543,906,-503,-826,-342,599,-726,960,-235,436,-91,-511,-793,-658,-143,-524,-609,-728,-734,273,-19,-10,630,-294,-453,149,-581,-405,984,154,-968,623,-631,384,-825,308,779,-7,617,221,394,151,-282,472,332,-5,-509,611,-116,113,672,-497,-182,307,-592,925,766,-62,237,-8,789,318,-314,-792,-632,-781,375,939,-304,-149,544,-742,663,484,802,616,501,-269,-458,-763,-950,-390,-816,683,-219,381,478,-129,602,-931,128,502,508,-565,-243,-695,-943,-987,-692,346,-13,-225,-740,-441,-112,658,855,-531,542,839,795,-664,404,-844,-164,-709,167,953,-941,-848,211,-75,792,-208,569,-647,-714,-76,-603,-852,-665,-897,-627,123,-177,-35,-519,-241,-711,-74,420,-2,-101,715,708,256,-307,466,-602,-636,990,857,70,590,-4,610,-151,196,-981,385,-689,-617,827,360,-959,-289,620,933,-522,597,-667,-882,524,181,-854,275,-600,453,-942,134]
# ,-2805),-2805)

print(s.threeSumClosest([-987 ,-981,-968,-959,-950,-943,-942,-941,-935,-931,-897,-882,-854,-852,-848,-844,-840]
,-2805),-2805)