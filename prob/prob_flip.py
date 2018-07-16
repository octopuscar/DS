import math

def get_coin_probs(number_of_heads, number_of_flips=10):
    """
    gets the probability of a certain number of heads per number of flips, assumes order doesn't matter
    """
    
    num_total_outcomes = 2**number_of_flips #either heads or tails

    number_of_ways_to_choose = math.factorial(number_of_flips) / (math.factorial(number_of_heads) * math.factorial(number_of_flips - number_of_heads))

    prob_of_getting_num_heads = number_of_ways_to_choose / num_total_outcomes

    return(prob_of_getting_num_heads)


number_of_heads = [0,1,2,3,4,5,6,7,8,9,10]
prob_of_getting_num_heads = []

sum = 0

for n in number_of_heads:
    prob_of_getting_num_heads.append(get_coin_probs(n))
    print(n)
    print (prob_of_getting_num_heads)  #for number_of_flips = 10, probs are highest at number_of_heads = 5, and are symmetric (prob of all heads same as none), as expected.
    sum += prob_of_getting_num_heads

print(sum) #should sum to one and indeed it does

import matplotlib.pyplot as plt
plt.plot(number_of_heads, prob_of_getting_num_heads)
plt.savefig("/Users/aford/out_figs/prob.pdf")
#plt.show()
plt.close()
