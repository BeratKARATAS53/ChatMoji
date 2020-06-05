import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="demo-header">
        <div className="demo-header--title">
          <a href="/">ChatMoji</a>
        </div>
        <h4 className="demo-body">
          "Did I add the right emoji to the message?" don't think. <br /> Send
          your message and step into the magic world of ChatMoji.
        </h4>
      </div>
    );
  }
}

export default Header;
