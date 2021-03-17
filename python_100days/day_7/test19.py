def is_leap_year(year):
    return year%4 == 0 and year%100 != 0 or year%400 == 0

def days_time(year, mouth, day):
    days_num = 0
    mouth_day = [
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ][is_leap_year(year)]
    for index in range(mouth-1):
        days_num += mouth_day[index]  
    return days_num + day

def main():
    print(days_time(1980, 11, 28))
    print(days_time(1981, 12, 31))
    print(days_time(2018, 1, 1))
    print(days_time(2016, 3, 1))

if __name__ == "__main__":
    main()