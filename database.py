import psycopg2
from yaml_parser import yaml_parser


class DatabaseConnection:
    CONN = None

    def __new__(cls, *args, **kwargs):
        if cls.CONN is None:
            return super().__new__(cls, *args, **kwargs)
        return cls.CONN

    def __init__(self):
        credentials = yaml_parser()
        self.conn = psycopg2.connect(**credentials)
        self.create_table()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS activities (
                id SERIAL PRIMARY KEY,
                activity TEXT,
                type TEXT,
                participants INTEGER,
                price REAL,
                link TEXT,
                key TEXT,
                accessibility REAL
            )
        """
        with self.conn.cursor() as cursor:
            cursor.execute(query)
        self.conn.commit()

    def save_activity(self, activity_data):
        query = (
            "INSERT INTO activities "
            "(activity, type, participants, price, link, key, accessibility)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )

        with self.conn.cursor() as cursor:
            cursor.execute(query, list(activity_data.values()))
        self.conn.commit()

    def get_latest_activities(self, limit=5):
        query = "SELECT * FROM activities ORDER BY id DESC LIMIT %s"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (limit,))
            return cursor.fetchall()
