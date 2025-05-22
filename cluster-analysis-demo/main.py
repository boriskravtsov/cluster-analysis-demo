# May-22-2025
# main.py

from pathlib import Path
from utils.src.dir_support import files_number_in_directory
from distances import distances
from clustering import clustering

dir_basket = Path.cwd() / 'BASKET'
n_objects = files_number_in_directory(dir_basket)

print(f'\nC L U S T E R I N G')
print(f'There are {n_objects} objects in the BASKET folder.')
input_string = input('Please enter the desired number of clusters: ')
number_of_clusters = int(input_string)

D = distances(dir_basket)

clustering(dir_basket, D, number_of_clusters)
