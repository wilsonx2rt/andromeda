import React, { Component } from 'react';
import { connect } from 'react-redux';
import StarRatingComponent from 'react-star-rating-component';

import './index.css';
import store from '../../../store'
import { fetchRestaurants } from '../../../store/actions/restaurants'

class RestaurantDetail extends Component {
  
  constructor() {
    super();
    this.state = {
      isActive: ''
    }
  }

  render() {
    
    console.log(this.props.details)

    const { id, name, country, street, city, zip, opening_hours, price_level } = this.props.details
    return (
      <div className='RestaurantBox'>
        <div className='RestText'> <span id='title'> {name} </span></div>
        <div className='RestText'>{street}</div>
        <div className='RestText'>{city}</div>
        <div className='RestText'>{price_level}</div>
        <StarRatingComponent
          name="rate1"
          starCount={Math.floor(Math.random() * 5) + 1  }
          value={5}
        />
        <img id='rest' src={opening_hours} alt="" />
      </div>
    )
  }
}

//const mapStateToProps = (state) => ({
//  restaurants: state.restaurants.restaurants
//});

const mapStateToProps = state => {
let restaurants = []
  if(state.restaurants) {
    restaurants = state.restaurants
  }
    return {
      restaurants: restaurants,
    }
}

export default connect(mapStateToProps)(RestaurantDetail)
