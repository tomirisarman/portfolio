import math
import numpy as np
import operator
from skimage.transform import resize
from skimage.io import imread


def euclidianDistance(image, test_image):
    summa = 0
    for row in range(len(image)):
        for pixel in range(len(image[row])):
            summa += (image[row][pixel] - test_image[row][pixel]) ** 2
    distance = math.sqrt(summa)
    return distance


def createDatabase(imageFolder):
    training = {}
    for index in range(1, 41):
        image = imread(imageFolder + "/" + str(index) + ".jpg", as_gray=True)
        image = resize(image, (64, 128))
        training[str(index) + ".jpg"] = np.array(image).tolist()

    for index in range(1, 41):
        image = imread(imageFolder + "/" + "horse" + "%.3d" % index + ".jpg", as_gray=True)
        image = resize(image, (64, 128))
        training["horse" + "%.3d" % index + ".jpg"] = np.array(image).tolist()
    return training


def findNeighbors(img, training):
    test_image = imread('test set/' + img + '.jpg', as_gray=True)
    test_image = resize(test_image, (64, 128))
    test_image = np.array(test_image).tolist()

    distances = {}
    for iname in training:
        image = training[iname]
        d = euclidianDistance(image, test_image)
        distances[iname] = d

    sorted_distances = sorted(distances.items(), key=operator.itemgetter(1))
    return sorted_distances


def classifyImage(k, image_name, distances_list):
    predict_horse = 0
    predict_not = 0
    print("\nTest image: " + image_name + ".jpg")
    for i in range(0, k):
        # print(dist_list[i][0] + ':' + str(dist_list[i][1]))
        if 'horse' in distances_list[i][0]:
            predict_horse += 1
        else:
            predict_not += 1
    if predict_horse > predict_not:
        print("Seems like it is a horse")
        if 'horse' in image_name:
            return 1
        else:
            return 0
    else:
        print("Seems like it is NOT a horse")
        if 'horse' in image_name:
            return 0
        else:
            return 1


tr = createDatabase('train set')
correct = 0
k = 7
for i in range(58, 73):
    name = str(i)
    dist_list = findNeighbors(name, tr)
    correct += classifyImage(k, name, dist_list)

for i in range(219, 236):
    if i == 224 or i == 233:
        continue
    name = 'horse'+str(i)
    dist_list = findNeighbors(name, tr)
    correct += classifyImage(k, name, dist_list)

print("\n", correct, " correct predictions out of 30 test images")
accuracy = correct / 30 * 100
print("\nClassification accuracy: ", "%.2f" % accuracy, "%")






"""
k = 7
correct = 0
tr = createDatabase('train set')
for i in range(58, 73):
    dist_list = classifyImage('test set/' + str(i) + '.jpg', tr)
    predict_horse = 0
    predict_not = 0
    print("\nTest image: " + str(i) + ".jpg")
    for i in range(0, k):
        # print(dist_list[i][0] + ':' + str(dist_list[i][1]))
        if 'horse' in dist_list[i][0]:
            predict_horse += 1
        else:
            predict_not += 1
    if predict_horse > predict_not:
        print("Seems like it is a horse")
    else:
        print("Seems like it is NOT a horse")
        correct += 1

for i in range(219, 236):
    if i == 224 or i == 233:
        continue
    dist_list = classifyImage('test set/horse' + str(i) + '.jpg', tr)
    predict_horse = 0
    predict_not = 0
    print("\nTest image: horse" + str(i) + ".jpg")
    for i in range(0, k):
        # print(dist_list[i][0] + ':' + str(dist_list[i][1]))
        if 'horse' in dist_list[i][0]:
            predict_horse += 1
        else:
            predict_not += 1
    if predict_horse > predict_not:
        print("Seems like it is a horse")
        correct += 1
    else:
        print("Seems like it is NOT a horse")

print("\n", correct, " correct predictions out of 30 test images")
accuracy = correct / 30 * 100
print("\nClassification accuracy: ", "%.2f" % accuracy, "%")

"""

