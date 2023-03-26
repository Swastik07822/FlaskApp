def customize(l):
    #
    print(l)
    k = ['Temparatue : '+str(l['current']['temperature'])+" \u2103",str(l['location']['name']+'/'+
        l['location']['country']),'Date-time : '+l['location']['localtime'],l['current']['weather_descriptions'][0]
        ,'Windspeed : '+str(l['current']['wind_speed'])+'KMPH',"Wind direction: "+l['current']['wind_dir'],
        'Wind_pressure : ' + str(l['current']['pressure'])+'mbar','Precipitation : ' +str(l['current']['precip']) + '%',
        'Humidity : '+str(l['current']['humidity'])+'%',
        'Feeelslike : '+str(l['current']['feelslike']) +" \u2103"]
    n = ['latitude : '+str(l['location']['lat']),'longitude : '+str(l['location']['lon']),
        'Timezone : '+l['location']['timezone_id']]
    m = ['UV index : '+str(l['current']['uv_index']),'Visibility : '+str(l['current']['visibility']),
        'Cloud cover : '+str(l['current']['cloudcover']) + '%']
    return  n,k,m

