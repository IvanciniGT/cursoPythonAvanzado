from servicio.inicializador import base_datos

class ObjetoPersistente(base_datos.Model):

    def guardar(self):
        # SQLAlchemy que lo guarde
        base_datos.session.add(self)
        base_datos.session.commit()
        
    def borrar(self):
        # SQLAlchemy que lo borre
        base_datos.session.delete(self)
        base_datos.session.commit()

    @classmethod
    def recuperarTodos(cls):
        # SQL Alchemy dame todos los objetos de un tipo determinado
        return cls.query.all()
    
    @classmethod
    def recuperar(cls, id):
        # SQL Alchemy dame todos los objetos de un tipo determinado
        return cls.query.get(id)
