import unittest
import web
import suma

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = web.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        assert b'Hola mundo' in rv.data

if __name__ == '__main__':
    unittest.main()



class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(mymodule.sum(5, 7), 12)
if __name__ == "__main__":
    unittest.main()