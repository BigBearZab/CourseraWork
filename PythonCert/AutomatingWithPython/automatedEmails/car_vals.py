import json

def import_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_max_model(car_dict):
    sorted_list = [{'model':d['car']['car_model'] , 'sales':d['total_sales']} for d in sorted(car_dict, key=lambda x : x['total_sales'])]
    return sorted_list[-1]

def get_most_popular_year(car_dict):
    year_dict = {}
    for car in car_dict:
        if car['car']['car_year'] in year_dict:
            year_dict[car['car']['car_year']] += car['total_sales']
        else:
            year_dict[car['car']['car_year']] = car['total_sales']
    highest_year = max(year_dict, key=year_dict.get)
    return {'highest_year':highest_year,'sales_vol':year_dict[highest_year]}

def main():
    car_dict = import_json('car_sales.json')
    # print(get_max_model(car_dict))
    print(get_most_popular_year(car_dict))
if __name__ == "__main__":
    main()