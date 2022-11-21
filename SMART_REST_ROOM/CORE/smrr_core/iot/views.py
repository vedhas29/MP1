# ..........................function based  api view...............................................#


from rest_framework.decorators import authentication_classes, permission_classes
from .models import iot_log
from .serializers import IotLogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from django.db.models.base import ObjectDoesNotExist
from flutter.models import room_state
from flutter.serializers import RoomStateSerializer


 
# ............................for user authentication......................................#


# ........................................................................#


@api_view(['GET', 'POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])

# ..............................GET.....................................#

def iot_gas_data(request):
    
    if request.method == 'GET':
        try:
            devices = iot_log.objects.all()
            serializer = IotLogSerializer(devices,many= True)
            return Response(serializer.data)
        except Exception as e :
            return Response({'success':False,'msg':' Error!'})


# ..............................POST.....................................#

    if request.method == 'POST':
        try:
            data = request.data
            room_id = data['room_id']
            gas01 = data['gas01']
            gas02 = data['gas02']
            gas03 = data['gas03']
            gas04 = data['gas04']
            state = "ML part is in progress"
            serializerlog = IotLogSerializer(data=data) 
            if serializerlog.is_valid()  :
                serializerlog.save() 
                room_state.objects.filter(room_id_id=room_id).update(room_id_id=room_id,gas01=gas01,gas02=gas02,gas03=gas03,gas04=gas04,state=state)
                return Response({'success': True, 'msg': 'Data Created'},status=status.HTTP_201_CREATED)
            return Response(serializerlog.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'success': False, 'msg': 'Error!!'}, status=status.HTTP_400_BAD_REQUEST)


# .........................................................................................................#
