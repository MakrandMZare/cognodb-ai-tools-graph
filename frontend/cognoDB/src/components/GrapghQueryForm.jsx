// frontend/src/components/GraphQueryForm.tsx
import * as React from "react";
import { useState } from "react";

interface Tool {
  id: string | number;
  name: string;
  vendor: string;
}

export function GraphQueryForm() {
  const [cap1, setCap1] = useState("Prompt Engineering");
  const [cap2, setCap2] = useState("MLOps");
  const [integration, setIntegration] = useState("Slack");
  const [domain, setDomain] = useState("Enterprise AI");
  const [loading, setLoading] = useState(false);
  const [tools, setTools] = useState<Tool[]>([]);
  const [error, setError] = useState<string | null>(null);

  const runQuery = async () => {
    setLoading(true);
    setError(null);
    try {
      const params = new URLSearchParams({ cap1, cap2, integration, domain });
      const res = await fetch(
        `${import.meta.env.VITE_API_URL}/tools/search?` + params.toString()
      );
      if (!res.ok) throw new Error("API error");
      const data = await res.json();
      setTools(data.tools);
    } catch (e: any) {
      setError("Could not reach the graph API. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  return React.createElement(
    "div",
    null,
    React.createElement("h2", null, "Find AI tools by graph relationships"),
    React.createElement("button", { onClick: runQuery }, "Search"),
    loading && React.createElement("p", null, "Loading..."),
    error && React.createElement("p", { className: "error" }, error),
    !loading && !error && tools.length === 0 && React.createElement("p", null, "No tools found."),
    React.createElement(
      "ul",
      null,
      tools.map((tool) =>
        React.createElement("li", { key: tool.id }, `${tool.name} (${tool.vendor})`)
      )
    )
  );
}