# 簡易刷箱功能

## 環境需求
* python 3.11.3+
* pyautogui
* 無容器化，本機執行
* bluestack 或是 nox 有紀錄動作的模擬器

## 使用說明
* 此功能是使用 pyautogui 監控螢幕畫面來判斷情況後**搭配模擬器的動作紀錄**執行
* 第一次需要先擷取好以下狀況的圖片，以應對不同環境不同解析度的狀況
    * 在選好友選單
        * in_friend = 'images/in_friend.png'
    * 連續出擊的按鈕
        * continue_battle = 'images/continue_battle.png'
    * 選完好友的進場畫面
        * mission_start = 'images/mission_start.png'
    * 進戰鬥後
        * in_battle = 'images/in_battle.png'
    * 金蘋果
        * gold_apple = 'images/gold_apple.png'
    * 金蘋果確定
        * gold_apple_confirm = 'images/gold_apple_confirm.png'
* **需要一個確保通關的動作紀錄**
    * 因為暴擊打法有不確定性，所以此功能中不考慮
    * 使用模擬器的動作紀錄，記錄下固定3T的技能施放 & 過場延遲，以確保 loop 能正確執行
    * 將此紀錄的動作設定快捷鍵
* 如果在該環境下直接擷取的圖片還是感應不到的話可去 code 中調整圖片判斷所需的準確度
* 對應不同場景的戰鬥需要設定以下內容
    * 複製 saber.py 檔案 rename 成任意你能理解的名稱，修改其中以下內容
        * in_battle_check_img
            * 用來判斷是否進入戰鬥畫面，並出現你所選定的戰鬥服
        * friend_1
            * 要選擇使用的好友
        * friend_2
            * 要選擇使用的好友，對應不同的靈基畫面
        * start_battle
            * 在這修改呼叫**動作紀錄**的快捷鍵
    * 以上都修改完後，在 main.py 加入你所新增的內容 XXX
        * import XXX
        * 在 main 中實例化 XXX.main() 後使用 obj.loop() 方法，即可自動刷箱子
        * 此功能不是背景執行，需要螢幕最上方是相對應的內容
        * 可關閉螢幕執行