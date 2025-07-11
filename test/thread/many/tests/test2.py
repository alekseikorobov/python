


#%%

import random
import matplotlib.pyplot as plt


plt.plot([1])

my_list = {
    i:0 for i in range(20)
}
my_list_1 = list(my_list)
for _ in range(200):
    i = random.choice(my_list_1)
    my_list[i] += 1

my_list
