import numpy as np
import matplotlib.pyplot as plt
import os
from skimage import io

# a)
print("# a)")
files = os.listdir("images")
filesArray = [np.load("images/" + files[i]) for i in range(0, len(files))]
images = np.array(filesArray)
print(images.shape)

# b)
print("# b)")
sum = 0
for image in images:
    sum += np.sum(image)
print(sum)
#sau
print(np.sum(images))

# c)
print("# c)")
for image in images:
    print(np.sum(image))


# d)
print("# d)")
maxIndex = -1
maxSum = max(np.sum(image) for image in images)
for idx,image in enumerate(images):
    if np.sum(image) == maxSum:
        maxIndex = idx

print(maxIndex)

# e)
print("# e)")
mean_image = np.mean(images, axis=0)
io.imshow(mean_image.astype(np.uint8))
io.show()

# f)
print("# f)")
sd = np.std(images)
print(sd)

# g)
print("# g)")
norm = (images - mean_image) / sd


# h)
print("# h)")
cut_images = images[:, 200:300, 280:400]
print(cut_images.shape)
