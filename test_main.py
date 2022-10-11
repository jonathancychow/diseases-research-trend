
import json
import pytest

from app.model.entry import Entry
from app.controller.database import EntrezDatabases
from app.controller.diseases import Diseases
from app.controller.enum import EInfoField

from unittest.mock import patch

@pytest.fixture
def setup_database():
    return EntrezDatabases()
    
@pytest.fixture
def setup_diseases():
    return Diseases()

def test_entry():
    entry = Entry()
    assert isinstance(entry.entry, list)
    assert isinstance(entry.year, list)

def test_get_database_valid_einforesult(setup_database):

    def mock_einforesult_valid(*args):
        with open('./test/einfo_response.json', 'r') as file:
            data = json.load(file)
        return data

    with patch("app.controller.database.EntrezDatabases.get_response_json", mock_einforesult_valid):
        db_list = setup_database.get_db_list()

    assert 'pubmed' in db_list
    assert mock_einforesult_valid()[EInfoField.RESULT.value][EInfoField.DB_LIST.value] == db_list

def test_get_database_invalid_einforesult(setup_database):

    def mock_einforesult_invalid(*args):
        return {
                "header": {
                    "type": "einfo",
                    "version": "0.3"
                }}

    with patch("app.controller.database.EntrezDatabases.get_response_json", mock_einforesult_invalid):
        db_list = setup_database.get_db_list()
    
    assert isinstance(db_list, list)
    assert db_list == []

def test_get_database_list(setup_database):
    db_list = setup_database.get_db_list()
    assert isinstance(db_list, list)
    assert len(db_list) > 0 
    assert 'pubmed' in db_list
    assert 'books' in db_list

def test_get_entries_by_year(setup_diseases):
    year, diseases, area = 2019, 'obstetrics', 'UK'
    entry = setup_diseases.get_entries_by_year(year, diseases, area)
    assert entry == 5856

def test_parse_xml_count():

    def read_response_xml(*args):
        with open('./test/egquery_response.xml', 'r') as file:
            data = file.read()
        return data

    diseases = Diseases()

    with patch("app.controller.diseases.Diseases.get_response_text", read_response_xml):
        entry = diseases.get_entries_by_year(2010,'Asthma','UK')
  
    assert entry == 828052
