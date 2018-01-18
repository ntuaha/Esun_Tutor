from TwoLayer import TwoLayerNet
from util import *
import pickle

def fix(x_train, t_train, x_test, t_test):
    return x_train / 255.0, one_hot_label(t_train, 10), x_test / 255.0, one_hot_label(t_test, 10)



def main():
  net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

  #修改輸入的值 preprocessing
  (x_train, t_train, x_test, t_test) = load_data(10000)
  (x_train_aha, t_train_aha, x_test_aha, t_test_aha) = fix(x_train, t_train, x_test, t_test)
  print(x_train_aha.shape)
  print(t_train_aha.shape)
  print(x_test_aha.shape)
  print(t_test_aha.shape)

  # meta parameter
  iters_num = 10000
  train_size = x_train.shape[0]
  batch_size = 100
  learning_rate = 0.1

  network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

  train_acc_list = []
  test_acc_list = []
  train_loss_list = []
  iter_per_epoch = max(train_size / batch_size, 1)
  for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train_aha[batch_mask]
    t_batch = t_train_aha[batch_mask]

    #計算梯度
    #grad = network.numerical_gradient(x_batch,t_batch) 好慢啊
    grad = network.gradient(x_batch, t_batch)

    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train_aha, t_train_aha)
        test_acc = network.accuracy(x_test_aha, t_test_aha)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc | %f , %f" % (train_acc, test_acc))
  plot(train_acc_list, test_acc_list)
  network.train_acc_list = train_acc_list
  network.test_acc_list = test_acc_list
  save(network)

def save(network):
  pickle.dump(network, open("network.pkl", "wb"))

def plot(train_acc_list, test_acc_list):
  markers = {'train': 'o', 'test': 's'}
  x = np.arange(len(train_acc_list))
  plt.plot(x, train_acc_list, label='train acc')
  plt.plot(x, test_acc_list, label='test acc', linestyle='--')
  plt.xlabel("epochs")
  plt.ylabel("accuracy")
  plt.ylim(0, 1.0)
  plt.legend(loc='lower right')
  plt.show()

if __name__ == "__main__":
  main()
