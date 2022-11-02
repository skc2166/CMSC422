from imports import *
import matplotlib.pyplot as plt

epochs = [1, 2, 4, 8, 16, 32]
data = datasets.SentimentData
plt.xlabel('# of epochs')
plt.ylabel('train/test accuracy')
plt.title('number of epochs vs train/test accuracy')
train_acc = []
test_acc = []
for x in epochs:
    # distances = computeDistancesSubdims(datasets.DigitData.Xall, d)
    train, test, _ = runClassifier.trainTest(perceptron.Perceptron({'numEpoch': x}), data.X, data.Y, data.Xte, data.Yte)
    print("current step at %d" % (x))
    train_acc.append(train)
    test_acc.append(test)
plt.plot(epochs,
         train_acc,
         color="RED")
plt.plot(epochs,
         test_acc,
         color="BLUE")

plt.legend(['%d dims' % d for d in epochs])
plt.show()