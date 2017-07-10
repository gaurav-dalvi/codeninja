# required for HTTP request, response
import requests
# required for date manipulation
from datetime import datetime

# Constants required in this program:
API_KEY = '9Jz6tLIeJ0yY9vjbEUWaH9fsXA930J9hspPchute'
BASE_URL = 'https://api.nasa.gov/planetary/earth/assets?'
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'


# To check whether we have got 200 OK response or not
def response_is_ok(inp):
    if inp.status_code != requests.codes.ok:
        print "ERROR - Expected HTTP Status 200.  Instead got:"
        print inp
        print inp.text
        return False
    return True


# Wrapper HTTP_GET function
def httpGet(url):
    ret = requests.get(url)
    return ret


def getMaxTime(obj, size):
    last_time = datetime.strptime(obj[u'results'][size - 1][u'date'], TIME_FORMAT)
    return int(last_time.strftime("%s")) * 1000


# core logic
def flyby(lattitude, longitude):
    # forming params string
    params = 'lon=' + str(longitude) + '&' + 'lat=' + str(
        lattitude) + '&' + 'begin=' + '2015-04-19' + '&' + 'api_key=' + API_KEY
    # main URL to be hit
    URL = BASE_URL + params

    response = httpGet(URL)
    if not (response_is_ok(response)):
        print 'ERROR: Unable to make reuqest'

    obj = response.json()
    size = obj[u'count']

    delta_time = []
    total = 0
    max_time = 0

    for i in xrange(size - 1):
        # print obj[u'results'][i][u'date']
        d1 = datetime.strptime(obj[u'results'][i][u'date'], TIME_FORMAT)
        d2 = datetime.strptime(obj[u'results'][i + 1][u'date'], TIME_FORMAT)
        d1_i = int(d1.strftime("%s")) * 1000
        d2_i = int(d2.strftime("%s")) * 1000

        if max_time < max(d1_i, d2_i):
            max_time = max(d1_i, d2_i)

        # finding delta between two consecutive times
        delta_time.append(abs(d1_i - d2_i))

        # print datetime.datetime.strptime(s, TIME_FORMAT)

    # calculating avarage time
    for i in xrange(len(delta_time)):
        total = total + delta_time[i]

    temp = (total / len(delta_time))
    avg_time = int(temp)

    # prediction_time
    # "Next time: " + (last_date + avg_time_delta)
    predicted_time = avg_time + max_time
    d = datetime.fromtimestamp(predicted_time / 1000.0)
    print 'predicted time:', d

if __name__ == '__main__':
    # flyby(37.7937007, -122.4039064)
    flyby(36.998979, -109.045183)