def load(dataset="training", path=None):
    """
    Загружает набор данных MNIST для обучения или тестирования.
    Возвращает пару, где первый элемент - коллекция изображений, столбцы которых объединены вместе,
    а второй элемент - вектор соответствующих меток от 0 до 9.

    Аргументы:
        dataset (строка, необязательно): либо "training", либо "testing".
            (по умолчанию: "training")
        path (строка, необязательно): путь к набору данных MNIST.
            Если path=None, функция последовательно ищет набор данных по пути:
            '/datasets/MNIST' и './MNIST'. (по умолчанию: None)

    Пример:
        x, lbl = load(dataset="testing", path="/Папка/для/MNIST")
    """
    import os
    import struct
    import numpy as np

    if path is None:
        path = '/datasets/MNIST'
        if not os.path.isdir(path):
            path = './MNIST'
    if not os.path.isdir(path):
        raise ValueError("Невозможно найти набор данных по пути '%s'" % path)

    if dataset == "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset == "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError("dataset должен быть 'testing' или 'training'")

    # Загрузка данных в массивы numpy
    with open(fname_lbl, 'rb') as flbl:
        magic, num = struct.unpack(">II", flbl.read(8))
        lbl = np.fromfile(flbl, dtype=np.int8)

    with open(fname_img, 'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = np.fromfile(fimg, dtype=np.uint8).reshape(len(lbl), rows * cols)

    img = np.moveaxis(img, 0, -1)
    lbl = lbl.astype(int)

    return img, lbl


def show(image):
    """
    Отображает изображение MNIST, представленное в виде столбца.

    Аргументы:
        image (массив): массив формы (28*28) или (28, 28), представляющий собой
            черно-белое изображение размером 28 x 28. Ожидается, что значения будут в диапазоне [0, 1].

    Пример:
        x, lbl = load(dataset="training", path="/datasets/MNIST")
        show(x[:, 0])
    """
    from matplotlib import pyplot
    import matplotlib as mpl

    rows = 28
    cols = 28
    if image.shape[0] != rows * cols and image.shape[0] * image.shape[1] != rows * cols:
        raise "Это не изображение MNIST."
    fig = pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    image = image.reshape(rows, cols)
    imgplot = ax.imshow(image, cmap=mpl.cm.Greys)
    imgplot.set_interpolation('nearest')
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('left')
    pyplot.show()
