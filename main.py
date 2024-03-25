import random
import pygame
from animals import Cow, Bull



class Board:
    def __init__(self, k=4):
        self.k = k
        self.board = [0] * k
        self.board1 = [0] * k
        self.left = 10
        self.top = 10
        self.cell_width = 30
        self.cell_height = self.cell_width
        self.h_v = 0

    def set_view(self, left, top, cell_width, cell_height, h_v=0, k=4):
        self.left, self.top, self.cell_width, self.cell_height, self.h_v, self.k = \
            left, top, cell_width, cell_height, h_v, k

    def cell_field(self, screen, clr='white', rect_width=1):
        for row, row_v in enumerate(self.board):
            b_h, b_v = self.left + row * self.cell_width, self.top
            if self.h_v:
                b_h, b_v = self.left, self.top + row * self.cell_height
            pygame.draw.rect(screen, pygame.Color(clr),
                             (b_h, b_v,
                              self.cell_width,
                              self.cell_height),
                             rect_width)

    def is_click(self, click_point):
        if self.left < click_point[0] < self.left + self.cell_width and \
                self.top < click_point[1] < self.top + self.cell_height:
            return True
        return False

def checker(n1, n2):
    n = len(n1)
    k = 0
    for i in range(n):
        if n1[i] == n2[i]:
            k += 1
    return [k, len(set(n1).intersection(set(n2))) - k]

def random_number(n):
    return ''.join(map(str, random.sample(range(10), n)))

def choice_numbers(sp, n):
    t = random_number(n)
    nb = int('1' + t)
    for m in range(nb, nb + 10 ** n):
        if len(set(str(m)[1:])) == n:
            fl_tr = True
            for st in sp:
                if checker(str(m)[1:], st[:n]) != [int(st[-2]), int(st[-1])]:
                    fl_tr = False
                    break
            if fl_tr:
                return str(m)[1:]
    return 'mistake'

def fnk(sp, n):
    s = '0123456789'
    return s[:n]

def fnk2(s):
    return '21'

