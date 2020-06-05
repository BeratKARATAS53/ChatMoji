import React, { Component } from 'react';
import closeIcon from './../assets/close-icon.png';
import avatar from "./../assets/avatar (5).jpg"


class Header extends Component {

  render() {
    return (
      <div className="sc-header">
        <img className="sc-header--img" src={avatar} alt="" />
        <div className="sc-header--team-name"> {this.props.teamName} </div>
      </div>
    );
  }
}

export default Header;
