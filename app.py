from PySide2 import QtCore, QtWidgets
import _tkinter
import matplotlib.pyplot as plt
from movie import Movie, get_movies

class App(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné club")
        self.setup_ui()
        self.resize(500,500)
        self.setup_connections()
        self.populate_movies()



    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.input_film = QtWidgets.QLineEdit()
        self.bouton_ajouter = QtWidgets.QPushButton("Ajouter un film")
        self.liste_film = QtWidgets.QListWidget()
        self.liste_film.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.bouton_supprimer = QtWidgets.QPushButton("Supprimer le(s) films(s)")


        self.layout.addWidget(self.input_film)
        self.layout.addWidget(self.bouton_ajouter)
        self.layout.addWidget(self.liste_film)
        self.layout.addWidget(self.bouton_supprimer)

    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.liste_film.addItem(lw_item)

    def setup_connections(self):
        self.bouton_ajouter.clicked.connect(self.add_movie)
        self.bouton_supprimer.clicked.connect(self.remove_movie)
        self.input_film.returnPressed.connect(self.add_movie)
        


    def add_movie(self):
        movie_title = self.input_film.text()
        if not movie_title:
            return False

        movie = Movie(movie_title)

        resultat = movie.add_to_movies()

        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.liste_film.addItem(lw_item)
    
        self.input_film.setText("")

            

    def remove_movie(self):
        for selected_item in self.liste_film.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.liste_film.takeItem(self.liste_film.row(selected_item))


        

app = QtWidgets.QApplication([])

win = App()

win.show()

app.exec_()

