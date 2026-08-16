
from .config import CONGODB_URI, CONGODB_USER, CONGODB_PASSWORD
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

driver = None
def get_driver():
    global driver
    if driver is None:
        driver = GraphDatabase.driver(
            CONGODB_URI,
            auth=(CONGODB_USER, CONGODB_PASSWORD),
        )
        driver.verify_connectivity()
    return driver
  
def close_driver():
    global driver
    if driver is not None:
        driver.close()
        driver = None
        