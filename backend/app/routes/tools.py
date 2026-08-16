from fastapi import APIRouter, Query
from app.db import get_driver

router = APIRouter()

@router.get("/search")
def search_tools(cap1: str, cap2: str, integration: str, domain: str):
    driver = get_driver()

    query = """
    MATCH (t:Tool)-[:SUPPORTS]->(c1:Capability {name: $cap1})
    MATCH (t)-[:SUPPORTS]->(c2:Capability {name: $cap2})
    RETURN DISTINCT t
    """

    with driver.session() as session:
        result = session.run(
            query=query,
            cap1=cap1,
            cap2=cap2,
            integration=integration,
            domain=domain
        )

    return [record["t"] for record in result]