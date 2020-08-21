# TWCC FAQ

[TOC]

## 帳號相關

## 運算服務

### 虛擬運算 

:::spoiler Q1. 虛擬運算的浮動IP範圍？
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

:::spoiler Q4. 請問要如何開啟虛擬網路?？
:::info

目前建立虛擬網路的權限，只給管理員與計畫建立者才擁有的，如需建立虛擬網路，請計劃管理員幫忙建立，或是提升您的權限為計劃管理員
建立虛擬網路的文件如下:
https://www.twcc.ai/doc?page=virtual_network

:::

:::spoiler Q5. 虛擬運算服務是否支援SMTP？
:::info

如果您是想要使用TWCC提供的虛擬運算服務作為SMTP的伺服器，是可以允許SMTP發送信件

:::

:::spoiler Q6. 虛擬運算服務個體是否可直接掛S3?
:::info

可以直接掛S3，您在VM擁有管理者權限，可以對VM進行任意操作，掛載S3建議使用s3fs之類的套件，可參考https://github.com/s3fs-fuse/s3fs-fuse

:::

:::spoiler Q7. 請問我要如何知道我們開的虛擬運算服務個體網路流量狀態?
:::info

使用者介面上有簡易呈現監控CPU、硬碟、記憶體、網路的狀態及流量，若需要更詳細的資訊可以自行安裝程式監控

:::

### 容器

:::spoiler Q1. 容器的浮動IP及Port範圍？
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

:::spoiler Q4. 開發型容器ssh連線時顯示Permission denied？
:::info

* 可能是主機密碼輸入錯誤，請重新輸入或到下列網址重設主機密碼  
https://iservice.nchc.org.tw/module_page.php?module=nchc_service#nchc_service/nchc_service.php?action=nchc_unix_account_edit

:::

:::spoiler Q5. 執行程式時發現I/O緩慢？
:::info

* 如果dataset是許多小檔案，且dataset佔很大空間，應將小檔案集合成大檔案減少I/O壓力
* 製作複本，再以複本開一個新的容器，看系統能否安排到較不忙的節點

:::

:::spoiler Q6. 程式執行時效能不如預期？
:::info

* 如在Pytorch環境下，可用NUMA control來鎖定CPU core
* 檢查套件相容性，使用以下文件進行套件管理  
https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh

:::

:::spoiler Q7. 程式執行時顯示insufficient shared memory？
:::info

* 在PyTorch環境下，將Dataloader的num workers設置為0
* 重新建立一個容器，選擇有share memory的設定

:::

:::spoiler Q8. 程式執行時顯示bus error？
:::info

* 檢查套件相容性，使用以下文件進行套件管理  
https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh
* 重新建立一個容器，選擇舊一點的映像檔版本

:::

:::spoiler Q9. 容器只能建立一次複本？
:::info

* 是的

:::

:::spoiler Q10. 如何建立第二次複本？
:::info

* 用複本建立一個新容器，進行修改後再建立複本

:::

### 台灣杉二號 (命令列介面)
:::spoiler Q1. 是否可以在台灣衫2號上面安裝Rclone軟體同步工具?
:::info
* 台灣杉二號有安裝最新版的Rclone，可以使用  "module  load  rclone" 來獲取  rclone  使用環境。而  rclone  是使用  go  語言撰寫，解壓縮在家目錄即可直接使用。
:::


## 儲存服務
### HFS儲存服務
:::spoiler Q1. HFS空間已滿，將部分資料刪除，發現容量還是一樣沒變化
:::info

* 如需詳細了解資料夾中資訊，可以在CLI中下指令”du –sh 資料夾”，方可了解是那些檔案佔據了空間

* 計算過程產生的暫存檔會存放在下列兩個隱藏目錄，可以下指令”ls -la”查看，也有可能是造成您空間滿的原因

    /home/主機帳號/.cache/
    
    /home/主機帳號/.local/
:::