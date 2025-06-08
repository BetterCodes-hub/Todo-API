from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
#Ustawia połączenie z bazą danych PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/tododb")
#Przygotowuje silnik połączeń i sesje.
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()