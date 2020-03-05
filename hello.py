class User:
    def __init__(self, username):
        self.username = username
    def welcomeMsg(self):
        return "hello "+self.username+",welcome to the git "

user_object = User("Divya")
print(user_object.welcomeMsg())