import json

def read_json(file):
    with open (file, "r") as teller_data:
        new_data = json.load(teller_data)
        return new_data

def modify_json(file, account_number, key, new_value):
    new_json = read_json(file)
    new_json[account_number][key] = new_value
    save_json(file, new_json)

def save_json(file, data):
    json_data = data
    with open(file, "w") as saved_data:
        json.dump(json_data, saved_data)

modify_json("tellerdata.json", "412689", "PIN", "2784")

#print(read_json())
