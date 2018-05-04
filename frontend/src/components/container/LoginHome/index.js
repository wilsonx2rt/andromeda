import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';


import Container from '../../presentational/Container'

import { login } from '../../../store/actions/currentUser';
import './index.css'

class LoginHome extends Component {

  constructor(props) {
    super(props);

    this.state = {
      username: 'superuser',
      password: 'superpassword',
    }
  }

  handleChange = e => {
    this.setState({
      [e.target.id]: e.target.value
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    this.props.login({ ...this.state })
    .then(() => this.props.history.push('/restaurants'));
  }

  render() {
    return (
      <div>
        <Container>
          <div className="LoginForm">
            <form onSubmit={this.handleSubmit}>
              <div className='LoginTitel'> <span>LOGIN</span> <hr></hr></div>
              <input className='Field' id='username' type="text" onChange={this.handleChange} />
              <input className='Field' id='password' onChange={this.handleChange} type="password" />
              <button className='LoginButton' type="submit"> Login </button>
            </form>
          </div>
        </Container>
      </div>
    );
  }
}

const mapDispatchToProps = (dispatch) => ({
  login: (data) => dispatch(login(data))
});

export default connect(null, mapDispatchToProps)(withRouter(LoginHome));
