# Очень плохо у меня с математикой для таких задач

my_sum = 0
def bank(x,y):
    i = 0
    while i < y:
        x = (x + x*0.1)
        i = (i + 1)
    return x

print(bank(100,3))

# Как я это поняла (я бы сама не сообразила, опять же): i - это 
# просто счетчик, пока счетчик меньше введенных нами лет (допустим, 
# мы берем займ на 3 года, значит будет 1 год, 2 год, 3 год), 
# денежка у нас равна этой денежке + денежке, умноженной на 10%. 
# И мы выходим из цикла, прибавляя к счетчику еще 1 год. Я только 
# не совсем понимаю, а там не должно быть i <= y? И в 0 год мы 
# получается тоже 10% прибавляем? Я эту логику в голове уложить 
# не могу, дальше такие задачи не пойдут, если не научусь сама 
# думать так же. 

def calc_deposit(sum, term):
    for term in range (0, term):
        sum = sum*1.1
    return round(sum,2)

print(calc_deposit(1000,9))

