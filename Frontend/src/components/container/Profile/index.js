import React, { Component } from 'react';

import './index.css';
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
    const name = 'Sonof Abitch'
    const reviews = ['this sucks', 'was quite good but also shitty', 'whatt the burger!']
    const comments = ''

    return (
      <div className="UserProfile">
        <img id='HeadPic' src={source} alt="ljk" />
        <div className='profReviw'>
          <img id='HeadPic' src={this.props.profPic} alt="ljk" />
          <span id="profName"> {name} 's Profile' </span>
          <ProfileTable />
        </div>
        <div id='profReviews'>
          <div id='headerTitel'>
            <p id='headerNameTitel'> {name} </p>
            <p> {comments} </p>
            <span id='Reviewtitle'> REVIEWS </span>
          </div>
        
          <ul id='reviewList'>
              {reviews.map(function(item,i) { 
                return <li key={i} text={item.value}/>
                })}
           </ul>

        </div>
        <div id='profileSideDetails'>
        </div>
      </div>
    )
  }
}

export default Profile;
