#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-02 10:18:16
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2, 1000)
y = x ** 2
plt.plot(x, y)
plt.fill_between(x, y, where=(y > 0), color='red', alpha=0.5)


N = 1000
points = [[xy[0] * 2, xy[1] * 4] for xy in np.random.rand(N, 2)]
plt.scatter([x[0] for x in points], [x[1] for x in points], s=5, c=np.random.rand(N), alpha=0.5)
plt.show()