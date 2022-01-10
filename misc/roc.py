"""
Calculate/Plot ROC given
    Model output probablities
    True Values
"""
from matplotlib import pyplot as plt


def roc(prob, y_true, n_points=100):
    point_x, point_y = [], []
    for thr in range(0, n_points+1):
        thr = 1.0 * thr / n_points
        y_pred = [1 if p >= thr else 0 for p in prob]
        print(thr, y_pred)

        fp = list(filter(lambda ys: ys[1] == 0 and ys[0] == 1, zip(y_pred, y_true)))
        tp = list(filter(lambda ys: ys[1] == 1 and ys[0] == 1, zip(y_pred, y_true)))

        fn = list(filter(lambda ys: ys[1] == 1 and ys[0] == 0, zip(y_pred, y_true)))
        tn = list(filter(lambda ys: ys[1] == 0 and ys[0] == 0, zip(y_pred, y_true)))

        point_x.append(len(fp) / (len(fp) + len(tn)))
        point_y.append(len(tp) / (len(tp) + len(fn)))
    return point_x, point_y


y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
prob = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
fpr, tpr = roc(prob, y_true)
plt.scatter(fpr, tpr)
plt.show()
