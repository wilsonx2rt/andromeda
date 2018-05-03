import {
  API,
  urlBase,
  REMOVE_CURRENT_USER,
  SET_CURRENT_USER,
} from '../constants';

const setCurrentUser = (user) => ({
  type: SET_CURRENT_USER,
  payload: { user }
});

const removeCurrentUser = () => ({
  type: REMOVE_CURRENT_USER,
})

export const login = (data) => (dispatch) => {
  const myHeaders = new Headers({
    'Content-Type': 'application/json'
  });
  let config = {
    method: 'POST',
    headers: myHeaders,
    body: JSON.stringify(data),
  };

 return fetch(`${urlBase}/api/token/`, config)
        .then(res => res.json())
        .then(user => {
          const action = setCurrentUser(user);
          dispatch(action);
          localStorage.setItem('userToken', JSON.stringify(user.access));
          console.log(user.Token)
          console.log(user.token, "request")
        })
        .catch(err => {
          console.log(err);
        })
}

const registerUser = (user) => (dispatch) => {
  const action = setCurrentUser(user);
  dispatch(action);
  localStorage.setItem('userToken', JSON.stringify(user.token));
}

export const register = (data) => ({
  type: API,
  url: '/api/registration/',
  method: 'POST',
  success: registerUser,
  data,
});

export const logout = () => (dispatch) => {
  const action = removeCurrentUser();
  dispatch(action);
  localStorage.clear();
}

export const fetchCurrentUser = () => ({
  type: API,
  url: '/api/me/',
  success: setCurrentUser,
});

export const fetchLocalUser = () => (dispatch) => {
  const userToken = localStorage.getItem('userToken');
  if (userToken) {
    dispatch(setCurrentUser({ token: userToken }));
  }
}