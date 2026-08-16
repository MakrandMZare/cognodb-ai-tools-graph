from fastapi import APIRouter, HTTPException
from .db import get_driver

router = APIRouter(prefix="/tools", tags=["tools"])

@router.get("/search")
def search_tools(cap1: str, cap2: str, integration: str, domain: str):
    driver = get_driver()

    try:
      with driver.session() as session:
          result = session.run(
              """
              MATCH (t:Tool)-[:SUPPORTS]->(c1:Capability {name: $cap1})
              MATCH (t)-[:SUPPORTS]->(c2:Capability {name: $cap2})
              MATCH (t)-[:INTEGRATES_WITH]->(:Integration {name: $integration})
              MATCH (t)-[:USED_IN]->(:Domain {name: $domain})
              RETURN DISTINCT t
              """,
              cap1=cap1,
              cap2=cap2,
              integration=integration,
              domain=domain,
          )
          tools = [record["t"] for record in result]
          return {"tools": [dict(tool) for tool in tools]}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database unavailable: {e}")