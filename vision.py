import httplib, urllib, base64, json
subscription_key = 'bd2a946f230b4f4faec329e9933ea477'
uri_base = 'westcentralus.api.cognitive.microsoft.com'
headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description',
    'language': 'en',
})
conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')

def getContents(addr):
    #body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/1/12/Broadway_and_Times_Square_by_night.jpg'}"
    body = json.dumps({'url':str(addr)})
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    parsed = json.loads(data)
    return parsed['description']['captions'][0]['text']

def connectionclose():
    conn.close()
