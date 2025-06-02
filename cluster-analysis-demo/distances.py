# Jun-02-2025
# distances.py

import numpy as np
import random
from utils.src.dir_support import read_directory_data


def distances(dir_basket):

    list_basket_paths = read_directory_data(dir_basket)
    random.shuffle(list_basket_paths)

    n_objects = len(list_basket_paths)
    n_objects_x = n_objects * n_objects

    D = np.zeros((n_objects, n_objects), dtype=np.float32)

    list_indexes = []
    for n in range(n_objects_x):

        j = n // n_objects
        i = n % n_objects

        if i <= j:
            continue

        list_indexes.append((j, i))

    n_calc = len(list_indexes)
    for n in range(n_calc):

        temp = list_indexes[n]

        j = temp[0]
        i = temp[1]

        with open(list_basket_paths[j], 'r') as file:
            for line in file:
                coord_str = line.strip()
                x_str, y_str = coord_str.split(' ')
                x1 = float(x_str)
                y1 = float(y_str)

        with open(list_basket_paths[i], 'r') as file:
            for line in file:
                coord_str = line.strip()
                x_str, y_str = coord_str.split(' ')
                x2 = float(x_str)
                y2 = float(y_str)

        dx = x1 - x2
        dy = y1 - y2

        distance = np.sqrt(dx * dx + dy * dy)

        D[j, i] = distance
        D[i, j] = distance

    return D, list_basket_paths
