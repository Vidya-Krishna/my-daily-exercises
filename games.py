#QUIZ 
ques = (('2. Which type of Programming does Python support?'),
        ('Is Python case sensitive when dealing with identifiers?'),
        (' Which of the following is the correct extension of the Python file?'),
        (' Is Python code compiled or interpreted?'))

ans = (('a) object-oriented programming','b) structured programming','c functional programming','d all of the mentioned'),
       ('a) no','b) yes','c) machine dependent','d) none'),
       ('a) .py','b) .ab','c) .pyt','d) .pl'),
       ('a)  Python code is both compiled and interpreted','b) Python code is neither compiled nor interpreted','c) Python code is only compiled','d) Python code is only interpreted'))
j_count = 0
score = 0
key = ('d', 'b', 'a', 'a')
for i in ques:
    print(i)
    for j in ans[j_count]:
        print(j)
    x = input('Choose an option: ')
    if x == key[j_count]:
        print('Currekt!!!')
        score+=1
    else: 
        print("Wurong Answer!!!")
    j_count += 1
    print('------------------------------------')
print('Tots scores is: ', int(score*100/len(key)),'%')

#There are a bunch of things I want to add but those things are breaking this. 

      

