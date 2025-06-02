# Jun-02-2025
# drawing_of_basket_content.py

import numpy as np
import matplotlib.pyplot as plt

from utils.src.dir_support import read_directory_data


def drawing_of_basket_content(dir_basket):

    list_basket_paths = read_directory_data(dir_basket)
    list_basket_paths.sort()

    all_points = []
    for point_path in list_basket_paths:
        with open(point_path, 'r') as file:
            for line in file:
                coord_str = line.strip()
                x_str, y_str = coord_str.split(' ')
                all_points.append((float(x_str), float(y_str)))

    # Separate coordinates
    x_coords = [x for x, y in all_points]
    y_coords = [y for x, y in all_points]

    # print(f'\nBASKET x_coords: {x_coords}')
    # print(f'BASKET y_coords: {y_coords}')

    # Create the plot
    fig, ax = plt.subplots(figsize=(5.0, 5.0))
    ax.scatter(x_coords, y_coords, color='#000000', marker='o', s=65)

    # Annotate each point
    for i, (x, y) in enumerate(all_points):
        ax.text(x + 0.13, y, f'p{i}', fontsize=10)

    # Set grid with 0.5 steps
    plt.xticks(fontsize=7, color='black', fontweight='ultralight')
    plt.yticks(fontsize=7, color='black', fontweight='ultralight')
    plt.xticks(np.arange(0, 9, 0.5))
    plt.yticks(np.arange(0, 9, 0.5))
    plt.grid(True, which='both', linestyle='--', linewidth=0.4)

    ax.set_title('Content of the BASKET', fontsize=9)
    ax.axis('equal')

    plt.savefig("PLOT_BASKET.png", dpi=150, bbox_inches='tight')

    return all_points
