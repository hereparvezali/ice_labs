import numpy as np
import scipy.stats as stats

dhaka = np.array([100,125,135,128,140,142,128,137,156,142])
chitta = np.array([95,87,100,75,110,105,85,95])

##### i #####
# Hnot: miu1=miu2 and H1: miu1!=miu2

n1,n2= len(dhaka),len(chitta)
df = n1+n2-2 # 16
a = 5/100
x1_bar = np.mean(dhaka) # 133.3
x2_bar = np.mean(chitta) # 94.0
s1 = stats.tstd(dhaka) # 14.76
s2 = stats.tstd(chitta) # 11.37
s=np.sqrt(((n1-1)*s1**2+(n2-1)*s2**2)/df) # 13.39

t = (x1_bar-x2_bar)/(s*np.sqrt(1/n1+1/n2)) # 6.18

ppf = stats.t.ppf(1-a/2,df) # 2.12
pvalue = (1-stats.t.cdf(np.abs(t),df))
# as t>ppf thus null hypothesis may be rejected at 5% level of significance so there is a significance difference between the traffic fines

##### ii #####
# Hnot: miu1=miu2 and H1: miu1>miu2
# t = t where t = 6.18
# in this case the t falls to the critical region also so the null hypothesis also rejected in 1% level of significance maybe
p_value_2 = 0.005 # as P(t>6.18)=0.005

