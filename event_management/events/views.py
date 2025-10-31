import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Event,Feedback
from django.views.decorators.csrf import csrf_exempt
from .serializers import EventSerializer, FeedbackSerializer
from django.db.models import Avg, Q

# event management

# Create your views here.
def home_page(request):
    return JsonResponse({'status':'Success'})


def get_event(request,input_id=None):
    # u1=Users.objects.get(id=input_id) to return only one data (field)
    title = request.GET.get('title')       # search by title
    location = request.GET.get('location') # filter by location
    date = request.GET.get('date')         # filter by date

    events = Event.objects.all()

    # Apply filters
    if title:
        events = events.filter(title__icontains=title)
    if location:
        events = events.filter(location__icontains=location)
    if date:
        events = events.filter(date=date)

    # Add average rating
    events = events.annotate(average_rating=Avg('feedbacks__rating'))

    serialized = EventSerializer(events, many=True)
    event_data = serialized.data

    # attach avg rating
    for i, event in enumerate(events):
        event_data[i]['average_rating'] = event.average_rating or 0

    return JsonResponse({'events': event_data}, safe=False)

    # u1=Event.objects.all()  # to retrive all data
    # u1_json=EventSerializer(u1, many=True) #if we use objects.all(), then we need to use many=True

    # return JsonResponse({
    #     'user_details':u1_json.data
    # })


@csrf_exempt
def create_event(request):
    print(request.body)

    data=json.loads(request.body)
    print(data)

            # Serializer
    input_event=EventSerializer(data = data)
    if input_event.is_valid(): #To validata data
        input_event.save()
        return JsonResponse(input_event.data)
    else:
        return JsonResponse(input_event.errors)
    
@csrf_exempt
def update_event(request,input_id):
    u1=Event.objects.get(id=input_id)
    data = json.loads(request.body)

    partial = request.method=='PATCH'

    updated_object=EventSerializer(u1,data=data,partial=partial) #  partial = False--> PUT, partial = True--> PATCH

    if updated_object.is_valid():
        updated_object.save()
        return JsonResponse(updated_object.data)
    else:
        return JsonResponse(updated_object.errors)
def delete_event(request,id):
    Event.objects.get(id=id).delete()

# feedback management

def get_feedback(request,input_id):
    # u2=Users.objects.get(id=input_id) to return only one data (field)

    u2=Feedback.objects.all()  # to retrive all data
    u2_json=FeedbackSerializer(u2, many=True) #if we use objects.all(), then we need to use many=True


    return JsonResponse({
        'user_details':u2_json.data
    })


@csrf_exempt
def create_feedback(request):
    print(request.body)

    data1=json.loads(request.body)
    print(data1)

            # Serializer
    input_feedback=FeedbackSerializer(data = data1)
    if input_feedback.is_valid(): #To validata data
        input_feedback.save()
        return JsonResponse(input_feedback.data)
    else:
        return JsonResponse(input_feedback.errors)
    
@csrf_exempt
def update_feedback(request,input_id):
    u2=Feedback.objects.get(id=input_id)
    data1 = json.loads(request.body)

    partial = request.method=='PATCH'

    updated_object1=FeedbackSerializer(u2,data=data1,partial=partial) #  partial = False--> PUT, partial = True--> PATCH

    if updated_object1.is_valid():
        updated_object1.save()
        return JsonResponse(updated_object1.data)
    else:
        return JsonResponse(updated_object1.errors)

@csrf_exempt
def delete_feedback(request,id):
    Feedback.objects.get(id=id).delete()

    

# ✅ Modified get_event to include search, filter, and average rating
def get_event(request, input_id=None):
    title = request.GET.get('title')       # search by title
    location = request.GET.get('location') # filter by location
    date = request.GET.get('date')         # filter by date

    events = Event.objects.all()

    # 🔍 Apply filters
    if title:
        events = events.filter(title__icontains=title)
    if location:
        events = events.filter(location__icontains=location)
    if date:
        events = events.filter(date=date)

    # 🌟 Add average rating
    events = events.annotate(average_rating=Avg('feedbacks__rating'))

    serialized = EventSerializer(events, many=True)
    event_data = serialized.data

    # attach avg rating
    for i, event in enumerate(events):
        event_data[i]['average_rating'] = event.average_rating or 0

    return JsonResponse({'events': event_data}, safe=False)
