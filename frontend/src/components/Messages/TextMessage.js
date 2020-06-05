import React from "react";
import Linkify from "react-linkify";

const TextMessage = (props) => {
  return (
    <div className="sc-message--text">
      {props.data.emoji ? (
        <Linkify properties={{ target: "_blank" }}>
          {props.data.text + " " + props.data.emoji}
        </Linkify>
      ) : (
        <Linkify properties={{ target: "_blank" }}>{props.data.text}</Linkify>
      )}
    </div>
  );
};

export default TextMessage;
