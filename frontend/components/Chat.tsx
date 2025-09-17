import { useEffect, useState } from "react";

export default function Home() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        async function fetchChat() {
            try {
                const res = await fetch("http://localhost:8000/chat");

                if (!res.ok) {
                    setMessage("ERROR");
                    return;
                }

                const data = await res.json();
                setMessage(data.message);
            } catch {
                setMessage("ERROR: no se pudo conectar al servidor");
            }
        }

        fetchChat();
    }, []);

    return (
    <div>
      <p>{message}</p>
    </div>
  );
}