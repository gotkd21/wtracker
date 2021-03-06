# Get data from Api

import requests
import time


def get_weatherdata(location,time_req):

    # define dictionary of all weather response attributes this applicatin tracksself.
    # these match the names of the data object in the return response from darksky

    darkskyattributes = {'time':0,'summary':"",'icon':"",'precipIntensity':0,'precipProbability':0,'precipAccumulation':0,'precipType':"",'temperature':999,'apparentTemperature':999,'dewPoint':100,'humidity':999,'pressure':9999,'uvIndex':999,'visibility':999,'ozone':""}

    # Define key Dictionaries
    bar_forecast = {}
    location = ""
    cur_time = int(time.time())
    time_req = ""

    # Define API Call parameters
    WEATHERSITE = "https://api.darksky.net/"
    default_location = "42.19364,-87.96736"
    API_KEY = "4c8784bca3dd0691b9b516c8bdea1734"
    FLAGS = "?exclude=[minutely,alerts,flags]"
    API_CALL = "forecast/"
    dsheaders = {'Accept-Encoding': 'gzip'}

    #set active_location
    # this logic may have to change when actually accepting input from device or user
    if len(location) < 2:
        active_location = default_location
    else:
        active_location = location

    if len(time_req) < 5:
        active_location_time = active_location + "," + str(cur_time)
    else:
        active_location_time = active_location + "," + str(time_req)

    # Get current forecast from API and return into json object
    cur_forecast = requests.get(WEATHERSITE + API_CALL + API_KEY + "/" + active_location_time + FLAGS, headers=dsheaders)
    print(cur_forecast)
    bar_forecast = cur_forecast.json()

    forecast_loc = {}
    forecast_loc = {'latitude': bar_forecast['latitude'], 'longitude': bar_forecast['longitude']}
    print(forecast_loc)
    # Pull location data out of Forecast object
    #loc_forecast = [bar_forecast['latitude'], bar_forecast['longitude']]
    #pressure_current = [bar_forecast['currently']['time'],bar_forecast['currently']['pressure']]

    # Initialize hourly_data as a list.
    hourly_data = []

    #print(type(bar_forecast['hourly']['data']))
    #print(bar_forecast['hourly']['data'])

    # Loop through all 'hourly' results from the API call to collect/format results into standardized
    # set of attributes.  Since darkskyapi does not always return all attributes, must set
    # default attributes if the data field has not been returned

    for fcast in bar_forecast['hourly']['data']:
        #fcast = bar_forecast['hourly']['data'][0]
        # print(fcast)
        hourly_pressure = {}
        for x,y in darkskyattributes.items():
            if x not in fcast:
                hourly_pressure[x]=darkskyattributes[x]
            else:
                hourly_pressure[x]=fcast[x]
        hourly_data.append(hourly_pressure)
    #print(hourly_data)


#        print(fcast['time'], " ", fcast['pressure'])

    # hourly_pressure = [bar_forecast['hourly']['data']]
#    print(type(hourly_pressure), type(hourly_pressure[0]))

    print(hourly_data)



    #for fcast in bar_forecast['hourly']['data']:
    #    print(fcast['time'], " ", fcast['pressure'])
    return hourly_data
