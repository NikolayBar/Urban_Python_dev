class User:

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return hash(self) == hash(other)


u1 = User('qwer')
a = 'qwer1'
print(u1 == a)
