import os
import csv
import settings

import itertools


def get_purchases_products(file_path=settings.PATHS['purchase_data_file']):
    purchase_data = {}
    products = set()
    with open(file_path, 'r') as purchases:

        # skip header
        next(purchases, None)

        reader = csv.reader(purchases)
        for row in reader:
            purchase_id, product_id, name, qty, date_created = row

            # store purchase : [object1, object2 ...]
            if purchase_id in purchase_data:
                purchase_data[purchase_id].append(name)
            else:
                purchase_data[purchase_id] = [name]

            # store product set : {(id,name), ...}
            products.add((product_id, name))
    return purchase_data, products


def get_only_lists(list_of_lists):
    list_of_l = []
    for l in list_of_lists:
        if len(l)>1:
            list_of_l.append(l)
    return list_of_l


def generate_candidates(interest_sets):
    for l in interest_sets:
        for combination_lenght in range(2,len(l)+1):
            for candidate in itertools.combinations(l, combination_lenght):
                yield candidate


def support(candidate, interest_sets):
    return sum([set(l).intersection(candidate) == set(candidate) for l in interest_sets])/float(len(interest_sets))


def confidence(candidate, interest_sets):
    conf = support(candidate, interest_sets)
    s = support([candidate[0]], interest_sets)
    conf = conf/s if s else conf
    return conf


def get_lift_confidence(candidate, interest_sets):
    if len(candidate) > 1:
        conf = support(candidate, interest_sets)
        s = support([candidate[0]], interest_sets)
        conf = conf/s if s else None
        lift_value = conf
        for item in candidate[1:]:
            s = support([item], interest_sets)
            lift_value = lift_value/s if s else lift_value
        return conf, lift_value
    raise AttributeError("Attribute 'candidate' MUST be at least of length 2.")


def lift(candidate, interest_sets):
    lift_value = support(candidate, interest_sets)
    for item in candidate:
        s = support([item], interest_sets)
        lift_value = lift_value/s if s else lift_value
    return lift_value


# Event Data Analysis Utility Functions
def get_edge(event_dir='./'+settings.PATHS['event_data_dir'], rule=lambda x: x == 'going', limit_files=2):
    i = 0
    for file in os.listdir(event_dir):
        if file.endswith('.csv'):
            i += 1
            with open(''.join([event_dir,file]), 'r') as csvfile:
                reader = csv.reader(csvfile)
                list_of_names = []
                for row in reader:
                    name, status = row
                    status = status.strip().lower()
                    name = name.strip().lower()
                    if rule(status):
                        list_of_names.append(name)
                for combination in itertools.combinations(list_of_names, 2):
                    yield combination
        if i > limit_files:
            break
