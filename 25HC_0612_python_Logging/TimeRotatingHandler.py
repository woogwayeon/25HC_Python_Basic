import logging
from logging.handlers import TimedRotatingFileHandler

def main():
        
    handler = TimedRotatingFileHandler('timelog.log.', when='M', interval=1, backupCount=7, encoding='utf-8')
    
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    handler.setFormatter(formatter)
    
    logger = logging.getLogger("timedLogger")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    logger.info("분마다 로그찍기")
    
if __name__ == "__main__":
    main()

'''
/* TimedRotatingFileHandler(파일명, when, interval, backupCount) */
    맨 처음 인자(string) // 저장할 파일명
    when = // 언제마다 새 파일? (예: 'S', 'M', 'H', 'D','midnight', 'W0' ~ 'W6')
    interval = // 몇 단위마다?
    backupCount = // 백업(보관)할 파일 수(초과 시 오래된 파일 자동 삭제)
    encoding = 'utf-8' // 한글 인코딩
'''