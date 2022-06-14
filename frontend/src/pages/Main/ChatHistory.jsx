import { Box } from '@mui/system';
import React from 'react';
import { useSelector } from 'react-redux';

function ChatHistory() {
  const { chatHistory } = useSelector(({ main }) => ({
    chatHistory: main.chatHistory,
  }));

  return (
    <Box style={{ height: 'calc(100vh - 160px)' }} border={1} padding={1}>
      <Box style={{ display: 'flex' }}>
        <Box style={{ wordBreak: 'break-all' }}>어서오세요</Box>
      </Box>
      {chatHistory.map(e => (
        <Box style={{ display: 'flex' }}>
          <Box style={{ minWidth: '80px' }}>{`${e.name} : `}</Box>
          <Box style={{ wordBreak: 'break-all' }}>{e.text}</Box>
        </Box>
      ))}
    </Box>
  );
}

export default ChatHistory;
