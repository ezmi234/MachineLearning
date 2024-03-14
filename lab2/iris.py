import numpy
import matplotlib
import matplotlib.pyplot as plt


def mcol(v):
    return v.reshape((v.size, 1))


def load(fname):
    DList = []
    labelsList = []
    hLabels = {
        'Iris-setosa': 0,
        'Iris-versicolor': 1,
        'Iris-virginica': 2
    }

    with open(fname) as f:
        for line in f:
            try:
                attrs = line.split(',')[0:-1]
                attrs = mcol(numpy.array([float(i) for i in attrs]))
                name = line.split(',')[-1].strip()
                label = hLabels[name]
                DList.append(attrs)
                labelsList.append(label)
            except:
                pass

    return numpy.hstack(DList), numpy.array(labelsList, dtype=numpy.int32)


def load2():
    # The dataset is already available in the sklearn library (pay attention that the library represents samples as row vectors, not column vectors - we need to transpose the data matrix)
    import sklearn.datasets
    return sklearn.datasets.load_iris()['data'].T, sklearn.datasets.load_iris()['target']


def plot_hist(D, L):
    D0 = D[:, L == 0]
    D1 = D[:, L == 1]
    D2 = D[:, L == 2]

    hFea = {
        0: 'Sepal length',
        1: 'Sepal width',
        2: 'Petal length',
        3: 'Petal width'
    }

    for dIdx in range(4):
        plt.figure()
        plt.xlabel(hFea[dIdx])
        plt.hist(D0[dIdx, :], bins=10, density=True, alpha=0.4, label='Setosa')
        plt.hist(D1[dIdx, :], bins=10, density=True, alpha=0.4, label='Versicolor')
        plt.hist(D2[dIdx, :], bins=10, density=True, alpha=0.4, label='Virginica')

        plt.legend()
        plt.tight_layout()  # Use with non-default font size to keep axis label inside the figure
        plt.savefig('hist_%d.pdf' % dIdx)
    plt.show()


def plot_scatter(D, L):
    D0 = D[:, L == 0]
    D1 = D[:, L == 1]
    D2 = D[:, L == 2]

    hFea = {
        0: 'Sepal length',
        1: 'Sepal width',
        2: 'Petal length',
        3: 'Petal width'
    }

    for dIdx1 in range(4):
        for dIdx2 in range(4):
            if dIdx1 == dIdx2:
                continue
            plt.figure()
            plt.xlabel(hFea[dIdx1])
            plt.ylabel(hFea[dIdx2])
            plt.scatter(D0[dIdx1, :], D0[dIdx2, :], label='Setosa')
            plt.scatter(D1[dIdx1, :], D1[dIdx2, :], label='Versicolor')
            plt.scatter(D2[dIdx1, :], D2[dIdx2, :], label='Virginica')

            plt.legend()
            plt.tight_layout()  # Use with non-default font size to keep axis label inside the figure
            plt.savefig('scatter_%d_%d.pdf' % (dIdx1, dIdx2))
        plt.show()


if __name__ == '__main__':

    # Change default font size - comment to use default values
    plt.rc('font', size=16)
    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)

    D, L = load('iris.csv')
    # plot_hist(D, L)
    # plot_scatter(D, L)

    '''Using `i:i+1` instead of just `i` is a way to ensure that the result of the slicing operation maintains the 
    columnar structure of the data, even though we're just selecting one column at a time.

    In Python, when you slice an array like `D[:, i]`, you get a 1D array (vector) containing the elements of the 
    `i`-th column. However, in certain numerical computing contexts, it's important to preserve the original 
    dimensionality of the data, especially when you're performing operations that expect a certain shape.

    For instance, if you're accumulating column sums as in your example, you want to make sure that each column you add 
    to the sum remains a column, so you can sum them together later to get the overall column sums. By using `i:i+1`, 
    you're effectively selecting a slice that maintains the columnar structure, even though it only contains one column.

    In summary, `i:i+1` ensures that each iteration of the loop produces a column vector, preserving the structure 
    necessary for subsequent operations.'''

    # mu = 0
    # for i in range(D.shape[1]):
    #     mu = mu + D[:, i:i + 1]

    mu = D.mean(1).reshape((D.shape[0], 1))
    print('Mean:')
    print(mu)
    print()

    DC = D - mu

    C = ((D - mu) @ (D - mu).T) / float(D.shape[1])
    print('Covariance:')
    print(C)
    print()

    var = D.var(1)
    std = D.std(1)
    print('Variance:', var)
    print('Std. dev.:', std)
    print()

    for cls in [0,1,2]:
        print('Class', cls)
        DCls = D[:, L==cls]
        mu = DCls.mean(1).reshape(DCls.shape[0], 1)
        print('Mean:')
        print(mu)
        C = ((DCls - mu) @ (DCls - mu).T) / float(DCls.shape[1])
        print('Covariance:')
        print(C)
        var = DCls.var(1)
        std = DCls.std(1)
        print('Variance:', var)
        print('Std. dev.:', std)
        print()
