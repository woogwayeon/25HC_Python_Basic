import logging

def main():
    # %(asctime)s - 로그 발생 시간
    # %(levelname)s - 로그 레벨명
    
    fmt = '[%(asctime)s] [%(levelname)s] %(message)s'
    
    logging.basicConfig(format=fmt, level=logging.DEBUG)
    logging.warning("시간 표시 테스트 !!")

    logging.info("INFO Level !!")
    logging.warning("warning Level !!")

if __name__ == '__main__':
    main()

'''
    파이선에서 로그가 중요한 이유
    프린트구문은 말 그대로 보고싶은걸 한번 찍어보는 정도이다.
    상황에 따라 어떻게 바뀌는 것을 유동적으로 표시할 수 없다
    그래서 아무튼 필요함
    
    Debug
    Info
    Warning
    Error
    Critical
    
    이렇게 레벨이 나뉜다 (아래로 올수록 심각)
'''