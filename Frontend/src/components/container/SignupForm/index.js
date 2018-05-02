import { connect } from 'react-redux';
import React, { Component } from 'react';

import { login } from '../../../store/actions/currentUser';
import './index.css';
import Container from '../../../components/presentational/Container';

class SignupForm extends Component {

  constructor(props) {
    super(props);

    this.state = {
      
    };
  }


  handleSubmit = (e) => {
    e.preventDefault();
    this.props.login({ ...this.state });
  }

  render() {
    return (
      <div className="SignUpForm">
        <form onSubmit={ this.handleSubmit }>
                <div className='LoginTitel'> <span>VERIFICATION</span> <hr></hr></div>
                <input className='Field' type="text" value="E-Mail adress" />
                <input className='Field' type="text" value="Validation Code" />
                <input className='Field' type="text" value="Username" />
                <input className='Field' type="text" value="Location" />
                <input className='Field' type="text" value="Password repeat" />

                <div className='LoginButton'> <p>Finish registratoin</p> </div>
            </form>

      </div>
    )
  }
}

const mapDispatchToProps = (dispatch) => ({
  login: (data) => dispatch(login(data))
});

export default connect(null, mapDispatchToProps)(SignupForm);
