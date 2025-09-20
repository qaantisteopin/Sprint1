string = "1h 45m,360s,25m,30m 120s,2h 60s"


def minutes_result(string: str):
    array = string.split(",")
    minutes_result = 0
    for element in array:
        elements = element.split()
        for el in elements:
            if "h" in el:
                hours = int(el.replace("h", ""))
                minutes_result += hours * 60
            elif "m" in el:
                minutes = int(el.replace("m", ""))
                minutes_result += minutes
            elif "s" in el:
                seconds = int(el.replace("s", ""))
                minutes_result += seconds / 60
    return minutes_result


print(f"Общее количество минут: {minutes_result(string)}")
