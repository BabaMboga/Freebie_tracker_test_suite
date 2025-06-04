import pytest
from sqlalchemy.inspection import inspect

"""Deliverables checklist based off on question"""

@pytest.mark.deliverable
class TestMigrationDeliverables:
    """Migration requirements if their models run"""

    def test_freebies_table_exists(self, db_session):
        inspector = inspect(db_session.bind)
        tables = inspector.get_table_names()
        assert 'freebies' in tables, "Freebies table not found"

    def test_freebies_table_structure(self, db_session):
        inspector = inspect(db_session.bind)
        columns = [col['name'] for col in inspector.get_columns('freebies')]
        required_columns = ['id', 'item_name', 'value', 'dev_id', 'company_id']
        for col in required_columns:
            assert col in columns, f"column '{col}' missing from freebies table"

@pytest.mark.deliverable
class TestRelationshipDeliverables:
    """Testing relationship requirements"""

    def test_freebie_dev_relationship(self, sample_freebies, sample_devs):
        """test freebie.dev returns a dev instance"""
        freebie = sample_freebies["hildah_tshirt"]
        assert freebie.dev == sample_devs["hildah"]

    def test_freebie_company_relationship(self, sample_freebies, sample_companies):
        """Freebie.company returns company instance"""