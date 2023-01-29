"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

s = '12:01:00PM'
Return '12:01:00'.

s = '12:01:00AM'
Return '00:01:00'.
"""

def timeConversion(s):
    s = list(s)
    if int("".join(s[:2])) == 12 and "".join(s[-2:]) == "AM":
        s[0] = "0"
        s[1] = "0"
    elif int("".join(s[:2])) != 12 and "".join(s[-2:]) == "PM":
        s[0] = str(int(s[0]) + 1)
        s[1] = str(int(s[1]) + 2)
        
    return "".join(s[:-2])

#Alternative
def timeConversion2(s):
    s = s.split(':')
    if int(s[0]) == 12 and s[2][2:] == "AM":
        s[0] = "00"
    elif int(s[0]) != 12 and s[2][2:] == "PM":
        s[0] = str(int(s[0]) + 12)

    s[2] = s[2][:2]
    return ":".join(s)

print(timeConversion("07:05:45PM"))
print(timeConversion2("07:05:45PM"))