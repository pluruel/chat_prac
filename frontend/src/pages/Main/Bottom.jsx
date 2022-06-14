/* eslint-disable no-unused-vars */
import { Button, Input } from '@mui/material';
import { Box } from '@mui/system';
import React, { useCallback } from 'react';
import { useSelector } from 'react-redux';

function Bottom({ socket }) {
  const { socketStatus } = useSelector(({ main }) => ({
    socketStatus: main.socketStatus,
  }));

  return (
    <Box
      style={{
        width: 'auto',
        display: 'flex',
        justifyContent: 'space-between',
      }}
      marginX={1}
    >
      {socketStatus === 1 ? (
        <>
          <Input color="info" style={{ width: '100%' }} />
          <Button style={{ marginLeft: '8px' }} color="info">
            Send
          </Button>
        </>
      ) : (
        <Box> Connect를 통해 매칭! </Box>
      )}
    </Box>
  );
}

export default Bottom;
