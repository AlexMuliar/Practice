class A:
    def __getitem__(self, key):
        if key < 10:
            return key
        else:
            raise StopIteration


for i in A():
    print(i)