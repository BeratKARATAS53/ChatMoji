import monsterImgUrl from "../../src/assets/aurora.jpg";

export default [
  // {type: 'text', author: 'me', data: { text: "Why don't they have salsa on the table?"} },
  // {type: 'text', author: 'them', data: { text: 'What do you need salsa for?'} },
  // {type: 'text', author: 'me', data: { text: 'Salsa is now the number one condiment in America.'} },
  // {type: 'text', author: 'them', data: { text: "You know why? Because people like to say 'salsa.' 'Excuse me, do you have salsa?' 'We need more salsa.' 'Where is the salsa? No salsa?'"} },
  // {type: 'text', author: 'me', data: { text: "You know it must be impossible for a Spanish person to order seltzer and not get salsa. 'I wanted seltzer, not salsa.'"} },
  // {type: 'text', author: 'them', data: { text: "Don't you know the difference between seltzer and salsa?? You have the seltezer after the salsa!"} },
  // {type: 'text', author: 'me', data: { text: 'See, this should be a show. This is the show. '} },
  // {type: 'text', author: 'them', data: { text: 'What?'} },
  // {type: 'text', author: 'me', data: { text: 'This. Just talking.'} },
  // {type: 'text', author: 'them', data: { text: 'Yeah, right.'} },
  {
    type: "text",
    author: "them",
    data: {
      text:
        "I just checked my stock market account and saw that I lost 1000 dollars.",
      emoji: "😱",
      result: { anger: "%23.3", fear: "%41.0", joy: "%0.0", sadness: "%35.7" },
    },
  },
  {
    type: "text",
    author: "me",
    data: {
      text: "It could be from Korona, this virus damaged the markets.",
      emoji: "😤",
      result: { anger: "%41.4", fear: "35.7", joy: "%0.1", sadness: "%23.9" },
    },
  },
  {
    type: "text",
    author: "them",
    data: {
      text: "Meanwhile, mothers happy day #peace, #love &amp; #joy.",
      emoji: "😍",
      result: { anger: "%0.0", fear: "%0.0", joy: "%100.0", sadness: "%0.0" },
    },
  },
  {
    type: "text",
    author: "me",
    data: {
      text: "No gifts?",
      emoji: "😤",
      result: { anger: "%39.3", fear: "%32.6", joy: "%1.7", sadness: "%26.4" },
    },
  },
];
