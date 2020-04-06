

class Person():
    def __init__(self,id, imun, status):
        self._id = id
        self._imun = imun
        self._status = status

    @property
    def id(self):
        return self._id
    @property
    def imun(self):
        return self._imun
    @property
    def status(self):
        return self._status

    def set_imun(self, newVal):
        self._imun = newVal
    def set_id(self, newVal):
        self._id = newVal
    def set_status(self, newVal):
        self._status = newVal

    def __str__(self):
        return str(self._id) +" " + str(self._imun) +" " + str(self._status)
