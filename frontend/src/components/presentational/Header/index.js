import React, { Component } from 'react';

import ButtonHeader from './ButtonHeader';
import NavBar from './NavBar';
import Logo from "./logo.svg";

import './index.css';

export default class Header extends Component {
  render() {
    return (
      <div className="Header">
        <img src={Logo} alt='' />
        <div className='nav'>
          <NavBar className='NavBar' />
          <ButtonHeader className='ButtonHeader' />
        </div>
      </div>
    )
  }
}