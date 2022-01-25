var aws = require("aws-sdk");
var ddb = new aws.DynamoDB({ params: { TableName: "dynamodb-ses-notification" } });

exports.handler = function (event, context, callback) {
  console.log("Received event:", JSON.stringify(event, null, 2));

  var SnsPublishTime = event.Records[0].Sns.Timestamp;
  //var SnsTopicArn = event.Records[0].Sns.TopicArn;
  var SESMessage = event.Records[0].Sns.Message;

  SESMessage = JSON.parse(SESMessage);
  console.log("SES Message: " + JSON.stringify(SESMessage, null, 2));

  const SesMessageType = SESMessage.eventType; //SESMessage.notificationType;
  var SesMessageId = SESMessage.mail.messageId;
  var SesDestinationAddress = SESMessage.mail.destination.toString();
  //var LambdaReceiveTime = new Date().toString();
  let ExpireDate = new Date();
  const TTL_DELTA = 60 * 60 * 24 * 90; // Keep records for 90 days
  let ExpireEpoch = (Math.floor(ExpireDate.valueOf() / 1000) + TTL_DELTA).toString();
  
  console.log("Got MessageType: " + SesMessageType);

  if (SesMessageType == "Bounce") {
    var SesReportingMTA = SESMessage.bounce.reportingMTA;
    var SesBounceSummary = JSON.stringify(SESMessage.bounce.bouncedRecipients);
    if (SesReportingMTA == null) {
        SesReportingMTA = "-";
    }
    var itemParams = {
      Item: {
        SesMessageId: { S: SesMessageId },
        SnsPublishTime: { S: SnsPublishTime },
        SesReportingMTA: { S: SesReportingMTA },
        SesDestinationAddress: { S: SesDestinationAddress },
        SesBounceSummary: { S: SesBounceSummary },
        SesMessageType: { S: SesMessageType },
        ExpireEpoch: { N: ExpireEpoch },
      },
    };
    ddb.putItem(itemParams, function (err, data) {
      if (err) {
        console.log("Error Saving Bounce: " + err);
        callback(err);
      } else {
        callback(null, '');
      }
    });
  } else if (SesMessageType == "Delivery") {
    var SesSmtpResponse1 = SESMessage.delivery.smtpResponse;
    var SesReportingMTA1 = SESMessage.delivery.reportingMTA;
    var itemParamsdel = {
      Item: {
        SesMessageId: { S: SesMessageId },
        SnsPublishTime: { S: SnsPublishTime },
        SesSmtpResponse: { S: SesSmtpResponse1 },
        SesReportingMTA: { S: SesReportingMTA1 },
        SesDestinationAddress: { S: SesDestinationAddress },
        SesMessageType: { S: SesMessageType },
        ExpireEpoch: { N: ExpireEpoch },
      },
    };
    ddb.putItem(itemParamsdel, function (err, data) {
      if (err) {
        console.log("Error Saving Delivery: " + err);
        callback(err);
      } else {
        callback(null, '');
      }
    });
  } else if (SesMessageType == "Complaint") {
    var SesComplaintFeedbackType = SESMessage.complaint.complaintFeedbackType;
    var SesFeedbackId = SESMessage.complaint.feedbackId;
    var itemParamscomp = {
      Item: {
        SesMessageId: { S: SesMessageId },
        SnsPublishTime: { S: SnsPublishTime },
        SesComplaintFeedbackType: { S: SesComplaintFeedbackType },
        SesFeedbackId: { S: SesFeedbackId },
        SesDestinationAddress: { S: SesDestinationAddress },
        SesMessageType: { S: SesMessageType },
        ExpireEpoch: { N: ExpireEpoch },
      },
    };
    ddb.putItem(itemParamscomp, function (err, data) {
      if (err) {
        console.log("Error Saving Complaint: " + err);
        callback(err);
      } else {
        callback(null, '');
      }
    });
  } else {
      let msg = `Unsupported Message Type: ${SesMessageType}`;
      console.log(msg);
      callback(null, msg);
  }
};
