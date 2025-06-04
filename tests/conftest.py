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

@pytest.fixture
def sample_devs(db_sesion):
    """create sample devs for testing based on given code challenge"""
    hildah = Dev(name="Hildah")
    ayim = Dev(name="Ayim")
    koba = Dev(name="Koba")
    db_session.add_all([hildah, ayim, koba])
    db_session.commit()
    return {"hildah": hildah, "ayim":ayim, "koba":koba}


@pytest.fixture
def sample_freebies(db_session, sample_companies, sample_devs):
    """Create sample freebies"""
    freebie1 = 
    freebie2 = 
    freebie3 =
    freebie4 = 