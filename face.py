import httplib, urllib, base64, json
subscription_key = '193d17a7ecc5494c8a1d751d6a104dbd'
uri_base = 'westcentralus.api.cognitive.microsoft.com'
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}
params = urllib.urlencode({
    'returnFaceId':'false',
    'returnFaceAttributes':'age',
})
conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')

def getAge(addr):
    # body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'}"
    body = json.dumps({'url':str(addr)})
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    parsed = json.loads(data)
    return parsed[0]['faceAttributes']['age']

def connectionclose():
    conn.close()
