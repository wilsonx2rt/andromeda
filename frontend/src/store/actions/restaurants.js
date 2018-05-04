import {
    API,
    ADD_RESTAURANT,
    ADD_RESTAURANTS,
    FETCH_RESTAURANTS_BEGIN,
    FETCH_RESTAURANTS_SUCCESS,
    FETCH_RESTAURANTS_FAILURE,
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
  

export const fetchRestaurantsBegin = () => ({
  type: FETCH_RESTAURANTS_BEGIN
});

export const fetchRestaurantsSuccess = restaurants => ({
  type: FETCH_RESTAURANTS_SUCCESS,
  payload: { restaurants }
});

export const fetchRestaurantsError = error => ({
  type: FETCH_RESTAURANTS_FAILURE,
  payload: { error }
});