import React, { Component } from 'react'
import './index.css';

class Footer extends Component {
  render() {
    return (
      <div className="Footer">
        <div className="footer-top">
          <div className="footer-nav">
            <div className="footer-nav-item">About Us</div>
            <div className="footer-nav-item">Press</div>
            <div className="footer-nav-item">Blog</div>
            <div className="footer-nav-item">iOS</div>
            <div className="footer-nav-item">Android</div>
          </div>
        </div>
        <div className="footer-bottom">© Copyright Luna 2018</div>
      </div>
    )
  }
}

export default Footer;
