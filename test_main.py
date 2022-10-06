
import pytest
import requests
import app.controller.diseases

from app.model.entry import Entry
from app.controller.database import EntrezDatabases
from app.controller.diseases import Diseases

from unittest import mock
from unittest.mock import patch

@pytest.fixture
def setup_database():
    return EntrezDatabases()
    
@pytest.fixture
def setup_diseases():
    return Diseases()

def test_entry():
    entry = Entry()
    assert isinstance(entry._entry, list)
    assert isinstance(entry._year, list)

def test_get_database_list(setup_database):
    db_list = setup_database.get_db_list()
    assert isinstance(db_list, list)
    assert len(db_list) > 0 
    assert 'pubmed' in db_list
    assert 'books' in db_list

def test_get_entries_by_year(setup_diseases):
    year, diseases, area = 2019, 'obstetrics', 'UK'
    d = setup_diseases.get_entries_by_year(year, diseases, area)
    assert d == 5856

def test_parse_xml_count():

    def read_response_xml(*args):
        with open('./test/egquery_response.xml', 'r') as file:
            data = file.read()
        return data

    d = Diseases()

    with patch("app.controller.diseases.Diseases.get_response_text", read_response_xml):
        val = d.get_entries_by_year(2010,'Asthma','UK')
  
    assert val == 828052


