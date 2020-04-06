
class Movie:
    def __init__(self, id, title, descr, genre):
        self.__id = id
        self.__title = title
        self.__descr = descr
        self.__genre = genre
    @property
    def id(self):
        return int(self.__id)

    @property
    def title(self):
        return self.__title

    @property
    def descr(self):
        return self.__descr

    @property
    def genre(self):
        return self.__genre

    @id.setter
    def id(self, new_ID):
        self.__id = new_ID

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @descr.setter
    def descr(self, new_descr):
         self.__descr = new_descr
    @genre.setter
    def genre(self, new_genre):
        self.__genre = new_genre

    def to_String(self):
        return [str(self.id), self.title, self.descr, self.genre]

    def __str__(self):
        return "<Id: " + str(self.__id) + "    ||    Title: " + self.__title + "   || Description: " + self.__descr + "   || Genre: " + self.__genre + ">"

# mov = Movie(123, "Titanic", "Lovely", "Romance")
# print(mov)
#
# print(mov.id)
# mov.id = 100
#
# #mov.id.setter(100)
#
# print(mov.id)