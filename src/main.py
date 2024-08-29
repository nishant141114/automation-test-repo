def lambda_handler(event, context):
    """
    AWS Lambda function handler.

    Parameters:
    event (dict): Event data passed by AWS services.
    context (object): Runtime information provided by AWS Lambda.

    Returns:
    dict: Response object with status code and message.
    """
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }