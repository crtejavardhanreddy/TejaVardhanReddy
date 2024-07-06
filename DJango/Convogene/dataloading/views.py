from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from link_extractor import UrlCollector
# Create your views here.

@csrf_exempt
def webscrapping(request):
    if request.method== 'POST':
        try:
            data = json.loads(request.body)
            url = data.get('url')
            max_depth = data.get('max_depth')
            _ = UrlCollector(url, max_depth)
            if url:
                # print(url,type(url))
                return JsonResponse({'message':"Web Scrapping is done "},safe=False)
            else:
                return JsonResponse({'error':'URL is missing'},status = 400)
            
        except json.JSONDecodeError:
            return JsonResponse({'error':'Invalid JSON input'},status=400)
    return JsonResponse({'Error': "BAD Request"},status=405)