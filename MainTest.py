import unittest
import os
from CLASES.echo import echo

print("Inicio del método main")

class MainTest(unittest.TestCase):
    #mi primer test
    
    def Test(self):
        #cargamos la clase que deseamos utilizar y verificamos su funcionamiento.
        echo.ObtenerNombre(nombre = "Aitor")
        


if __name__ == '__main__':
    unittest.main()