import { Box } from '@mui/system';
import React, { useRef } from 'react';
import Bottom from './Bottom';
import ChatHistory from './ChatHistory';
import Header from './Header';

function Main() {
  const socket = useRef(null);

  // const onMessage = useCallback(() => {
  //   socket.current.
  // }, []);
  const setSocket = newSoc => {
    socket.current = newSoc;
  };

  return (
    <Box
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        width: '100%',
        height: '100vh',
      }}
    >
      <Box
        style={{
          width: '600px',
          height: 'auto',
        }}
      >
        <Header socket={socket} setSocket={setSocket} />
        <ChatHistory />
        <Bottom socket={socket} setSocket={setSocket} />
      </Box>
    </Box>
  );
}

export default Main;
