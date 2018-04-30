import React, { Component } from "react";
import "./index.css";
import Facebook from "../../../assets/facebook.svg";
import Twitter from "../../../assets/twitter.svg";
import GooglePlus from "../../../assets/googleplus.svg";
import Instagram from "../../../assets/instagram.svg";

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
          <div className="footer-social-div">
            <img className="footer-social-icon" src={Facebook} alt="facebook" />
            <img className="footer-social-icon" src={Twitter} alt="twitter" />
            <img
              className="footer-social-icon"
              src={GooglePlus}
              alt="google plus"
            />
            <img
              className="footer-social-icon"
              src={Instagram}
              alt="instagram"
            />
          </div>
        </div>
        <div className="footer-bottom">© Copyright Luna 2018</div>
      </div>
    );
  }
}

export default Footer;
