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
def sample_companies(db_session):
    """Sample companies for testing"""
    google = Company(name="Google", founding_year=1998)
    facebook = Company(name="Facebook", founding_year=2004)
    apple = Company(name="Apple", founding_year=1976)
    db_session.add_all([google, facebook, apple])
    db_session.commit()
    return {"google": google, "facebook": facebook, "apple": apple}

@pytest.fixture
def sample_devs(db_session):
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
    freebie1 = Freebie(iten_name="T-shirt", value=25, dev=sample_devs["hildah"], company=sample_companies["google"])
    freebie2 = Freebie(iten_name="Stickers", value=5, dev=sample_devs["hildah"], company=sample_companies["google"])
    freebie3 = Freebie(iten_name="Mug", value=15, dev=sample_devs["ayim"], company=sample_companies["facebook"])
    freebie4 = Freebie(iten_name="T-shirt", value=30, dev=sample_devs["koba"], company=sample_companies["apple"])
    db_session.add_all([freebie1, freebie2, freebie3, freebie4])
    db_session.commit()
    return{"hildah_tshirt": freebie1, "hildah_stickers": freebie2, "ayim_mug": freebie3, "koba_tshirt": freebie4}
    