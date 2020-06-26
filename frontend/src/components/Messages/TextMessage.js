import React from "react";
import Linkify from "react-linkify";

const TextMessage = (props) => {
  return (
    <div className="sc-message--text">
      {props.data.emoji ? (
        <div>
          {props.data.text + " " + props.data.emoji}
          <hr />
          <p>{JSON.stringify(props.data.result)}</p>
        </div>
      ) : (
        <div>{props.data.text}</div>
      )}
    </div>
  );
};

export default TextMessage;
