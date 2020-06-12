sum_hours = {}
'''
with open('text_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        subject, lecture, practice, lab = line.split()
        key = subject
        print(key)
        s = str(lecture) + str(practice) + str(lab)
        l = len(s)
        integ = []
        i = 0
        while i < l:
            s_int = ''
            a = s[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < l:
                    a = s[i]
                else:
                    break
            i += 1
            if s_int != '':
                integ.append(int(s_int))
            val = sum(integ)
        #print(sum(integ))
        print(f' {val}')
'''


