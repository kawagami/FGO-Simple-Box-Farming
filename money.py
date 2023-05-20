import fgo
import pyautogui

class main(fgo.actions):

    # 在這改進戰鬥確認用的圖片
    in_battle_check_img = 'images/in_battle.png'

    # 控制 要選什麼好友
    friend_1 = 'images/friend_caster_saber_2.png'
    friend_2 = 'images/friend_caster_saber.png'

    # 控制 call 哪個動作
    def start_battle(self):
        pyautogui.hotkey('ctrl', 'alt', '2')
        print("開始 QP 極 小文西")

