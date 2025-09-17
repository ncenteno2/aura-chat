// import { useState } from 'react'
import { Routes, Route } from 'react-router-dom';
import Home from '../components/Home'
import Login from '../components/LoginForm'
import Chat from '../components/Chat'
import './App.css'

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/chat" element={<Chat />} />
      </Routes>
    </>
  )
}

export default App
