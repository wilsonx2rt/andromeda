import { combineReducers } from 'redux';

import {
  ADD_USER,
  ADD_USERS,
  REMOVE_CURRENT_USER,
  SET_CURRENT_USER,
  ADD_RESTAURANT,
  ADD_RESTAURANTS,
} from './constants';


const currentUser = (state = {}, action) => {
  switch (action.type) {
    case SET_CURRENT_USER:
      return Object.assign({}, state, action.payload.user);
    case REMOVE_CURRENT_USER:
      return {};
    default:
      return state;
  }
}

const users = (state = {}, action) => {
  switch (action.type) {
    case ADD_USER:
      const { user } = action.payload;
      return Object.assign({}, state, {
        [user.id]: user,
      });
    case ADD_USERS:
      const { users } = action.payload;
      const newState = { ...state };
      users.forEach(user => {
        newState[user.id] = user;
      });

      return newState;
    default:
      return state;
  }
}

const restaurants = (state = {}, action) => {
  switch (action.type) {
    case ADD_RESTAURANT:
      return state
    case ADD_RESTAURANTS:
      console.log('create Restaurant fired')
      const restaurants = action.payload;
      const newState = { ...restaurants, ...state };
      return newState
    default:
      return state;
  }
}


export default combineReducers({
  currentUser,
  users,
  restaurants,
});
