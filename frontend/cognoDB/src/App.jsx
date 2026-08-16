import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/`)
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => console.error(err));
  }, []);


  const cap1 = "Prompt Engineering";
  const cap2 = "MLOps";
  const integration = "Slack";
  const domain = "Enterprise AI";

  fetch(
    `${import.meta.env.VITE_API_URL}/tools/search?cap1=${encodeURIComponent(cap1)}&cap2=${encodeURIComponent(cap2)}&integration=${encodeURIComponent(integration)}&domain=${encodeURIComponent(domain)}`
  )
    .then((res) => res.json())
    .then((data) => console.log(data));

  return (
    <div>
      <h1>React + FastAPI Test</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;