exports.handler = async (context, event, callback) => {

    const flow = event.flow;
    const body = event.body;
    const knowledge = event.knowledge;
    const start = event.start;
  
    const settings = {
          method: 'POST',
          headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            flow: flow,
            body: body,
            knowledge: knowledge,
            start: start
          })
      };
  
    const fetchResponse = await fetch(`url here`, settings);
    const response = await fetchResponse.json()
  
    return callback(null, response);
  };