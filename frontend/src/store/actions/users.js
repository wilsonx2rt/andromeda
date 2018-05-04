import {
    urlBase,
    API,
    ADD_USER,
    ADD_USERS
  } from '../constants';
  
  export const addUser = (user) => ({
    type: ADD_USER,
    payload: { user }
  });
  
  const addUsers = (users) => ({
    type: ADD_USERS,
    payload: { users },
  });

  
  /*
  export const fetchUser = () => {

    return fetch(`https://randomuser.me/api/`)
    .then(res => console.log(res.json()))
    .then(data => {

    .catch(err => {
        console.log('in da fetchUser error');
        console.log(err);
      })
  }
*/