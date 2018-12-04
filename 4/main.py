#!/usr/bin/python3
import re
import sys
import datetime
from collections import defaultdict

GUARD_RE = re.compile(
    r"(\[\d+-\d+-\d+ \d+:(\d+)\]) (?:(falls asleep)|(wakes up)|Guard #(\d+) begins shift)")

schedule = []
for line in sys.stdin.readlines():
    schedule.append(tuple(GUARD_RE.match(line).groups()))

schedule.sort(key=lambda x: datetime.datetime.strptime(
    x[0], "[%Y-%m-%d %H:%M]").timestamp())

guard_minutes = defaultdict(int)
guard_total = defaultdict(int)
current_guard = None
sleep_begin = None

for date, minute, sleep, wake, guard_id in schedule:
    if guard_id:
        current_guard = int(guard_id)
    elif sleep:
        sleep_begin = int(minute)
    elif wake:
        for i in range(sleep_begin,int(minute)):
            guard_minutes[(current_guard,i)] += 1
            guard_total[current_guard] += 1

print(guard_minutes)
print(guard_total)
best_guard, _ = max(guard_total.items(), key = lambda kv: kv[1])
_, minute = max(((k,v) for k,v in guard_minutes.items() if k[0] == best_guard), key=lambda kv: kv[1])[0]
print(best_guard,minute)

print('Part 1:',best_guard * minute)

best_guard2, best_minute = max(guard_minutes.items(), key=lambda kv: kv[1])[0]
print('Part 2:',best_guard2 * best_minute)
