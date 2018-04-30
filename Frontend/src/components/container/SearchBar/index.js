import React, { Component } from 'react';
import './index.css';

class SearchBar extends Component {
  render() {
    return (
      <div className="SearchBar">
        <form id="search-form" action="">
          <input id="search-input" type="text" name="" placeholder="Search..." />
          <div className="search-btn">Search</div>
        </form>
      </div>
    )
  }
}

export default SearchBar;
