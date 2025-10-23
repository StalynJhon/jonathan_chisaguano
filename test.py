import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Crea un cliente de prueba de Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_respuesta_exitosa(self):
        # Verifica que la ruta principal responda con código 200
        respuesta = self.app.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_contiene_primos_correctos(self):
        # Verifica que los números primos esperados estén en la respuesta
        respuesta = self.app.get('/')
        texto = respuesta.get_data(as_text=True)

        # Convertimos el string de salida en una lista de enteros
        # Ej: 'Números primos del 1 al 20: [2, 3, 5, 7, 11, 13, 17, 19]'
        lista_str = texto.split(':')[1].strip().strip('[]')
        primos_en_app = [int(n.strip()) for n in lista_str.split(',')]

        # Comprobaciones
        self.assertIn(2, primos_en_app)
        self.assertIn(19, primos_en_app)
        self.assertNotIn(1, primos_en_app)  # 1 no es primo

if __name__ == '__main__':
    unittest.main()
