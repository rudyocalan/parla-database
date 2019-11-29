import csv
from random import randrange
from datetime import timedelta, datetime
from string import Template

def load_hikes(hikes_file):
    hikes = []
    with open(hikes_file, newline='') as hikes_csv:
        hikes_dict = csv.DictReader(hikes_csv, delimiter=',', fieldnames=['hikeid', 'hikename'])
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

def number_of_time_user_rates():
    return randrange(1, 8)

def star_hikes():
    stars = randrange(0, 6)
    return stars

def rate_time():
    days_ago = randrange(0, 31)
    hours_ago = randrange(0, 25)
    minutes_ago = randrange(0, 61)
    datetime_delta = timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
    return int((datetime.now() - datetime_delta).timestamp() * 1000)

def pick_hike_randomly(hikes, already_picked=[]):
    random_index = randrange(0, len(hikes) - 1)
    hike_picked = hikes[random_index]
    if hike_picked['hikeid'] in already_picked:
        return pick_hike_randomly(hikes, already_picked)
    return hike_picked

def create_ratings(user_id, hikes):
    ratings = []
    already_rated_hike_ids = []
    user_rate_hikes_at = rate_time()
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

def generate_ratings(ratings_file):
    with open(ratings_file, mode='w+') as ratings_csv:
        field_names = ['userid', 'hikeid', 'rate', 'timestamp']
        ratings_writer = csv.DictWriter(ratings_csv, fieldnames=field_names)
        ratings_writer.writeheader()
        for user in users:
            hike = pick_hike_randomly(hikes)
            rating_rows = create_ratings(user['userid'], hikes)
            ratings_writer.writerows(rating_rows)


if __name__ == "__main__":
    hikes = load_hikes('hikes.csv')
    users = load_users('users.csv')
    generate_ratings('ratings.csv')
