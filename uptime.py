import ctypes

lib = ctypes.windll.kernel32

t = lib.GetTickCount64()

t = int(str(t)[:-3])

mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)

print(f"{days} days, {hour:02}:{mins:02}:{sec:02}")
if mins >= 40:
    print("Its more than 40")
else:
    print("Its not more than 40")