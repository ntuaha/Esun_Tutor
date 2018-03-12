import numpy as np

class ReLU:
    def __init__(self):
        self.mask = None
        
    def forward(self,x):
        self.mask = (x < 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    
    def backward(self,dout):
        dout[self.mask] = 0 
        dx = dout
        return dx

class Sigmoid:
    def __init__(self):
        self.y = 0
    
    def forward(self,x):
        self.y = 1 / (1+np.exp(x))
        return self.y
    
    def backward(self,dout):
        dx = dout * self.y * (1-self.y)
        return dx
    
class Affine:
    def __init__(self,W,b):       
        self.W = W
        self.b = b
        self.x = None
        self.original_x_shape = None
        self.dW = None
        self.db = None
        #print(self.W.shape)
        #print("++")
    
    def forward(self,x):
        #記得要讓x攤平
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        
        self.x = x
        out = np.dot(x,self.W) + self.b
        return out
    
    def backward(self,dout):
        self.db = np.sum(dout,axis = 0)
        self.dW = np.dot(self.x.T,dout)
        dx = np.dot(dout,self.W.T)
        dx = dx.reshape(*self.original_x_shape) 
        return dx

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

class SoftmaxWithLoss:
    def __init__(self):
        self.y = None
        self.t = None
        self.loss =None
        
    def forward(self,x,t):
        self.y = softmax(x)
        self.t = t
        self.loss = cross_entropy_error(self.y,t)
        return self.loss
    
    def backward(self,dout =1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t)/batch_size
        return dx

class SGD:
    def __init__(self,ln):
        self.ln = ln
    
    def update(self,params,grads):
        for key in params.keys():
            params[key] -= self.ln * grads[key]
        return params
            

if __name__ == "__main__":
    print("test")