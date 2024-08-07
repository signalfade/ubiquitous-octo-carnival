import logging
import azure.functions as func
from azure.core.credentials import AzureKeyCredential
from azure.eventgrid import EventGridPublisherClient

def main(cloudevent: func.EventGridEvent):
    logging.info('Python EventGrid trigger function processed an event: %s', cloudevent.id)

    # Extract the data from the CloudEvent
    data = cloudevent.get_json()

    # Make a call to the HTTP endpoint
    response = requests.post('http://100.93.93.93', json=data)

    if response.status_code == 200:
        logging.info('HTTP request successful')
    else:
        logging.error('HTTP request failed with status code: %d', response.status_code)