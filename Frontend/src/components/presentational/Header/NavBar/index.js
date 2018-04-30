import React, { Component } from 'react';
import '../index.css'

export default class NavItem extends Component {
    render () {
        return (
            <div className="NavBar">
                <div className="NavItem" > Home</div>
                <div className="NavItem" > Search</div>
                <div className="NavItem" > Profile</div>
          </div>
          )
        }
      }