import React, { Component } from 'react';

import ButtonHeader from './ButtonHeader';
import NavBar from './NavBar';
import Logo from "./logo.svg";

import './index.css';

export default class Header extends Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }

  render() {
    return (
      <div className="Header">
          <img src={Logo}/>
          <NavBar className='NavBar'/>
          <ButtonHeader className='ButtonHeader'/>
      </div>
    )
  }
}