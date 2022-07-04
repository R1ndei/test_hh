intervals = {
    "lesson": [1594663200, 1594666800],
    "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    "tutor": [1594663290, 1594663430, 1594663443, 1594666473]
}


def appearance(intervals: dict) -> int:
    lesson, pupil, tutor = intervals["lesson"], intervals["pupil"], intervals["tutor"]
    lesson_range = range(lesson[0], lesson[1] + 1)
    pupil_range, tutor_range = make_range(pupil), make_range(tutor)
    interval_list = []
    check_list = [] + lesson + pupil + tutor
    for timestamp in check_list:
        if timestamp in lesson_range:
            pupil_result = check_in_range(timestamp, pupil_range)
            tutor_result = check_in_range(timestamp, tutor_range)
            if pupil_result and tutor_result:
                interval_list.append(timestamp)
    interval_list.sort()
    time = 0
    for i in range(1, len(interval_list), 2):
        delta = interval_list[i] - interval_list[i - 1]
        time += delta
    return time


def check_in_range(timestamp: int, ranges: list) -> bool:
    for timedelta in ranges:
        if timestamp in timedelta:
            return True


def make_range(intervals: list) -> list:
    range_list = []
    for i in range(1, len(intervals), 2):
        range_list.append(range(intervals[i - 1], intervals[i] + 1))
    return range_list


print(appearance(intervals))