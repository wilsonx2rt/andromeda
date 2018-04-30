import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter, Link } from 'react-router-dom';
import { logout } from '../../../store/actions/currentUser';

import Header from '../../../components/presentational/Header'
import './index.css'


class Layout extends Component {

  handleLogout = () => {
    this.props.logout();
    this.props.history.push('/');
  }


  render() {
    return (
      <div>
        <Header/>
        { this.props.children }
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
