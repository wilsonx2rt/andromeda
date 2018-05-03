import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

class LoginButton extends Component {

  handleOnChange(event) {
    this.props.history.push('/login');
    }

  render() {
    return (
      <div className="button" onClick={this.handleOnChange.bind(this)}> Login</div>
    )
  }
}

export default connect()(withRouter(LoginButton));