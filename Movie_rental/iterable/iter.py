from domain.client import Client
#from repository.clients_repo import Clients_Repository
class Iterable():
    def __init__(self):
        self._items = []
        self._index = 0
    @property
    def iter(self):
        return self._items
    def add(self, obj):
        self._items.append(obj)
    def remove(self, pos):
        self._items.pop(pos)


    def getAll(self):
        return self._items

    def find_by_id(self, id):
        for client in self._items:
            if client.id == id:
                return True
        return False
    def delete_id(self, id):
        i = 0
        for client in self._items:
            if client.id == id:
                self.remove(i)
            i += 1
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._items):
            self._index += 1
        else:
            raise StopIteration

    def __setitem__(self, key, value):
        self._items[key] = value

    def __getitem__(self, item):
        return self._items[item]

    def __str__(self):
        s = ''
        for item in self._items:
            s += str(item)
            s +='\n'
        return s

    def shellSort(self, key=lambda x: x):
        gap = len(self._items) // 2
        while gap > 0:
            for start in range(gap):
                for i in range(start + gap, len(self._items), gap):

                    currentvalue = self._items[i]
                    # currentvalue = key(_list[i])
                    position = i

                    while position >= gap and key(self._items[position - gap]) < key(currentvalue):
                        self._items[position] = self._items[position - gap]
                        position = position - gap

                    self._items[position] = currentvalue
            gap = gap // 2

    @staticmethod
    def starts_with_letter(item, letter):
        if item[0] == str(letter):
            return True
        return False
    @staticmethod
    def age_less_than(item, _age):
        if item["age"] < _age:
            return True
        return False

    def filter(self,  funct = None):
        filter_list = []
        for item in self._items:
            if funct(item) == True:
                filter_list.append(item)
        return filter_list

    #???
    def filter1(self, starts_with_letter, *params):
        fiter_list = []
        for item in self._items:
            if starts_with_letter(item, *params) == True:
                fiter_list.append(item)
        return fiter_list

    def filter2(self, age_less_than, some_age):
        filter_list = []
        for item in self._items:
            if age_less_than(item, some_age):
                filter_list.append(item)
        return filter_list
    #???
def test_somtehing():
    test_list = Iterable()
    c1 = Client("George", 100)
    c2 = Client("Dennis", 101)
    c3 = Client("Anna", 102)
    test_list.add(c1)
    test_list.add(c2)
    test_list.add(c3)
    #print(test_list[0])
    # for client in test_list:
    #    print(client)
    print(test_list)

def test1():
    c1 = {"name":"George" , "id":100, "age":16}
    c2 = {"name":"Alex" , "id":101, "age":20}
    c3 = {"name":"Anna", "id":102, "age":19}
    c4 = {"name":"Jason" , "id":103, "age":15}
    some_list =Iterable()
    some_list.add(c1)
    some_list.add(c2)
    some_list.add(c3)
    some_list.add(c4)
    shellSort(some_list, lambda x: x["age"])

    print(some_list.filter( lambda x: x["age"] > 18))

def shellSort(_list, key = lambda x: x ):
    gap = len(_list) // 2
    while gap > 0:
        for start in range(gap):
            for i in range(start + gap, len(_list), gap):

                currentvalue = _list[i]
                #currentvalue = key(_list[i])
                position = i

                while position >= gap and key(_list[position - gap]) < key(currentvalue):
                    _list[position] = _list[position - gap]
                    position = position - gap

                _list[position] = currentvalue
        gap = gap // 2
#
def test2():
    lst = [2,8,1,7,5,6,3,4,2,7,8,3]
    lst2 = ['ab','cb','b']
    shellSort(lst2)
    print(lst2)

def test3():
    _list = Iterable()
    #c0 = ObjectsClass(99, "some_name", 11)
    c1 = ObjectsClass(100, "Abby", 12)
    c2 = ObjectsClass(101, "Dennis", 16)
    c3 = ObjectsClass(102, "Daniel", 21)
    c4 = ObjectsClass(103, "Marmota", 15)
    _list.add(c1)
    _list.add(c2)
    _list.add(c3)
    _list.add(c4)

    shellSort(_list, key = lambda field: field.age)

def test4():
    _list = Iterable()
    c1 = "Alex"
    c2 = "George"
    c3 = "Andra"
    c4 = "Dennis"
    c5 = "Anna"
    _list.add(c1)
    _list.add(c2)
    _list.add(c3)
    _list.add(c4)
    _list.add(c5)
    print(_list)
    # print(_list.filter1(_list.starts_with_letter,"A" ))
    #print(_list.filter(key = lambda x : _list.starts_with_letter))
    # shellSort(_list, key = lambda x : x

# test1()
