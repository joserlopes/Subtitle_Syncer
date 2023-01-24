import sys
from MyTime import MyTime
import pysrt

def parseTime(standardTime):
    timeList = standardTime.split(":")
    return {"hours": int(timeList[0]), "minutes": int(timeList[1]), "seconds": int(timeList[2])}

def getMyTime(standardTime):
    timeList = standardTime.split(":")
    return MyTime(int(timeList[0]), int(timeList[1]), int(timeList[2]))

def main(args):
    try:
        to_start = parseTime(args[1])
        to_end = parseTime(args[2])
        to_start_MyTime = getMyTime(args[1])
        to_end_MyTime = getMyTime(args[2])
        to_save_path = args[3]
        difference = to_end_MyTime - to_start_MyTime
        subs = pysrt.open(args[0])
        part = subs.slice(starts_after=to_start, ends_before=to_end)
        new_subs = [x for x in subs if x not in part]
        for sub in new_subs:
            sub_end = MyTime(sub.end.hours, sub.end.minutes, sub.end.seconds)
            if (sub_end >= to_end_MyTime):
                sub.shift(hours=-difference.hours, minutes=-difference.minutes, seconds=-difference.seconds)

        with open(to_save_path, "w") as file:
            for sub in new_subs:
                file.write(str(sub) + '\n')
    except IndexError:
        print("Too few arguments were given.")

if __name__ == "__main__": 
    main(sys.argv[1:])