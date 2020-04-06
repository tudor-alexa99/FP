from iterable.iter import Iterable


class Movie_Repository:
    def __init__(self):
        self._movieList = []# Iterable()

    def initialise(self):
        pass
        # movie1= Movie(100, "Titanic", "Lame", "Romance")
        # movie2= Movie(101, "Life Of Pi", "Kids stuff", "Something")
        # movie3= Movie(102, "F&F", "Boys stuff", "Action")
        # movie4 = Movie(103, "Godzilla", "Description", "Fiction")
        # movie5 = Movie(104, "La La Land", "Description", "Musical")
        # movie6 = Movie(105, "Silence of the lambs", "Description", "Thriller")
        # self.__movieList = [movie1, movie2, movie3, movie4, movie5, movie6]
    def __len__(self):
        return len(self._movieList)
    def add(self, new_movie):
        self._movieList.append(new_movie)
    @property
    def iter(self):
        return self._movieList.iter
    def getAll(self):
        return list(self._movieList)

    # def initialise_repository(self):
    #     movie1= Movie(100, "Titanic", "Lame", "Romance")
    #     movie2= Movie(101, "Life Of Pi", "Kids stuff", "Something")
    #     movie3= Movie(102, "F&F", "Boys stuff", "Action")

    def __getitem__(self, item):
        return self._movieList[item]

    def remove(self, pos):
        self._movieList.pop(pos)

    # def update(self, id, title, descr, genre):
    #     for movie in self.__movieList:
    #         if movie.id == id:
    #             movie.descr = descr
    #             movie.title = title
    #             movie.genre = genre

    # def find_by_id(self, id):
    #     for movie in self.__movieList:
    #         if movie.id == id:
    #             return True
    #     return False

    # def toString(self):
    #     lst = []
    #     for movie in self.__movieList:
    #         lst.extend(movie.to_String())
    #     return lst
    def length(self):
        return len(self._movieList)



#movieList = Movie_Repository()

#print(getAll())

#test add too

# def test_toString():
#     movie = Movie(1000, "Title", "descr", "Genre")
#     movie2 = Movie(1001, "Title 2", "descr 2", "Genre 2")
#     rep = Movie_Repository()
#     rep.add( movie )
#     rep.add(movie2)
#     #print(rep.toString())
#     assert len(rep.toString()) %4 == 0
#     assert len(rep.toString()) == 8


#test_toString()


