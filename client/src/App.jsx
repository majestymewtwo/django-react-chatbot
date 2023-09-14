import { useEffect, useRef, useState } from 'react'
import { Chat } from './components/Chat';

function App() {
  const [chats, setChats] = useState([
    {
      type : "bot",
      message : "What can I do for you?"
    }
  ]);
  const [message, setMessage] = useState("");
  const lastMessageRef = useRef(null);

  const sendQuery = async (e) => {
    setChats((chats) => [...chats, {
      type : "user",
      message : message
    }]);
    setMessage("");
    e.preventDefault();
    const response = await fetch("http://localhost:8000/chatbot/get-response/", {
      method : "POST",
      headers : {
        "Content-Type" : "application/json",
      },
      body : JSON.stringify({
        user_query : message
      })
    });
    const data = await response.json();
    setChats((chats) => [
      ...chats,
      {
        type: "bot",
        message: data.bot_response,
      },
    ]);
  }

  useEffect(() => {
    lastMessageRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chats])

  return (
    <section className='bg-gradient-to-br from-[#E4F1FF] to-[#8ECDDD] h-screen px-20'>
      <div className='py-10 text-[#27005D] h-[20%]'>
        <h1 className='font-bold text-2xl tracking-tight'>
          Substation Asset Maintanence - Chatbot
        </h1>
        <p className='text-sm'>
          Unlock instant answers on substation maintenance with our chatbot!
          Expertise at your fingertips, 24/7.
        </p>
      </div>
      {/* Chats */}
      <div className='h-[70%] overflow-y-scroll space-y-3 w-full'>
        {chats.map((chat, index) => (
          <Chat key={index} type={chat.type} message={chat.message} ref={index===chats.length-1 ? lastMessageRef : null} />
        ))}
      </div>
      <form onSubmit={sendQuery} className='h-[10%] flex justify-center items-center'>
        <input
          type='text'
          spellCheck={false}
          placeholder='Ask a question'
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          className='w-[90%] focus:outline-none px-4 py-2 rounded-l-lg text-sm text-slate-700'
        />
        <button className='bg-gradient-to-br from-[#016A70] to-[#183D3D] text-white px-3 py-2 rounded-r-lg'>
          Ask
        </button>
      </form>
    </section>
  );
}

export default App
