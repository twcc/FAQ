# TWCC FAQs | 容器運算服務 (CCS)


:::spoiler Q1. 容器的浮動 IP及 Port 範圍？

:::info

* IP:
203.145.219.128/25 (包含203.145.219.128)
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
- 檢查套件相容性，使用以下文件進行套件管理：
https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh

:::

:::spoiler Q7. 程式執行時顯示 insufficient shared memory？ 

:::info

- 在 PyTorch 環境下，將 Dataloader 的 num workers 設置為 0
- 重新建立一個容器，選擇有 share memory 的設定。

:::

:::spoiler Q8. 程式執行時顯示 bus error？ 

:::info

- 檢查套件相容性，使用以下文件進行套件管理。
https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh
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
