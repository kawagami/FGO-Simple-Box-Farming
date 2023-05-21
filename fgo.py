import pyautogui
import time
import sys
import datetime

class images:
    # 禮拜 1 的種火
    monday_fire = 'images/monday_fire.png'

    # 禮拜 2 的種火
    tuesday = 'images/tuesday_fire.png'

    # 禮拜 日 的種火
    sunday_fire = 'images/sunday_fire.png'

    # 羈絆 15% 的術傻
    friend_caster_saber = 'images/friend_caster_saber.png'

    # 羈絆 15% 的靈三術傻
    friend_caster_saber_2 = 'images/friend_caster_saber_2.png'

    # QP 15% 的靈一術傻
    friend_caster_saber_money_1 = 'images/friend_caster_saber_money_1.png'

    # 在選好友選單
    in_friend = 'images/in_friend.png'

    # 連續出擊的按鈕
    continue_battle = 'images/continue_battle.png'

    # 選完好友的進場畫面
    mission_start = 'images/mission_start.png'

    # 進戰鬥後
    in_battle = 'images/in_battle.png'

    # 金蘋果
    gold_apple = 'images/gold_apple.png'

    # 金蘋果確定
    gold_apple_confirm = 'images/gold_apple_confirm.png'

    battle_CD_clothing = 'images/battle_CD_clothing.png'
    fox_ass_15 = 'images/fox_ass_15.png'
    fox_ass_15_2 = 'images/fox_ass_15_2.png'

class actions:

    continue_start = 0
    continue_end = 0

    total_battle_time = 0

    battle_count = 0
    apple_count = 0

    battile_limit = sys.maxsize

    # 客製部分
    in_battle_check_img = images.in_battle
    friend_1 = images.friend_caster_saber
    friend_2 = images.friend_caster_saber_2

    def loop(self, limit = sys.maxsize):
        action = actions

        action.battile_limit = limit

        while True:
            action.continue_start = datetime.datetime.now()

            action.must_click_center(images.continue_battle)
            time.sleep(0.5)

            if action.on_screen(images.gold_apple):
                action.waiting_for(images.gold_apple)
                action.click_center(images.gold_apple)
                action.waiting_for(images.gold_apple_confirm)
                action.click_center(images.gold_apple_confirm)

                action.apple_count += 1
                print(f"吃了 {action.apple_count} 次蘋果")
            else:
                action.waiting_for(images.in_friend)

            while True:
                # 要替換的地方 1
                if self.friend():
                    break
                time.sleep(0.5)

            # 要替換的地方 2
            self.in_battle_check()
            time.sleep(1)

            # 要替換的地方 3
            self.start_battle()

            action.waiting_for(images.continue_battle)
            # time.sleep(4)

            action.continue_end = datetime.datetime.now()

            result = action.continue_end - action.continue_start

            print(f"這輪花費時間 {result}")

            if action.total_battle_time == 0:
                action.total_battle_time = result
            else:
                action.total_battle_time += result

            print(f"總共花費時間 {action.total_battle_time}")

            action.battle_count += 1
            print(f"戰鬥了 {action.battle_count} 次")

            average = action.total_battle_time/action.battle_count
            print(f"平均一輪時間 {average}")

            if action.battle_count >= action.battile_limit:
                print(f"刷了指定的次數 : {action.battile_limit}")
                break

    # 點擊 input 的圖片的中心
    def must_click_center(image_path, second=1.0, input_confidence=0.999) -> bool:
        while True:
            target = pyautogui.locateOnScreen(image_path, second, confidence=input_confidence)
            if target:
                # 點擊 停止 紀錄的動作
                pyautogui.click(1501, 38)

                center = pyautogui.center(target)
                pyautogui.click(center)
                time.sleep(0.5)
                # print(f"點擊了 {image_path} 中心")

                # return True
            else:
                return True
                # time.sleep(0.5)
                # print(f"沒找到圖 {image_path}")

                # return False

    # 點擊 input 的圖片的中心
    def click_center(image_path, second=1.0, input_confidence=0.999) -> bool:
        target = pyautogui.locateOnScreen(image_path, second, confidence=input_confidence)
        if target:
            center = pyautogui.center(target)
            pyautogui.click(center)
            # print(f"點擊了 {image_path} 中心")

            return True
        else:
            # print(f"沒找到圖 {image_path}")

            return False

    def waiting_for(image_path):
        while True:
            if pyautogui.locateOnScreen(image_path):
                # print(f"發現 {image_path}")
                break
            else:
                # print(f"待機 1s {image_path}")
                time.sleep(1)

    def in_battle_check(self):
        while True:
            target = pyautogui.locateOnScreen(self.in_battle_check_img)
            if target:
                center = pyautogui.center(target)
                pyautogui.click(center)
                # print(f"發現 {self.in_battle_check_img}")
                break
            else:
                # print(f"待機 1s {self.in_battle_check_img}")
                time.sleep(1)

    # 控制要選甚麼禮裝的好友
    def friend(self) -> bool:
        if actions.click_center(self.friend_1, input_confidence=0.95):
            return True
        elif actions.click_center(self.friend_2, input_confidence=0.95):
            return True
        else:
            actions.drag_some_distance_from(1040, 778)
            time.sleep(0.5)
            return False

    # 啟動錄好的動作
    def start_battle(self):
        pyautogui.hotkey('ctrl', 'alt', '1')
        # print("開始 一般仇凜")

    def on_screen(image_path):
        if pyautogui.locateOnScreen(image_path):
            return True
        else:
            return False

    def get_position():
        pos = pyautogui.position()
        print(pos)

    # 模擬手機下滑的動作
    def drag_some_distance_from(x : int, y : int):
        # 從 input 的座標
        pyautogui.moveTo(x, y)
        
        # 花費 1s 往下拉
        pyautogui.dragRel(0, -400, 1)
        # print("拖曳一段距離")
