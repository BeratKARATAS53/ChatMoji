import PropTypes from "prop-types";
import React, { Component } from "react";
import ChatWindow from "./ChatWindow";
import launcherIcon from "./../assets/logo-no-bg.svg";
import incomingMessageSound from "./../assets/sounds/notification.mp3";
import launcherIconActive from "./../assets/close-icon.png";

class Launcher extends Component {
  constructor() {
    super();
    this.state = {
      launcherIcon,
    };
  }

  componentWillReceiveProps(nextProps) {
    if (this.props.mute) {
      return;
    }
    const nextMessage = nextProps.messageList[nextProps.messageList.length - 1];
    const isIncoming = (nextMessage || {}).author === "them";
    const isNew = nextProps.messageList.length > this.props.messageList.length;
    if (isIncoming && isNew) {
      this.playIncomingMessageSound();
    }
  }

  playIncomingMessageSound() {
    var audio = new Audio(incomingMessageSound);
    audio.play();
  }

  render() {
    return (
      <div id="sc-launcher">
        <ChatWindow
          messageList={this.props.messageList}
          onUserInputSubmit={this.props.onMessageWasSent}
          onFilesSelected={this.props.onFilesSelected}
          agentProfile={this.props.agentProfile}
          showEmoji={this.props.showEmoji}
        />
      </div>
    );
  }
}

Launcher.propTypes = {
  onMessageWasReceived: PropTypes.func,
  onMessageWasSent: PropTypes.func,
  newMessagesCount: PropTypes.number,
  isOpen: PropTypes.bool,
  handleClick: PropTypes.func,
  messageList: PropTypes.arrayOf(PropTypes.object),
  mute: PropTypes.bool,
  showEmoji: PropTypes.bool,
};

Launcher.defaultProps = {
  newMessagesCount: 0,
  showEmoji: true,
};

export default Launcher;
