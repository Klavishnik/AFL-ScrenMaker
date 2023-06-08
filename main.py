import curses

def main(stdscr):
    # Инициализация библиотеки curses
    curses.curs_set(0)  # Скрыть курсор
    stdscr.nodelay(1)  # Сделать getch() неблокирующим
    stdscr.timeout(100)  # Установить таймаут ожидания ввода в миллисекундах


    # Определим все переменные, какие могут понадобиться
    var = {
        "AFL_VERSION" : "4.05c",
        "NAME" : "default",
        "PATH" : "/tmp/libxml2",
        #process timing
        "RUN_TIME_DAYS": 2,
        "RUN_TIME_HRS": 22,
        "RUN_TIME_MIN": 32,
        "RUN_TIME_SEC": 46,
        "LAST_NEW_FIND_DAYS": 4,
        "LAST_NEW_FIND_HRS": 5,
        "LAST_NEW_FIND_MIN": 6,
        "LAST_NEW_FIND_SEC": 7,
        "LAST_SAVED_CRASH_DAYS": 0, # |
        "LAST_SAVED_CRASH_HRS": 1,  # | | Если все по нулям ты выводит
        "LAST_SAVED_CRASH_MIN": 0,  # | | none seen yet
        "LAST_SAVED_CRASH_SEC": 0,  # |
        "LAST_SAVED_HANG_DAYS": 0, 
        "LAST_SAVED_HANG_HRS": 0, 
        "LAST_SAVED_HANG_MIN": 0, 
        "LAST_SAVED_HANG_SEC": 0, 
        #overall results
        "CYCLES_DONE": 1200,  #     <---- 0-50 red, 50-150 yellow, 150+ green
        "CORPUS_COUNT": 102,
        "SAVED_CRASHES": 1,
        "SAVED_HANGS": 0,
        #cycle progress
        "NOW_PROCESSING_NUM": 83.21,
        "NOW_PROCESSING_PERCENT": 88.3,
        #map coverage
        "MAP_DENSITY_1": 0.17,
        "MAP_DENSITY_2": 0.18,
        "COUNT_COVERAGE" : 1.67, 
        #stage progress
        "NOW_TRYING": "havoc", #      <----  splice [1-15]
        "STAGE_EXECS1": 105, 
        "STAGE_EXECS2": 384,
        "STAGE_EXECS_PERCENT": 5.48,
        "TOTAL_EXECS": 1.05,
        "EXEC_SPEED": 182.3,   #<----  <100 - RED< > 100 WHITE
        #finding in depth
        "FAVORED_ITEMS_NUM": 21,
        "FAVORED_ITEMS_PERCENT": 20.39,
        "NEW_EDGES_ON_NUM": 39,
        "NEW_EDGES_ON_PERCENT": 37.86,
        "TOTAL_CRASHES": 2, #     <----  ==0 - WHITE , >0 -- RED
        "TOTAL_TMOUTS": 0,
        #item_geometry
        "LEVELS": 11,
        "PENDING" : 2,
        "PEND_FAV": 0,
        "OWN_FINDS" : 90,
        "IMPORTED" : 12,
        "STABILITY": 87.75,
        "CPU": 55,      #<-----------  >90 RED, < GREEN
        "HAVOC1" : 84,
        "HAVOC2" : 1.04,
        "SPLICE1" : 21,
        "SPLICE2" : 1.79
    }

    # Настройка цветов
    curses.init_pair(1, 8, curses.COLOR_BLACK)                      # Серый цвет
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)      # Синий цвет
    curses.init_pair(3, 11,  curses.COLOR_BLACK)                    # Желтый цвет
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)     # Зеленый цвет
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)      # Светологубоватый  цвет
    curses.init_pair(6, 13 , curses.COLOR_BLACK)                    # Бордовый цвет
    curses.init_pair(7, 32 , curses.COLOR_BLACK)                    # ГОЛУБОЙ
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)     # Белый цвет
    curses.init_pair(9, curses.COLOR_RED, curses.COLOR_BLACK)       # Красный цвет

    # Определим цвета в переменные
    COLOR_GREY =        curses.color_pair(1)
    COLOR_BLUE =        curses.color_pair(2)
    COLOR_YELLOW  =     curses.color_pair(3)
    COLOR_GREEN =       curses.color_pair(4)
    COLOR_CYAN =        curses.color_pair(5)
    COLOR_BURGUNDY =    curses.color_pair(6)
    COLOR_WHITEBULE =   curses.color_pair(7)
    COLOR_WHITE =       curses.color_pair(8)
    COLOR_RED =         curses.color_pair(9)


    # Основной цикл программы
    while True:
        # Получить ввод пользователя
        key = stdscr.getch()
        if key == ord('q'):
            break  # Выход из программы при нажатии клавиши 'q'

        # Очистить экран
        stdscr.erase()

        # Вывести данные на экран
        stdscr.erase()
