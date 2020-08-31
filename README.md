# TWCC FAQ

[TOC]

## 帳號相關

## 運算服務

### 虛擬運算 

:::spoiler Q1. 虛擬運算的浮動IP範圍為何？
:::info

- 203.145.217.0/24
- 203.145.218.0/24
- 203.145.220.0/22
- 203.145.219.0/24
- 103.124.73.0/24
- 103.124.74.0/24
- 103.124.75.0/24

:::

:::spoiler Q2. 如何使虛擬運算個體進行自動快照？
:::info

使用corntab的方式設定定時的時間，對虛擬運算個體執行快照的功能。

:::

:::spoiler Q3. 如何將虛擬運算中資料定期備份至雲端物件儲存
:::info

使用corntab指令碼設定時間、備份資料路徑和雲端物件儲存的目標儲存體，即可完成虛擬運算中資料定時備份。

:::

:::spoiler Q4. 虛擬運算服務是否支援SMTP？
:::info

如果您是想要使用TWCC提供的虛擬運算服務作為SMTP的伺服器，是可以允許SMTP發送信件

:::

:::spoiler Q5. 虛擬運算服務個體是否可直接掛載COS?
:::info

可以直接掛載 COS，您擁有虛擬運算個體的管理者權限，可以對個體進行任意操作，掛載 COS 建議使用 s3fs 之類的套件，可參考：https://github.com/s3fs-fuse/s3fs-fuse

:::

:::spoiler Q6. 請問我要如何知道我們開的虛擬運算服務個體網路流量狀態?
:::info

使用者介面上有簡易呈現監控CPU、硬碟、記憶體、網路的狀態及流量，若需要更詳細的資訊可以自行安裝程式監控

:::
:::spoiler Q7. 請問我虛擬運算建立後為何無法連線網路?
:::info
* 請檢查虛擬網路設定是否有誤
* 如果有啟用虛擬網路防火牆，規則不知道怎麼設定的話建議請先把防火牆關閉

:::

:::spoiler Q8. 如果把超過100GB的映像檔輸入虛擬運算服務個體，會有什麼影響?
:::info
* 系統碟的大小為100GB，使用超過100GB會使整台虛擬運算個體無法開啟，不會額外收費

:::





### 容器

:::spoiler Q1. 容器的浮動IP及Port範圍為何？
:::info

* IP:
203.145.219.128/25 (包含203.145.219.128)

* Port:
50000-60000
:::

:::spoiler Q2. 如何從容器轉移至HPC進行訓練運算？
:::info

* 可參考網路上Horovod和Singularity的使用說明文件
* 參考網址中的tutorial進行  
https://www.twcc.ai/doc?page=howto_hpc3  
https://www.twcc.ai/doc?page=howto_hpc4

:::

:::spoiler Q3. 如何使用超過一個容器8張卡以上的資源？
:::info

* 請改為使用HPC，使用方法可參考網路上Horovod和Singularity的使用說明文件
* 或參考網址中的tutorial進行  
https://www.twcc.ai/doc?page=howto_hpc3  
https://www.twcc.ai/doc?page=howto_hpc4

:::

:::spoiler Q4. ssh連線容器時顯示Permission denied如何處理？
:::info

* 可能是主機密碼輸入錯誤，請重新輸入或到下列網址重設主機密碼  
https://iservice.nchc.org.tw/module_page.php?module=nchc_service#nchc_service/nchc_service.php?action=nchc_unix_account_edit

:::

:::spoiler Q5. 執行程式時發現I/O緩慢如何處理？
:::info

* 如果dataset是許多小檔案，且dataset佔很大空間，應將小檔案集合成大檔案減少I/O壓力
* 製作複本，再以複本開一個新的容器，看系統能否安排到較不忙的節點
* 將dataset放到/tmp

:::

:::spoiler Q6. 執行程式時，效能不如預期如何處理？
:::info

* 如在Pytorch環境下，可用NUMA control來鎖定CPU core
* 檢查套件相容性，使用以下文件進行套件管理  
https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh
* 將dataset放到/tmp

:::

:::spoiler Q7. 程式執行時顯示insufficient shared memory如何處理？
:::info

* 在PyTorch環境下，將Dataloader的num workers設置為0
* 重新建立一個容器，選擇有share memory的設定

:::

:::spoiler Q8. 程式執行時顯示bus error如何處理？
:::info

* 檢查套件相容性，使用以下文件進行套件管理  
https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh
* 重新建立一個容器，選擇舊一點的映像檔版本

:::

:::spoiler Q9. 容器能建立幾次複本？
:::info

* 目前系統只容許一個容器建立一次複本

:::

:::spoiler Q10. 如何建立第二次複本？
:::info

* 用複本建立一個新容器，進行修改後再建立複本

:::

:::spoiler Q11. 如何暫停容器？
:::info

* 目前系統不支援容器暫停的功能

:::


### 台灣杉二號 (命令列介面)
:::spoiler Q1. 是否可以在台灣衫2號上面安裝Rclone軟體同步工具?
:::info
* 台灣杉二號有安裝最新版的Rclone，可以使用  "module  load  rclone" 來獲取  rclone  使用環境。而  rclone  是使用  go  語言撰寫，解壓縮在家目錄即可直接使用。
:::
## 網路與安全
### 虛擬網路
:::spoiler Q1. 我在建虛擬運算服務的時候要選填虛擬網路才能建立，但是我無法去建立虛擬網路?
:::info

* 建立虛擬網路必須為租戶管理者身分，而成為租戶管理者身分需找計畫建立者或是已是管理者身分的人來提高自身權限。
* 建立虛擬網路的文件如下:
https://www.twcc.ai/doc?page=virtual_network

:::

## 儲存服務
### HFS儲存服務
:::spoiler Q1. HFS空間已滿，將部分資料刪除，發現容量還是一樣沒變化
:::info

* 如需詳細了解資料夾中資訊，可以在命令列中下指令”du –sh 資料夾”，方可了解是那些檔案佔據了空間

* 計算過程產生的暫存檔會存放在下列兩個隱藏目錄，可以下指令”ls -la”查看，也有可能是造成您空間滿的原因

    /home/主機帳號/.cache/
    
    /home/主機帳號/.local/
:::

:::spoiler Q2. 我使用 SFTP 的方式連入 xdata1.twcc.ai 資料傳輸節點，為何無法登入?
:::info

* 請先確認您登入憑證使用的是 SSH 私密金鑰，而非您的主機密碼。若確認登入憑證無誤但登入仍有問題，請洽詢客服人員。
:::


### 區塊儲存
:::spoiler Q1. 為何之前保留的 SSD 無法成功掛載到新的虛擬運算服務個體上？
:::info

掛載 SSD 至虛擬運算服務個體，建議先確認其狀態為 `AVAILABLE`，才可以對新的虛擬運算服務個體進行掛載，如非此狀態請先將 SSD 與原本的個體分離，或是將原先的個體刪除，確認狀態為 `AVAILABLE`後，再進行掛載。若上述情況確認後，仍無法掛載，請洽技術支援服務。

:::

## TWCC-CLI

### 部屬環境

:::spoiler Q1. 請問 TWCC-CLI 怎麼安裝?
:::info

* 請參考 [TWCC-CLI v0.5](https://github.com/TW-NCHC/TWCC-CLI/tree/v0.5) 操作文件進行安裝及使用，謝謝!
:::

