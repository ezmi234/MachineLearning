import numpy as np

def mcol(v):
    return v.reshape((v.size, 1))
def load_dataset(filename, delimiter=','):
    """
    Load a dataset from a file.

    :param filename: The name of the file to load.
    :param delimiter: The delimiter used in the file.
    :return: A tuple containing the data and the labels.
    """

    with open(filename) as f:
        data = []
        labels = []
        unique_labels = {}
        for line in f:
            try:
                attrs = line.split(delimiter)[0:-1]
                attrs = mcol(np.array([float(i) for i in attrs]))
                name = line.split(delimiter)[-1].strip()
                data.append(attrs)
                labels.append(name)
                if name not in unique_labels:
                    unique_labels[name] = len(unique_labels)
            except:
                pass

    normalized_labels = [unique_labels[label] for label in labels]
    return np.hstack(data), np.array(normalized_labels, dtype=np.int32)