def game_field(screen):

    global rules_game, count_digits, play_with_program, start_game, selected_digits, all_digits, question_digits, \
        check_button, cells_for_II, riddle_number, k_bull_kow, check_bull_kow, ans, rules_text, pr, flag_rules, \
        game_status, mistake_text

    rules_game = Board(1)
    rules_game.set_view(25, 95, 200, 50, 0)
    rules_game.cell_field(screen, (237, 138, 116), 0)
    myfont = pygame.font.Font('font.ttf', 33)
    text_surface = myfont.render('ПРАВИЛА ИГРЫ', False, (150, 200, 250))
    screen.blit(text_surface, (25, 95))

    count_digits = Board(1)
    count_digits.set_view(275, 95, 200, 50, 0)
    count_digits.cell_field(screen, (237, 138, 116), 0)
    myfont = pygame.font.Font('font.ttf', 26)
    text_surface = myfont.render(f' количество цифр: {int(game_status[0])}', False, (150, 200, 250))
    screen.blit(text_surface, (275, 95))

    play_with_program = Board(1)
    play_with_program.set_view(525, 95, 200, 50, 0)
    play_with_program.cell_field(screen, (237, 138, 116), 0)
    myfont = pygame.font.Font('font.ttf', 24)
    st = 'Играть против ИИ: Нет'
    if int(game_status[1]):
        st = 'Играть против ИИ: Да'
    text_surface = myfont.render(st, False, (150, 200, 250))
    screen.blit(text_surface, (525, 95))

    start_game = Board(1)
    start_game.set_view(775, 95, 200, 50, 0)
    start_game.cell_field(screen, (237, 138, 116), 0)
    myfont = pygame.font.Font('font.ttf', 35)
    text_surface = myfont.render('  НАЧАТЬ ИГРУ', False, (150, 200, 250))
    screen.blit(text_surface, (775, 95))

    board = Board(1)
    board.set_view(25, 150, 200, 50, 0)
    clr = (160, 116, 237)
    if flag_rules and game_status[2] == '1' and game_status[3] in '01':
        clr = 'green'
    board.cell_field(screen, clr, 0)
    myfont = pygame.font.Font('font.ttf', 28)
    text_surface = myfont.render('   составьте число', False, (150, 200, 250))
    screen.blit(text_surface, (25, 150))

    check_button = Board(1)
    check_button.set_view(275, 150, 200, 50, 0)
    clr = (160, 116, 237)
    if flag_rules and game_status[2:4] == '12':
        clr = 'green'
    check_button.cell_field(screen, clr, 0)
    myfont = pygame.font.Font('font.ttf', 28)
    text_surface = myfont.render('       проверить', False, (150, 200, 250))
    screen.blit(text_surface, (275, 150))

    board = Board(1)
    board.set_view(525, 150, 200, 50, 0)
    clr = (160, 116, 237)
    if flag_rules and game_status[1] == '1' and game_status[3] in '34' and game_status[4] == '0':
        clr = 'green'
    board.cell_field(screen, clr, 0)
    myfont = pygame.font.Font('font.ttf', 28)
    text_surface = myfont.render('   загадайте число', False, (150, 200, 250))
    screen.blit(text_surface, (525, 150))

    riddle_number = Board(1)
    riddle_number.set_view(775, 150, 200, 50, 0)
    clr = (160, 116, 237)
    if flag_rules and game_status[1] == '1' and game_status[3] in '345'  and game_status[4] == '0':
        clr = 'green'
    riddle_number.cell_field(screen, clr, 0)
    myfont = pygame.font.Font('font.ttf', 28)
    text_surface = myfont.render('   число загадано', False, (150, 200, 250))
    screen.blit(text_surface, (775, 150))

    myfont = pygame.font.Font('Anta-Regular.ttf', 40)

    if flag_rules and game_status[2] == '1':
        question_digits = [-1] * int(game_status[0])
        for i in range(int(game_status[0])):
            question_digits[i] = Board(1)
            question_digits[i].set_view(25 + i * 50, 200, 50, 50, 0)
            question_digits[i].cell_field(screen)


        for i in range(int(game_status[0])):
            if pos_occupied[i] == -1:
                continue
            text_surface = myfont.render(str(pos_occupied[i]), False, (250, 250, 250))
            screen.blit(text_surface, (38 + i * 50, 200))

    all_digits = [0] * 10
    for i in range(10):
        all_digits[i] = Board(1)
        all_digits[i].set_view(475, 200 + i * 50, 50, 50, 1)
        all_digits[i].cell_field(screen)


    for i in range(10):
        if i in selected_digits:
            continue
        text_surface = myfont.render(str(i), False, ((i * 50) % 250, (150 - i * 25) % 250, (250 - i * 100) % 250))
        screen.blit(text_surface, (485, 200 + i * 50))

    dist_top = 200
    if game_status[3] in '012':
        dist_top = 250
    for sp in sp_check:
        n = int(game_status[0])
        board = Board(n)
        board.set_view(25, dist_top, 50, 50, 0)
        board.cell_field(screen, (250, 250, 250), 1)
        board = Board(1)
        board.set_view(25 + n * 50, dist_top, 50, 50, 0)
        board.cell_field(screen, 'red', 0)
        board = Board(1)
        board.set_view(75 + n * 50, dist_top, 50, 50, 0)
        board.cell_field(screen, 'blue', 0)

        for i in range(n + 2):
            text_surface = myfont.render(str(sp[i]), False, (250, 250, 250))
            screen.blit(text_surface, (38 + i * 50,  dist_top))
        dist_top += 50

    if flag_rules and game_status[1:3] == '11' and game_status[4] in '123':
        k_bull_kow = [0, 0]
        n = int(game_status[0])
        board = Board(n)
        board.set_view(525, 200, 50, 50, 0)
        board.cell_field(screen, (250, 250, 250), 1)
        k_bull_kow[0] = Board(1)
        k_bull_kow[0].set_view(525 + n * 50, 200, 50, 50, 0)
        k_bull_kow[0].cell_field(screen, 'red', 0)
        k_bull_kow[1] = Board(1)
        k_bull_kow[1].set_view(575 + n * 50, 200, 50, 50, 0)
        k_bull_kow[1].cell_field(screen, 'blue', 0)
        if game_status[3] == '3' and game_status[4] in '1':
            ans = choice_numbers(sp_II ,int(game_status[0]))
            if ans == 'mistake':
                game_status = game_status[:3] + '88'
                flag_rules = 0
            game_status = game_status[:4] + '2'
        for i in range(n):
            text_surface = myfont.render(ans[i], False, (250, 250, 250))
            screen.blit(text_surface, (538 + i * 50, 200))
        for i in range(2):
            if digits_bull_kow[i] == -1:
                continue
            text_surface = myfont.render(str(digits_bull_kow[i]), False, (250, 250, 250))
            screen.blit(text_surface, (538 + (n + i) * 50, 200))

    dist_top = 200
    if game_status[3] in '34':
        dist_top = 250
    for sp in sp_II:
        n = int(game_status[0])
        board = Board(n)
        board.set_view(525, dist_top, 50, 50, 0)
        board.cell_field(screen, (250, 250, 250), 1)
        board = Board(1)
        board.set_view(525 + n * 50, dist_top, 50, 50, 0)
        board.cell_field(screen, 'red', 0)
        board = Board(1)
        board.set_view(575 + n * 50, dist_top, 50, 50, 0)
        board.cell_field(screen, 'blue', 0)

        for i in range(n + 2):
            text_surface = myfont.render(str(sp[i]), False, (250, 250, 250))
            screen.blit(text_surface, (538 + i * 50, dist_top))
        dist_top += 50

    if flag_rules and game_status[1:3] == '11' and game_status[4] in '123':
        check_bull_kow = Board(1)
        check_bull_kow.set_view(525, 150, 450, 50, 0)
        clr = (160, 116, 237)
        if game_status and game_status[3] in '34':
            clr = 'green'
        check_bull_kow.cell_field(screen, clr, 0)
        myfont = pygame.font.Font('font.ttf', 28)
        text_surface = myfont.render('   вставьте количество быков и коров', False, (150, 200, 250))
        screen.blit(text_surface, (525, 150))

    rules_text = Board(1)
    if flag_rules == 0 and ans != 'mistake':
        rules_text = Board(1)
        rules_text.set_view(130, 120, 650, 450, 0)
        rules_text.cell_field(screen, (250, 250, 200), 0)
        myfont = pygame.font.Font('font.ttf', 25)
        # with open('data.csv', 'r') as spc:
        #     sg = spc.readline().strip().split(',')
        k = 0
        with open('rul_text.txt', encoding='utf-8') as file:
            text_inf = file.readline().strip()
            while text_inf:
                text_surface = myfont.render(text_inf, False, (60, 69, 166))
                screen.blit(text_surface, (140, 130 + k * 30))
                text_inf = file.readline().strip()
                k += 1
    mistake_text = Board(1)
    if ans == 'mistake':
        mistake_text = Board(1)
        mistake_text.set_view(200, 40, 650, 105, 0)
        mistake_text.cell_field(screen, (250, 250, 200), 0)
        myfont = pygame.font.Font('font.ttf', 25)
        k = 0
        with open('mistake.txt', encoding='utf-8') as file:
            text_inf = file.readline().strip()
            while text_inf:
                text_surface = myfont.render(text_inf, False, (60, 69, 166))
                screen.blit(text_surface, (210, 45 + k * 30))
                text_inf = file.readline().strip()
                k += 1

