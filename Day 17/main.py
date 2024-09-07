# def function():
#     pass
# print('Hello')

""" name classes in Python using PascalCase, different from camelCase,
different from snake_case where all the words are lowercase but separated by _"""


# writing the class
class User:
    # init function is called every time a new object is created from this class
    def __init__(self):
        print("new user being created...")


# building an object called user_1 out of the User class
user_1 = User()
# to create an attribute for the class
user_1.id = "001"
user_1.username = "Bean"

print(user_1.username)

# this can be tedious when creating multiple users
user_2 = User()
user_2.id = "002"
user_2.username = "Dip"

print(user_2.username)


class UserExample:
    # innit function is the constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # default value, doesn't need to be passed in with every user that is created
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


new_user1 = UserExample(16, "BeanieBoop")
new_user2 = UserExample(3, "Dee")
print(new_user1.id)
print(new_user1.username)
print(new_user1.followers)

new_user1.follow(new_user2)
print(new_user1.followers) #0
print(new_user1.following) #1
print(new_user2.followers) #1
print(new_user2.following) #0


class Car:
    # self is the object
    def __init__(self, seats):
        self.seats = seats

    # method
    def enter_race_mode(self):
        self.seats = 2


my_car = Car(5)
my_car.enter_race_mode()
