import fgo
import pyautogui

class main(fgo.actions):

    # 在這改進戰鬥確認用的圖片
    in_battle_check_img = 'images/battle_SWAP_clothing.png'

    # 控制 要選什麼好友
    friend_1 = 'images/friend_nero_fox_1.png'
    friend_2 = 'images/friend_nero_fox_1.png'

    # 控制 call 哪個動作
    def start_battle(self):
        pyautogui.hotkey('ctrl', 'alt', '6')
        # print("開始 尼祿祭妖蘭")

