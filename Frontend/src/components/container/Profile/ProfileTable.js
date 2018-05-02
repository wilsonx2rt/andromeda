import React, { Component } from 'react';

import star from "../../../assets/star.svg";
import comment from "../../../assets/comment.svg";
import restaurant from "../../../assets/restaurant.svg";
import edit from "../../../assets/edit.svg";

export default class ProfileTable extends Component {

  render() {
    
    return (
        <div className='NavBarProfile'>
            <div>
                <img className="Nav-img-1" src={star} alt="" />
            </div>
            <div>
                <img className="Nav-img-2" src={comment} alt="" />
            </div>
            <div>
                <img className="Nav-img-3" src={restaurant} alt="restaurant" />
            </div>
            <div>
            <img className="Nav-img-4" src={edit} alt="edit" />
            </div>
        </div>
    )
  }
}

