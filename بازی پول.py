#https://quera.ir/problemset/technology/87184/سؤال-پایتون-بازی-پول



import string, hashlib

def nationalCode_check(Code):
    if len(str(Code)) < 10 :
        raise ValueError('Input Code incorrect')
    try:
        num = list(map(int, list(Code)))[0:9]
        index_num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        index_num.reverse()
        totals = zip(index_num, num)
        total_sum = sum([(value* key) for value,key in [(value, key) for key, value in totals]])
        if (total_sum % 11) >= 2:
            control = -(total_sum % 11) ; control += 11
            if int(Code[-1]) == int(control):
                return True
            else:
                return False
        else:
            if int(Code[-1]) == int(total_sum % 11):
                return True
            else:
                return False
    except:
        raise ValueError('Input Code incorrect')



def phone_number_check(mobile_number):
    assert len(mobile_number) == 11 or len(mobile_number) == 13 , 'Invalid phone number'
    if mobile_number[:3] == '+98':
        mobile_number = '0' + mobile_number[3:]
        return mobile_number
    else:
        return mobile_number

#____________________________________________________________________

class Site:
    def __init__(self, url_address):
        pass

    def show_users(self):
        pass

    def register(self, user):
        pass

    def login(self, **kwargs):
        pass

    def logout(self, user):
        pass

    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

    def __str__(self):
        return self.url

#____________________________________________________________________

class Account:
    def __init__(self, username, password, user_id, phone, email):

        #username
        if len(username.split('_')) == 2:
            splited_userName = username.split('_')
            name_is_english = True

            for part in splited_userName:
                for letter in part:
                    if letter not in string.ascii_letters:
                        name_is_english = False

            if name_is_english:
                self.username = username 

        else: 
            raise ValueError('invalid username')

        #password
        if len(password) >= 8 and set(string.ascii_uppercase).intersection(password): 
           self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        #user_id
        if nationalCode_check(user_id):
            self.user_id = user_id

        #phone
        if phone_number_check(phone):
            self.phone = phone_number_check(phone)

        #email



    def set_new_password(self, password):
        pass

    def username_validation(self, username):
        pass

    def password_validation(self, password):
        pass

    def id_validation(self, id):
        pass

    def phone_validation(self, phone):
        pass

    def email_validation(self, email):
        pass

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username


def show_welcome(func):
    pass

def verify_change_password(func):
    pass

@show_welcome
def welcome(user):
    return ("welcome to our site %s" % user)

@verify_change_password
def change_password(user, old_pass, new_pass):
    return ("your password is changed successfully.")


ins = Account("Mahdi_ebrahimi", "mahdi", '0200616791', "09129729277", 'mahdiebi@gmail.com')

