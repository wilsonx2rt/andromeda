import { connect } from 'react-redux';
import React, { Component } from 'react';

import { login } from '../../../store/actions/currentUser';
import './index.css';
import Container from '../../../components/presentational/Container';


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

  handleSubmit = (e) => {
    e.preventDefault();
    
    /*this.props.login({ ...this.state });*/
  }

  render() {
    return (
      <div className="UserRegistrationForm">
          <form onSubmit={ this.handleSubmit }>
            <div className='RegistrationTitel'> <span>REGISTRATION</span> <hr></hr></div>
            <input className='Field' type="text" value="E-Mail adress"/>
            <div className='RegisterButton'> <p>Register</p> </div>
          </form>
      </div>
    )
  }
}

const mapDispatchToProps = (dispatch) => ({
  login: (data) => dispatch(login(data))
});

export default connect(null, mapDispatchToProps)(UserRegister);
