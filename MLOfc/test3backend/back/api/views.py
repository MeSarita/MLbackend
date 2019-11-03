from django.shortcuts import render

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import pandas as pd 
from sklearn import preprocessing 
import json


from .serializers import FileSerializer
# Create your views here.

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DatasetView(APIView):
    def get(self, request, *args, **kwargs):

        data = request.data
        print(data)
        df = pd.read_csv("http://localhost:8000/media/iris.csv", sep = ",", header = 0, index_col = False)
        df = df.head(5)
        csv_file = pd.DataFrame(df)
        res = csv_file.to_json( orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
        return Response(res, status=status.HTTP_201_CREATED)
class DatasetView2(APIView):
    def get(self, request, *args, **kwargs):
        data = request.data
        print(data)
        df = pd.read_csv("http://localhost:8000/media/iris.csv", sep = ",", header = 0, index_col = False)
        df1 = df._get_numeric_data().columns
        x = df.iloc[:,0:4] #returns a numpy array
        #min_max_scaler = preprocessing.MinMaxScaler()
        #x_scaled = min_max_scaler.fit_transform(x)
        normalized_X = preprocessing.normalize(x)
        csv_file = pd.DataFrame(normalized_X)
        csv_file.columns =df1
        #csv_file = pd.DataFrame(df.values[:,0:3])
        res = csv_file.to_json( orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
        return Response(res, status=status.HTTP_201_CREATED)        
class DatasetView3(APIView):
    def get(self, request, *args, **kwargs):

        data = request.data
        print(data)
        df = pd.read_csv("http://localhost:8000/media/iris.csv", sep = ",", header = 0, index_col = False)
        #df = df.head(5)
        df1 = df.columns
        features = df._get_numeric_data().columns
        labels = df.select_dtypes(include=['object']).copy()
        categoricaldata = labels.drop_duplicates()
        categoricaldata1= pd.DataFrame(categoricaldata)
        print(categoricaldata1)
        csv_file = categoricaldata1
        #csv_file = pd.DataFrame(df)
        res = csv_file.to_json( orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
        return Response(res, status=status.HTTP_201_CREATED)