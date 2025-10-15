class dog:
    species="dog"
    def __init__(self, name, age):
        self.name=name
        self.age=age
lu=parrot("blu",1)
j=parrot("woo",5)
print("lu is a {}".format(lu.species))
print("j is also a {}".format(j.species))
print("{} is {} years old".format(lu.name,lu.age))
print("{} is {} years old".format(j.name,j.age))