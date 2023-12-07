# thread.py
import threading
import time
from crowling import data_crowling
from predictor import start_predictor

# Event 객체 생성
input_received_event = threading.Event()

# 크롤링을 위한 스레드
crowling_thread = threading.Thread(target=data_crowling, args=(input_received_event,))
crowling_thread.start()

# 크롤링 스레드가 input_value를 받아올 때까지 대기
input_received_event.wait()

# 예측을 위한 스레드
predictor_thread = threading.Thread(target=start_predictor)
predictor_thread.start()
