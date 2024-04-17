class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_secret_key'