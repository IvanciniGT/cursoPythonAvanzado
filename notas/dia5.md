https - TLS

Ayuda a frustrarlos 2 tipos de ataques:
- Suplantación de identidad: Phishing
- Man in the middle: Encriptación

Clave simetrica o asimetrica:
      ---------
      
asimetrica: Publica + Privada < Servidor
Cliente <> Servidor


Clave publica se envía en un certificado: Va firmado por una CA
                        Información de autenticación
                              DNI - Policia Nacional
                              
                              
       CARPETA_ENTORNO                 
       VVVVVVV
source ../env/bin/activate


-------

Está funcionando el cliente?        SI
Está funcionando el servidor?       SI

Cómo lo sabemos?            Lo hemos probado...
Cómo lo hemos probado?      Ejecutando + Ver la salida de la ejecución... con qué hemos visto esa salida?
                                                                            CON NUESTROS OJOS

Hemos hecho una prueba CUTRE manual = RUINA GRANDE !!!!!!!

Prueba Unitaria - Mocks

Qué problema tenemos con lo que tenemos hasta ahora?
- Las pruebas a mano no son fiables... porque yo no soy fiable
- Se me va mucho tiempo haciendo pruebas... y cada vez más con las nuevas metodologías (ágiles): 
    SCRUM
    Xtreme programming < TDD

Iteraciones (SPRINT): Cada entre "2 semanas" y 8 semanas hacemos una entra al cliente EN PROD.
Güevon de pruebas.
Entrega 1 - 10 funciones - 10 pruebas???   < min(Complejidad ciclomática)  % Cobertura
Entrega 2 -  5 funciones más - 15 pruebas

Metodologia de desarrollo:
    TDD

PRUEBAS:
  Pruebas dinamicas:  Requieren ejecutar código
    Funcionales:
        Unitarias: Comprobar que una función o componente aislado funciona
        Integración: Comprobar que 2 componentes se comunican bien entre si
        Sistema: Comprobar todo el sistema completo en funcionamiento
        Aceptación: Las que hace el cliente
    Rendimiento
    Carga
    Estres
    HA
    UI
    UX
        
  Pruebas estáticas: Requieren ejecutar código
    Sonarqube: Calidad código



src
    main
        py
        resources < configuracion...
    test
        py
        resources < configuracion, datos