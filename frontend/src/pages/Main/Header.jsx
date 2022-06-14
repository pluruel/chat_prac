/* eslint-disable no-unused-vars */
import { Button } from '@mui/material';
import { Box } from '@mui/system';
import React, { useCallback } from 'react';
import { useDispatch } from 'react-redux';
import { connectServer } from './store';

function Header({ socket, setSocket }) {
  const dispatch = useDispatch();
  const onClickBtn = useCallback(() => {
    if (socket.current == null) {
      const soc = new WebSocket('ws://localhost:8000/ws');
      soc.onopen = e => {
        soc.send(JSON.stringify({ type: 'system', data: 'handshake' }));
        setSocket(soc);
        dispatch(connectServer());
      };
    } else {
      socket.current.close();
    }
  }, []);

  return (
    <Box
      style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: '16px',
      }}
      marginX={1}
    >
      <Box>채팅하자!</Box>
      <Button onClick={onClickBtn}>Connect</Button>
    </Box>
  );
}

export default Header;
