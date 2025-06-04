import pytest
import sys
import os 
sys.path.append(os.path.join(o.s.path.dirname(__file__), '..' 'app'))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

@pytest.fixture(scope="function")
def db_session():
    """Create a virtual test database for each student case test run."""
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

    