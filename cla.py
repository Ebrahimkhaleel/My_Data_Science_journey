"""import math

# Calculate the number of combinations
n = 45
k = 22
combinations = math.comb(n, k)

print(f"The number of distinct groups of 22 people that can be promoted is: {combinations}")

# Calculate the probability
total_outcomes = 6 ** 6  # Total possible outcomes
favorable_outcomes = 1    # Favorable outcomes

probability = favorable_outcomes / total_outcomes
print(f"The probability is: {probability}")
# Probabilities
prob_fair_tails = 1 - 0.5  # Probability of fair coin tails
prob_bent_tails = 1 - 0.75  # Probability of bent coin tails

# Probability of both tails
prob_both_tails = prob_fair_tails * prob_bent_tails

# Probability of at least one head
prob_at_least_one_head = 1 - prob_both_tails
print(f"The probability of at least one head is: {prob_at_least_one_head}")"""
# Probabilities
prob_not_ring_given_fire = 1 / 10000
prob_fire = 1 / 1000
prob_not_ring_given_no_fire = 9889 / 10000
prob_no_fire = 9999 / 10000

# Probability that the fire alarm does not ring
prob_not_ring = (prob_not_ring_given_fire * prob_fire) + (prob_not_ring_given_no_fire * prob_no_fire)

# Conditional probability of fire given the fire alarm does not ring
prob_fire_given_not_ring = (prob_not_ring_given_fire * prob_fire) / prob_not_ring
print(f"The conditional probability of fire given the fire alarm does not ring is: {prob_fire_given_not_ring}")