#------------------------------ СТРОКА 1 -----------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
        #Рисуем построчно - в первом комментарии формат строки, а далее идет код, который её отрисовывает
        # СТРОКА 1
        #    american fuzzy lop ++3.15a {default} (/tmp/nyx_libxml2/) [fast] - NYX
        stdscr.addstr(1, 0, "         american fuzzy lop", COLOR_YELLOW)  
        stdscr.addstr(" ++" + str(var["AFL_VERSION"]), COLOR_CYAN | curses.A_BOLD)

        stdscr.addstr(" {" + str(var["NAME"] + "}"), COLOR_BLUE | curses.A_BOLD)
        stdscr.addstr(" (" + str(var["PATH"] + ")"), COLOR_GREEN | curses.A_BOLD)
        stdscr.addstr(" [fast]", COLOR_BURGUNDY | curses.A_BOLD)

#------------------------------ СТРОКА 2 -----------------------------------------------------------------------------
#    ┌─ process timing ────────────────────────────────────┬─ overall results ────┐
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(2, 0, "┌─ ", COLOR_GREY)  
        stdscr.addstr("process timing", COLOR_WHITEBULE | curses.A_BOLD)  
        stdscr.addstr(" ────────────────────────────────────┬─", COLOR_GREY)  
        stdscr.addstr(" overall results", COLOR_WHITEBULE)  
        stdscr.addstr(" ────┐", COLOR_GREY)  

