import json
from copy import copy
from random import randrange
from datetime import timedelta, datetime
from string import Template

def write_mongo_script(file_path, var_name, json_arr):
    with open(file_path, 'w+') as mongo_script_file:
      var_declaration = f'var {var_name} = ['
      mongo_script_file.write(var_declaration)
      for document in json_arr:
          doc_str = json.dumps(document)
          mongo_script_file.write(f'{doc_str},\n')
      mongo_script_file.write(']\n')

def create_labels_import_script(labels_file_path, script_path):
    with open(labels_file_path) as json_file:
        labels = json.load(json_file)
        write_mongo_script(script_path, 'labels', labels)

def create_hikes_import_script(hikes_file_path):
    with open(hikes_file_path) as json_file:
        hikes = json.load(json_file)
        #with open(label)

if __name__ == "__main__":
    create_labels_import_script('./labels.json', './labels.js')
    # hikes_loaded = load_hikes('hikes.json')
    # users_loaded = load_users('users.json')
    # landtypes_loaded = load_landtypes('landtypes.json')
    # labels_loaded = load_labels('labels.json')
    # ratings = load_ratings('ratings.json')
    # hike_landtypes = load_hike_landtypes('hike-landtypes.jsonon')
    # hike_labels = load_hike_labels('hike-labels.jsonon')
