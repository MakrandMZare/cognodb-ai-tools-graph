# cognodb-ai-tools-graph
cognodb AI Projects
Title & summary
“CognoDB AI Tools Graph — Exploring AI tooling via graph relationships”
Use case
Short description, example questions.
Why a graph database?
Explain multi-hop queries, evolving relationships, awkwardness in relational schema.
Data model
Diagram (docs/data-model-diagram.png) with:
Node labels, relationship types, key properties.
Tech stack
Backend, frontend, hosting, CognoDB.
Setup instructions
CognoDB:
Sign up, create c0 instance, copy bolt+s://... URI and password.
Environment variables:
COGNODB_URI, COGNODB_USER=cognodb, COGNODB_PASSWORD.
Backend:
pip install -r backend/requirements.txt
python backend/scripts/seed_data.py
uvicorn app.main:app --host 0.0.0.0 --port 8000
Frontend:
cd frontend && npm install
Set VITE_API_URL in .env (e.g., http://localhost:8000)
npm run dev
Main queries explained
Show Cypher snippets and what they answer.
Screenshots & demo
UI screenshots from docs/ui-screenshots/.
Hosted demo URL.
Link to short screen recording (docs/demo-recording.mp4 or external link).
8. Hosting & deployment
8.1 Backend (Render example)
Create new Web Service from GitHub repo.
Environment:
Runtime: Python.
Start command: uvicorn app.main:app --host 0.0.0.0 --port 8000.
Env vars:
COGNODB_URI, COGNODB_USER, COGNODB_PASSWORD.
Ensure CognoDB instance is reachable from hosting region.
8.2 Frontend (Vercel example)
Import GitHub repo.
Set project root to frontend/.
Set env var VITE_API_URL to backend URL (Render service).
Deploy; verify CORS.