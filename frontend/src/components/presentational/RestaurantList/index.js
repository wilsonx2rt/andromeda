import { List } from 'material-ui';
import React from 'react';
import store from './store';


import RestaurantDetail from '../../containers/RestaurantDetail';
import { fetchRestaurants } from '../../../store/actions/restaurants';

export default ({ restaurants }) =>
  <List>
    {
      restaurants.map(restaurant =>
        <RestaurantDetail key={ restaurant.name } restaurant={ restaurant } />
      )
    }
  </List>
