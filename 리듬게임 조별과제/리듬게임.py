import pygame
import time
import math
import random
import pyautogui

IDIN = ["test1"]
PWIN = ["1234567890"]

BASE_ADD = "C:\\Users\\곽도훈\\Desktop\\리듬게임 조별과제\\리듬게임 조별과제\\"
BACK_ADD = BASE_ADD + "배경음악.wav"
MUSIC_ADD = [BASE_ADD + "Lagtrain.wav", BASE_ADD + "WaterDrops.wav", BASE_ADD + "Mountain.wav"]
MUSIC_LIST =  [[[8.1, 9.3, 10.2, 11.0, 11.8, 12.2, 13.2, 14.0, 14.6, 15.1, 15.9, 17.5, 18.1, 18.7
                ,19.3, 20.0, 20.4, 21.2, 22.4, 23.2, 24.2, 24.8, 25.3, 25.7, 26.3, 26.7, 27.1, 27.7
                ,28.9, 30.0, 30.6, 31.2, 31.8, 32.4, 33.8, 34.2],  #music1, difficulty: easy
                [8.1 ,8.3 ,8.5 ,8.7 ,8.9 ,9.3 ,9.5 ,9.7 ,10.2 ,10.4 ,10.6 ,11.0 ,11.2 ,11.4 ,11.8
                ,12.2 ,12.4 ,12.5 ,12.6 ,12.8 ,13.2 ,13.4 ,13.6 ,14.0 ,14.2 ,14.6 ,14.8 ,15.1 ,15.3 ,15.5 ,15.9
                ,16.1 ,16.3 ,16.5 ,16.7 ,16.9 ,17.1 ,17.5 ,17.7 ,18.1 ,18.3 ,18.7 ,18.9 ,19.3 ,19.5 ,20.0 ,20.4
                ,20.6 ,20.8 ,21.2 ,21.4 ,21.6 ,21.8 ,22.0 ,22.4 ,22.6 ,22.8 ,23.2 ,23.4 ,23.6 ,24.2 ,24.4 ,24.8
                ,25.3 ,25.7 ,25.9 ,26.3 ,26.5 ,26.7 ,27.1 ,27.3 ,27.7 ,27.9 ,28.1 ,28.3 ,28.5 ,28.9 ,29.1 ,29.3
                ,29.5 ,29.7 ,30.0 ,30.2 ,30.6 ,30.8 ,31.2 ,31.4 ,31.8 ,32.0 ,32.4 ,32.6 ,32.8 ,33.0 ,33.2 ,33.4 ,33.8 ,34.2]], #music1, difficulty: hard
               [[5.3,6.0,6.3,6.6,7.3,7.6,7.8,8.1,8.3,8.6,8.7,9.1,9.2,9.7,10.4,10.7,11.3,11.5,12.0,
                12.2,12.5,13.1,13.4,13.9,14.4,14.6,15.2,15.2,15.4,
                16.0,16.4,16.7,17.2,17.3,17.7,18.0,18.6,18.8,
                19.1,19.3,19.6,19.9,20.1,20.4,20.7,21.2,21.4,21.7,22.0,22.2,22.9,
                23.5,24.5,25.0,25.1,25.4,25.6,25.9,26.1,26.3,26.4,26.5,27.2,27.2,
                27.4,28.0,28.5,28.7,29.5,29.7,30.0,30.6,31.1,31.4],  #music2, difficulty: easy
                [5.0 ,5.2 ,5.3 ,5.5 ,5.7 ,5.8 ,5.9 ,6.0 ,6.1 ,6.2 ,6.3 ,6.5 ,6.6 ,6.8 ,7.0 ,7.3 ,7.4 ,7.6 ,7.8 ,7.9 ,8.1,
                8.3 ,8.4 ,8.6 ,8.7 ,8.9 ,9.1 ,9.2 ,9.4 ,9.6 ,9.7 ,9.9 ,10.0 ,10.2 ,10.4 ,10.7 ,10.9 ,11.0 ,11.1 ,11.2 ,11.3 ,11.5 ,11.7 ,11.8 ,12.0,
                12.2 ,12.5 ,12.7 ,12.8 ,13.0 ,13.1 ,13.3 ,13.4 ,13.6 ,13.7 ,13.8 ,13.9 ,14.0 ,14.1 ,14.3 ,14.4 ,14.6 ,14.7 ,15.1 ,15.2 ,15.4 ,15.6,
                15.7 ,15.9 ,16.0 ,16.2 ,16.3 ,16.4 ,16.5 ,16.7 ,16.9 ,17.0 ,17.2 ,17.3 ,17.7 ,17.8 ,18.0 ,18.2 ,18.3 ,18.5 ,18.6 ,18.8 ,19.0,
                19.1 ,19.3 ,19.4 ,19.6 ,19.8 ,20.0 ,20.1 ,20.3 ,20.4,20.6,20.7,21.1,21.4,21.7,21.9,22.0,22.2,22.4,22.5,22.9,23.0,23.3,
                23.5,23.7,23.8,24.0,24.5,24.6,24.8,25.0,25.1,25.4,25.6,25.8,25.9,26.1,26.3,26.4,26.5,26.6,26.9,27.0,27.1,27.2,
                27.4,27.6,27.7,28.0,28.2,28.5,28.7,28.9,29.0,29.2,29.5,29.7,29.8,30.0,30.2,30.3,30.6,30.8,31.0,31.1,31.4]],#music2, difficulty: hard
               [[05.1, 05.3, 05.7, 06.0, 06.6, 06.8, 07.5, 07.7, 08.3, 09.0, 10.0, 11.7, 13.6, 14.3, 15.0, 
                 16.0, 17.5, 18.2, 21.0, 23.5, 24.0, 26.4, 27.4, 28.0, 28.7, 29.5, 30.0, 
                 30.8, 31.5, 32.3, 33.4, 34.7, 38.0, 39.0, 44.5],
                [05.1, 05.3, 05.4, 05.5, 05.7, 06.0, 06.2, 06.3, 06.4, 06.6, 06.8, 07.1, 07.2, 07.5, 07.7, 07.9, 08.0, 08.1, 08.3,
                 08.5, 08.7, 09.0, 09.2, 09.4, 09.6, 09.7, 09.8, 10.0, 10.2, 10.5, 10.7, 10.9, 11.1, 11.3, 11.5, 11.7, 12.0, 12.1, 
                 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13.1, 13.2, 13.3, 13.5, 13.6, 13.7, 14.3, 15.0, 15.4, 15.8, 
                 16.0, 16.2, 16.7, 17.1, 17.5, 17.7, 18.0, 18.2, 18.3, 18.4, 18.6, 18.7, 18.8, 19.0, 19.1, 19.2, 19.5, 19.7, 20.1, 
                 20.3, 20.5, 21.0, 21.2, 21.4, 21.8, 22.0, 22.2, 22.6, 22.9, 23.1, 23.5, 23.7, 24.0, 24.2, 24.3, 24.4, 24.6, 24.8, 
                 25.2, 25.5, 25.7, 25.8, 25.9, 26.0, 26.1, 26.2, 26.4, 26.5, 27.2, 27.4, 28.0, 28.7, 29.1, 29.5, 29.7, 30.0, 30.4, 
                 30.8, 31.5, 31.7, 31.9, 32.0, 32.3, 32.4, 32.5, 32.7, 32.8, 33.0, 33.2, 33.4, 33.8, 34.0, 34.2, 34.7, 34.9, 35.1, 
                 35.5, 35.7, 36.0, 36.3, 36.6, 36.8, 37.2, 37.5, 37.7, 37.9, 38.0, 38.1, 38.3, 38.5, 39.0, 39.2, 39.4, 39.5, 39.6,
                 39.7, 39.8, 39.9, 40.1, 40.2, 40.7, 40.9, 41.1, 44.5]]]
