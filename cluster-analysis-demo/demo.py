# Jun-10-2025
# demo.py

"""
How to use: python demo.py
"""

from pathlib import Path
from utils.src.dir_support import files_number_in_directory
from distances import distances
from clustering import clustering
from drawing_of_basket_content import drawing_of_basket_content
from drawing_of_clusters_content import drawing_of_clusters_content


def main():
    dir_basket = Path.cwd() / 'BASKET'
    n_objects = files_number_in_directory(dir_basket)

    print(f'\nC L U S T E R I N G')
    print(f'There are {n_objects} objects in the BASKET folder.')
    input_string \
        = input('Please enter the desired number of clusters: ')
    number_of_clusters = int(input_string)

    D, list_basket_paths = distances(dir_basket)

    clustering(dir_basket,
               D,
               list_basket_paths,
               number_of_clusters)

    all_points = drawing_of_basket_content(dir_basket)
    drawing_of_clusters_content(number_of_clusters, all_points)


if __name__ == "__main__":
    main()
