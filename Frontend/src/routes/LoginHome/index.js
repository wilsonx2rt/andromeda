import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import Container from '../../components/presentational/Container'
import Login from '../../components/container/Login';

class LoginHome extends Component {

  constructor(props) {
    super(props);
    
    this.state = {
      activeTab: 'login'
    }
  }

  componentDidMount() {
    this.checkUser();
  }

  componentDidUpdate() {
    this.checkUser();
  }

  checkUser() {
    if (this.props.currentUser.token) {
    }
  }

  handleChange = (activeTab) => {
    this.setState({ activeTab });
  }

  render() {
    return (
      <div>
        <Container>
           <Login />
        </Container>
      </div>

    );
  }
}

const mapStateToProps = (state) => {
  return {
    currentUser: state.currentUser
  };
}

export default connect(mapStateToProps)(withRouter(LoginHome));
