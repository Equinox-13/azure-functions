import logging
import urllib.request
import azure.functions as func



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Retrieve the html content
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()
    return func.HttpResponse(html)
    
    # Retrieve response from an api
    with urllib.request.urlopen('https://catfact.ninja/fact') as response:
        string = response.read().decode('utf-8')
        # json_obj = json.loads(string)
        return func.HttpResponse(string)
