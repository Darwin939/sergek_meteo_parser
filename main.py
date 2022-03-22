from parser.parser import SergekParser
import schedule
import time


if __name__ == '__main__':
    s = SergekParser()

    schedule.every(1).minutes.do(s.parse)
    while True:
        schedule.run_pending()
        time.sleep(1)
