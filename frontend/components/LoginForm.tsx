import { useState } from "react";

export default function LoginForm() {
  const[username,setUsername] = useState("")
  const[password,setPassword] = useState("")
  const[message,setMessage] = useState("")

  async function handleLogIn() {
    const response = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username: username, password: password }),
    });

    const data = await response.json();
    setMessage(data.message);
  }

  return (
    <div>
      <div>
        <h2>Login</h2>
        <input
          placeholder="Ingresar usuario"
          onChange={(e)=>setUsername(e.target.value)}>
        </input>
      </div>
      <div>
        <input
          type="password"
          placeholder="Ingresar contraseña"
          onChange={(e)=>setPassword(e.target.value)}>
        </input>
      </div>
      <button
      onClick={handleLogIn}>
        Log In
      </button>
      {message && <p>{message}</p>}
    </div>
  );
}