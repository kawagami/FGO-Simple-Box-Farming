import fgo
import pyautogui
import time

class main(fgo.actions):

    # 在這改進戰鬥確認用的圖片
    in_battle_check_img = 'images/in_battle.png'

    # 控制 要選什麼好友
    friend_1 = 'images/friend_caster_saber_2.png'
    friend_2 = 'images/friend_caster_saber.png'
    friend_3 = 'images/friend_caster_saber_money_1.png'

    # 控制要選甚麼禮裝的好友
    def friend(self) -> bool:
        if fgo.actions.click_center(self.friend_3, input_confidence=0.95):
            return True
        elif fgo.actions.click_center(self.friend_2, input_confidence=0.95):
            return True
        elif fgo.actions.click_center(self.friend_1, input_confidence=0.95):
            return True
        else:
            # print(f"no {self.friend_1} & {self.friend_2}")
            fgo.actions.drag_some_distance_from(1040, 778)
            time.sleep(0.5)
            return False

    # 控制 call 哪個動作
    def start_battle(self):
        pyautogui.hotkey('ctrl', 'alt', '2')
        print("開始 QP 極 小文西")

