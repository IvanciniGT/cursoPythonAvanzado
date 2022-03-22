# Orientación a objetos

Paradigma de programación.
Definimos nuestros propios tipos de datos complejos, pueden tener sus propios métodos.

Servidor:
- nombre
- ips
- servicios:
    - nombre
      puertos
      protocolo


# JAVA

class Servidor{
    
    private String nombre;
    public Array<String> ips;
    
    public Servidor(String nombre, Array<String> ips){
        this.nombre=nombre;
        this.ips=ips;
    }
    public void setNombre(String nuevoNombre){
        this.nombre=nuevoNombre;
    }
    public String getNombre(){
        return this.nombre;
    }
}

Servidor servidor_web=new Servidor("servidor.produccion.es", .... );
servidor_web.setNombre(servidor.desarrollo.es");

# Encapsulación