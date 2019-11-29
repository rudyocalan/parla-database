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

def load_hike_labels(hike_labels_path):
    hike_labels = []
    with open(hike_labels_path) as json_file:
        hike_labels = json.load(json_file)
    return hike_labels

def create_labels_import_script(labels_file_path, script_path):
    labels = []
    with open(labels_file_path) as json_file:
        labels = json.load(json_file)
        label_docs = map(
            lambda label: {
                "_id": label['labelid'],
                "labelinfo": label['labelinfo']
            },
            labels
        )
        write_mongo_script(script_path, 'labels', label_docs)
    return labels

def create_users_import_script(users_file_path, script_path):
    with open(users_file_path) as json_file:
        users = json.load(json_file)
        user_docs = map(
            lambda user: {
                "_id": user['userid'],
                "username": user['username']
            },
            users
        )
        write_mongo_script(script_path, 'users', user_docs)

def create_ratings_import_script(ratings_file_path, script_path):
    with open(ratings_file_path) as json_file:
        ratings = json.load(json_file)
        rating_docs = map(
            lambda rating: {
                "user_id": rating['userid'],
                "hike_id": rating['hikeid'],
                "rating": rating['rate'],
                "timestamp": rating['timestamp']
            },
            ratings
        )
        write_mongo_script(script_path, 'ratings', rating_docs)


def hike_label_id_list(hike_id, hike_labels):
    labels = list(filter(
        lambda hike_label: hike_id == hike_label['hikeid'],
        hike_labels
    ))
    label_list = list(map(lambda label: label['labelid'], labels))
    return label_list

def create_hikes_import_script(hikes_file_path, script_path, hike_labels=[]):
    with open(hikes_file_path) as json_file:
        hikes = json.load(json_file)
        hike_docs = map(
            lambda hike: {
                "_id": hike['hikeid'],
                "hikename": hike['hikename'],
                "labels": hike_label_id_list(hike['hikeid'], hike_labels)
            },
            hikes
        )
        write_mongo_script(script_path, 'hikes', hike_docs)

if __name__ == "__main__":
    labels = create_labels_import_script('./labels.json', './labels.js')
    create_users_import_script('./users.json', './users.js')
    create_ratings_import_script('./ratings.json', './ratings.js')
    hike_labels = load_hike_labels('./hike-labels.json')
    create_hikes_import_script('./hikes.json', './hikes.js', hike_labels=hike_labels)
