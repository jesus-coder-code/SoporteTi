import mysql.connector;

def connection():
    db = mysql.connector.connect(
        host = "mysql-jesus.alwaysdata.net",
        user = "jesus",
        password = "51246380",
        database = "jesus_soporte"
    )

    return db