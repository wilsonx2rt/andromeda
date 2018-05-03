import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import Container from '../../components/presentational/Container'
import UserRegister from '../../components/container/UserRegister';

class UserRegistration extends Component {

  constructor(props) {
    super(props);
    
    this.state = {
      activeTab: 'register'
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
           <UserRegister />
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

export default connect(mapStateToProps)(withRouter(UserRegistration));
