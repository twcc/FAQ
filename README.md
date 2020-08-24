# TWCC FAQ

[TOC]

## 帳號相關

:::spoiler 帳 Q1. 如何註冊帳號？
:::info


至 iService...點選右上角註冊按鈕...


:::




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

## 儲存服務
### HFS儲存服務
:::spoiler Q1. HFS空間已滿，將部分資料刪除，發現容量還是一樣沒變化
:::info

* 如需詳細了解資料夾中資訊，可以在CLI中下指令”du –sh 資料夾”，方可了解是那些檔案佔據了空間

* 計算過程產生的暫存檔會存放在下列兩個隱藏目錄，可以下指令”ls -la”查看，也有可能是造成您空間滿的原因

    /home/主機帳號/.cache/
    
    /home/主機帳號/.local/
:::

## 其它服務

### TWCC-CLI


:::spoiler Q1. 請問 TWCC-CLI 怎麼安裝，謝謝!
:::info

* 請參考 [TWCC-CLI v0.5](https://github.com/TW-NCHC/TWCC-CLI/tree/v0.5) 操作文件進行安裝及使用，謝謝!
:::

