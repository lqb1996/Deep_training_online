from django.shortcuts import render
from django.http import HttpResponse
import sys
import torch.nn as nn
import torch.nn.utils.rnn as rnn_utils
import numpy as np
import json
sys.path.append('/Users/lche/Desktop/OneDrive/workspace/ais_mining/')
# from module.lstm_acc import *
# from test_kalman import *


def show_aisline(request, ais_id='Hello World'):
    return HttpResponse(ais_id)


def predict(request):
    ais_line = {
        'mmsi': 574128065,
        'route': [
            {
                'longitude': 108.213585,
                'latitude': 16.139267,
                'cog': 284.6,
                'rot': 0,
                'trueHeading': 169,
                'sog': 0.1,
                'time': '2019-10-02 08:56:00',
                'navStatus': 15
            },
            {
                'longitude': 108.2048,
                'latitude': 16.126,
                'cog': 195.4,
                'rot': -126,
                'trueHeading': 189,
                'sog': 8.0,
                'time': '2019-10-02 09:30:00',
                'navStatus': 15
            }
        ],
    }
    rnn = KalmanTrans4PRE_large(input_size=24, hidden_size=24*2, num_hidden_encoder_layers=12)

    return HttpResponse(json.dumps(ais_line, ensure_ascii=False), content_type="application/json,charset=utf-8")
