from sqlalchemy import create_engine


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self) -> None:
        return self.__engine


db_connection_handler = DBConnectionHandler()
