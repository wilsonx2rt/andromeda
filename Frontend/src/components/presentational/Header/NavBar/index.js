import React, { Component } from 'react';
import '../index.css'
import { Link } from 'react-router-dom'

export default class NavItem extends Component {

    render() {
        return (
            <div className="NavBar">
                <Link to='/' className="NavItem" > Home</Link>
                <Link to='/RestaurantPage' className="NavItem" > Search</Link>
                <Link to='/user' className="NavItem" > Profile</Link>
            </div>
        )
    }
}