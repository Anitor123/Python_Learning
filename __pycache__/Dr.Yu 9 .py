class User:
    
    def __init__(self, user_id, username):
        print("new user being created ...")
        self.id = user_id
        self.username = username
        self.followers = 0
        

user_1 = User("23", "Joel")
user_2 = User("24", "Nehe")

print(user_1.username)
print(user_1.id)
print(user_2.username)
print(user_2.id)
print(user_1.followers)