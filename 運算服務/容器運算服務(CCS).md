# TWCC FAQs | 容器運算服務 (CCS)

:::spoiler Q1. 容器的 Port 範圍是什麼？

:::info
* Port:
50000-60000

:::

:::spoiler Q2. 如何從容器轉移至 HPC 進行訓練運算？ 

:::info
- 可參考網路上 Horovod 和 Singularity 的使用說明文件
- 參考網址中的 tutorial 進行
https://www.twcc.ai/doc?page=howto_hpc3
https://www.twcc.ai/doc?page=howto_hpc4

:::

:::spoiler Q3. 如何使用 8 張 GPU 以上的資源？ 
:::info
請改為使用 HPC 台灣杉二號 (命令列介面)，使用方法可參考網路上 Horovod 和 Singularity 的使用說明文件，或參考以下的 tutorial 進行：
https://www.twcc.ai/doc?page=howto_hpc3
https://www.twcc.ai/doc?page=howto_hpc4

:::

:::spoiler Q4. 開發型容器 SSH 連線時顯示 Permission denied？ 

:::info

可能是主機密碼輸入錯誤，請重新輸入或到下列網址重設主機密碼：
https://iservice.nchc.org.tw/module_page.php?module=nchc_service#nchc_service/nchc_service.php?action=nchc_unix_account_edit

:::

:::spoiler Q5. 執行程式時發現 I/O 緩慢？ 

:::info

可能是 dataset 問題或是容器所處的節點較為繁忙：
- 若您的 dataset 為許多小檔案，且 dataset 佔了大量空間，我們建議您將小檔案集合成大檔案，以減少 I/O 壓力。
- 製作容器複本，再以複本開一個新的容器，若系統整體負載仍有餘裕，可以安排到較不繁忙的節點。

:::

:::spoiler Q6. 程式執行時效能不如預期？ 

:::info

- 如在 PyTorch 環境下，可用 NUMA control 來鎖定 CPU core。
- 檢查套件相容性，使用[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh)進行套件管理。

:::

:::spoiler Q7. 程式執行時顯示 insufficient shared memory？ 

:::info

- 在 PyTorch 環境下，將 Dataloader 的 num workers 設置為 0
- 重新建立一個容器，選擇有 share memory 的設定。
:::

:::spoiler Q8. 程式執行時顯示 bus error？ 

:::info

- 檢查套件相容性，使用[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh)進行套件管理。
- 重新建立一個容器，選擇較舊的映像檔版本。
:::

:::spoiler Q9. 容器只能建立一次複本？ 

:::info

目前系統只容許每個容器建立一次複本。

:::

:::spoiler Q10. 如何建立第二次複本？ 

:::info

使用複本建立一個新容器，進行修改後再建立複本。

:::

:::spoiler Q11. 如何暫停容器？ 

:::info
目前系統不支援容器暫停的功能。

:::

:::spoiler Q12. 程式執行時發現比 local 端還慢？ 

:::info
- 檢查套件相容性，使用[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh)進行套件管理。
- 如在 PyTorch 環境下，可用 NUMA control 來鎖定 CPU core。
- 若您的 dataset 為許多小檔案，且 dataset 佔了大量空間，我們建議您將小檔案集合成大檔案，以減少 I/O 壓力。
- 製作容器複本，再以複本開一個新的容器，若系統整體負載仍有餘裕，可以安排到較不繁忙的節點。

:::

:::spoiler Q13. 程式執行時發生有些 library 無法載入 (Could not load dynamic library...)？ 

:::info
- 可能是程式中呼叫的 library 版本與容器中的版本不符。請執行以下指令，取得環境中的 library 版本後，再修改程所呼叫的 library 版本：  
  `$sudo find / -name "library名稱"`

:::

:::spoiler Q14. 無法連線 Jupyter notebook 時如何處理？ 

:::info
- 請您檢查套件相容性，並使用以[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh)進行套件管理。

:::

:::spoiler Q15. 為何切換成 root 無法存取自己的 /home 與 /work？ 

:::info
- 為保障資料安全，/home 與 /work 僅限使用者本身的帳號能存取，root 身分及其他使用者皆無法存取您的 /home 與 /work。

:::

:::spoiler Q16. 要如何分享/home與/work的資料給其他同計畫使用者？ 

:::info
- 請使用 TWCC 雲端物件儲存 (COS) 為媒介，以 TWCC CLI 為工具，操作方式請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/twcc-cli-v05#4-%E9%9B%B2%E7%AB%AF%E7%89%A9%E4%BB%B6%E5%84%B2%E5%AD%98%E6%9C%8D%E5%8B%99COS-Cloud-Object-Storage)。

:::


:::spoiler Q17. 為何 sudo  apt  update 產生 Unable  to  change  to  /home/wistron1/ -chdir  (13:  Permission  denied)？ 

:::info
- 請切換成 root 身分後再執行：  
  `$ apt update`

:::

