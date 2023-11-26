# main.py
import threading
import time
from crowling import data_crowling
from predictor import start_predictor

# 크롤링을 위한 스레드
crowling_thread = threading.Thread(target=data_crowling)
crowling_thread.start()

# 20초 대기
time.sleep(20)

# 예측을 위한 스레드
predictor_thread = threading.Thread(target=start_predictor)
predictor_thread.start()
