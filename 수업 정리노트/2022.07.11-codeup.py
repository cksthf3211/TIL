dust = 100
# dust가 150보다 크면, 매우 나쁨
if dust > 150:
    print('매우나쁨')
# dust가 80보다 크면, 나쁨
elif dust > 80:
    print('나쁨')
# dust가 30보다 크면, 보통
elif dust > 30:
    print('보통')
else:
    print('좋음')