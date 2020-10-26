# הדפסה של הטבלה
def print_list(list):
    mone=1
    for x in range(1,4):
        for y in range(1,4):
            print(list[mone],end=' ')
            mone=mone+1
        print()


# בדיקה האם התא המבוקש פנוי
def check_if_cell_is_empty(list,place):
    print(list[int(place)])
    if list[int(place)] >= '1' and list[int(place)] <= '9':
        return True

# בדיקה האם יש נצחון
def check_win(list):
    if list[0]==list[1]==list[2] or list[3]==list[4]==list[5] or list[6]==list[7]==list[8] or list[0]==list[4]==list[8] or list[2]==list[4]==list[6] or list[0]==list[3]==list[6] or list[1]==list[4]==list[7] or list[2]==list[5]==list[8]:
        return True

# בדיקה האפ קיימים תאים פנויים
def check_if_can_cuntinue(list):
    for x in range(1,10):
        if list[x]==str(x):
            return True

# בדיקת בחירת משתמש והאם התא פנוי
def check_entry(list,opt):
    if opt=='E':
        return opt,True
    elif opt >='1' and opt <='9':
        if check_if_cell_is_empty(list,opt)==True:
            return opt,True
        else:
            return opt, False
    else:
        return opt,False



# תחילת תוכנית
play_num=1 # מי השחקן הפעיל
list = ['0','1','2','3','4','5','6','7','8','9']
print_list(list)

# בחירת X/O
while 1==1:
    player1 = str(input('player1: choose if you are X or O\n'))
    if player1.upper()=='O' or player1.upper()=='X':
        if player1.upper()=='X':
            player2 = 'O'
            break
        else:
            player2 = 'X'
            break


# המשחק מתחיל
while 1==1:

    # בדיקת בחירת משתמש
    while 1==1:
        if play_num==1:
            opt=str(input('player1 please choose cell, or choose E for exit\n'))
        else:
            opt = str(input('player2 please choose cell, or choose E for exit\n'))

        opt,flag =  check_entry(list,opt)
        if flag == True:
            break



    if opt == 'E':
        print('you choose to end the game')
        break

    if play_num == 1:
        list[int(opt)]=player1
    else:
        list[int(opt)]=player2


    if check_win(list)==True:
        if play_num==1:
            print(player1,'you win')
            print_list(list)
            break
        else:
            print(player2,'you win')
            print_list(list)
            break

    if check_if_can_cuntinue(list)==False:
        print('end game')
        break

    print_list(list)
    if play_num==1:
        play_num=2
    else:
        play_num=1