from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("CONGODB_URI")
user = os.getenv("CONGODB_USER")
password = os.getenv("CONGODB_PASSWORD")

driver = GraphDatabase.driver(uri, auth=(user, password))

def seed(tx):
    tx.run("MATCH (n) DETACH DELETE n")  # Clear existing data
    tx.run("""
           CREATE (t1:Tool {id: 'tool-1', name: 'Copilot', vendor: 'Microsoft', category: 'Assistant'})
           CREATE (t2:Tool {id: 'tool-2', name: 'ChatGPT', vendor: 'OpenAI', category: 'Assistant'})
           CREATE (c1:Capability {id: 'cap-1', name: 'Prompt Engineering'})
           CREATE (c2:Capability {id: 'cap-2', name: 'Code Generation'})
           CREATE (d1:Domain {id: 'domain-1', name: 'Artificial Intelligence'}
           CREATE (i1:Integration {id: 'integration-1', name: 'Slack Integration', type: 'Chat'})
           CREATE (t1)-[:SUPPORTS]->(c1)
           CREATE (t2)-[:SUPPORTS]->(c2)
           CREATE (t1)-[:USED_IN]->(d1)
           CREATE (t2)-[:USED_IN]->(d1)
           CREATE (t1)-[:INTEGRATES_WITH]->(i1)
           CREATE (c1)-[:RELATED_TO]->(c2)
           """)
    

if __name__ == "__main__":
    with driver.session() as session:
        
      session.execute_write(seed)
      driver.close()