"""
Program that verfies my answer for 11a. This program randomly draws
50 integer letter equivalent values and checks to see if there is
at least one pair of students with the same birthday. Then it computes
the probability of this happening by repeating the experiment 10000 times.
"""
import numpy as np
from collections import Counter

num_ppl = 50
num_dup = 0
times_ran = 100000

for y in range(times_ran):
    vals = np.random.randint(1, 365, num_ppl)
    count_dup = Counter(vals)
    
    for x in range(1,366):
        if(count_dup[x] > 1):
            num_dup += 1
            break
    
tot_prob = num_dup / times_ran

print("The simulated probability that there will be at least" +
      " one pair of students having the same birthday is " +
      str(tot_prob))

