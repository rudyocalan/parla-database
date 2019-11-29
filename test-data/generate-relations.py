import csv
from copy import copy
from random import randrange
from datetime import timedelta, datetime
from string import Template

def load_hikes(hikes_file):
    hikes = []
    with open(hikes_file, newline='') as hikes_csv:
        hikes_dict = csv.DictReader(hikes_csv, delimiter=',')
        for hike in hikes_dict:
            hikes.insert(0, hike)
    hikes.reverse();
    return hikes

def load_users(users_file):
    users = []
    with open(users_file, newline='') as users_csv:
        users_dict = csv.DictReader(users_csv, delimiter=',')
        for user in users_dict:
            users.insert(0, user)
    users.reverse()
    return users

def load_landtypes(landtypes_file):
    landtypes = []
    with open(landtypes_file, newline='') as landtypes_csv:
        landtypes_dict = csv.DictReader(landtypes_csv, delimiter=',')
        for landtype in landtypes_dict:
            landtypes.insert(0, landtype)
    landtypes.reverse();
    return landtypes

def load_labels(labels_file):
    labels = []
    with open(labels_file, newline='') as labels_csv:
        labels_dict = csv.DictReader(labels_csv, delimiter=',')
        for label in labels_dict:
            labels.insert(0, label)
    labels.reverse()
    return labels

def number_of_time_user_rates():
    return randrange(1, 8)

def number_of_landtypes():
    return randrange(0, 3)

def number_of_hike_labels():
    return randrange(1, 4)

def number_of_labeled_hike():
    return randrange(0, 5)

def star_hikes():
    stars = randrange(0, 6)
    return stars

def rate_or_label_time():
    days_ago = randrange(0, 31)
    hours_ago = randrange(0, 25)
    minutes_ago = randrange(0, 61)
    datetime_delta = timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
    return int((datetime.now() - datetime_delta).timestamp() * 1000)

def pick_hike_randomly(hikes, already_picked=[]):
    random_index = randrange(0, len(hikes))
    hike_picked = hikes[random_index]
    if hike_picked['hikeid'] in already_picked:
        return pick_hike_randomly(hikes, already_picked)
    return hike_picked

def pick_landtypes_randomly(landtypes, already_picked=[]):
    random_index = randrange(0, len(landtypes))
    landtype_picked = landtypes[random_index]
    if landtype_picked['landid'] in already_picked:
        return pick_landtypes_randomly(landtypes, already_picked)
    return landtype_picked

def pick_label_randomly(labels, already_picked=[]):
    random_index = randrange(0, len(labels))
    label_picked = labels[random_index]
    if label_picked['labelid'] in already_picked:
        return pick_label_randomly(labels, already_picked)
    return label_picked

def create_ratings(user_id, hikes):
    ratings = []
    already_rated_hike_ids = []
    user_rate_hikes_at = rate_or_label_time()
    user_hike_rate = star_hikes()
    user_number_of_rates = number_of_time_user_rates()
    for i in range(user_number_of_rates):
        hike = pick_hike_randomly(hikes, already_picked=already_rated_hike_ids)
        already_rated_hike_ids.insert(0, hike['hikeid'])
        rating = {
            'userid': user_id,
            'hikeid': hike['hikeid'],
            'rate': user_hike_rate,
            'timestamp': user_rate_hikes_at
        }
        ratings.insert(0, rating)
    ratings.reverse()
    if len(set(map(lambda r: r['hikeid'], ratings))) != user_number_of_rates:
        print(ratings)
        raise Exception("user can't rate twice the same hike")
    return ratings

def generate_ratings(ratings_file, users, hikes):
    generated_user_ratings = []
    with open(ratings_file, mode='w+') as ratings_csv:
        field_names = ['userid', 'hikeid', 'rate', 'timestamp']
        ratings_writer = csv.DictWriter(ratings_csv, fieldnames=field_names)
        ratings_writer.writeheader()
        for user in users:
            hike = pick_hike_randomly(hikes)
            rating_rows = create_ratings(user['userid'], hikes)
            ratings_writer.writerows(rating_rows)
            generated_user_ratings = [*rating_rows, *generated_user_ratings]
    generated_user_ratings.reverse()
    return generated_user_ratings

