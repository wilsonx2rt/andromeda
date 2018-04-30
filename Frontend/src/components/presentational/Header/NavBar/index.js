import React, { Component } from 'react';

import '../index.css'

export default class NavItem extends Component {
    render () {
        return (
            <div className="NavBar">
                <div>Home</div>
                <div>Search</div>
                <div>Profile</div>
          </div>
          )
        }
      }