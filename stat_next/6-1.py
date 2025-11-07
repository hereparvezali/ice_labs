import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

items = np.array([110, 118, 130, 140, 142, 146, 112,
                 100, 95, 98, 96, 122, 123, 124, 130])
n = 15
var = 300
a = 5/100

miu = 110  # Null hypothesis (Hnot)
# Alternative hypothesis miu != 110

##### a #####
x_bar = np.mean(items)

z = (x_bar - miu) / np.sqrt(var)*np.sqrt(n)  # 2.03

zt_low = stats.norm.ppf(a/2)  # -1.96
zt_high = stats.norm.ppf(1-a/2)  # 1.96
# as z is not in the bound of zt_low and zt_high since Hnot rejected

# P value
p_value = 2 * (1-stats.norm.cdf(z))  # 0.0426

##### b #####
# Null Hypothesis miu > 110 so,
# z is z where z = 2.03
zt_r = stats.norm.ppf(1-a)  # 1.645
p_value_r = 1 - stats.norm.cdf(z)  # 0.021
# as z falls in the critical region the Hnot rejected

##### c #####
# Null Hypothesis miu < 110 so,
# z is z where z = 2.03
zt_l = stats.norm.ppf(a) # -1.645
p_value_l = stats.norm.cdf(z) # 0.978
#  as the z value in accepted region then Hnot accepted

