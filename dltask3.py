import numpy as np

sampleNo = 100;
mu = 0.0
sigma = 0.1
s = np.random.normal(mu, sigma, sampleNo) #正太分布
print(s)

s[s < 0] = 0  #向量化，将<0的元素设置成0
print(s)
