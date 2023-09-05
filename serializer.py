from exceptions import UnexpectedKeyException, UnexpectedValueTypeException


class Serializer:

    def __init__(self, data, model):
        self.data = data
        self.model = model

    def validate(self):
        if not self.data.keys() == self.model.keys():
            raise UnexpectedKeyException()
        if not all(
            [
                isinstance(v, self.model.get(k))
                for k, v in self.data.items()
            ]
        ):
            raise UnexpectedValueTypeException()

    def save(self, conn):
        self.validate()
        conn.save_activity(self.data)
