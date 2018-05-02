import { connect } from 'react-redux';
import React, { Component } from 'react';

import { login } from '../../../store/actions/currentUser';
import './index.css';
import { RaisedButton, TextField } from 'material-ui';
import Container from '../../../components/presentational/Container';


class Login extends Component {

  constructor(props) {
    super(props);

    this.state = {
      email: '',
      password: '',
    };
  }

  handleEmailChange = (e, email) => {
    this.setState({ email });
  }

  handlePasswordChange = (e, password) => {
    this.setState({ password });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    this.props.login({ ...this.state });
  }

  render() {
    return (
      <div className="LoginForm">
          <form onSubmit={ this.handleSubmit }>
            <div className='LoginTitel'> <span>LOGIN</span> <hr></hr></div>
            <input className='Field' type="text" value="Username" />
            <input className='Field' type="password" value="Password"/>
            <div className='LoginButton'> <p>Login</p> </div>
          </form>
      </div>
    )
  }
}

const mapDispatchToProps = (dispatch) => ({
  login: (data) => dispatch(login(data))
});

export default connect(null, mapDispatchToProps)(Login);
