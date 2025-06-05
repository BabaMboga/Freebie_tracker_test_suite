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
        freebie = sample_freebies["hildah_tshirt"]
        assert freebie.company == sample_companies["google"]

    def test_company_freebie_relationships(self, sample_freebies, sample_companies):
        """company.freebies returns collection of freebies"""
        google = sample_companies["google"]
        assert len(google.freebies) == 2
        assert hasattr(google, 'freebies')

    def test_company_devs_relationship(self, sample_freebies, sample_companies):
        """company.devs returns collection of devs"""

        google = sample_companies["google"]
        assert len(google.devs) == 2
        dev_names = [d.name for d in google.devs]
        assert "Alice" in dev_names and "Bob" in dev_names

    def test_dev_freebies_relationship(self, sample_freebies, sample_devs):
        """dev.freebies returns collection of freebies"""
        hildah = sample_devs["hildah"]
        assert len(hildah.freebies) == 2
        assert hasattr(hildah, 'freebies')

    def test_dev_companies_relationship(self, sample_freebies, sample_devs):
        """ dev.companies returns collection of companies"""
        hildah = sample_devs["hildah"]
        assert len(hildah.companies) == 2
        company_names = [c.name for c in hildah.companies]
        assert "Goodle" in company_names and "Facebook" in company_names

@pytest.mark.deliverable
class TestAggregateMethodDelivaries:
    """Aggregate method test"""

    def test_freevie_print_details(safe, sample_freebies):
        """Freebie.print_details() returns formatted string"""
        freebie = sample_freebies["hildah_tshirt"]
        expected =  "Hildah owns a T-shirt from Google."
        assert freebie.print_details() == expected

    def test_compaby_give_freebie(self, db_session, sample_companies, sample_devs):
        """Company.give_freebie() creates new freebie"""
        google = sample_companies["google"]
        hildah = sample_devs["hildah"]
        initial_count = len(google.freebies)

        new_freebie = google.give_freebie(hildah, "Notebook", 10)
        db_session.commit()

        assert new_freebie.item_name == "Notebook"
        assert new_freebie.value == 10
        assert new_freebie.dev == hildah
        assert new_freebie.company == google
        assert len(google.freebies) == initial_count + 1

    def test_company_oldest_company(self, sample_companies):
        """Company.oldest_company returns oldest company"""
        oldest = Company.oldest_company()
        assert oldest.name == "Apple"
        assert oldest.founding_year == 1976

    def test_dev_received_one_true(self, sample_freebies,sample_devs):
        """Dev.received_one() returns true when item exists"""
        hildah = sample_devs["hildah"]
        assert hildah.received_one("T-shirt") is True

    def test_dev_received_one_false(self, sample_freebies, sample_devs):
        """Dev.received_one() returns false when item does not exist"""
        hildah = sample_devs["hildah"]
        assert hildah.received_one("Laptop") is False

    def test_dev_give_away_valid(self,db_session, sample_freebies, sample_devs):
        """Dev.give_away() transfers freebie when valid"""
        hildah = sample_devs["hildah"]
        ayim = sample_devs["ayim"]
        freebie = sample_freebies["hildah_tshirt"]

        hildah.give_away(ayim, freebie)
        db_session.commit()

        assert freebie.dev == ayim
        assert freebie in ayim.freebies
        assert freebie not in hildah.freebies

"""test summary"""

def test_deliverable_summary():
    deliverables = {
        "Migration - Freebies table exists": "test_freebies_table_exists",
        "Migration - Correct table structure": "test_freebies_table_structure", 
        "Relationship - Freebie.dev": "test_freebie_dev_relationship",
        "Relationship - Freebie.company": "test_freebie_company_relationship",
        "Relationship - Company.freebies": "test_company_freebies_relationship",
        "Relationship - Company.devs": "test_company_devs_relationship",
        "Relationship - Dev.freebies": "test_dev_freebies_relationship",
        "Relationship - Dev.companies": "test_dev_companies_relationship",
        "Method - Freebie.print_details()": "test_freebie_print_details",
        "Method - Company.give_freebie()": "test_company_give_freebie",
        "Method - Company.oldest_company()": "test_company_oldest_company",
        "Method - Dev.received_one() True": "test_dev_received_one_true",
        "Method - Dev.received_one() False": "test_dev_received_one_false", 
        "Method - Dev.give_away()": "test_dev_give_away_valid"
    }

    print(f"\n=== DELIVERABLE CHECKLIST ({len(deliverables)} total) ===")
    for desc, test_name in deliverables.items():
        print(f"□ {desc}")
    print("=" * 50)

    