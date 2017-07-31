from django.http import JsonResponse
import time
import datetime

def data_validate(string):
    try:
        str = datetime.datetime.strptime(string, '%B %d, %Y')
        return str
    except ValueError:
        return 'null'

def data(request):
    data_dic = {}
    data_url = request.path.replace('/', '')
    datetime_obj = data_validate(data_url)
    if datetime_obj == 'null':
        data_dic['unix'] = 'null'
        data_dic['natural'] = 'null'
    else:
        data_unix = time.mktime(datetime_obj.timetuple())
        data_dic['unix'] = int(data_unix)
        data_dic['natural'] = data_url
    return JsonResponse(data_dic)

def timestamp(request):

    data_dic = {}
    data_url = request.path.replace('/', '')
    try:
        string = datetime.datetime.fromtimestamp(int(data_url)).strftime('%B %d, %Y')
    except ValueError:
        string = 'null'
    if string == 'null':
        data_dic['unix'] = 'null'
        data_dic['natural'] = 'null'
    else:
        data_dic['unix'] = int(data_url)
        data_dic['natural'] = string
    return JsonResponse(data_dic)
