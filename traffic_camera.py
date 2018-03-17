import requests
import urllib
import time

cnt=0
while True:
    api_key = 'CiGeh3e4F9Vr2G6i9z5UJvgDhHy0pNpDANRq'
    headers = {'Authorization':'apikey ' + api_key}
    traffic_feeds = requests.get('https://api.transport.nsw.gov.au/v1/live/cameras', headers=headers)
    traffic_json = traffic_feeds.json()
    start=time.clock()
    for each in traffic_json['features']:
        if each['id']=='d2e386':
            cam_image = each['properties']['href']
            try:
                cam_image_name = 'trainer\\img'+str(cnt)+'.png'
                urllib.request.urlretrieve(cam_image,cam_image_name)
                cnt += 1
                break
            except Exception as ex:
                print(str(ex))
    end=time.clock()-start

    print('run '+str(cnt)+' completed in '+str(end))
    time.sleep(60)


