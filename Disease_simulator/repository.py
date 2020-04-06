from person import Person
class Repository():
    def __init__(self, file_name):
        self._repo = []
        self._fileName = file_name
        self._load_file()

    def _add(self, object):
        self._repo.append(object)

    def remove(self, id):
        for obj in self._repo:
            if obj._id == id:
                self._repo.remove(obj)
                self._save_file()

    def __getitem__(self, item):
        return self._repo[item]

    def getAll(self):
        lst = []
        for obj in self._repo:
            lst.append(obj)
        return lst

    def __str__(self):
        for obj in self._repo:
            return str(obj)
    def __len__(self):
        return len(self._repo)

    def _load_file(self):
        try:
            f = open(self._fileName, 'r')
            line = f.readline()
            while line != '':
                tok = line.split(",")
                id = int(tok[0])
                immune = tok[1]
                status = tok[2]
                person = Person(id, immune, status)
                self._add(person)
                line = f.readline()
        except IOError as e:
            raise Exception("Cannot load file " + str(e))
        finally:
            f.close()

    def _save_file(self):
        try:
            f = open(self._fileName, "w")

            for obj in self._repo:
                f.write(self._to_string(obj) + "\n")
        except IOError as e:
            raise Exception("cannot write file -"  + str(e))
        finally:
            f.close()

    def _to_string(self, obj):
        return str(obj._id) + "," + obj.imune + "," + obj.status



def t1():
    p1 = Person(1, "vaccinated", "sick")
    repo = Repository()
    repo._add(p1)

    print(repo)

