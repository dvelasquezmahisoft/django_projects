import re

def getElements():
    return map(int, raw_input().split())

def getAllWords(size):
    res = []
    for i in range(0, size):
        res.append(raw_input())
    
    return res


def prepareTestCases(tests_cases, size, L):
    
    news = []
    for i in xrange(size):
        new_word = tests_cases[i].replace('(', '[').replace(')', ']')
        
        word = ""
        c_pos = 0 #posicion caracter
       
        while c_pos < L:
            char = new_word[c_pos]
            if char == '[':
                word = word + char
                char2 = char
                c_pos = c_pos + 1

                while char2 != ']':
                    char2 = new_word[c_pos]
                    word = word + char2 + ","
                    c_pos += 1
            else:
                word = word + char
                c_pos += 1

        word = word.replace('],', ']').replace(',]', ']').replace(',[', '[')
        
        news.append(word)

    return news

#####################################


(L, D, N) = getElements()
words = getAllWords(D)
tests_cases = prepareTestCases(getAllWords(N), D, L)

case_num = 1

for case in tests_cases:
    success_counter = 0
    for word in words:
        m = re.search(case, word)
        if m != None:
            success_counter += 1

    print "Case # %d: %d" % (case_num, success_counter)
    case_num += 1