WIDTH = 480
HEIGHT = 680

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
YELLOW= (255, 255,   0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
music_select = 0
difficulty = 0
note_speed = 0

perfect = 0 
good = 0 
miss = 0

D_N = ["easy", "hard"]

def fillWhite(s_pos_x, s_pos_y, f_pos_x, f_pos_y):
    global screen
    pygame.draw.rect(screen, WHITE,[s_pos_x, s_pos_y, f_pos_x - s_pos_x, f_pos_y - s_pos_y])

def draw_str(s, size, pos_x, pos_y):
    global screen
    font = pygame.font.SysFont("arial", size, False, False) #글씨체, 크기조절
    text = font.render(s, True, BLACK) #노래제목 출력
    screen.blit(text,(pos_x ,pos_y))
    
def login_regist():
    pygame.init()
    screen = pygame.display.set_mode((480, 680))
    pygame.display.set_caption("게암을 들어가기전")
    background_addr = BASE_ADD + "로그인화면.png"
    background = pygame.image.load(background_addr)
    screen.blit(background, (0, 0))
    clock = pygame.time.Clock()
    
    login = [[162, 150],[292, 200]]
    SignUp = [[156, 400],[322, 455]]

    running =True
    while running:
        clock.tick_busy_loop(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = [event.pos[0],event.pos[1]]
                if event.button == 1:
                    if (login[0][0] <= pos[0] <= login[1][0]) & (login[0][1] <= pos[1] <= login[1][1]):
                        return 0
                    elif (SignUp[0][0] <= pos[0] <= SignUp[1][0]) & (SignUp[0][1] <= pos[1] <= SignUp[1][1]):
                        return 6
        pygame.display.update()
    return -1

def regist():
    id = (str)(pyautogui.prompt(title='ID',text='생성할 ID를 입력하세요'))
    if id in IDIN:
        return 6
    pw = (str)(pyautogui.password(title='PW', text='생성할 PW를 입력하세요.'))
    IDIN.append(id)
    PWIN.append(pw)
    return 7
    
def login():
    id = (str)(pyautogui.prompt(title='ID',text='ID를 입력하세요'))
    for i in range(len(IDIN)):
        if id == IDIN[i] and id != "":
            pw = (str)(pyautogui.password(title='PW', text='PW를 입력하세요.'))
            if pw == PWIN[i]:
                return 1
            else:
                return 7
    return 7


def main():
    screensize = (1280,720)
    screentitle = "리듬게임"
    screen = pygame.display.set_mode(screensize)
    pygame.display.set_caption(screentitle)
    bgimg = pygame.image.load(BASE_ADD+"/메인화면.png")
    sound = pygame.mixer.Sound(BACK_ADD)
    sound.play(-1)
    bgimg = pygame.transform.scale(bgimg, screensize)
    screen.blit(bgimg,(0,0))
    repeatflag=True
    start_pos=[(385,345),(930,480)]
    quit_pos=[(385,520),(930,650)]
    #마우스 클릭이 (710,535),(1250,535),(710,665),(1250,665)이면 종료
    #마우스 클릭이 (710,705),(1250,705),(710,835),(1250,835)이면 종료
    while repeatflag:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    if (start_pos[0][0] <= pos [0] <= start_pos[1][0]) & (start_pos[0][1] <= pos[1]<= start_pos[1][1]):
                        sound.stop()
                        return 2
                    elif (quit_pos[0][0]  <= pos [0] <= quit_pos[1][0]) & (quit_pos[0][1] <= pos[1]<= quit_pos[1][1]):
                        sound.stop()
                        return -1
            if event.type == pygame.QUIT:
                repeatflag = False
        pygame.display.update()
    return -1

def music():
    global screen, music_select
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("노래 선택창")
    background_addr = BASE_ADD+"/노래선택화면.png"
    sound = pygame.mixer.Sound(BACK_ADD)
    sound.play(-1)
    background = pygame.image.load(background_addr)
    screen.blit(background, (0, 0))

    lagtrain = [[73, 102],[408, 253]]
    waterdrop = [[73, 289],[408, 439]]
    mountain = [[73, 475],[408, 626]]
    
    running =True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = [event.pos[0],event.pos[1]]
                if event.button == 1:
                    if (lagtrain[0][0] <= pos[0] <= lagtrain[1][0]) & (lagtrain[0][1] <= pos[1] <= lagtrain[1][1]):
                        music_select = 0
                        sound.stop()
                        return 3
                    elif (waterdrop[0][0] <= pos[0] <= waterdrop[1][0]) & (waterdrop[0][1] <= pos[1] <= waterdrop[1][1]):
                        music_select = 1
                        sound.stop()
                        return 3
                    elif (mountain[0][0] <= pos[0] <= mountain[1][0]) & (mountain[0][1] <= pos[1] <= mountain[1][1]):
                        music_select = 2
                        sound.stop()
                        return 3
        pygame.display.update()
    sound.stop()
    return -1


def level():
    global difficulty, music_select, note_speed
    pygame.init()
    pygame.display.set_caption("난이도선택창")
    sound = pygame.mixer.Sound(MUSIC_ADD[music_select])
    sound.play(-1)
    screen.fill(WHITE)
    clock = pygame.time.Clock()
    start_pos = [[180 ,580], [290 ,620]]#시작버튼 위치
    back_pos = [[350 ,10], [450 ,55]]#뒤로가기버튼 위치
    speed1_pos = [[300 ,225], [430 ,260]]#속도1버튼 위치
    speed2_pos = [[300 ,325], [430 ,360]]#속도2버튼 위치
    speed3_pos = [[300 ,425], [430 ,460]]#속도3버튼 위치
    difficulty1_pos = [[40 ,225], [130 ,265]]#난이도1버튼 위치
    difficulty3_pos = [[40 ,425], [135 ,465]]#난이도3버튼 위치
    draw_str("BACK", 40, 350, 10)
    draw_str("START", 40, 180, 580)
    
    draw_str("EASY", 40, 40, 225)
    draw_str("HARD", 40, 40, 425)
    
    draw_str("SPEED1", 40, 300, 225)
    draw_str("SPEED2", 40, 300, 325)
    draw_str("SPEED3", 40, 300, 425)

    running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
    while running:
        clock.tick(10)
        fillWhite(180, 100, 450 ,160)
        fillWhite(0, 480, 480 ,560)
        
        draw_str("MUSIC : "+ "lagtrain"if music_select == 0 else "waterdrop" if music_select == 1 else "mountain", 40, 120, 100)
        draw_str("difficulty: " + D_N[difficulty], 30, 40, 525)
        draw_str("Note Speed: " + (str)(note_speed + 1), 30, 300, 525)
                    
        for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
            if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = [event.pos[0],event.pos[1]]
                if event.button == 1:
                    
                    if (start_pos[0][0] <= pos[0] <= start_pos[1][0]) & (start_pos[0][1] <= pos[1] <= start_pos[1][1]):
                        sound.stop()
                        return 4
                    
                    elif (back_pos[0][0] <= pos[0] <= back_pos[1][0]) & (back_pos[0][1] <= pos[1] <= back_pos[1][1]):
                        sound.stop()
                        return 2
                    
                    elif (speed1_pos[0][0] <= pos[0] <= speed1_pos[1][0]) & (speed1_pos[0][1] <= pos[1] <= speed1_pos[1][1]):
                        note_speed = 0
                    
                    elif (speed2_pos[0][0] <= pos[0] <= speed2_pos[1][0]) & (speed2_pos[0][1] <= pos[1] <= speed2_pos[1][1]):
                        note_speed = 1
                    
                    elif (speed3_pos[0][0] <= pos[0] <= speed3_pos[1][0]) & (speed3_pos[0][1] <= pos[1] <= speed3_pos[1][1]):
                        note_speed = 2
                    
                    elif (difficulty1_pos[0][0] <= pos[0] <= difficulty1_pos[1][0]) & (difficulty1_pos[0][1] <= pos[1] <= difficulty1_pos[1][1]):
                        difficulty = 0
                        
                    elif (difficulty3_pos[0][0] <= pos[0] <= difficulty3_pos[1][0]) & (difficulty3_pos[0][1] <= pos[1] <= difficulty3_pos[1][1]):
                        difficulty = 1
                    
        pygame.display.update()
    sound.stop()
    return -1

def note_acc(curr_note, currunt, k_num):
    global perfect, good
    new_curr_note=[]
    isdone = False
    for note in curr_note:
        if (note[2] == k_num) and (note[0] - 0.2 < currunt < note[0] + 0.2) and not isdone:
            if (note[0] - 0.1 < currunt < note[0] + 0.1):
                perfect += 1
            else:
                good += 1
            isdone = True
        else:
            new_curr_note.append(note)
    return new_curr_note

def play():
    global perfect, good, miss, difficulty, music_select, note_speed
    perfect = 0
    good = 0 
    miss = 0
    pygame.init()
    pygame.display.set_caption("리듬게임")
    clock = pygame.time.Clock()
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [80, 0], [80,680], 3)
    pygame.draw.line(screen, BLACK, [160, 0], [160,680], 3)
    pygame.draw.line(screen, BLACK, [240, 0], [240,680], 3)
    pygame.draw.line(screen, BLACK, [320, 0], [320,680], 3)
    pygame.draw.line(screen, BLACK, [400, 0], [400,680], 3)
    pygame.draw.line(screen, BLACK, [0, 600], [480,600], 3)
    pygame.display.flip()
    speed = (note_speed + 1) * 5
    top_to_down = math.ceil((600 / (speed * 60)* 100) / 100)
    block_time = MUSIC_LIST[music_select][difficulty]
    note_cnt = 0
    curr_note = []
    running = True 
    note_x = [10, 90, 170, 250, 330, 410]
    length = len(block_time)
    end_time = block_time[-1] + 3 
    sound = pygame.mixer.Sound(MUSIC_ADD[music_select])
    sound.play(-1)
    start = time.time()
    
    while running:
        clock.tick_busy_loop(60)
        currunt = math.ceil((time.time() - start) * 100) / 100
        
        if note_cnt < length and currunt >= block_time[note_cnt] - top_to_down:
            curr_note.append([block_time[note_cnt], 20 ,random.randrange(0,6)])
            note_cnt += 1
            
        for j in range(6):
            pygame.draw.rect(screen, WHITE, [note_x[j]-10, 0, 70, 680])
        pygame.draw.line(screen, BLACK, [0, 600], [480,600], 3)
        
        new_curr_note=[]
        for j in curr_note:
            if j[1] >= 660:
                miss += 1
            else:
                new_curr_note.append([j[0],j[1] + speed ,j[2]])
                pygame.draw.rect(screen, BLUE, [note_x[j[2]], j[1], 60, 15])
        curr_note = new_curr_note
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    curr_note = note_acc(curr_note, currunt, 0)
                elif event.key == pygame.K_s:
                    curr_note = note_acc(curr_note, currunt, 1)
                elif event.key == pygame.K_d:
                    curr_note = note_acc(curr_note, currunt, 2)
                elif event.key == pygame.K_j:
                    curr_note = note_acc(curr_note, currunt, 3)
                elif event.key == pygame.K_k:
                    curr_note = note_acc(curr_note, currunt, 4)
                elif event.key == pygame.K_l:
                    curr_note = note_acc(curr_note, currunt, 5)
                    
            
        if end_time <= currunt:
            sound.stop()
            return 5
            
        pygame.display.update()
    sound.stop()
    return -1
            

def score():
    global perfect, good, miss
    pygame.init()
    pygame.display.set_caption("결과창")
    background_addr = BASE_ADD+"결과화면.png"
    background = pygame.image.load(background_addr)
    sound = pygame.mixer.Sound(MUSIC_ADD[music_select])
    sound.play(-1)
    screen.blit(background, (0, 0))
    total_score = perfect * 100 + good * 50
    
    font = pygame.font.SysFont("arial", 40, False, False) #글씨체, 크기조절
    text = font.render((str)(total_score), True, BLACK) #노래 선택 출력
    screen.blit(text,(120, 265)) #위치
    
    font = pygame.font.SysFont("arial", 20, False, False) #perfect
    text = font.render((str)(perfect), True, BLACK) 
    screen.blit(text,(167, 435)) #위치
    
    font = pygame.font.SysFont("arial", 20, False, False) #good
    text = font.render((str)(good), True, BLACK)
    screen.blit(text,(167, 483)) #위치
    
    font = pygame.font.SysFont("arial", 20, False, False) #miss
    text = font.render((str)(miss), True, BLACK)
    screen.blit(text,(167, 536)) #위치
    ReturnMain_pos = [(342, 21), (459, 36)]#메인화면 버튼 위치
    ReStart_pos = [(35, 615), (167, 639)]#다시 시작 버튼 위치
    Quit_pos = [(346, 615), (442, 639)]#끝내기 버튼 위치
    
    running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
    while running:
        for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
            if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    
                    if (ReturnMain_pos[0][0] <= pos[0] <= ReturnMain_pos[1][0]) & (ReturnMain_pos[0][1] <= pos[1] <= ReturnMain_pos[1][1]):
                        sound.stop()
                        return 1
                    
                    elif (ReStart_pos[0][0] <= pos[0] <= ReStart_pos[1][0]) & (ReStart_pos[0][1] <= pos[1] <= ReStart_pos[1][1]):
                        sound.stop()
                        return 4
                    
                    elif (Quit_pos[0][0] <= pos[0] <= Quit_pos[1][0]) & (Quit_pos[0][1] <= pos[1] <= Quit_pos[1][1]):
                        sound.stop()
                        return -1
                
        pygame.display.update()
    return -1

mode = 7
while (mode != -1):
    if mode == 0:
        mode = login()
    elif mode == 1:
        mode = main()   
    elif mode == 2:
        mode = music()
    elif mode == 3:
        mode = level()
    elif mode == 4:
        mode = play()
    elif mode == 5:
        mode = score()
    elif mode == 6:
        mode = regist()
    else:
        mode = login_regist()
        
pygame.quit()