import { connect } from 'react-redux';
import React, { Component } from 'react';

import { login } from '../../../store/actions/currentUser';
import './index.css';
import Container from '../../../components/presentational/Container';
import RestaurantDetail from './RestaurantDetail'


class Restaurants extends Component {

  constructor(props) {
    super(props);

    this.state = {
      activeTab: 'restaurants',
    };
  }

  render() {
    return (
    <RestaurantDetail/>
    )
  }
}

export default Restaurants
