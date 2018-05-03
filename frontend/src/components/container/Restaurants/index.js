import { connect } from 'react-redux';
import React, { Component } from 'react';

import './index.css';
import store from '../../../store'
import { fetchRestaurants } from '../../../store/actions/restaurants'


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
    return (
      <div> ReASDF </div>
    )
  }
}

const mapStateToProps = (state) => ({
  restaurants: state.restaurants
});

export default connect(mapStateToProps)(Restaurants)



