import unittest
from serializer import Serializer
from exceptions import UnexpectedKeyException, UnexpectedValueTypeException


class TestSerializer(unittest.TestCase):
    test_model = {
        "param1": int,
        "param2": str
    }

    def test_validation(self):
        test_ser1 = Serializer(
            model=self.test_model,
            data={"param3": 3, "param4": "pupa"}
        )
        self.assertRaises(UnexpectedKeyException, test_ser1.validate)

        test_ser2 = Serializer(
            model=self.test_model,
            data={"param3": 3, "param4": "pupa", "key": 5}
        )
        self.assertRaises(UnexpectedKeyException, test_ser2.validate)

        test_ser3 = Serializer(
            model=self.test_model,
            data={"param1": "3", "param2": "pupa"}
        )
        self.assertRaises(UnexpectedValueTypeException, test_ser3.validate)

        test_ser4 = Serializer(
            model=self.test_model,
            data={"param1": 3, "param2": "pupa"}
        )
        test_ser4.validate()


if __name__ == "__main__":
    unittest.main()
