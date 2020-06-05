import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="demo-header">
        <div className="demo-header--title">
          <a href="/">ChatMoji</a>
        </div>
        <h4 className="demo-body">
          Don't think, "Did I send the correct emoji according to the sentence I
          wrote?"
          <br /> You send the sentence. We add emoji.
        </h4>
      </div>
    );
  }
}

export default Header;
