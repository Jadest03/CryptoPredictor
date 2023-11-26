import time

file_path = 'coin.csv'

def data_get():
    def read_file_content():
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            content = file.read()
            return content

    while True:
        content = read_file_content()
        # 가져온 내용(content)을 다른 프로그램에서 활용
        print(content)
        time.sleep(1)
