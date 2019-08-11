from config import Config
import csv
import json
from flask import jsonify
from entity.response import product, keyword_frequency

types = {"name": 1, "brand": 3, "category": 5}

def auto_complete_svc(type: str, prefix: str) -> list:
    with open(Config.DATA_PATH, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        ac_results = []
        for line in csv_reader:
            column_data = line[types[type]]
            if str(column_data).lower().startswith(prefix.lower()) and column_data not in ac_results:
                ac_results.append(column_data)
    return ac_results

#Did not use filter/map
def search_product_svc(conditions, pagination):
    with open(Config.DATA_PATH, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")

        sp_results = []
        if type(conditions) == dict:
            for line in csv_reader:
                if conditions["type"] == "brandName":
                    for brand_name in conditions["values"]:
                        if str(brand_name).lower() == str(line[3]).lower():
                            new_product = product.Product()
                            #str(line[0]), str(line[1]), str(line[2]), str(line[3]), str(line[4]), str(line[5])
                            new_product.product_id = str(line[0])
                            new_product.title = str(line[1])
                            new_product.brand_id = str(line[2])
                            new_product.brand_name = str(line[3])
                            new_product.category_id = str(line[4])
                            new_product.category_name = str(line[5])
                            sp_results.append(serialise(new_product))


                if conditions["type"] == "categoryName":
                    for category_name in conditions["values"]:
                        if str(category_name).lower() == str(line[5]).lower():
                            new_product = product.Product()
                            # str(line[0]), str(line[1]), str(line[2]), str(line[3]), str(line[4]), str(line[5])
                            new_product.product_id = str(line[0])
                            new_product.title = str(line[1])
                            new_product.brand_id = str(line[2])
                            new_product.brand_name = str(line[3])
                            new_product.category_id = str(line[4])
                            new_product.category_name = str(line[5])
                            sp_results.append(serialise(new_product))
        else:
            for condition in conditions:
                for line in csv_reader:
                    if condition["type"] == "brandName":
                        for brand_name in condition["values"]:
                            if str(brand_name).lower() == str(line[3]).lower():
                                new_product = product.Product()
                                # str(line[0]), str(line[1]), str(line[2]), str(line[3]), str(line[4]), str(line[5])
                                new_product.product_id = str(line[0])
                                new_product.title = str(line[1])
                                new_product.brand_id = str(line[2])
                                new_product.brand_name = str(line[3])
                                new_product.category_id = str(line[4])
                                new_product.category_name = str(line[5])
                                sp_results.append(serialise(new_product))

                    if condition["type"] == "categoryName":
                        for category_name in condition["values"]:
                            if str(category_name).lower() == str(line[5]).lower():
                                new_product = product.Product()
                                # str(line[0]), str(line[1]), str(line[2]), str(line[3]), str(line[4]), str(line[5])
                                new_product.product_id = str(line[0])
                                new_product.title = str(line[1])
                                new_product.brand_id = str(line[2])
                                new_product.brand_name = str(line[3])
                                new_product.category_id = str(line[4])
                                new_product.category_name = str(line[5])
                                sp_results.append(serialise(new_product))
    return sp_results


def count_keywords(kw_list: list):
    with open(Config.DATA_PATH, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        title_list = []
        for line in csv_reader:
            title_list.append(str(line[1]))

    keyword_response = {"keywordFrequencies": []}
    for keyword in kw_list:
        kw_frequency = keyword_frequency.KeywordFrequency()
        kw_frequency.keyword = keyword
        count = 0

        for title in title_list:
            split_title = title.split(" ")
            for word in split_title:
                if word == keyword:
                    count += 1

        kw_frequency.count = count
        keyword_response["keywordFrequencies"].append(serialise(kw_frequency))
    return keyword_response


def serialise(obj):
    snake_to_camel_dict =  {snake_to_camel(k): v for k, v in obj.__dict__.items()}
    return strip_underscore(snake_to_camel_dict)

def snake_to_camel(s):
    a = s.split('_')
    a[1] = a[1].lower()
    if len(a) > 1:
        a[2:] = [u.title() for u in a[2:]]
    return ''.join(a)

def strip_underscore(o):
    return {k.lstrip('_'): v for k, v in o.items()}

def paginate(data, size, start, result_size):
    product_list = list()
    for i in range(size):
        if start > result_size - 1:
            break
        product_list.append(data[start])
        start += 1
    return product_list






