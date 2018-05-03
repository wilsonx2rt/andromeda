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
    
    const img = 'https://www.ahstatic.com/photos/3373_ho_00_p_2048x1536.jpg'
    const title = 'Bullshit Restaurant'
    const adress = 'zürich 04434'
    const rating = 5


    //const { id, name, country, street, city, zip, opening_hours, price_level } = this.props.restaurants
    return (
      <div className='RestaurantBox'>
        <div className='RestText'>{this.props.name}</div>
        <div className='RestText'>{adress}</div>
        <StarRatingComponent
          name="rate1"
          starCount={5}
          value={rating}
        />
        <img id='rest' src={img} alt="" />
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