def create_hike_landtypes(hikeid, landtypes):
    hike_landtypes = []
    number_of_landtype_for_hike = number_of_landtypes()
    land_already_picked = []
    for i in range(number_of_landtype_for_hike):
        land = pick_landtypes_randomly(landtypes, land_already_picked)
        land_already_picked.insert(0, land['landid'])
        hike_landtype = {
            'hikeid': hikeid,
            'landid': land['landid']
        }
        hike_landtypes.insert(0, hike_landtype)
    if len(set(map(lambda land: land['landid'], hike_landtypes))) != number_of_landtype_for_hike:
        print(hike_landtypes)
        raise Exception("can't apply same landtype twice to a same hike")
    return hike_landtypes

def generate_hikes_landtypes(hikes_landtypes_file, hikes, landtypes):
    generated_hike_landtypes = []
    with open(hikes_landtypes_file, mode='w+') as landtypes_csv:
        hike_landtypes_writer = csv.DictWriter(landtypes_csv, fieldnames=['hikeid', 'landid'])
        hike_landtypes_writer.writeheader()
        for hike in hikes:
            hike_landtype_rows = create_hike_landtypes(hike['hikeid'], landtypes)
            hike_landtypes_writer.writerows(hike_landtype_rows)
            generated_hike_landtypes = [*hike_landtype_rows, *generated_hike_landtypes]
    return generated_hike_landtypes

def create_hikes_labels(userid, hikes, labels):
    hikes_labels = []
    number_of_labels_for_hike = number_of_hike_labels()
    number_of_hike_to_be_labeled = number_of_labeled_hike()
    for i in range(number_of_hike_to_be_labeled):
        hike_ids_already_picked = []
        hike = pick_hike_randomly(hikes, hike_ids_already_picked)
        hike_ids_already_picked.insert(0, hike['hikeid'])
        for j in range(number_of_labels_for_hike):
            label_ids_already_picked = []
            label = pick_label_randomly(labels, label_ids_already_picked)
            label_ids_already_picked.insert(0, label['labelid'])
            hike_label= {
                'userid': userid,
                'hikeid': hike['hikeid'],
                'labelid': label['labelid'],
                'timestamp': rate_or_label_time()
            }
            hikes_labels.insert(0, hike_label)
    return hikes_labels

def generate_hikes_labels(hike_labels_file, users, hikes, labels):
    generated_hike_labels = []
    with open(hike_labels_file, mode='w+') as hike_labels_csv:
        hike_labels_writer = csv.DictWriter(
            hike_labels_csv, 
            fieldnames=['userid', 'hikeid', 'labelid', 'timestamp']
        )
        hike_labels_writer.writeheader()
        for user in users:
            hike_labels_rows = create_hikes_labels(user['userid'], hikes, labels)
            hike_labels_writer.writerows(hike_labels_rows)
            generated_hike_labels = [*hike_labels_rows, *generated_hike_labels]
    
    generated_hike_labels.reverse()
    return generated_hike_labels



if __name__ == "__main__":
    hikes_loaded = load_hikes('hikes.csv')
    users_loaded = load_users('users.csv')
    landtypes_loaded = load_landtypes('landtypes.csv')
    labels_loaded = load_labels('labels.csv')
    print(users_loaded[0])
    print(hikes_loaded[0])
    print(landtypes_loaded[0])
    print(labels_loaded[0])
    generate_ratings('ratings.csv', copy(users_loaded), copy(hikes_loaded))
    generate_hikes_landtypes('hike-landtypes.csv', copy(hikes_loaded), landtypes_loaded)
    generate_hikes_labels('hike-labels.csv', copy(users_loaded), copy(hikes_loaded), labels_loaded)
