import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import Container from '../../components/presentational/Container';
import Login from '../../components/container/Login'
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

  componentDidUpdate() {
    this.checkUser();
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
