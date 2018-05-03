import {
    API,
    ADD_RESTAURANT,
    ADD_RESTAURANTS,
  } from '../constants';
  
  export const addRestaurants = (restaurants) => ({
    type: ADD_RESTAURANTS,
    payload: { restaurants }
  });
  
  const addRestaurant = (restaurant) => ({
    type: ADD_RESTAURANT,
    payload: { restaurant }
  });
  

  export const fetchRestaurants = () => ({
    type: API,
    url: '/api/restaurants/',
    method: 'GET',
    success: addRestaurants,
  });
  
  export const createRestaurant = (data) => ({
    type: API,
    url: '/api/restaurants/new/',
    method: 'POST',
    data,
    success: addRestaurant,
  });
  