#------------------------------ СТРОКА 3 -----------------------------------------------------------------------------
#│        run time : 0 days, 0 hrs, 0 min, 14 sec      │  cycles done : 0     │
#---------------------------------------------------------------------------------------------------------------------
        
        stdscr.addstr(3, 0, "│        run time :", COLOR_GREY)
        stdscr.addstr(" " + str(var["RUN_TIME_DAYS"]) + " days,", COLOR_WHITE)
        stdscr.addstr(" " + str(var["RUN_TIME_HRS"]) + " hrs,", COLOR_WHITE)
        stdscr.addstr(" " + str(var["RUN_TIME_MIN"]) + " min,", COLOR_WHITE)
        stdscr.addstr(" " + str(var["RUN_TIME_SEC"]) + " sec", COLOR_WHITE)
        stdscr.addstr(3 , 54, "│  cycles done : ", COLOR_GREY)  
        if var["CYCLES_DONE"] < 50:
            stdscr.addstr(str(var["CYCLES_DONE"]) , COLOR_BURGUNDY)  
        elif var["CYCLES_DONE"] > 50 and var["CYCLES_DONE"] < 150:
            stdscr.addstr(str(var["CYCLES_DONE"]) , COLOR_YELLOW)  
        else:
            stdscr.addstr(str(var["CYCLES_DONE"]) , COLOR_GREEN)  
        stdscr.addstr(3 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 4 -----------------------------------------------------------------------------
#│   last new find : 0 days, 0 hrs, 0 min, 0 sec       │ corpus count : 96    │
#---------------------------------------------------------------------------------------------------------------------       
        stdscr.addstr(4, 0, "│   last new find :", COLOR_GREY)
        stdscr.addstr(" " + str(var["LAST_NEW_FIND_DAYS"]) + " days,", COLOR_WHITE)
        stdscr.addstr(" " + str(var["LAST_NEW_FIND_HRS"]) + " hrs,", COLOR_WHITE)
        stdscr.addstr(" " + str(var["LAST_NEW_FIND_MIN"]) + " min,", COLOR_WHITE)
        stdscr.addstr(" " + str(var["LAST_NEW_FIND_SEC"]) + " sec", COLOR_WHITE)
        stdscr.addstr(4 , 54, "│ corpus count : ", COLOR_GREY)  
        stdscr.addstr(str(var["CORPUS_COUNT"]) , COLOR_WHITE)  
        stdscr.addstr(4 , 77, "│", COLOR_GREY)  


#------------------------------ СТРОКА 5 -----------------------------------------------------------------------------
#│last saved crash : none seen yet                     │saved crashes : 0     │
#---------------------------------------------------------------------------------------------------------------------       
    
        stdscr.addstr(5, 0, "│last saved crash :", COLOR_GREY)
        if var["LAST_SAVED_CRASH_DAYS"] == 0 and var["LAST_SAVED_CRASH_HRS"] == 0 and var["LAST_SAVED_CRASH_MIN"] == 0 and var["LAST_SAVED_CRASH_SEC"] == 0:
            stdscr.addstr("none seen yet", COLOR_WHITE)  
        else: 
            stdscr.addstr(" " + str(var["LAST_SAVED_CRASH_DAYS"]) + " days,", COLOR_WHITE)
            stdscr.addstr(" " + str(var["LAST_SAVED_CRASH_HRS"]) + " hrs,", COLOR_WHITE)
            stdscr.addstr(" " + str(var["LAST_SAVED_CRASH_MIN"]) + " min,", COLOR_WHITE)
            stdscr.addstr(" " + str(var["LAST_SAVED_CRASH_SEC"]) + " sec", COLOR_WHITE)

        stdscr.addstr( 5 , 54, "│saved crashes : ", COLOR_GREY)  
        if var["SAVED_CRASHES"] == 0:
            stdscr.addstr(str(var["SAVED_CRASHES"]) , COLOR_WHITE)  
        else: 
            stdscr.addstr(str(var["SAVED_CRASHES"]) , COLOR_RED)  

        stdscr.addstr(5 , 77, "│", COLOR_GREY)  
      
#------------------------------ СТРОКА 6 -----------------------------------------------------------------------------
#│ last saved hang : none seen yet                     │  saved hangs : 0     │
#---------------------------------------------------------------------------------------------------------------------       
        stdscr.addstr(6, 0, "│ last saved hang : ", COLOR_GREY)
        if var["LAST_SAVED_HANG_DAYS"] == 0 and var["LAST_SAVED_HANG_HRS"] == 0 and var["LAST_SAVED_HANG_MIN"] == 0 and var["LAST_SAVED_HANG_SEC"] == 0:
            stdscr.addstr("none seen yet", COLOR_WHITE)  
        else: 
            stdscr.addstr(" " + str(var["LAST_SAVED_HANG_DAYS"]) + " days,", COLOR_WHITE)
            stdscr.addstr(" " + str(var["LAST_SAVED_HANG_HRS"]) + " hrs,", COLOR_WHITE)
            stdscr.addstr(" " + str(var["LAST_SAVED_HANG_MIN"]) + " min,", COLOR_WHITE)
            stdscr.addstr(" " + str(var["LAST_SAVED_HANG_SEC"]) + " sec", COLOR_WHITE)

        stdscr.addstr( 6 , 54, "│  saved hangs : ", COLOR_GREY)  
        stdscr.addstr(str(var["SAVED_HANGS"]) , COLOR_WHITE)  
        stdscr.addstr( 6 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 7 -----------------------------------------------------------------------------
#├─ cycle progress ─────────────────────┬─ map coverage┴──────────────────────┤
#---------------------------------------------------------------------------------------------------------------------     
        stdscr.addstr(7, 0, "├─ ", COLOR_GREY)  
        stdscr.addstr("cycle progress", COLOR_WHITEBULE | curses.A_BOLD)  
        stdscr.addstr(" ─────────────────────┬─", COLOR_GREY)  
        stdscr.addstr(" map coverage", COLOR_WHITEBULE)  
        stdscr.addstr("┴──────────────────────┤", COLOR_GREY)  

#------------------------------ СТРОКА 8 -----------------------------------------------------------------------------
#│  now processing : 28.0 (29.2%)       │    map density : 2.17% / 3.61%      │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(8, 0, "│  now processing :", COLOR_GREY)
        stdscr.addstr(" " + str(var["NOW_PROCESSING_NUM"]), COLOR_WHITE)
        stdscr.addstr(" (" + str(var["NOW_PROCESSING_PERCENT"]) + "%) ", COLOR_WHITE)
        stdscr.addstr(8 , 39, "│    map density : ", COLOR_GREY)  
        stdscr.addstr(str(var["MAP_DENSITY_1"]) + "% / ", COLOR_WHITE)  
        stdscr.addstr(str(var["MAP_DENSITY_2"]) + "%", COLOR_WHITE)  
        stdscr.addstr(8 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 9 -----------------------------------------------------------------------------
#│  runs timed out : 0 (0.00%)          │ count coverage : 1.67 bits/tuple    │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(9, 0, "│  runs timed out :", COLOR_GREY)
        stdscr.addstr(" 0 (0.00%)", COLOR_WHITE)
        stdscr.addstr(9 , 39, "│ count coverage : ", COLOR_GREY)  
        stdscr.addstr(str(var["COUNT_COVERAGE"]) + " bits/tuple", COLOR_WHITE)  
        stdscr.addstr(9 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 10 -----------------------------------------------------------------------------
#├─ stage progress ─────────────────────┼─ findings in depth ─────────────────┤
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(10, 0, "├─ ", COLOR_GREY)  
        stdscr.addstr("stage progress", COLOR_WHITEBULE | curses.A_BOLD)  
        stdscr.addstr(" ─────────────────────┼─ ", COLOR_GREY)  
        stdscr.addstr("findings in depth", COLOR_WHITEBULE)  
        stdscr.addstr(" ─────────────────┤", COLOR_GREY)  

#------------------------------ СТРОКА 11 -----------------------------------------------------------------------------
#│  now trying : havoc                  │ favored items : 27 (28.12%)         │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(11, 0, "│  now trying :", COLOR_GREY)
        stdscr.addstr(" " + str(var["NOW_TRYING"]), COLOR_WHITE)
        stdscr.addstr(11 , 39, "│ favored items : ", COLOR_GREY)  
        stdscr.addstr(str(var["FAVORED_ITEMS_NUM"]), COLOR_WHITE)  
        stdscr.addstr(" (" + str(var["FAVORED_ITEMS_PERCENT"]) + "%)", COLOR_WHITE)  
        stdscr.addstr(11 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 12 -----------------------------------------------------------------------------
#│ stage execs : 22.3k/32.8k (68.19%)   │  new edges on : 58 (60.42%)         │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(12, 0, "│ stage execs :", COLOR_GREY)
        stdscr.addstr(" " + str(var["STAGE_EXECS1"]), COLOR_WHITE)
        stdscr.addstr("/" + str(var["STAGE_EXECS2"]), COLOR_WHITE)
        stdscr.addstr(" (" + "{:.2f}".format(var["STAGE_EXECS1"] / var["STAGE_EXECS2"] * 100 ) + "%)", COLOR_WHITE)
        stdscr.addstr(12 , 39, "│  new edges on : ", COLOR_GREY)  
        stdscr.addstr(str(var["NEW_EDGES_ON_NUM"]), COLOR_WHITE)  
        stdscr.addstr(" (" + str(var["NEW_EDGES_ON_PERCENT"]) + "%)", COLOR_WHITE)  
        stdscr.addstr(12 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 13 -----------------------------------------------------------------------------
#│ total execs : 55.9k                  │ total crashes : 0 (0 saved)         │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(13, 0, "│ total execs :", COLOR_GREY)
        stdscr.addstr(" " + str(var["TOTAL_EXECS"]), COLOR_WHITE)
        stdscr.addstr(13 , 39, "│ total crashes : ", COLOR_GREY)  
        if var["TOTAL_CRASHES"] == 0:
            stdscr.addstr(str(var["TOTAL_CRASHES"]), COLOR_WHITE)  
            stdscr.addstr(" (0 saved)", COLOR_WHITE)  
        else:
            stdscr.addstr(str(var["TOTAL_CRASHES"]), COLOR_RED)  
            stdscr.addstr(" (" + str(var["TOTAL_CRASHES"]) + " unique)", COLOR_RED)  
        stdscr.addstr(13 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 13 -----------------------------------------------------------------------------
#│  exec speed : 3810/sec               │  total tmouts : 0 (0 saved)         │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(14, 0, "│  exec speed : ", COLOR_GREY)
        if var["EXEC_SPEED"] < 100:
            stdscr.addstr(str(var["EXEC_SPEED"]) + "/sec ", COLOR_RED)  
        else:
            stdscr.addstr(str(var["EXEC_SPEED"]) + "/sec ", COLOR_WHITE)  

        stdscr.addstr(14 , 39, "│  total tmouts : ", COLOR_GREY)  
        stdscr.addstr(str(var["TOTAL_TMOUTS"]), COLOR_WHITE)  
        stdscr.addstr(" (" + str(var["TOTAL_TMOUTS"]) + " saved)", COLOR_WHITE)  
        stdscr.addstr(14 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 15 -----------------------------------------------------------------------------
#├─ fuzzing strategy yields ────────────┴─────────────┬─ item geometry ───────┤
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(15, 0, "├─ ", COLOR_GREY)  
        stdscr.addstr("fuzzing strategy yields", COLOR_WHITEBULE | curses.A_BOLD)  
        stdscr.addstr(" ────────────┴─────────────┬─ ", COLOR_GREY)  
        stdscr.addstr("item geometry", COLOR_WHITEBULE)  
        stdscr.addstr(" ───────┤", COLOR_GREY)  

#------------------------------ СТРОКА 16 -----------------------------------------------------------------------------
#│   bit flips : disabled (default, enable with -D)   │    levels : 3         │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(16, 0, "│   bit flips :", COLOR_GREY)
        stdscr.addstr(" disabled (default, enable with -D)", COLOR_WHITE)
        stdscr.addstr(16 , 53, "│    levels : ", COLOR_GREY)  
        stdscr.addstr(str(var["LEVELS"]), COLOR_WHITE)  
        stdscr.addstr(16 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 17 -----------------------------------------------------------------------------
#│  byte flips : disabled (default, enable with -D)   │   pending : 95        │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(17, 0, "│  byte flips :", COLOR_GREY)
        stdscr.addstr(" disabled (default, enable with -D)", COLOR_WHITE)
        stdscr.addstr(17 , 53, "│   pending : ", COLOR_GREY)  
        stdscr.addstr(str(var["PENDING"]), COLOR_WHITE)  
        stdscr.addstr(17 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 18 -----------------------------------------------------------------------------
#│  arithmetics : disabled (default, enable with -D)   │  pend fav : 27        │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(18, 0, "│ arithmetics :", COLOR_GREY)
        stdscr.addstr(" disabled (default, enable with -D)", COLOR_WHITE)
        stdscr.addstr(18 , 53, "│  pend fav : ", COLOR_GREY)  
        stdscr.addstr(str(var["PEND_FAV"]), COLOR_WHITE)  
        stdscr.addstr(18 , 77, "│", COLOR_GREY)  


#------------------------------ СТРОКА 19 -----------------------------------------------------------------------------
#│ known ints : disabled (default, enable with -D)   │ own finds : 95 |
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(19, 0, "│  known ints :", COLOR_GREY)
        stdscr.addstr(" disabled (default, enable with -D)", COLOR_WHITE)
        stdscr.addstr(19 , 53, "│ own finds : ", COLOR_GREY)  
        stdscr.addstr(str(var["OWN_FINDS"]), COLOR_WHITE)  
        stdscr.addstr(19 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 20 -----------------------------------------------------------------------------
#│ dictionary : n/a                                  │  imported : 0         │
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(20, 0, "│  dictionary :", COLOR_GREY)
        stdscr.addstr(" n/a  ", COLOR_WHITE)
        stdscr.addstr(20 , 53, "│  imported : ", COLOR_GREY)  
        stdscr.addstr(str(var["IMPORTED"]), COLOR_WHITE)  
        stdscr.addstr(20 , 77, "│", COLOR_GREY)  

#------------------------------ СТРОКА 21 -----------------------------------------------------------------------------
#│ havoc/splice : 57/32.8k, 0/0                        │ stability : 100.00% 
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(21, 0, "│havoc/splice :", COLOR_GREY)
        stdscr.addstr(" " + str(var["HAVOC1"]), COLOR_WHITE)
        stdscr.addstr("/" + str(var["HAVOC2"]) + "M,", COLOR_WHITE)
         
        stdscr.addstr(" " + str(var["STAGE_EXECS1"]), COLOR_WHITE)
        stdscr.addstr("/" + str(var["STAGE_EXECS2"]) + "M,", COLOR_WHITE)

        stdscr.addstr(21 , 53, "│ stability : ", COLOR_GREY)  
        stdscr.addstr(str(var["STABILITY"]), COLOR_BURGUNDY)  
        stdscr.addstr(21 , 77, "│", COLOR_GREY)  


#------------------------------ СТРОКА 22 -----------------------------------------------------------------------------
#│ py/custom/rq : unused, unused, unused, unused       ├───────────────────────┘
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(22, 0, "│py/custom/rq :", COLOR_GREY)
        stdscr.addstr(" unused, unused, unused, unused  ", COLOR_WHITE)
        stdscr.addstr(22 , 53, "├───────────────────────┘", COLOR_GREY)  

#------------------------------ СТРОКА 23 -----------------------------------------------------------------------------
#│    trim/eff : n/a, disabled                        │          [cpu000: 25%]
#---------------------------------------------------------------------------------------------------------------------
        stdscr.addstr(23, 0, "|    trim/eff :", COLOR_GREY)
        stdscr.addstr(" n/a, disabled  ", COLOR_WHITE)
        stdscr.addstr(23 , 53, "│", COLOR_GREY)  
        stdscr.addstr(23 , 63, " [cpu000: ", COLOR_GREY)  
        
        if var["CPU"] < 90:
            stdscr.addstr(str(var["CPU"]), COLOR_GREEN)  
            stdscr.addstr("%", COLOR_GREEN)
        else:
            stdscr.addstr(str(var["CPU"]), COLOR_RED)  
            stdscr.addstr("%", COLOR_RED)
        stdscr.addstr("]", COLOR_GREY)

#------------------------------ СТРОКА 24 -----------------------------------------------------------------------------
#└────────────────────────────────────────────────────┘
#---------------------------------------------------------------------------------------------------------------------
        # Отрисовка нижней границы окна
        stdscr.addstr(24, 0, "└────────────────────────────────────────────────────┘", COLOR_GREY)


#------------------------------ КОНЕЦ -----------------------------------------------------------------------------
        # Обновить экран
        stdscr.refresh()

# Запуск программы
if __name__ == "__main__":
    curses.wrapper(main)
