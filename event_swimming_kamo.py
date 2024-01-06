import fgo
import pyautogui

class main(fgo.actions):

    # 不使用預設的戰鬥服
    in_battle_check_img = 'images/battle_aloha_v2_clothing.png'

    # 控制 要選什麼好友
    friend_1 = 'images/event_caster_saber_1.png'
    friend_2 = 'images/event_caster_saber_2.png'

    # 控制 call 哪個動作
    def start_battle(self):
        pyautogui.hotkey('ctrl', 'alt', '8')
        # print("開始 泳裝活動泳迦摩")

