import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import Container from '../../components/presentational/Container';
import Login from '../../components/container/Login'
import Restaurants from '../../components/container/Restaurants'

class Rests extends Component {

  render() {
    return (
      <Container>
        <Restaurants />
      </Container>
    );
  }
}

export default Rests
