import configparser

class Config:
    pass

class DatabaseConfig(Config):
    def load(self):
        config = configparser.ConfigParser()
        config.read("db.ini")

        if "DATABASE" not in config:
            print("DATABASE section missing")
            return

        required = ["host", "user", "password"]

        for key in required:
            if key not in config["DATABASE"]:
                print(key, "missing")
                return

        print("Configuration Loaded")
        print(dict(config["DATABASE"]))

db = DatabaseConfig()
db.load()