"""
La clase principal está compuesta del metodo echo, a la que debemos introducir nuestro nombre
y la clase nos saludará
"""


class echo:
    
    def ObtenerNombre( nombre ):
        
        nombre = str(nombre)
        
        #saludamos
        print("Hola "+ nombre +"es un placer conocerte")