import json

class Account:
    file_path = "tellerdata.json"
    def __init__(self, account_number):
        self.account_number = account_number
        self.pin = None
        self.balance = 0.0
        #self.fullname = ""
        self.data = {}
        self.load_json()

    def load_json(self):
        #TODO add try and except 
        with open (file_path, "r") as teller_data:
            self.data = json.load(teller_data)
        if self.account_number in self.data:
            self.pin = self.data[self.account_number]["PIN"]
            self.balance = self.data[self.account_number]["Balance"]
            #self.fullname = self.data[self.account_number]["fullname"]
    def save_file(self):
        self.data[self.account_number] = {"PIN":self.pin, "Balance":self.balance}
        with open (file_path, "w") as teller_data:
            json.dump(self.data, teller_data)
    def withdraw(self, w_amount):
        if w_amount < 0:
            raise ValueError("Amount needs to be positive")
        if w_amount > self.balance:
            raise ValueError("Insuffiecient funds")
        self.balance -= w_amount
    def deposit(self):
        
    @classmethod
    def login(cls, account_number, pin):
        pass
    
















'''def read_json(file):
    
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
'''