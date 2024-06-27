import string

input_int = ""

while not input_int.isdigit() or int(input_int) not in range(0, 8640000):
    input_int = input("Input an integer in range [0, 8640000): ").strip(string.punctuation + " ")

work_int = int(input_int)

days, work_int = divmod(work_int, 60 * 60 * 24)
hours, work_int = divmod(work_int, 60 * 60)
mins, secs = divmod(work_int, 60)

result = str(days).zfill(1) + " days " + ":".join((str(hours).zfill(2), str(mins).zfill(2), str(secs).zfill(2)))

if str(days)[-1] == "1" and days not in range(10, 20):
    result = result.replace("days", "день")
elif str(days)[-1] in ("2", "3", "4") and days not in range(10, 20):
    result = result.replace("days", "дні")
else:
    result = result.replace("days", "днів")

print(input_int, result, sep=" -> ")