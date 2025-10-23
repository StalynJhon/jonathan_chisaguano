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
        self.assertEqual(respuesta.status_code, 404)

    def test_contiene_primos_correctos(self):
        # Verifica que los números primos esperados estén en la respuesta
        respuesta = self.app.get('/')
        texto = respuesta.get_data(as_text=True)
        self.assertIn('3', texto)
        self.assertIn('15', texto)
        self.assertNotIn('8', texto)  # 1 no es primo

if __name__ == '__main__':
    unittest.main()
