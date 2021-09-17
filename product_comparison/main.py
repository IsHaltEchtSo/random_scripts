"""
THIS SCRIPT IS USED TO INSERT COSTS OF PRODUCT AND FRIGHT
TO DETERMINE WHERE TO BUY FOR A CERTAIN QUANTITY
"""
import matplotlib.pyplot as plt
from data import *

PRODUCT_RANGE = [amount for amount in range(1, MAXIMUM_PRODUCT_AMOUNT + 1)]

COMPARISON_INFORMATION = [
    {"website": website1, "p_cost": p_cost1, "f_cost": f_cost1},
    {"website": website2, "p_cost": p_cost2, "f_cost": f_cost2},
    {"website": website3, "p_cost": p_cost3, "f_cost": f_cost3},
    {"website": website4, "p_cost": p_cost4, "f_cost": f_cost4},
    {"website": website5, "p_cost": p_cost5, "f_cost": f_cost5},
]

# calculate the cost for each provider & product_amount
comparison_data = {}
for provider in COMPARISON_INFORMATION:
    comparison_data[provider["website"]] = [
        (provider["p_cost"] * product_amount + provider["f_cost"]) for product_amount in PRODUCT_RANGE
    ]

# plot the calculations
for provider, cost in comparison_data.items():
    plt.plot(PRODUCT_RANGE, cost)

# add legend
plt.legend([provider["website"] for provider in COMPARISON_INFORMATION])
plt.show()
