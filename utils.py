import json
import os

webhookFilePath = '/workingDir/webhook_data.json'

# function to save webhook data
def saveWebhookData(webDict):
    
    try:
        # check if file exists and if it's valid JSON
        if os.path.exists(webhookFilePath) and os.path.getsize(webhookFilePath) > 0:
            with open(webhookFilePath, 'r+') as f:
                existing_data = json.load(f)
                
                if isinstance(existing_data, list):
                    existing_data.extend(webDict)
                    f.seek(0)
                    json.dump(existing_data, f, indent=4)
        else:
            with open(webhookFilePath, 'w') as f:
                json.dump(webDict, f, indent=4)  # start a new list if file doesn't exist or is empty
                
        print("Webhook data received and saved.", flush=True)
    
    except Exception as e:
        print(f"Error saving webhook data: {e}", flush=True)


# function to read webhook data - return only "commits"
def readWebhookData():
    data = []
    try:
        if os.path.exists(webhookFilePath):
            with open(webhookFilePath, 'r') as f:
                data = json.load(f)  # load the list of webhooks
        return data
    except Exception as e:
        print(f"Error reading webhook data: {e}", flush=True)
        return []


# function to process the data - TO COMPLETE!
def processWebhookData(webhookData):
    data = readWebhookData()
    repoName = webhookData.get('repository', {}).get('name', 'Missing Repo Name')
    for commit in webhookData['commits']:
        commitID = commit.get('id', 'No ID')
        timestamp = commit.get('timestamp')
        author = commit.get('author', {}).get('name')
        message = commit.get('message')
        added = commit.get('added', [])
        removed = commit.get('removed', "None")
        modified = commit.get('modified', "None")
        url = commit.get('url')
        parsedDict = {
        "repoName" : repoName,
        "commitID" : commitID,
        "timestamp" : timestamp,
        "author" : author,
        "message" : message,
        "added" : added,
        "removed" : removed,
        "modified" : modified,
        "url" : url
        }
        data.append(parsedDict)
    
    
    print(f"Commit ID: {parsedDict['commitID']}, Author: {parsedDict['author']}, Message: {parsedDict['message']}/n", flush=True)
    return (data)