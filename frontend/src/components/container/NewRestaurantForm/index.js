import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { createRestaurant } from '../../../store/actions/restaurants';
import './index.css';

class NewRestaurantForm extends Component {

  constructor(props) {
    super(props);

    this.state = {
      restaurant_name: '',
      country: '',
      city: '',
      street: '',
      zip_code: '',
      opening_hours: '',
      price_level: '',
    }
  }

  handleNameChange = (e, restaurant_name) => {
    this.setState({ restaurant_name });
  }
  handleCountryChange = (e, country) => {
    this.setState({ country });
  }
  handleCityChange = (e, city) => {
    this.setState({ city });
  }
  handleStreetChange = (e, street) => {
    this.setState({ street });
  }
  handleZipCodeChange = (e, zip_code) => {
    this.setState({ zip_code });
  }
  handleOpeningChange = (e, opening_hours) => {
    this.setState({ opening_hours });
  }
  handlePriceLevelChange = (e, price_level) => {
    this.setState({ price_level });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    this.props.createRestaurant({ content: this.state.content });
    this.setState({ content: '' });
  }

  render() {
    return (
      <div className="NewRestaurantForm">
        <form onSubmit={this.handleSubmit}>
          <div className='NewRestaurantTitel'> <span>CREATE NEW RESTAURANT</span> <hr></hr></div>
          <span>Name</span>
          <input className='Field' onChange={this.handleNameChange} type="text" value={this.state.restaurant_name} />
          <span>Country</span>
          <input className='Field' onChange={this.handleCountryChange} type="text" value={this.state.country} />
          <span>City</span>
          <input className='Field' onChange={this.handleCityChange} type="text" value={this.state.city} />
          <span>Street</span>
          <input className='Field' onChange={this.handleStreetChange} type="text" value={this.state.street} />
          <span>Zip code</span>
          <input className='Field' onChange={this.handleZipCodeChange} type="text" value={this.state.zip_code} />
          <span>Opening houers</span>
          <input className='Field' onChange={this.handleOpeningChange} type="text" value={this.state.opening_hours} />
          <button className='SubmitButton' type="submit"> Submit </button>
        </form>
      </div>
    )
  }
}

const mapDispatchToProps = (dispatch) => ({
  createRestaurant: (data) => dispatch(createRestaurant(data))
});

export default connect(null, mapDispatchToProps)(withRouter(NewRestaurantForm));