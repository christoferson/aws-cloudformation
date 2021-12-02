exports.handler = async (event, context) => {
    console.log('## ENVIRONMENT VARIABLES: ' + serialize(process.env))
    console.log('## CONTEXT: ' + serialize(context))
    console.log('## EVENT: ' + serialize(event))
    
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hi from the ' + event.routeKey + ' route!'),
    };
    return response;
};

var serialize = function(object) {
  return JSON.stringify(object, null, 2)
}