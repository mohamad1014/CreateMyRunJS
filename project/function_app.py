import azure.functions as func
import logging
import os
import uuid
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Initialize the BlobServiceClient
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_name = "create-my-run-logs"
container_client = blob_service_client.get_container_client(container_name)

# Create the container if it does not exist
if not container_client.exists():
    container_client.create_container()

@app.route(route="CreateMyRun", methods=["OPTIONS", "POST"])
def CreateMyRun(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    if req.method == "OPTIONS":
        # Handle CORS preflight request
        return func.HttpResponse(status_code=204, headers=headers)

    try:
        req_body = req.get_json()
        logging.info(f"Request body JSON: {req_body}")
        messages = req_body.get('messages')
    except ValueError as e:
        messages = None
        logging.error(f"Error parsing JSON: {e}")

    if messages:
        # Convert the list of messages to a JSON string
        messages_str = json.dumps(messages)
        
        # Generate a unique filename
        unique_filename = f"messages_{uuid.uuid4()}.txt"
        blob_client = container_client.get_blob_client(unique_filename)
        
        # Upload the messages as a text file
        blob_client.upload_blob(messages_str, overwrite=True)
        logging.info(f"Messages stored in blob: {unique_filename}")

        return func.HttpResponse(
            f"Received messages: {messages_str}",
            headers=headers
        )
    else:
        logging.warning("No messages received.")
        return func.HttpResponse(
            "No messages received.",
            status_code=200,
            headers=headers
        )