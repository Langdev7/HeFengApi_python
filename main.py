import requests
import json

location_name = '西安&adm=陕西'
location_ID = '101110109'
key = '5099f7604c6c4519bb10d94dbe2c9212'

# 访问的API接口
city_url = f'https://geoapi.qweather.com/v2/city/lookup?{location_name}'
weather_url = f'https://devapi.qweather.com/v7/weather/now?location={location_ID}&key={key}'

value = {
    'location': location_ID,
    'key': key,
    'lang': 'zh'
}
# 接收城市信息及天气信息
city_name = requests.get(city_url, params=value)
weather_list = requests.request(url=weather_url, method='get')

print(type(city_name))
print(city_name)
# 将接收的数据转化成JSON格式
cnj = city_name.json()
wlj = weather_list.json()
# 输出键名为location的值
city_data = cnj['location']
# 输出所有城市名称
# for i in range(0, 10):
#     print(city_data[i]['country']+city_data[i]['adm1']+city_data[i]['adm2']+city_data[i]['name'])

print(cnj['location'][0]['country']+city_data[0]['adm1']+city_data[0]['adm2']+city_data[0]['name'])

print(wlj)
# 输出天气信息
print(wlj['now']['obsTime'])
print('温度：'+wlj['now']['temp'])
# for key in cnj.keys():
#     print(key)
# for value in cnj.values():
#     print(value)
# 获取的数据信息储存至JSON文件中
# with open('weather.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(cnj))
# 从JSON文件中获取数据
# with open('weather.json', 'r', encoding='utf-8') as f:
#     date = json.load(f)
