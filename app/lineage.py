import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword

def extract_lineage(sql):
    parsed = sqlparse.parse(sql)[0]

    tables = []
    columns = []

    for token in parsed.tokens:
        if token.ttype is Keyword and token.value.upper() == "FROM":
            idx = parsed.token_index(token)
            next_token = parsed.tokens[idx + 2]
            tables.append(str(next_token))

    for token in parsed.tokens:
        if isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                columns.append(identifier.get_name())
        elif isinstance(token, Identifier):
            columns.append(token.get_name())

    return list(set(tables)), list(set(columns))

