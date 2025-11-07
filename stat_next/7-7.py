from scipy import stats
from numpy import array,mean

x = array([29, 32, 31, 32, 32, 29, 31, 30])
y = array([26, 27, 28, 27, 30, 26, 33, 36])
d = x-y
d_bar = mean(d)

d_d_bar = d-d_bar
d_d_bar_2 = d_d_bar**2

s = stats.tstd(d)

t = d_bar/s/