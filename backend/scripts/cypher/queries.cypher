from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    URI,
    auth=(USER, PASSWORD)
)

schema_query = """
CREATE CONSTRAINT tool_id IF NOT EXISTS
FOR (t:Tool)
REQUIRE t.id IS UNIQUE
"""

with driver.session() as session:
    session.run(schema_query)

print("Schema created")