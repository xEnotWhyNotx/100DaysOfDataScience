import os
import shutil

# Путь к каталогу, в котором был разархивирован исходный набор данных с котами
ORIGINAL_CAT_DATASET_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/Kaggle-cats"
# Путь к каталогу, в котором был разархивирован исходный набор данных с собаками
ORIGINAL_DOG_DATASET_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/Kaggle-dogs"
# Каталог, где мы будем хранить наш небольшой набор данных
BASE_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/cats_and_dogs_small"


def main():
    os.mkdir(BASE_DIR)

    # Каталоги для наших наборов данных: обучение, валидация и тест
    train_dir = os.path.join(BASE_DIR, 'train')
    os.mkdir(train_dir)
    validation_dir = os.path.join(BASE_DIR, 'validation')
    os.mkdir(validation_dir)
    test_dir = os.path.join(BASE_DIR, 'test')
    os.mkdir(test_dir)

    # Каталог с обучающими изображениями котов
    train_cats_dir = os.path.join(train_dir, 'cats')
    os.mkdir(train_cats_dir)

    # Каталог с обучающими изображениями собак
    train_dogs_dir = os.path.join(train_dir, 'dogs')
    os.mkdir(train_dogs_dir)

    # Каталог с валидационными изображениями котов
    validation_cats_dir = os.path.join(validation_dir, 'cats')
    os.mkdir(validation_cats_dir)

    # Каталог с валидационными изображениями собак
    validation_dogs_dir = os.path.join(validation_dir, 'dogs')
    os.mkdir(validation_dogs_dir)

    # Каталог с тестовыми изображениями котов
    test_cats_dir = os.path.join(test_dir, 'cats')
    os.mkdir(test_cats_dir)

    # Каталог с тестовыми изображениями собак
    test_dogs_dir = os.path.join(test_dir, 'dogs')
    os.mkdir(test_dogs_dir)

    # Копирование первых 1000 изображений с котами в каталог train_cats_dir
    fnames = ['{}.jpg'.format(i) for i in range(1000)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_CAT_DATASET_DIR, fname)
        dst = os.path.join(train_cats_dir, fname)
        shutil.copyfile(src, dst)

    # Копирование следующих 500 изображений с котами в каталог validation_cats_dir
    fnames = ['{}.jpg'.format(i) for i in range(1000, 1500)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_CAT_DATASET_DIR, fname)
        dst = os.path.join(validation_cats_dir, fname)
        shutil.copyfile(src, dst)

    # Копирование следующих 500 изображений с котами в каталог test_cats_dir
    fnames = ['{}.jpg'.format(i) for i in range(1500, 2000)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_CAT_DATASET_DIR, fname)
        dst = os.path.join(test_cats_dir, fname)
        shutil.copyfile(src, dst)

    # Копирование первых 1000 изображений с собаками в каталог train_dogs_dir
    fnames = ['{}.jpg'.format(i) for i in range(1000)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_DOG_DATASET_DIR, fname)
        dst = os.path.join(train_dogs_dir, fname)
        shutil.copyfile(src, dst)

    # Копирование следующих 500 изображений с собаками в каталог validation_dogs_dir
    fnames = ['{}.jpg'.format(i) for i in range(1000, 1500)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_DOG_DATASET_DIR, fname)
        dst = os.path.join(validation_dogs_dir, fname)
        shutil.copyfile(src, dst)

    # Копирование следующих 500 изображений с собаками в каталог test_dogs_dir
    fnames = ['{}.jpg'.format(i) for i in range(1500, 2000)]
    for fname in fnames:
        src = os.path.join(ORIGINAL_DOG_DATASET_DIR, fname)
        dst = os.path.join(test_dogs_dir, fname)
        shutil.copyfile(src, dst)

    # Проверка корректности выполнения копирования
    print('total training cat images:', len(os.listdir(train_cats_dir)))
    print('total training dog images:', len(os.listdir(train_dogs_dir)))
    print('total validation cat images:', len(os.listdir(validation_cats_dir)))
    print('total validation dog images:', len(os.listdir(validation_dogs_dir)))
    print('total test cat images:', len(os.listdir(test_cats_dir)))
    print('total test dog images:', len(os.listdir(test_dogs_dir)))


if __name__ == "__main__":
    main()
