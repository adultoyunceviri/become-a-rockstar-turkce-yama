init -1 python:

    def Set_Time_of_Day(timeValue):
        return TimeOfDay_Dict[ TimeOfDay_Dict.keys()[TimeOfDay_Dict.values().index(timeValue)] ]
    def Increment_Time_Of_Day():
            if time_of_day == 'MORNING':
                temp = Set_Time_of_Day('AFTERNOON')
            elif time_of_day == 'AFTERNOON':
                temp = Set_Time_of_Day('EVENING')
            elif time_of_day == 'EVENING':
                temp = Set_Time_of_Day('NIGHT')
            else:
                temp = 'NIGHT'
            return temp

    def setReplay():
        global mc        
        global n
        global name
        global dep
        mc = ""
        dep = 5        
        if persistent.n:
                mc = persistent.n
        else:
                mc = "John"


init -2 python:
    import string

    qte_word = ""
    next_k = ""
    qteTime = .0
    qteMaxTime = 5.0
    abc = list(string.ascii_lowercase)

    def qte_init(word="", time=5.0, length=5):
        global qte_word, next_k, qteMaxTime, qteTime
        qteMaxTime = time
        qteTime = time
        qte_word = word.lower()
        if word:
            next_k = qte_word[0]
        else:
            for i in range(0, length):
                qte_word = qte_word + renpy.random.choice(abc)
                next_k = qte_word[0]
        renpy.restart_interaction()

    def next_key():
        global qte_word, next_k
        qte_word = qte_word[1:]
        next_k = ""
        if qte_word:
            next_k = qte_word[0]
        renpy.restart_interaction()
    NextKey = renpy.curry(next_key)
    qteInit = renpy.curry(qte_init)

screen scr_qte(word="", time=5.0, length=5):

    on 'show' action qteInit(word, time, length)
    modal True
    if qte_word:
        timer 0.01 repeat True action [SetVariable("qteTime", qteTime - .01), If(qteTime <= .0, true=Return(False))]
        text next_k.upper() align(.5, .5) size 96
        if len(next_k) == 1:
            key next_k action NextKey()
    else:
        timer .1 action Return(True)
    bar value StaticValue(qteTime, qteMaxTime) align(.5, .1) xmaximum 600
