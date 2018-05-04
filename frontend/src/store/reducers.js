import { combineReducers } from 'redux';

import {
  ADD_USER,
  ADD_USERS,
  REMOVE_CURRENT_USER,
  SET_CURRENT_USER,
  ADD_RESTAURANT,
  ADD_RESTAURANTS,
  FETCH_RESTAURANTS_BEGIN,
  FETCH_RESTAURANTS_SUCCESS,
  FETCH_RESTAURANTS_FAILURE,
  FETCHING_START,
  FETCH_USERS,
} from './constants';


const initialState = {
  restaurants: [],
  loading: false,
  error: null,
};


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
    case ADD_USER: {
      const { user } = action.payload;
      const newState = {...state, randomUser : action.payload}
      return newState
    }
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
    case FETCHING_START:
    return {
      ...state,
      fetching: true,
    };

    /*
    case FETCH_RESTAURANTS_SUCCESS:
    const restaurants = action.payload;
    const newState = { ...restaurants, loading: false, ...state };
    return newState
    case FETCH_RESTAURANTS_FAILURE:
    return {
      ...state,
      loading: false,
      error: action.payload.error,
      restaurants: []
    };
    */

    case ADD_RESTAURANTS:
      const restaurants = action.payload;
      const newState = { ...state, ...restaurants, fetching: false};
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
