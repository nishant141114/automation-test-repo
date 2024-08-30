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



# git remote set-url origin https://github.com/nishant141114/auto-using-workflow.git
# git add .
# git commit -m "Your commit message"
# git push origin main

# git credential-cache exit


# Remove the existing credentials from the macOS Keychain:

# Open the Keychain Access application on your Mac.
# Search for github.com.
# Delete any entries related to github.com.





# git pull origin main --no-rebase
# git push origin main



# git pull origin main --rebase
# git push origin main