# Jun-02-2025
# drawing_of_clusters_content.py

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from utils.src.dir_support import read_directory_data, get_subdirectories


def drawing_of_clusters_content(all_points):

    list_cluster_numbers, list_all_points = get_clusters_content()

    n_cluster = len(list_cluster_numbers)

    # Create the plot
    fig, ax = plt.subplots(figsize=(5.0, 5.0))

    for n in range(n_cluster):

        points_of_cluster = []

        list_cluster_points = list_all_points[n]

        for point in list_cluster_points:
            with open(point, 'r') as file:
                for line in file:
                    coord_str = line.strip()
                    x_str, y_str = coord_str.split(' ')
                    points_of_cluster.append((float(x_str), float(y_str)))

        x_coords = [x for x, y in points_of_cluster]
        y_coords = [y for x, y in points_of_cluster]

        # print(f'\nCLUSTER_{n} x_coords: {x_coords}')
        # print(f'CLUSTER_{n} y_coords: {y_coords}')

        match str(n):
            case '0':
                ax.scatter(x_coords, y_coords, color='#FF2600', marker='o', s=65)   # maraschino
            case '1':
                ax.scatter(x_coords, y_coords, color='#008F00', marker='o', s=65)   # clover
            case '2':
                ax.scatter(x_coords, y_coords, color='#0096FF', marker='o', s=65)   # aqua
            case '3':
                ax.scatter(x_coords, y_coords, color='#FF9300', marker='o', s=65)   # orange
            case '4':
                ax.scatter(x_coords, y_coords, color='#941100', marker='o', s=65)   # cayenne
            case '5':
                ax.scatter(x_coords, y_coords, color='#0433FF', marker='o', s=65)   # blueberry
            case '6':
                ax.scatter(x_coords, y_coords, color='#FF40FF', marker='o', s=65)   # magenta
            case '7':
                ax.scatter(x_coords, y_coords, color='#00F900', marker='o', s=65)   # spring
            case '8':
                ax.scatter(x_coords, y_coords, color='#942192', marker='o', s=65)   # purple
            case _:
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

        ax.set_title('CLUSTERS (distinguished by the points color)', fontsize=9)
        ax.axis('equal')

        plt.savefig("PLOT_CLUSTERS.png", dpi=150, bbox_inches='tight')


def get_clusters_content():

    dir_clusters = Path.cwd() / 'CLUSTERS'

    list_cluster_numbers = get_subdirectories(dir_clusters)

    list_all_points = []
    for cluster_number in list_cluster_numbers:

        dir_cluster = Path.cwd() / 'CLUSTERS' / cluster_number

        list_of_points_paths = read_directory_data(dir_cluster)
        list_of_points_paths.sort()

        list_all_points.append(list_of_points_paths)

    return list_cluster_numbers, list_all_points
