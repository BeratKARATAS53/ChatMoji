# Warning!

This project was developed based on the react-chat-window project developed by "kingofthestack".

# ChatMoji

`ChatMoji` is a messaging interface based on the message and the emoji that is appropriate for the content and meaning of that message. It is written for visualization purposes only. It does not provide messaging.

![Demo gif of react-chat-window being used](https://puu.sh/xei2F/fd4a121185.gif)

## Features

- Customizeable
- Free

## Table of Contents
- [Installation](#installation)
- [Example](#example)
- [Components](#components)

## Installation

```
$ npm install react-chat-window
```

## Example

``` javascript
import React, { Component } from "react";
import { render } from "react-dom";
import { Launcher } from "../../src";
import messageHistory from "./messageHistory";
import TestArea from "./TestArea";
import Header from "./Header";
import Footer from "./Footer";
import "./../assets/styles";

class Demo extends Component {
  constructor() {
    super();
    this.state = {
      messageList: messageHistory,
      newMessagesCount: 0,
      isOpen: false,
    };
  }

  _onMessageWasSent(message) {
    this.setState({
      messageList: [...this.state.messageList, message],
    });
  }

  _onFilesSelected(fileList) {
    const objectURL = window.URL.createObjectURL(fileList[0]);
    this.setState({
      messageList: [
        ...this.state.messageList,
        {
          type: "file",
          author: "me",
          data: {
            url: objectURL,
            fileName: fileList[0].name,
          },
        },
      ],
    });
  }

  async _sendMessage(text) {
    if (text.length > 0) {
      const newMessagesCount = this.state.isOpen
        ? this.state.newMessagesCount
        : this.state.newMessagesCount + 1;
      (async () => {
        const response = await fetch("http://127.0.0.1:5000/predictModel", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ sentence: text }),
        });
        let emoji = await response.json();
        emoji = emoji.sentence;
        this.setState({
          newMessagesCount: newMessagesCount,
          messageList: [
            ...this.state.messageList,
            {
              author: "them",
              type: "text",
              data: { text, emoji },
            },
          ],
        });
      })();
    }
  }

  _handleClick() {
    this.setState({
      isOpen: !this.state.isOpen,
      newMessagesCount: 0,
    });
  }

  render() {
    return (
      <div>
        <Header />
        <TestArea onMessage={this._sendMessage.bind(this)} />
        <Launcher
          agentProfile={{
            teamName: "chat-moji",
            imageUrl:
              "https://a.slack-edge.com/66f9/img/avatars-teams/ava_0001-34.png",
          }}
          onMessageWasSent={this._onMessageWasSent.bind(this)}
          onFilesSelected={this._onFilesSelected.bind(this)}
          messageList={this.state.messageList}
          newMessagesCount={this.state.newMessagesCount}
          handleClick={this._handleClick.bind(this)}
          showEmoji
        />
        <Footer />
      </div>
    );
  }
}
```

For more detailed examples see the demo folder.

## Components

# Launcher

`Launcher` is the only component needed to use react-chat-window. It will react dynamically to changes in messages. All new messages must be added via a change in props as shown in the example.

Launcher props:

|      prop        | type   | required | description |
|------------------|--------|----------|-------------|
| agentProfile     | [object](#agent-profile-objects) | yes | Represents your product or service's customer service agent. Fields: imageUrl (string), teamName (string). |
| messageList      | [[message](#message-objects)] | yes | An array of message objects to be rendered as a conversation. |
| mute             | boolean | no | Don't play sound for incoming messages. Defaults to `false`. |
| newMessagesCount | number | no | The number of new messages. If greater than 0, this number will be displayed in a badge on the launcher. Defaults to `0`. |
| onFilesSelected  | function([fileList](https://developer.mozilla.org/en-US/docs/Web/API/FileList)) | no | Called after file has been selected from dialogue in chat window. |
| onMessageWasSent | function([message](#message-objects)) | yes | Called when a message is sent, with a message object as an argument. |
| showEmoji        | boolean | no | Whether or not to show the emoji button in the input bar. Defaults to `true`.


### Message Objects

Message objects are rendered differently depending on their type. Currently, only text, file, and emoji types are supported. Each message object has an `author` field which can have the value 'me' or 'them'.

``` javascript
{
  author: 'them',
  type: 'text',
  data: {
    text: 'some text'
  }
}

{
  author: 'me',
  type: 'emoji',
  data: {
    code: 'someCode'
  }
}


{
  author: 'me',
  type: 'file',
  data: {
    url: 'somefile.mp3',
    fileName: 'Any old name'
  }
}

```

### Agent Profile Objects

Look like this:

```js
{
  imageUrl: 'https://somewhere.on/the_web.png',
  teamName: 'Da best'
}
```
