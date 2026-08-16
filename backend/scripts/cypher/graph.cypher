CREATE (t1:Tool {
  id: "tool-1",
  name: "GitHub Copilot",
  vendor: "Microsoft"
})

CREATE (c1:Capability {
  id: "cap-1",
  name: "Code Generation"
})

CREATE (d1:Domain {
  id: "dom-1",
  name: "Software Development"
})

CREATE (i1:Integration {
  id: "int-1",
  name: "VS Code"
})

CREATE (t1)-[:SUPPORTS]->(c1)
CREATE (t1)-[:USED_IN]->(d1)
CREATE (t1)-[:INTEGRATES_WITH]->(i1);