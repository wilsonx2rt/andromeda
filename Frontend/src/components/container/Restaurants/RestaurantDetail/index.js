import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import StarRatingComponent from 'react-star-rating-component';

import './index.css';

class RestaurantDetail extends Component {
  constructor() {
    super();
    this.state = {
      isActive : ''
    }
  }

  render() {
    const img = 'https://www.ahstatic.com/photos/3373_ho_00_p_2048x1536.jpg'
    const title = 'Bullshit Restaurant'
    const review = 3
    const adress = 'zürich 04434'
    const rating = 5

    return (
      <div className='RestaurantBox'>
        <div className='RestText'>{title}</div>
        <div  className='RestText'>{adress}</div>
        <StarRatingComponent 
          name="rate1" 
          starCount={5}
          value={rating}
        />
        <img id='rest' src={img} alt=""/>
      </div>
    )
  }
}

export default connect()(RestaurantDetail);
