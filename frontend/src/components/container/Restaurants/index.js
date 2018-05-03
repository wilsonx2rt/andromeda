import { connect } from 'react-redux';
import React, { Component } from 'react';

import './index.css';
import store from '../../../store'
import { fetchRestaurants } from '../../../store/actions/restaurants'
import RestaurantDetail from '../RestaurantDetail'

class Restaurants extends Component {

  constructor(props) {
    super(props);
    this.state = {
      restaurants: ['dasdf', 'asdfasdf', 'sdfasd']
    };
  }
  
  componentDidMount() {
    store.dispatch(fetchRestaurants());
  }

  render() {
    console.log(this.props.restaurants, 'asfasdfdsafsaf')
    return (
      <div>
      { this.props.restaurants.fetching ? <div>LOADING</div> : 
      <div>
        {
      this.props.restaurants.restaurants.map((restaurant, i) =>
        <RestaurantDetail key={ i } name={ restaurant.name } restaurant={ restaurant } />
      )
       }
      </div> } </div>
    )
  }
}

const mapStateToProps = (state) => ({
  restaurants: state.restaurants
});

export default connect(mapStateToProps)(Restaurants)



