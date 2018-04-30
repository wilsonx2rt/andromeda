import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter, Link } from 'react-router-dom';

import { logout } from '../../../store/actions/currentUser';

import Header from '../../../components/presentational/Header';
import Footer from '../../../components/presentational/Footer';
import SearchBar from '../../../components/container/SearchBar';

class Layout extends Component {

  render() {
    return (
      <div>
        <Header />
      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  currentUser: state.currentUser,
});

const mapDispatchToProps = (dispatch) => ({
  logout: () => dispatch(logout())
});

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Layout));
