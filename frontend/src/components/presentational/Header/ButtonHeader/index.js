import React, { Component } from 'react';
import LoginButton from './Login'
import SignUpButton from './SignUp'

import '../index.css'

export default class Button extends Component {
  render() {

    return (
      <div className='ButtonHeader'>
        <SignUpButton />
        <LoginButton />
      </div>
    )
  }
}

