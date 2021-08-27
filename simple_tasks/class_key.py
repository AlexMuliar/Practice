# TODO Object as key


class Obj:
    def __init__(self) -> None:
        self.param = 1

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return type(self) == type(other)


    # def __repr__(self) -> str:
    #     return "1"

if __name__ == '__main__':
    my_dict = {
        Obj() : 1,
        Obj() : 2,
    }
    print(hash(Obj()))

    print(my_dict)
