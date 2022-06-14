import { call, put, takeEvery, takeLatest } from 'redux-saga/effects';

// worker Saga: will be fired on USER_FETCH_REQUESTED actions
function* fetchUser(action) {}

function* globalSaga() {
  yield takeLatest('USER_FETCH_REQUESTED', fetchUser);
}

export default globalSaga;
