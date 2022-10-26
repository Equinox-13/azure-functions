import logging
import urllib.request
import azure.functions as func



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()
    return func.HttpResponse(html)
