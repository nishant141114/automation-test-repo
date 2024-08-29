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



# git remote set-url origin https://github.com/NEW_USERNAME/NEW_REPO.git

# git add .
# git commit -m "Your commit message"
# git push origin main