"""
Program that verfies my answer for 10a. This program randomly draws
two letters without replacement and checks whether one is a vowel
and the other is consonant. Then it computes the probability of this 
happening by repeating the experiment 10000 times.
"""

import random
import string

num_times = 0
times_ran = 10000

for y in range(times_ran):
    val1 = random.choice(string.ascii_lowercase)
    r = list(range(97, ord(val1))) + list(range(ord(val1) + 1, 123))
    val2 = chr(random.choice(r))
    
    if val1 in ('a', 'e', 'i', 'o', 'u'):
        if not val2 in ('a', 'e', 'i', 'o', 'u'):
            num_times += 1
            
    if not val1 in ('a', 'e', 'i', 'o', 'u'):
        if val2 in ('a', 'e', 'i', 'o', 'u'):
            num_times += 1
    

tot_prob = num_times / times_ran

print("The simulated probability that two letters randomly drawn" +
      " without replacement will be a vowel and a consonant " +
      "(where order does not matter) is " + str(tot_prob))

