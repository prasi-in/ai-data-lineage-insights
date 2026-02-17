from fastapi import FastAPI
from pydantic import BaseModel
from app.lineage import extract_lineage
from app.llm import generate_description
from app.graph_builder import build_graph

app = FastAPI(title="AI Data Lineage Insights")

class SQLRequest(BaseModel):
    sql: str

@app.post("/analyze")
def analyze_sql(request: SQLRequest):
    tables, columns = extract_lineage(request.sql)

    ai_descriptions = {}
    for table in tables:
        ai_descriptions[table] = generate_description(table)

    graph = build_graph(tables)

    return {
        "tables": tables,
        "columns": columns,
        "ai_descriptions": ai_descriptions,
        "lineage_graph": graph
    }

