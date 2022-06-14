/* eslint-disable no-param-reassign */
import { createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'chat',
  initialState: {
    chatHistory: [],
    socketStatus: 'DISCONNECT',
  },
  reducers: {
    receiveChat: (state, action) => {
      state.chatHistory = state.chatHistory.concat(action.payload);
    },
    clearChat: state => {
      state.chatHistory = [];
    },
    connectServer: state => {
      state.socketStatus = 'CONNECT';
    },
    disConnectServer: state => {
      state.socketStatus = 'DISCONNECT';
    },
    matchedPartner: state => {
      state.socketStatus = 'MATCHED';
    },
  },
});

const { actions, reducer: mainReducer } = counterSlice;
// Extract and export each action creator by name
export const { receiveChat, clearChat, connectServer, disConnectServer } =
  actions;
// Export the reducer, either as a default or named export
export default mainReducer;
