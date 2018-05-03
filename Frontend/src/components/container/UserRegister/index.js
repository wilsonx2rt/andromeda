import { connect } from 'react-redux';
import React, { Component } from 'react';

import { login } from '../../../store/actions/currentUser';
import './index.css';

class UserRegister extends Component {

  constructor(props) {
    super(props);

    this.state = {
      email: '',
    };
  }

  handleEmailChange = (e, email) => {
    this.setState({ email });
  }

  handleSubmit = e => e.preventDefault();
  
  render() {
    return (
      <div className="UserRegistrationForm">
        <form onSubmit={this.handleSubmit}>
          <p className='RegistrationTitel'> <span>REGISTRATION</span> <hr></hr></p>
          <input className='Field' type="text" onChange={this.handleEmailChange} value={this.state.email} />
          <button className='RegisterButton' type="submit"> Login </button>
        </form>
      </div>
    )
  }
}

const mapDispatchToProps = (dispatch) => ({
  register: (data) => dispatch(login(data))
});

export default connect(null, mapDispatchToProps)(UserRegister);
