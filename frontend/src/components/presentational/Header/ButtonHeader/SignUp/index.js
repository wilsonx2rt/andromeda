import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';


class SignUpButton extends Component {
  handleOnChange(event) {
    this.props.history.push('/register');
    }
  

  render() {
    return (
      <div className="button" id='sign-up-btn' onClick={this.handleOnChange.bind(this)}> Sign Up!</div>
    )
  }
}

export default connect()(withRouter(SignUpButton));

