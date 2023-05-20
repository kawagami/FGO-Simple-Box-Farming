import fgo
import pyautogui

class main(fgo.actions):

    # 在這改進戰鬥確認用的圖片
    in_battle_check_img = 'images/battle_CD_clothing.png'

    # 控制 要選什麼好友
    friend_1 = fgo.images.fox_ass_15
    friend_2 = fgo.images.fox_ass_15_2
    # friend_1 = 'images/fox_ass_15.png'
    # friend_2 = 'images/fox_ass_15_2.png'

    # 控制 call 哪個動作
    def start_battle(self):
        pyautogui.hotkey('ctrl', 'alt', '3')
        print("開始 特斯拉+殺狐")

