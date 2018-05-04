import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { fetchCurrentUser } from '../../../store/actions/currentUser';
import { addUser } from '../../../store/actions/users';

import StarRatingComponent from 'react-star-rating-component';


import './index.css';
import ProfileTable from './ProfileTable'
import './blabla.jpg'

import store from './../../../store'

var url = 'https://example.com/profile';
var data = {username: 'example'};

String.prototype.capitalize = function() {
  return this.charAt(0).toUpperCase() + this.slice(1);
}

class Profile extends Component {

  constructor(props) {
    super(props);

    this.state = {
      users: [],
      randomUser: []
    };
  }

  componentWillMount() {
    fetch('https://randomuser.me/api/')
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    store.dispatch(addUser(myJson.results[0]))
    var randomUser = myJson.results[0]
    console.log(randomUser)
  });
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
    //console.log(randomUser)
    console.log(this.props, 'asdfasdfsd')

    return (
      <div>
      { !this.props.randomUser ? <div>LOADING</div> :
      <div className="UserProfile">
        <img id='HeadPic' src={'https://picsum.photos/2000/300/?random'} alt="ljk" />
        <div className='profReviw'>
          <img id='HeadPic' src={ this.props.randomUser.picture.large.capitalize()} alt="ljk" />
          <span id="profName"> {this.props.randomUser.name.first.capitalize()} 's profile! </span>
          <hr/>
          <span id="profName"> Gender: {this.props.randomUser.gender} </span>
          <hr/>
          <span id="profName"> Favorite password: {this.props.randomUser.login.password} </span>
          <ProfileTable />
        </div>
        <div id='profReviews'>
          <div id='headerTitel'>
            <p id='headerNameTitel'> {this.props.randomUser.name.first.capitalize()}  {this.props.randomUser.name.last.capitalize()} </p>
            <p id='headerNameTitel'> {this.props.randomUser.name.last.capitalize()} </p>
            <p> {comments} </p>
            <div id='Reviewtitle'> REVIEWS <hr></hr>
            <StarRatingComponent
          name="rate1"
          starCount={Math.floor(Math.random() * 5) + 1  }
          value={5}
        />
            <p> Lorizzle ipsizzle dolizzle stuff crazy, shit adipiscing elit. Shizzle my nizzle crocodizzle sapizzle velit, sizzle volutpizzle, pot quizzle, gravida vizzle, fo shizzle. Pellentesque owned tortizzle. Sed go to hizzle. izzle pizzle dapibus turpis tempizzle go to hizzle. Maurizzle pellentesque nibh izzle turpizzle. Sizzle cool stuff. That's the shizzle eleifend rhoncizzle sheezy. In fo shizzle my nizzle habitasse platea dictumst. Sheezy dapibizzle. Curabitizzle tellus get down get down, pretizzle sizzle, i saw beyonces tizzles and my pizzle went crizzle uhuh ... yih!, boofron boom shackalack, nunc. Dang ma nizzle. Integizzle crunk velit sed purizzle. </p>
            </div>
          </div>
        </div>
        <div id='profileSideDetails'>
        </div>
      </div> } </div>
    )
  }
}

const mapStateToProps = (state) => {
  if (state.users.randomUser) {
  console.log(state)
return{
  currentUser: state.currentUser,
  randomUser: state.users.randomUser.user,
}
  } else { return {} }
}


const mapDispatchToProps = (dispatch) => ({
  fetchCurrentUser: (data) => dispatch(fetchCurrentUser(data)),
  addUser: (data) => dispatch(addUser(data))
});

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Profile));

