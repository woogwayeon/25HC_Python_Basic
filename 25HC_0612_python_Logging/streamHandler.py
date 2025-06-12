import logging

def main():
    
    handler = logging.StreamHandler()
    logger = logging.getLogger("consoleLogger")
    logger.addHandler(handler) # 더해줘야함 두개를.. 그래서 addHandler
    logger.warning("콘솔에 나와라")
    
if __name__ == "__main__":
    main()