#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-02 10:18:16
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

npoints = 1000 # 抽取1000个m维球内均匀分布的点
plt.figure(figsize=(20, 4))
for i, m in enumerate((2, 3, 5, 8)):
    # 这里模拟m维球中的均匀分布用到了拒绝采样，即先生成m维立方中的均匀分布，再剔除m维球外部的点
    accepts = []
    while len(accepts) < 1000:
        points = np.random.rand(500, m)
        accepts.extend([d for d in norm(points, axis=1) if d <= 1.0]) # 拒绝采样
        # print(type(accepts))
    accepts = accepts[:npoints]
    ax = plt.subplot(1, 4, i+1)
    ax.set_xlabel('distance') # x轴表示点到圆心的距离
    if i == 0:
        ax.set_ylabel('count') # y轴表示点的数量
    ax.hist(accepts, bins=np.linspace(0., 1., 50), color='green')
    ax.set_title('m={0}'.format(str(m)), loc='left')
plt.show()