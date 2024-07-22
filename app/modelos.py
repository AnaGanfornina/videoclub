from abc import ABC, abstractmethod
import csv

class Director:
    def __init__(self,nombre : str,id:int = -1): 
        self.nombre = nombre
        self.id = id

    def __repr__(self) -> str:
        return f"Director ({self.id}): {self.nombre}"
    
    def __eq__(self, other: object) -> bool:

        if  isinstance(other,self.__class__):
            return self.id == other.id and self.nombre == other.nombre
        
        return False
    
        #if isinstance(other, Director):                        
            #return self.id == other.id and self.nombre == other.nombre
        #return False
    
    def __hash__(self):
        return hash((self.id, self.nombre))

    
class Pelicula():
    def __init__(self,titulo :str,sinopsis:str,id_director:int , id: int = -1):
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.id_director = id_director
        self.id = id
        self.id_director = None





class DAO(ABC):
    #El ABC lo que hace es que no tengamos que escribr este init de abajo, python lo hace por nosotros
    #def guardar(self,instancia):
       #raise NotImplementedError("No se debe usar el DAO, es una interfaz")
    

    """
    @abstractmethod
    def actualizar(self,instancia):
        pass
    @abstractmethod
    def borrar(self,instancia):
        pass
    @abstractmethod
    def consultar(self,instancia):
        pass
    """
    @abstractmethod
    def todos(self):
        pass

class DAO_CSV_Director(DAO):
    def __init__(self,path):
        self.path = path

    def todos(self):
        with open(self.path,"r",newline="") as fichero:
            lector_csv = csv.DictReader(fichero,delimiter=";",quotechar="'")
            lista = []
            for registro in lector_csv:
                lista.append(Director(registro["nombre"],int(registro["id"])))
        return lista