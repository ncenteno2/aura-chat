import { useNavigate } from 'react-router-dom';

export default function Home() {
    const navigate = useNavigate();

    return (
    <div>
      <h1>Aura Chat</h1>
      <nav>
        <button
        onClick={() => navigate('/register')}
        >Register</button>

        <button
        onClick={() => navigate('/login')}
        >Login</button>

        <button
        onClick={() => navigate('/')}
        >Join as Guest</button>
      </nav>
    </div>
  );
}
