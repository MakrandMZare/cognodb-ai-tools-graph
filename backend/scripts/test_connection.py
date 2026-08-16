import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("CONGODB_URI")
user = os.getenv("CONGODB_USER")
password = os.getenv("CONGODB_PASSWORD")

driver = GraphDatabase.driver(uri, auth=(user, password))

with driver.session() as session:
    result = session.run("RETURN 'Connected Successfully' AS message")

    for record in result:
        print(record["message"])