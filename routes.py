from flask import Blueprint, request, render_template, jsonify
from utils import saveWebhookData, readWebhookData, processWebhookData

bp = Blueprint('main', __name__)
webhooksLst = []
parsedDict = {}

# route to create main page
@bp.route('/')
def mainPage():
    global webhooksLst
    # create webhooks list
    webhooksLst = sorted(readWebhookData(), key=lambda commit:commit['timestamp'])

    # render the main page
    return render_template("main.html", commits=webhooksLst)

# Webhook route to handle incoming data
@bp.route('/webhook', methods=['POST'])
def webhook_arrived():
    
    global parsedDict
    webhook_data = request.get_json()

    if webhook_data:  # Webhook just arrived
        parsedDict = processWebhookData(webhook_data)
        print(parsedDict)
        saveWebhookData(parsedDict)
        return jsonify({"message": "Webhook received and saved."}), 200
    else:
        return jsonify({"message": "No webhook data provided."}), 400



# route to show webhook payload file
@bp.route('/payload')
def show_payload():

    return readWebhookData()


# route to show log file
@bp.route('/log')
def show_log():
    with open('C:/Users/elad.GLOBUS0/Desktop/private/project/devops/classroom/GitHub Push Event Logging Service/webhook_data.json', 'r') as f:
        log_data = f.read()
     # Wrap the log data in a <pre> tag to preserve formatting
    return f"<pre>{log_data}</pre>"