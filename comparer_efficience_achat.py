# 36분할
# 0.5555% 간격
# 총투입금액 1억

import math

t = 36
proportion = [0] * t
for n in range(1, t + 1):
    proportion[n - 1] = 0.5 * n ** 2 - 0.5 * n + 1

somme = 100000000
Sv = Sq = 0
rn = []
for n in range(t):
    pn = 100 - 0.3333 * n
    qn = somme * proportion[n] / sum(proportion)
    vn = qn / pn
    print(int(qn))
    Sq += qn
    Sv += vn
    rn.append(Sq / Sv)

for r in rn:
    print(round(r, 4))
#import matplotlib.pyplot as plt
#import numpy as np

#plt.plot(np.arange(1, t + 1), rn, 'b-')
#plt.ylim(89, 101)
#plt.show()