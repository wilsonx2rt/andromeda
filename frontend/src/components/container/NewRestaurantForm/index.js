import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { createRestaurant } from '../../../store/actions/restaurants';
import './index.css';

class NewRestaurantForm extends Component {

  constructor(props) {
    super(props);

    this.state = {
      Creator: 'superuser',
      Restaurant_name: '',
      Country: 'Switzerland',
      City: '',
      Street: '',
      Zip_code: '',
      Opening_hours: '',
      Price_level: '',
    }
  }

  handleChange = e => {
    this.setState({
      [e.target.id]: e.target.value
    });
  };


  handleSubmit = (e) => {
    console.log(this.state)
    e.preventDefault();
    this.props.createRestaurant({ ...this.state })
    //.then(() => this.props.history.push('/'));
  }

  render() {
    return (
      <div className="NewRestaurantForm">
        <form onSubmit={this.handleSubmit}>
        <div id='title-wraper'>
          <div className='NewRestaurantTitel'> <span>CREATE NEW RESTAURANT</span> <hr></hr></div>
        </div>
          <div id='restaurant-form-flex-container'>
            <div>
              <span>Name</span>
              <input className='Field' id='Restaurant_name' onChange={this.handleChange} type="text" />
            </div>
            <div>
              <span>Country</span>
              <input className='Field' id='Country' onChange={this.handleChange} type="text" /> 
            </div>
            <div>
              <span>City</span>
              <input className='Field' id='City' onChange={this.handleChange} type="text" />
            </div>
            <div>
              <span>Street</span>
              <input className='Field' id='Street' onChange={this.handleChange} type="text" />
            </div>
            <div>
              <span>Zip Code</span>
              <input className='Field' id='Zip_code' onChange={this.handleChange} type="text" />
            </div>
            <div>
                <span>Image URL</span>
                <input className='Field' id='Opening_hours' onChange={this.handleChange} type="text" />
            </div>
            <div>
              <span>Price Level</span>
              <input className='Field' id='Price_level' onChange={this.handleChange} type="text" />
            <button className='SubmitButton' type="submit"> Submit </button>
            </div>
          </div>
        </form>
      </div>
    )
  }
}

const mapDispatchToProps = (dispatch) => ({
  createRestaurant: (data) => dispatch(createRestaurant(data))
});

export default connect(null, mapDispatchToProps)(withRouter(NewRestaurantForm));