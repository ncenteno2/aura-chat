import { useEffect, useState } from "react";

export default function Home() {
    const [messages, setMessages] = useState([]);
    const [newMessage, setNewMessage] = useState("");

    useEffect(() => {
        async function fetchChat() {
            try {
                const res = await fetch("http://localhost:8000/chat");

                if (!res.ok) {
                    setMessage("ERROR");
                    return;
                }

                const data = await res.json();
                setMessage(data.messages);
            } catch {
                setMessage("ERROR: no se pudo conectar al servidor");
            }
        }

        fetchChat();
    }, []);

    async function handleSendMessage() {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: newMessage }),
      });

      if (!response.ok) {
        console.error("Error al enviar el mensaje");
        return;
      }
      setMessages(prev => [...prev, newMessage]); 
      setNewMessage("");
    }


    return (
    <div>
      <div>
        {messages.map((msg, i) => (
          <p key={i}>{msg}</p>
        ))}
      </div>
      <input
        placeholder="Type your message here..."
        value={newMessage}
        onChange={(e) => setNewMessage(e.target.value)}
      />
      <button onClick = {handleSendMessage}>
        Send
      </button>
    </div>
  );
}