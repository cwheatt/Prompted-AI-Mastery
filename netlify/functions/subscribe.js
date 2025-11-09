exports.handler = async (event, context) => {
  // Only allow POST requests
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    const { email } = JSON.parse(event.body);

    if (!email) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Email is required' })
      };
    }

    // Call Brevo API
    const response = await fetch('https://api.brevo.com/v3/contacts', {
      method: 'POST',
      headers: {
        'accept': 'application/json',
        'api-key': process.env.BREVO_API_KEY,
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        email: email,
        listIds: [parseInt(process.env.BREVO_LIST_ID)],
        updateEnabled: false
      })
    });

    const data = await response.json();

    if (response.ok || response.status === 201) {
      return {
        statusCode: 200,
        body: JSON.stringify({ success: true, message: 'Subscribed successfully' })
      };
    } else if (response.status === 400 && data.code === 'duplicate_parameter') {
      return {
        statusCode: 200,
        body: JSON.stringify({ success: true, message: 'Already subscribed' })
      };
    } else {
      return {
        statusCode: response.status,
        body: JSON.stringify({ error: data.message || 'Subscription failed' })
      };
    }
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message || 'Internal server error' })
    };
  }
};