import React, { Component } from 'react';

class Footer extends Component {
  render () {
    return (
      <div className="demo-footer">
        <div>
          <div>Copyright {new Date().getFullYear()}. King of the Stack</div>
          <div>All rights reserved</div>
        </div>
        <div>
          <div>Made with React Framework & Flask API</div>
        </div>
      </div>
    );
  }
}

export default Footer;
