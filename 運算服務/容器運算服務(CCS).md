## 容器運算服務(CCS)

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
* 製作複本，再以複本開一個新的容器，看系統能否安排到較不忙的節點

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

:::spoiler Q12. 執行程式時顯示GPU error或無法獲取GPU如何處理？
:::info

* 檢查程式呼叫函式庫版本是否符合環境，例如libcudart.so，下指令搜尋並確認是否符合程式呼叫版本  
`$sudo find / -name libcudart.so*`
:::

:::spoiler Q13. 執行程式時發現比local端執行還緩慢如何處理？
:::info

* 如果dataset是許多小檔案，且dataset佔很大空間，應將小檔案集合成大檔案減少I/O壓力
* 製作複本，再以複本開一個新的容器，看系統能否安排到較不忙的節點
* 將dataset放到/tmp
* 如在Pytorch環境下，可用NUMA control來鎖定CPU core
* 檢查套件相容性，使用以下文件進行套件管理
https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh
:::