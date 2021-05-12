# exam2

在mqtt的source和gesture_UI的source中可能有些名詞有重複定義到所以要再建立一個新的mbed-os-build2來compile這次的考試

跟著以下步驟執行

mkdir -p ~/ee2405new

cp -r ~/ee2405/mbed-os ~/ee2405new

cd ~/ee2405new

mbed compile --library --no-archive -t GCC_ARM -m B_L4S5I_IOT01A --build ~/ee2405new/mbed-os-build2

然後用 sudo mbed compile --source . --source ~/ee2405new/mbed-os-build2/ -m B_L4S5I_IOT01A -t GCC_ARM --profile tflite.json -ff 去compile hw3

接著就可以開始執行main.cpp了 如果有改變網路IP記得要重設

首先開啟兩個terminal一個執行sudo screen /dev/ttyACM0 另一個執行sudo python3 wifi_mqtt/mqtt_client.py

然後因為我是拿hw3的程式碼來改的，多了考試不需要的tilt_mode那塊，所以那塊不用看

首先在screen內輸入/UI_mode/run進入手勢加速度儲存模式，接著在揮手的同時按下user_button

會在螢幕上顯示出當前的加速度值和判斷出可能是什麼手勢還有ulcd也會顯示出TF所判斷出來手勢的結果
(如下圖)

![60551](https://user-images.githubusercontent.com/76942544/117967954-3acdec80-b358-11eb-8f44-cf2d8382a23c.jpg)

![Screenshot from 2021-05-12 04-26-32](https://user-images.githubusercontent.com/76942544/117967766-06f2c700-b358-11eb-9a8d-1667e0fd321c.png)

接下來按下enter後剛剛所記下來的加速度就會開始藉由MQTT傳給PC/Python
(如下圖)

![Screenshot from 2021-05-12 04-29-58](https://user-images.githubusercontent.com/76942544/117968387-b5970780-b358-11eb-9f89-46a957ec92a8.png)

傳送結束之後會回到RPC指令模式
接著等到PC/Python端接收到指令後會開始傳送手勢的特徵值
(如下圖)
0代表判斷手勢為circle
1代表判斷手勢為slope
2代表判斷手勢為nike
![Screenshot from 2021-05-12 04-39-38](https://user-images.githubusercontent.com/76942544/117969310-d449ce00-b359-11eb-8e07-80c951be0813.png)

考試的最後一小題是要藉由特徵值作圖，但我在這出了bug弄不出來QQ



