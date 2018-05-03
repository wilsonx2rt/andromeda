import thunk from 'redux-thunk';
import { applyMiddleware, createStore } from 'redux';
import apiMiddleware from './apiMiddleware';

import reducers from './reducers';

export default createStore(
  reducers,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
  applyMiddleware(thunk, apiMiddleware),
);
