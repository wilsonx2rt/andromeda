import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import Container from '../../components/presentational/Container';
import SearchBar from '../../components/container/SearchBar'

import './index.css'

class Home extends Component {

  constructor(props) {
    super(props);

    this.state = {
      activeTab: 'login'
    }
  }

  componentDidMount() {
    this.checkUser();
  }


  checkUser() {
    console.log('checking user')
    if (this.props.currentUser.token) {
      console.log('token ok')
    }
    else { console.log('no token')}
  }

  handleChange = (activeTab) => {
    this.setState({ activeTab });
  }

  render() {
    return (
      <Container>
        <SearchBar />
      </Container>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    currentUser: state.currentUser
  };
}

export default connect(mapStateToProps)(withRouter(Home));
