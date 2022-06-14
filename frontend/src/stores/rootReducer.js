import { configureStore } from '@reduxjs/toolkit';
import mainReducer from '../pages/Main/store';

export const store = configureStore({
  reducer: {
    main: mainReducer,
  },
});
export default store;
