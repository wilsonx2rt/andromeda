import React, { Component } from 'react';
import Login from './Login'
import SignUp from './SignUp'
// import pictures

export default class Button extends Component {
  render() {

    return (
        <div className='ButtonHeader'>
            <SignUp />
            <Login />
        </div>
    )
  }
}