def processing_click(click_position):
    global game_status, selected_digits, pos_occupied, sp_check, digits_for_II, sp_II, digits_bull_kow, ans, str_ans, \
        flag_rules, number_for_guess, cow

    if rules_game.is_click(click_position):
        flag_rules = 0
        print(game_status)

    if ans != 'mistake' and flag_rules == 0:
        if rules_text.is_click(click_position):
            flag_rules = 1

    if ans == 'mistake' :
        if mistake_text.is_click(click_position):
            flag_rules = 1
            ans = 'a' * int(game_status[0])
            game_status = game_status[:3] + '88'

    if flag_rules and count_digits.is_click(click_position):
        game_status = game_status[:2] + '0' + game_status[3:]
        k = 2 + (int(game_status[0]) - 1) % 6
        game_status = str(k) + game_status[1:]
        selected_digits = []
        sp_check = []
        sp_II = []

    if flag_rules and play_with_program.is_click(click_position):
        game_status = game_status[:2] + '0' + game_status[3:]
        k = (int(game_status[1]) + 1) % 2
        game_status = game_status[0] + str(k) + game_status[2:]
        selected_digits = []
        sp_check = []
        sp_II = []

    if flag_rules and start_game.is_click(click_position):
        game_status = game_status[:2] + '100'
        selected_digits = []
        sp_check = []
        sp_II = []
        pos_occupied = [-1] * int(game_status[0])
        digits_for_II = [-1] * int(game_status[0])
        digits_bull_kow = [-1, -1]
        number_for_guess = random_number(int(game_status[0]))
        cow.is_press = True
        bull.is_press = True

    if flag_rules and ((game_status[2:4] == '10' or game_status[1:4] == '113') and game_status[3:5] != '33'):
        for i in range(10):
            if i in selected_digits:
                continue
            if all_digits[i].is_click(click_position):
                selected_digits += [i]
                game_status = game_status[:3] + str(int(game_status[3]) + 1) + game_status[4] + str(i)

    if flag_rules and game_status[2] == '1' and game_status[3] == '1':
        for i in range(int(game_status[0])):
            if pos_occupied[i] != -1:
                continue
            if question_digits[i].is_click(click_position):
                pos_occupied[i] = int(game_status[5])
                if pos_occupied.count(-1):
                    game_status = game_status[:3] + '0' + game_status[4:]
                else:
                    game_status = game_status[:3] + '2' + game_status[4:]

    if flag_rules and game_status[1:5] == '1142':
        for i in range(2):
            if digits_bull_kow[i] != -1:
                continue
            if k_bull_kow[i].is_click(click_position):
                digits_bull_kow[i] = int(game_status[5])
                selected_digits = []
                if digits_bull_kow.count(-1):
                    game_status = game_status[:3] + '32'
                else:
                    game_status = game_status[:3] + '33'
                    str_ans = ans + str(digits_bull_kow[0]) + str(digits_bull_kow[1])


    if flag_rules and game_status[2:4] == '12':
        if check_button.is_click(click_position):
            pos_occupied += checker(''.join(map(str, pos_occupied)), number_for_guess)
            selected_digits = []
            sp_check = [pos_occupied] + sp_check
            if pos_occupied[-2] == int(game_status[0]):
                game_status = game_status[:3] + '88'
                bull.is_press = True
            elif game_status[1] == '1' and game_status[4] == '0':
                game_status = game_status[:3] + '3' + game_status[4:]
            elif game_status[1] == '1' and game_status[4] == '1':
                game_status = game_status[:3] + '3' + game_status[4:]
            else:
                game_status = game_status[:3] + '0' + game_status[4:]
            pos_occupied = [-1] * int(game_status[0])

    if flag_rules and game_status[1:3] == '11' and game_status[3] in '345' and game_status[4] == '0':
        if riddle_number.is_click(click_position):
            game_status = game_status[:4] + '1'
            selected_digits = []

    if game_status[3:5] == '67':
        selected_digits = []

    if flag_rules and game_status[1:5] == '1133':
        if check_bull_kow.is_click(click_position):
            game_status = game_status[:3] + '01'
            if str_ans[-2] == game_status[0]:
                game_status = game_status[:4] + '7'
                cow.is_press = True
            sp_II = [str_ans] + sp_II
            digits_bull_kow = [-1, -1]

def actions():
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('bull and cow')
    global cow, bull

    myfont = pygame.font.Font('Anta-Regular.ttf', 40)
    text_surface = myfont.render('Bull and Cow', False, 'Green')

    cow = Cow(WINDOW_WIDTH=width)
    bull = Bull(WINDOW_WIDTH=width)

    running = True
    while running:
        screen.fill(pygame.Color('#74cbed'))
        screen.blit(text_surface, (380, 35))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                processing_click(event.pos)

        game_field(screen)
        cow.update(window=screen)
        bull.update(window=screen)
        pygame.display.update()


pygame.init()
game_status = '40000'
selected_digits = []
pos_occupied = []
sp_check = []
sp_II = []
flag_rules = 1
ans = ''
actions()
pygame.quit()

