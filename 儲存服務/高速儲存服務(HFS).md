---
title : FAQ-HFS | zh
tags: FAQ, ZH
GA: UA-155999456-1
---

{%hackmd @docsharedstyle/default %}

# TWCC FAQs | 高速檔案系統 (HFS)

:::spoiler Q1. 高速檔案系統空間已滿，將部分資料刪除，為何容量還是一樣沒變化？

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

:::spoiler Q3. 如何將檔案上傳到高速檔案系統？

:::info

請先利用容器環境取得金鑰，再利用 SFTP 軟體 (例：Filezilla) 連線到資料傳輸節點(xdata1.twcc.ai)，請參考[<ins>此文件</ins>](https://www.twcc.ai/doc?page=hfs)。
:::

:::spoiler Q4. 如何增購高速檔案系統空間？

:::info

請參考[<ins>此文件</ins>](https://www.twcc.ai/doc?page=hfs)中「**查看容量**」及「**HFS空間管理政策**」兩個段落，即可得知價格以及增購空間的方法。

:::

:::spoiler Q5. 請問高速檔案系統的 IP 位置為何？

:::info
203.145.219.101

:::

:::spoiler Q6. 高速檔案系統畫面顯示快用滿，要如何知道是哪些檔案佔據儲存空間？

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

:::spoiler Q7. 增購高速檔案系統空間後多久生效？

:::info
- 在 [<ins>Service 會員服務系統 <i class="fa fa-question-circle fa-question-circle-for-service" aria-hidden="true"></i></ins>](https://man.twcc.ai/@twsdocs/howto-service-access-service-zh) 完成增購空間步驟後，稍等 15 分鐘後即可使用。
:::

:::spoiler Q8. 已刪除高速檔案系統內資料，為何在儲存與資源用量頁面中的已使用容量並未減少？

:::info

頁面中所顯示的已使用容量需一段時間進行更新，請您在刪除檔案約 1-2 小時後，再至頁面查看。

:::


:::spoiler Q9. JupyterNotebook刪除檔案後沒有立即釋放空間?

:::info

在JupyterNotebook使用UI介面進行刪除檔案，  
該檔案會移至`/home/<主機帳號>/.local/share/Trash`下，  
若是要立即釋放空間，則需要在terminal下輸入`rm -r /home/<主機帳號>/.local/share/Trash`，
將先前使用JupyterNotebook刪除檔案的保留檔案刪除。  
或是在刪除檔案時選擇使用FileZilla或terminal等工具進行，即可立即釋放空間。

:::
