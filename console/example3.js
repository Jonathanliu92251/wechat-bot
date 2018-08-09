// Example 3: maintains state.

var prompt = require('prompt-sync')();
var ConversationV1 = require('watson-developer-cloud/conversation/v1');

// Set up Conversation service.
var conversation = new ConversationV1({
  username: '27e428e6-90a2-4287-8739-90e07b9c7596', // replace with username from service key
  password: 'ylqDhDhewLv0', // replace with password from service key
  path: { workspace_id: '9523a515-db89-4911-836e-390f9309b8cb' }, // replace with workspace ID
  version_date: '2016-07-11'
});

// Start conversation with empty message.
conversation.message({}, processResponse);

// Process the conversation response.
function processResponse(err, response) {
  if (err) {
    console.error(err); // something went wrong
    return;
  }

  // If an intent was detected, log it out to the console.
  if (response.intents.length > 0) {
    console.log('Detected intent: #' + response.intents[0].intent);
  }

  // Display the output from dialog, if any.
  if (response.output.text.length != 0) {
      console.log(response.output.text[0]);
  }

  // Prompt for the next round of input.
    var newMessageFromUser = prompt('>> ');
    // Send back the context to maintain state.
    conversation.message({
      input: { text: newMessageFromUser },
      context : response.context,
    }, processResponse)
}
