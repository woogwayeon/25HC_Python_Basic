import logging

def main():
    
    handler = logging.FileHandler("my.log")
    logger = logging.getLogger("fileLogger")
    logger.addHandler(handler) # 더해줘야함 두개를.. 그래서 addHandler
    logger.warning("이 메세지는 my.log에 저장됨")
    
if __name__ == "__main__":
    main()
    
'''
    대상: 지정된 파일
    - 사용처: 운영 환경 로그 기록, 장기 보관, 프로그램 종료후 분석. 
    
    - 인자
        • filename: 로그 파일 경로 및 이름. 
        • mode: 'a'(이어쓰기, 기본), 'w'(덮어쓰기). 
        • encoding: 인코딩 지정 (한글 등 utf-8 권장). 
    
    - 특징: 파일 크기 제한 없음, 직접 관리 필요
'''