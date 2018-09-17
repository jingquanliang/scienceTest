from scipy.misc import imread, imresize, imsave
import matplotlib.pyplot as plt
from skimage import transform,data

import os
import glob

a = 'C:\\Users\\Administrator\\Desktop'
# b = 'picture'
c = '*.jpg'

path = os.path.join(a,c)
print('path = ',path)

listglob = []
listglob = glob.glob(path)
# listglob.sort()
print(listglob)

print('---' * 30)

print('---' * 30)

I = imread('./cat.jpg')
print(I.shape)

I_tinted = I * (1, .95, .9)

# I_tinted = imresize(I_tinted, (300, 300))

I_trans = transform.resize(I, (300, 300))
print(type(I_trans))

# imsave('./cat_tinted.jpg', I_tinted)


# plt.subplot(1, 3, 1)
# plt.imshow(I)
# plt.axis('off')

# plt.subplot(1, 3, 2)
# plt.imshow(I_tinted)
# plt.axis('off')

# plt.subplot(1, 3, 3)
# plt.imshow(I_trans)
# plt.axis('off')

# plt.show()