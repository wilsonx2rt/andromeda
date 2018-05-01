import { connect } from 'react-redux';
import React, { Component } from 'react';

import { login } from '../../../store/actions/currentUser';
import './index.css';
import Container from '../../../components/presentational/Container';
import ProfileTable from './ProfileTable'
import './blabla.jpg'


class Profile extends Component {

  constructor(props) {
    super(props);

    this.state = {
      activeTab: 'reviews'
    };
  }


  handleSubmit = (e) => {
    e.preventDefault();
    this.props.login({ ...this.state });
  }

  render() {
    
    const source = "https://themoscowtimes.com/static/uploads_new/publications/2014/7/30/7d006149af99469180d492c1f84f370a.jpg"
    const profPic = "data:image/jpeg;base64,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"
    const name = 'Placeholder'
    const reviews = ''
    const comments = ''

    
    return (
      <div className="UserProfile">
        <img id='HeadPic' src={source} alt="ljk"/>
        <div className='profReviw'>
          <img id='HeadPic' src={profPic} alt="ljk"/>
          <span id="profName"> {name} 's Profile' </span>
          <ProfileTable/>
        </div>
        <div id='profReviews'>
          <div id='headerTitel'>
            <p id='headerNameTitel'> {name} </p>
            <p> { reviews }  </p>
            <p> { comments } </p>
          <span id='Reviewtitle'> REVIEWS </span>
        </div>
      </div>
      <div id='profileSideDetails'>
      </div>


    </div>
    )
  }
}

const mapDispatchToProps = (dispatch) => ({
  login: (data) => dispatch(login(data))
});

export default connect(null, mapDispatchToProps)(Profile);
