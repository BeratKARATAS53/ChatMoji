import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="demo-header">
        <div className="demo-header--title">
          <a href="/">ChatMoji</a>
        </div>
        <h4 className="demo-body">
          ChatMoji is an Emotion Detection Model written using Python, powered
          with Sentiment Analysis. The structure is pretty simple. A sentence
          that you enter is sent to the model through Flask and it returns a
          percentage slice according to the 4 emotion categories used while
          training this model.
          <br />
          From here, based on the highest percentage, the emoji determined by
          that category is randomly selected and added to the end of your
          sentence.
          <br />
          <br />
          Emojis In Emotion Categories:
          <table>
            <tr>
              <th>FEAR</th>
              <th>JOY</th>
              <th>SADNESS</th>
              <th>ANGER</th>
            </tr>
            <tr>
              <td>😨, 😱, 😰</td>
              <td>😂, 😆, 😀, 😃, 😄, 😊, 😍</td>
              <td>😢, 😭, 😿</td>
              <td>😠, 👿, 😤, 😡, 🤬</td>
            </tr>
          </table>
          <br />
          Briefly, "Did I add the right emoji to the message?" don't think. Send
          your message and step into the magic world of ChatMoji.
          <hr style={{ border: "1px solid DodgerBlue", marginTop: "20px" }} />
        </h4>
      </div>
    );
  }
}

export default Header;
