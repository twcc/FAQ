---
title : FAQ-HFS | zh
tags: FAQ, ZH
GA: UA-155999456-1
---

{%hackmd @docsharedstyle/default %}

# TWCC FAQs | 高速儲存服務 (HFS)

:::spoiler Q1. 高速儲存服務空間已滿，將部分資料刪除，為何容量還是一樣沒變化？

:::info
- 在容器或台灣杉二號環境中，執行以下指令，即可檢視是哪些檔案佔據了空間：
    ```
    $ du –sh 資料夾名稱
    ```
 
- 計算過程產生的暫存檔，也有可能是造成您空間佔滿的原因。暫存檔會存放在以下兩個隱藏目錄：
    - /home/主機帳號/.cache/  
    - /home/主機帳號/.local/ 
  
    可切換至以上兩個目錄，並執行以下指令查看目錄下之檔案：  
    ```
    $ ls -la
    ```  
:::

:::spoiler Q2. 我使用 SFTP 的方式連入 xdata1.twcc.ai 資料傳輸節點，為何無法登入？

:::info

請先確認您登入憑證使用的是 SSH 私密金鑰，而非您的主機密碼。若確認登入憑證無誤但登入仍有問題，請洽詢客服人員。 
:::

:::spoiler Q3. 如何將檔案上傳到高速儲存服務？

:::info

請先利用容器環境取得金鑰，再利用 SFTP 軟體 (例：Filezilla) 連線到資料傳輸節點(xdata1.twcc.ai)，請參考[<ins>此文件</ins>](https://www.twcc.ai/doc?page=hfs)。
:::

:::spoiler Q4. 如何增購高速儲存服務空間？

:::info

請參考[<ins>此文件</ins>](https://www.twcc.ai/doc?page=hfs)中「**查看容量**」及「**HFS空間管理政策**」兩個段落，即可得知價格以及增購空間的方法。

:::

:::spoiler Q5. 請問高速儲存服務的 IP 位置為何？

:::info
203.145.219.101

:::

:::spoiler Q6. 高速儲存服務畫面顯示快用滿，要如何知道是哪些檔案佔據儲存空間？

:::info
- 在容器或台灣杉二號環境中，執行以下指令，即可檢視是哪些檔案佔據了空間：
    ```
    $ du –sh 資料夾名稱
    ```
 
- 計算過程產生的暫存檔，也有可能是造成您空間佔滿的原因。暫存檔會存放在以下兩個隱藏目錄：
    - /home/主機帳號/.cache/  
    - /home/主機帳號/.local/ 
  
    可切換至以上兩個目錄，並執行以下指令查看目錄下之檔案：  
    ```
    $ ls -la
    ```  
:::

:::spoiler Q7. 增購高速儲存服務空間後多久生效？

:::info
- 在 [<ins>Service 會員服務系統 <i class="fa fa-question-circle fa-question-circle-for-service" aria-hidden="true"></i></ins>](https://man.twcc.ai/@twsdocs/howto-service-access-service-zh) 完成增購空間步驟後，稍等 15 分鐘後即可使用。
:::
