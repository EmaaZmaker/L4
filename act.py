class myclass:
    __privatevar=50
    def __privatemeth(self):
        print("yhis is private method")
    def hello(self):
        print("private variable value",myclass.__privatevar)
obj1=myclass()
obj1.hello()
obj1.__privatemeth()