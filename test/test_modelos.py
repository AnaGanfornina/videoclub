from app.modelos import Director, DAO_CSV_Director,Pelicula,Director,DAO_CSV_Peliculas


def test_crate_director():
    director = Director ("Robert Redford")

    assert director.nombre == "Robert Redford"
    assert director.id == -1

def test_directores_traer_todos():
    dao = DAO_CSV_Director("test/data/directores.csv")
    directores = dao.todos()

    assert len(directores) == 8
    assert directores[7] == Director ("Charlie Chaplin",8)

def test_create_pelicula():
    pelicula = Pelicula("El señor de los anillos","Sauron es mu malo",9)
    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es mu malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula.director is None

def test_create_pelicula_and_informar_director_completo():
    director = Director("Peter Jackson",9)
    pelicula = Pelicula("El señor de los anillos","Sauron es mu malo",9)

    pelicula = Pelicula("El señor de los anillos","Sauron es mu malo",director)
    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es mu malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula.director == director
def test_asigna_director_a_pelicula():

    pelicula = Pelicula("El señor de los anillos","Sauron es mu malo",-1)

    director = Director("Peter Jackson",9)
    
    pelicula.director = director

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es mu malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula.director == director

def test_dao_peliculas_traer_todos():
    dao = DAO_CSV_Peliculas("test/data/peliculas_test.csv")
    peliculas = dao.todos()

    assert len(peliculas) == 5
    assert peliculas[1] == Pelicula("Los siete samuráis","Una banda de forajidos atemorizan a los habitantes de un pequeño pueblo, saqueándolos periódicamente sin piedad. Para repeler estos ataques, los aldeanos deciden contratar a mercenarios. Finalmente, consiguen los servicios de 7 guerreros, 7 samurais dispuestos a defenderlos a cambio, tan solo, de cobijo y comida.",2,17)
     