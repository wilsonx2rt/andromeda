import { combineReducers } from 'redux';

import {
  ADD_USER,
  ADD_USERS,
  REMOVE_CURRENT_USER,
  SET_CURRENT_USER,
  TOGGLE_FOLLOW
} from './constants';


const currentUser = (state = {}, action) => {
  switch (action.type) {
    case SET_CURRENT_USER:
      return Object.assign({}, state, action.payload.user);
    case TOGGLE_FOLLOW:
      const newUser = { ...state };
      const toggleFollowId = action.payload.userId;
      newUser.follows = newUser.follows.indexOf(toggleFollowId) > -1
        ? newUser.follows.filter(followId => followId !== toggleFollowId)
        : [...newUser.follows, toggleFollowId];

      return newUser;
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
        [user._id]: user,
      });
    case ADD_USERS:
      const { users } = action.payload;
      const newState = { ...state };
      users.forEach(user => {
        newState[user._id] = user;
      });

      return newState;
    default:
      return state;
  }
}


export default combineReducers({
  currentUser,
  users,
});
