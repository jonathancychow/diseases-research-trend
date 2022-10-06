from enum import Enum

class EInfoField(Enum):
    RETMODE = 'retmode'
    RESULT = 'einforesult'
    DB_LIST = 'dblist'

class EUtilityField(Enum):
    TERM = 'term'

class EQueryField(Enum):
    COUNT = 'Count'
    RESULT = 'eGQueryResult'
    ITEM = 'ResultItem'
    ERROR = 'Error'

class ESearchField(Enum):
    RESULT = 'esearchresult'
    RETMAX = 'retmax'
    RETMODE = 'retmode'
    DATATYPE = 'datetype'
    TERM = 'term'
    DB = 'db'
    COUNT = 'count'

