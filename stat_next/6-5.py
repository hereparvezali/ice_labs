import numpy as np
import scipy.stats as stats



sales = np.array([19.2, 18.4, 19.8, 20.2, 20.4, 19.0])
n = len(sales) # 6
x_bar = np.mean(sales) # 19.5
s = stats.tstd(sales) # 0.766
a = 10/100 # 0.1

##### a #####
# Hnot: miu = 20 and H1: miu != 20
miu = 20
t = (x_bar - miu)/(s/np.sqrt(n)) # -1.6
ppf = stats.norm.ppf(a/2) # |1.644|
# as t lies in the bound then the null hypothesis is failed to reject

##### b #####
# Hnot: miu = 20 and H1: miu > 20
t = t  # -1.6
ppf_r = stats.norm.ppf(1-a) # 1.28
pvalue_l = 2*(1-stats.t.cdf(abs(t),len(sales)-1))
# as t < ppf_r thus we fail to reject null hypothesis

##### c #####
# Hnot: miu = 20 and H1: miu < 20
t = t # -1.6
ppf_l = stats.norm.ppf(a) # -1.28
# as t < ppf_l thus we can reject the null hypthesis