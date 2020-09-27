bandwidth = 10000000
delay = 10

metric = int(256 * ((10**7 / bandwidth) + (delay / 10)))

print(metric)
