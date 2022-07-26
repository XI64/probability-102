# max group size, we pick 367 to also
# illustrate the pigeonhole principle!
n = 367
# number of days in the year, assume not a leap year.
days = 365
# calculate probability
p = 1.0
for i in range(1, n):
        av = days - i
        p *= av / days
        print('n=%d, %d/%d, p=%.3f 1-p=%.3f' % (i+1, av, days, p*100, (1-p)*100))
