import random

# הדפסה של הטבלה
def print_list(list):
    mone = 1
    for x in range(1, 4):
        for y in range(1, 4):
            print(list[mone], end=' ')
            mone = mone + 1
        print()

# בדיקה האם התא המבוקש פנוי
def check_if_cell_is_empty(list, opt):
    # בדיקה האם הערך בתא הוא בין 1-9
    if list[int(opt)] >= '1' and list[int(opt)] <= '9':
        return True
    else:
        return False

# בדיקה האם יש נצחון
def check_win(list):
    if list[1] == list[2] == list[3]  \
     or list[4] == list[5] == list[6] \
     or list[7] == list[8] == list[9]  \
     or list[1] == list[5] == list[9]  \
     or list[3] == list[5] == list[7]  \
     or list[1] == list[4] == list[7]  \
     or list[2] == list[5] == list[8]  \
     or list[3] == list[6] == list[9] :
        return True


# בדיקה האפ קיימים תאים פנויים
def check_if_can_cuntinue(list):
    for x in range(1, 10):
        if list[x] == str(x):
            return True






# בדיקת בחירת משתמש והאם התא פנוי
def check_entry(list, opt):
    if opt.upper() == 'E':
        return opt, True
    if opt >= "1" and opt <= "9" and len(opt) == 1:
        if check_if_cell_is_empty(list, opt) == True:
            return opt, True
        else:
            return opt, False
    else:
        return opt, False

#בודקת האם יש צמדים
def check_place_computer(list ,place_computer):
    if list[1] == list[2] and check_if_cell_is_empty(list,'3')==True:
        place_computer = '3'
        return place_computer
    if list[1] == list[3] and check_if_cell_is_empty(list,'2')==True:
        place_computer = '2'
        return place_computer
    if list[2] == list[3] and check_if_cell_is_empty(list,'1')==True:
        place_computer = '1'
        return place_computer
    if list[5] == list[6] and check_if_cell_is_empty(list,'4')==True:
        place_computer = '4'
        return place_computer
    if list[4] == list[5] and check_if_cell_is_empty(list,'6')==True:
        place_computer = '6'
        return place_computer
    if list[4] == list[6] and check_if_cell_is_empty(list,'5')==True:
        place_computer = '5'
        return place_computer
    if list[7] == list[8] and check_if_cell_is_empty(list,'9')==True:
        place_computer = '9'
        return place_computer
    if list[9] == list[8] and check_if_cell_is_empty(list,'7')==True:
        place_computer = '7'
        return place_computer
    if list[7] == list[9] and check_if_cell_is_empty(list,'8')==True:
        place_computer = '8'
        return place_computer
    if list[3] == list[6] and check_if_cell_is_empty(list,'9')==True:
        place_computer = '9'
        return place_computer
    if list[6] == list[9] and check_if_cell_is_empty(list,'3')==True:
        place_computer = '3'
        return place_computer
    if list[3] == list[9] and check_if_cell_is_empty(list,'6')==True:
        place_computer = '6'
        return place_computer
    if list[2] == list[5] and check_if_cell_is_empty(list,'8')==True:
        place_computer = '8'
        return place_computer
    if list[5] == list[8] and check_if_cell_is_empty(list,'2')==True:
        place_computer = '2'
        return place_computer
    if list[2] == list[8] and check_if_cell_is_empty(list,'5')==True:
        place_computer = '5'
        return place_computer
    if list[4] == list[1] and check_if_cell_is_empty(list,'7')==True:
        place_computer = '7'
        return place_computer
    if list[7] == list[4] and check_if_cell_is_empty(list,'1')==True:
        place_computer = '1'
        return place_computer
    if list[1] == list[7] and check_if_cell_is_empty(list,'4')==True:
        place_computer = '4'
        return place_computer
    if list[3] == list[5] and check_if_cell_is_empty(list,'7')==True:
        place_computer = '7'
        return place_computer
    if list[5] == list[7] and check_if_cell_is_empty(list,'3')==True:
        place_computer = '3'
        return place_computer
    if list[3] == list[7] and check_if_cell_is_empty(list,'5')==True:
        place_computer = '5'
        return place_computer
    if list[1] == list[5] and check_if_cell_is_empty(list,'9')==True:
        place_computer = '9'
        return place_computer
    if list[5] == list[9] and check_if_cell_is_empty(list,'1')==True:
        place_computer = '1'
        return place_computer
    if list[1] == list[9] and check_if_cell_is_empty(list,'5')==True:
        place_computer = '5'
        return place_computer
    else:
        place_computer = '0'
        return place_computer

# בחירה רנדומלית של המחשב
def random_place(list,place_computer):
    while 1 == 1:
        place_computer=random.randint(1, 9)
        if check_if_cell_is_empty(list, place_computer) == True:
            return place_computer, True



# =================================================================
# תחילת תוכנית
# =================================================================
play_num = 1  # מי השחקן הפעיל
list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print_list(list)

while 1==1:
    computr_1= str(input('please choose 1=player vs computer, 2=player vs player , E = exit'))
    if computr_1 == '1' or computr_1 == '2' or computr_1.upper() == 'E':
        break

if computr_1.upper() == 'E':
    exit()

#בחירת X או O
while 1 == 1:
    player1 = str(input('player1: choose if you are X or O\n'))
    if player1.upper()=='O' or player1.upper() == 'X':
        if player1.upper() == 'X':
            player2 = 'O'
            break
        else:
            player2 = 'X'
            break

print('we start')
print_list(list)
while 1 == 1:
    if computr_1.upper() == 'E':
        break
    place_computer = '0'
    # בדיקת בחירת משתמש
    while 1 == 1:
        if play_num == 1:
            opt = str(input('player1 please choose cell, or choose E for exit\n'))
        if int(computr_1) == 2 and play_num == 2:  # player vs player
            opt = str(input('player2 please choose cell, or choose E for exit\n'))
        opt,flag = check_entry(list,opt)
        if flag == True:
            break
        if int(computr_1) == 1 and play_num == 2:
            break


    if opt.upper() == 'E':
        break


    if play_num==1:
        list[int(opt)]=player1


    if int(computr_1) == 1 and play_num ==2:
        place_computer = check_place_computer(list, place_computer)


    while 1 == 1:
        if int(place_computer) == 0 and int(computr_1) == 1 and play_num == 2:
            place_computer,m = random_place(list,place_computer)
            if m==True:
                break
        else:
            break




    if int(computr_1) == 1 and play_num == 2:
        list[int(place_computer)]=player2

    if play_num==2 and int(computr_1) == 2:
        list[int(opt)]=player2


    if check_win(list)==True:
        if play_num==1 and check_win(list)==True:
            print("you win player 1")
            print_list(list)
            break
        if play_num==2 and int(computr_1)==1 and check_win(list)==True:
            print("the computer win")
            print_list(list)
            break
        if play_num==2 and int(computr_1)==2 and check_win(list) ==True:
            print("you win player 2")
            print_list(list)
            break

    if check_if_can_cuntinue(list) != True:
        print('end game')
        break

    if play_num == 1:
        print_list(list)
        print('player turn')
    if play_num ==2 and computr_1 == '1':
        print_list(list)
        print('computer turn')
    if play_num == 2 and computr_1 == '2':
        print_list(list)
        print('player 2 turn')



    if play_num == 1:
        play_num = 2
    else:
        play_num = 1