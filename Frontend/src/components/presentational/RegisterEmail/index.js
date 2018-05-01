import { connect } from 'react-redux';
import React, { Component } from 'react';

import { login } from '../../../store/actions/currentUser';
import './index.css';
import Container from '../../../components/presentational/Container';

class RegisterEmail extends Component {

  constructor(props) {
    super(props);
  }

  handleSubmit = (e) => {
    e.preventDefault();
    this.props.login({ ...this.state });
  }

  render() {
      let filler = "Your review helps others learn about great local businesses. Please don't review this business if you received a freebie for writing this review, or if you're connected in any way to the owner or employees."
    return (
        <div className="RegisterEmail">
        <form onSubmit={ this.handleSubmit }>
                <input className='Field' type="text" value={ filler } />
                <div className='ReviewButton'> <p>Post</p> </div>
            </form>
      </div>
    )
  }
}

const mapDispatchToProps = (dispatch) => ({
  login: (data) => dispatch(login(data))
});

export default connect(null, mapDispatchToProps)(RegisterEmail);
