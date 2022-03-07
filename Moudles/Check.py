from . import asqlite

def CheckConnection(Connection, filepath) -> None:
    try:
        Connection.cursor()
    except Exception as ex:
        Connection = asqlite.connect(filepath)
