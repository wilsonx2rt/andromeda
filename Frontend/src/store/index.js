import thunk from 'redux-thunk';
import reducers from './reducers';
import { applyMiddleware, createStore } from 'redux';

export default createStore(
  reducers,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
  applyMiddleware(thunk),
);
