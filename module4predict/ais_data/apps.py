from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules
import sys
sys.path.append('/Users/lche/Desktop/OneDrive/workspace/ais_mining/')
# from module.lstm_acc import *


class AisDataConfig(AppConfig):
    name = 'ais_data'

    def ready(self):
        autodiscover_modules('test_kalman.py')
