# -----------------------------------------------------------------
# O N L Y  T O  T E S T RANDINT C L O S U R E T Y P E
# -----------------------------------------------------------------

import random
results_distribution = {k: 0 for k in range(30, 41)}

for num in range(500):
    # add rnd to distribution
    rnd = random.randint(30, 40)
    results_distribution[rnd] += 1

# return distribution
print(results_distribution.items())

