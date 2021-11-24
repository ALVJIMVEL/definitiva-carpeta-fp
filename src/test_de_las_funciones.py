from funciones_de_proyecto import Ethereum


from funciones_de_proyecto import funcion_lectura
def test_funcion_lectura():
    test_lect= funcion_lectura('data/Ethereum Historical Data.csv')
    print(test_lect[:3])
test_funcion_lectura()
#con esta funcion comprobamos que la función de lectura funciona correctamente

