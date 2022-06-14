/* eslint-disable no-param-reassign */
import { configureStore, createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: {
    value: 0,
  },
  reducers: {
    incremented: state => {
      // Redux Toolkit allows us to write "mutating" logic in reducers. It
      // doesn't actually mutate the state because it uses the Immer library,
      // which detects changes to a "draft state" and produces a brand new
      // immutable state based off those changes
      state.value += 1;
    },
    decremented: state => {
      state.value -= 1;
    },
    multiple: state => {
      state.value *= 2;
    },
  },
});

const { actions, reducer } = counterSlice;
// Extract and export each action creator by name
export const { incremented, decremented } = actions;
// Export the reducer, either as a default or named export
