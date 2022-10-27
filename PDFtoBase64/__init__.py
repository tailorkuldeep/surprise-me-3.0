import logging

import azure.functions as func
from azure.storage.blob import BlobServiceClient
import base64


def main(req: func.HttpRequest) -> func.HttpResponse:
    connection_string = req.params.get('connection_string')
    container = req.params.get('container')
    blob = req.params.get('blob')
   
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container)
    blob_client = container_client.get_blob_client(blob)
 
    download_stream = blob_client.download_blob()
    data = download_stream.readall()
    #print(data)
    base64_bytes = base64.b64encode(data)
    base64_string = base64_bytes.decode("ascii")
    #print(base64_string)

    return func.HttpResponse(base64_string,status_code=200)
    