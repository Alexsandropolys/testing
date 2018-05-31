import unittest
from  unittest.mock import MagicMock, Mock, patch
import main


class Generator:
    def iter(self):
        for i in [1, 2, 3]:
            yield i

class LMAO_Consumer:
    def __init__(self, name, kekMock):
        print("Here is " + name + ", and now i'll consume " + kekMock.name)

    @patch('main.Kek')
    def STFU(self, kekMock):
        assert kekMock is main.Kek

# Unittest

class TestClass(unittest.TestCase):
    def test_initialization(self):
      kek = main.Kek("Troll Face", 10)
      self.assertEqual(kek.name, 'Troll Face')
      #self.assertEqual(kek.rofl, 10)

    #def test_secondmarkname(self):
     # car = object.Car("Troll Face", 99000)
      #self.assertTrue(car.second_mark_name("Volga"))

    def test_object(self):
      kek = main.Kek("Troll Face", 10)
      assert isinstance(kek, main.Kek)

    def test_printer(self):
      self.assertTrue(main.Kek.get_rofl_of_old_kek)

if __name__ == "__main__":
    unittest.main()

    kek = main.Kek("Dat feel", 20)
    kek.is_equal_name = MagicMock(return_value="true");
    print(kek.is_equal_name("Absolutely different meme"));

    mock = MagicMock()
    mock.name = "Troll Face"
    mock.rofl = 10

    kek2 = main.Kek("@Is this@ mem", 30)
    kek2.name = mock.name
    print(kek2.name)

    consumer = LMAO_Consumer("Bred", mock);
    consumer.STFU();

    gen = Generator()
    print(list(gen.iter()))

    mock_foo = MagicMock()
    mock_foo.iter.return_value = iter([1, 2, 3])
    print(list(mock_foo.iter()))

    #mock2 = Mock(side_effect=KeyError('llololololololo')) 
    #mock2()
   
