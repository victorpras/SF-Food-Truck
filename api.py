def pretty_print(json_str):
    return json.dumps(json_str, sort_keys=True, indent=2, separators=(',', ': ')) 

def foodtrucks_around(truck, x, y):
    return truck.get('x') > x and truck.get('y') > y

def find_truck(truck, name):
    return truck.get('applicant') == name
