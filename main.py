x = str(input('Please enter a string:'))
consonants = 'qwrtyplkjhgfdszxcvbnm'
vowels = 'aeiou'

def cvCount(word):
    counter_c = 0
    counter_v = 0
    for i in word.lower():
        if i in consonants:
            counter_c +=1
        elif i in vowels:
            counter_v +=1
    return counter_c, counter_v

result = cvCount(x)

print('\nThe word', x, 'contains', result[0],'consonants and', result[1],'vowels')