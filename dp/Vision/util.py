import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from PIL import Image

mnist = datasets.fetch_mldata('MNIST original')


def load_data(size):
    mnist = datasets.fetch_mldata('MNIST original')
    s = mnist.data.shape[0]
    c = np.zeros(s)
    c[np.random.choice(s, size, replace=False)] = 1
    #n_train = size
    data_train = mnist.data[c == 1]
    target_train = mnist.target[c == 1]
    data_test = mnist.data[c == 0]
    target_test = mnist.target[c == 0]
    return (data_train.astype(np.float32), target_train.astype(np.float32), data_test.astype(np.float32), target_test.astype(np.float32))


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))


def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t)**2)


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


def one_hot_label(y, size):
    a = np.zeros([y.shape[0], size])
    for i in range(y.shape[0]):
        a[i, int(y[i])] = 1
    return a

#為了加速增加的
def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)
