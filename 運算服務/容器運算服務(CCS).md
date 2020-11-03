---
title : FAQ-CCS | zh
tags: FAQ, ZH
GA: UA-155999456-1
---


{%hackmd @docsharedstyle/default %}

# TWCC FAQs | 容器運算服務 (CCS)

:::spoiler Q1. 容器的 Port 範圍是什麼？

:::info
* Port:
50000-60000

:::

:::spoiler Q2. 如何從容器轉移至台灣杉二號(命令列介面)進行訓練運算？ 

:::info
- 可參考網路上 Horovod 和 Singularity 的使用說明文件
- 參考網址中的 tutorial 進行：  
https://www.twcc.ai/doc?page=howto_hpc3  
https://www.twcc.ai/doc?page=howto_hpc4

:::

:::spoiler Q3. 如何使用 8 張 GPU 以上的資源？ 
:::info
請改為使用 台灣杉二號 (命令列介面)，使用方法可參考網路上 Horovod 和 Singularity 的使用說明文件，或參考以下的 tutorial 進行：  
https://www.twcc.ai/doc?page=howto_hpc3  
https://www.twcc.ai/doc?page=howto_hpc4

:::

:::spoiler Q4. 開發型容器 SSH 連線時顯示 Permission denied？ 

:::info

可能是主機密碼輸入錯誤，請重新輸入或到[<ins>此網址</ins>](https://iservice.nchc.org.tw/module_page.php?module=nchc_service#nchc_service/nchc_service.php?action=nchc_unix_account_edit)重設主機密碼。


:::

:::spoiler Q5. 執行程式時發現 I/O 緩慢？ 

:::info

可能是 dataset 問題或是容器所處的節點較為繁忙：
- 若您的 dataset 為許多小檔案，且 dataset 佔了大量空間，我們建議您將小檔案集合成大檔案，以減少 I/O 壓力。
- 製作容器複本，再以複本開一個新的容器，若系統整體負載仍有餘裕，可以安排到較不繁忙的節點。

:::

:::spoiler Q6. 程式執行時效能不如預期？ 

:::info

- 可使用 NUMA control 套件來鎖定 CPU 使用數量，改善效能，詳情可參考[<ins>此說明</ins>](https://man.twcc.ai/@twccdocs/howto-ccs-numactl-zh)。
- 或檢查套件相容性，使用[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh)進行套件管理。

:::

:::spoiler Q7. 程式執行時顯示 insufficient shared memory？ 

:::info

- 在 PyTorch 環境下，將 Dataloader 的 num workers 設置為 0。
- 或重新建立一個容器，並選擇有 shared memory 的規格。

:::

:::spoiler Q8. 程式執行時顯示 bus error？ 

:::info

- 檢查套件相容性，使用[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh)進行套件管理。
- 重新建立一個容器，選擇較舊的映像檔版本。

:::

:::spoiler Q9. 容器能建立幾次複本？ 

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
- 用 NUMA control 來鎖定 CPU core，詳情可參考[<ins>此連結</ins>](https://man.twcc.ai/@twccdocs/howto-ccs-numactl-zh)。
- 若您的 dataset 為許多小檔案，且 dataset 佔了大量空間，我們建議您將小檔案集合成大檔案，以減少 I/O 壓力。
- 製作容器複本，再以複本開一個新的容器，若系統整體負載仍有餘裕，可以安排到較不繁忙的節點。

:::

:::spoiler Q13. 程式執行時發生有些 library 無法載入 (Could not load dynamic library...)？ 

:::info
可能是程式中呼叫的 library 版本與容器中的版本不符。請執行以下指令，取得環境中的 library 版本後，再修改程所呼叫的 library 版本：  
`$ sudo find / -name [library名稱]`

:::

:::spoiler Q14. 無法連線 Jupyter notebook 時如何處理？ 

:::info
- 請檢查套件相容性，並使用以[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh)進行套件管理。
- 部分套件會改變 Jupyter 的設定 (例：`anaconda3`)，且使用上述套件管理方法時無法檢查，請備份該資料夾並移除套件，即可連線。
- 請檢查貴單位防火牆設定是否有擋 port，容器 port 範圍請參考 Q1。
:::

:::spoiler Q15. 為何切換成 root 無法存取自己的 /home 與 /work？ 

:::info
- 為保障資料安全，容器的 root 身分無法存取您的目錄，僅限使用者與租戶管理員之帳號有權限存取。
- /home 與 /work 為高速檔案系統 (HFS) 掛載於容器的兩個目錄空間，其 root 權限為 HFS 系統管理員所擁有，非使用者可取得。
:::

:::spoiler Q16. 要如何分享 /home 與 /work 的資料給其他同計畫使用者？ 

:::info
可以透過 TWCC CLI 操作 TWCC 雲端物件儲存 (COS)，將容器資料分享給其他使用者，操作方式請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/twcc-cli-v05#4-%E9%9B%B2%E7%AB%AF%E7%89%A9%E4%BB%B6%E5%84%B2%E5%AD%98%E6%9C%8D%E5%8B%99COS-Cloud-Object-Storage)。

:::


:::spoiler Q17. 為何 sudo  apt  update 產生 Unable  to  change  to  /home/wistron1/ -chdir  (13:  Permission  denied)？ 

:::info
請切換成 root 身分後再執行：  
`$ apt update`

:::


:::spoiler Q18. 如何設定自動化將容器內資料回傳 local 端？ 

:::info
- 容器服務的網路設定有開啟 port：22、53、80、443，請利用這 4 個 port 進行資料傳送。  

:::

:::spoiler Q19. 以 Matlab 映像檔建立的容器為何無法存取 /home 及 /work？ 

:::info
因目前的 Matlab 映像檔尚未整合 HFS 高速檔案系統，因此請在 terminal 執行以下指令來存取 /home 及 /work：  
```
$ sudo su -
$ su [主機帳號]
$ /opt/matlab/R2019b/bin/matlab
```

:::

:::spoiler Q20. 在程式執行時，如何知道 GPU 使用情況？ 

:::info
Step 1. 在 terminal 執行指令： `$ nvidia-smi`  
Step 2. 確認 `GPU-Util` 欄位，非 0% 代表使用中，0% 即為未使用 (如下圖)。

![](https://cos.twcc.ai/SYS-MANUAL/uploads/upload_dbfac86546357537571cb99c4cceb37d.png)


:::

:::spoiler Q21. 目前容器支援多少種計算環境？ 

:::info
在 TWCC 的容器服務中，提供了 14 種環境供使用者選擇，包含：

* TensorFlow
* PyTorch
* CUDA
* MATLAB (目前為公開預覽版，如有特殊需求請透過客服人員提出需求)
* Caffe
* CNTK
* MXNet
* Caffe2
* TensorRT
* TensorRT Server
* Theano
* DIGITS
* RAPIDS
:::

:::spoiler Q22. 如何登入容器？ 

:::info
可以透過 SSH 或 Jupyter notebook 連線容器，請參考 [<ins>連線使用方式</ins>](https://www.twcc.ai/doc?page=container#%E9%80%A3%E7%B7%9A%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%8F)。
:::

:::spoiler Q23. 我可以建立一個容器給其他人用嗎？ 

:::info
建立容器給他人使用時，需考量以下幾點注意事項：

* 您的主機密碼必須提供給他人連線容器。
* /home 與/work 為您的個人 HFS 儲存空間，他人在使用上可能造成這兩個檔案夾中的資料毀損、遺失...等可能，即使您再開新容器也無法復原這些變動。
* 分享計算資源會有資料安全的風險，請審慎考慮。

因此，除為他人建立容器之外，您亦可以透過 iService 將他人加入計畫中，該使用者即可自行運用容器資源。
:::

:::spoiler Q24. 怎麼使用超級電腦？ 

:::info
TWCC 中有許多超級電腦的運算資源，您可以透過下列方式使用：

* 開發型容器：您可參考[<ins>此文件</ins>](https://www.twcc.ai/doc?page=container)，建立快速部署的容器環境。
* 高速運算服務：您可參考[<ins>此文件</ins>](https://www.twcc.ai/doc?page=hpc_cli)，連線進入高速運算節點，以 Command Line 的方式使用超級電腦資源，進行跨節點的高速運算。
:::

:::spoiler Q25. 如何確認容器映像檔中包了什麼套件及其版本？ 

:::info
以下兩種方法皆可以確認：
* 在 [<ins>NGC 網站</ins>](https://docs.nvidia.com/deeplearning/frameworks/index.html) 中，在右上角搜尋框依不同框架輸入 **TensorFlow release notes**、**PyTorch release notes** ...等內容，進入 release notes 列表頁面後，再點擊您要確認的框架版本，即可檢視套件內容及版本。
* 建立開發型容器、選擇映像檔類型時，請將滑鼠移至 <i class="fa fa-info-circle" aria-hidden="true"></i> ，提示內容將顯示 NGC 的網址，進入後即可找到相關資訊。
:::

:::spoiler Q26. 如何將檔案上傳至容器，或從容器下載？ 

:::info
請參考此[<ins>文件</ins>](https://www.twcc.ai/doc?page=hfs#%E4%BD%BF%E7%94%A8-SFTP--Filezilla-%E5%82%B3%E8%BC%B8%E6%AA%94%E6%A1%88)，將檔案上傳到容器的 /home 或 /work 中，或將檔案下載到 local 端。 
:::

:::spoiler Q27. 為何我刪除容器後再重新建立容器，新容器內仍存在舊容器上的套件？ 

:::info
為提供運算便利性，TWCC 預設會將高速檔案系統之儲存空間 (/home 及 /work，綁定個人帳號) 掛載至您建立的所有容器，讓您的資料或套件可跨容器使用，因此刪除容器不會影響安裝在 /home 及 /work 的套件與資料。 
:::

:::spoiler Q28. 我要如何將容器還原至初始狀態？ 

:::info
進行以下操作即可將容器還原至初始狀態：

- 參考[<ins>程式執行異常的建議排除方式</ins>](https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh#%E7%A8%8B%E5%BC%8F%E5%9F%B7%E8%A1%8C%E7%95%B0%E5%B8%B8%E7%9A%84%E5%BB%BA%E8%AD%B0%E6%8E%92%E9%99%A4%E6%96%B9%E5%BC%8F) 清空或搬移`/home/主機帳號/.local/` 目錄下之套件。
- 進入 `/home/主機帳號/.cache/` 目錄，清除計算過程產生的暫存檔。
    
:::

:::spoiler Q29. 如何切換成容器的 root 身份？ 

:::info

執行以下指令即可切換為 root 身分：  
```
$ sudo su

或

$ sudo -i
```    
:::

:::spoiler Q30. 為何無法使用容器內的 GPU？ 

:::info
- 請先確認您的程式使用的 GPU 數量。
- 可能是套件版本相容性問題，請使用[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/ccs-intactv-howto-zh)進行套件管理。
- 可能是您的程式與您所選擇的容器映像檔有版本相容性問題，請您參考 Q25，選擇適合的映像檔版本。

:::

:::spoiler Q31. 安裝套件時發生錯誤訊息 Permission denied 如何處理？ 

:::info
- 以下圖為例，如果 Permission denied 指出的檔案，其位置不在 /home 或 /work 底下，請參考 Q29 切換成容器 root 身分後再行安裝。

![](https://i.imgur.com/oKeqxdV.png)

:::

:::spoiler Q32. 為何 Jupyter notebook 無法寫入檔案？ 

:::info
高速檔案系統空間已快用滿，導致無法寫入檔案，請參考[<ins>高速檔案系統 FAQ Q6</ins>](https://man.twcc.ai/@twccdocs/faq-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Ffaq-hfs-zh)，檢查並清理您的儲存空間，或參考 Q4 增購更多儲存空間。

:::

:::spoiler Q33. 為何 Jupyter notebook 儲存檔案失敗？ 

:::info
高速檔案系統空間已快用滿，導致無法寫入檔案，請參考[<ins>高速檔案系統 FAQ Q6</ins>](https://man.twcc.ai/@twccdocs/faq-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Ffaq-hfs-zh)，檢查並清理您的儲存空間，或參考Q4增購更多儲存空間。

:::

:::spoiler Q34. 如何開始使用容器？ 

:::info
- 請先準備好您要訓練的程式，參考 Q26 上傳至高速檔案系統。
- 參考[<ins>開發型容器文件</ins>](https://www.twcc.ai/doc?page=container)，建立容器，並連線容器進行訓練。
- 訓練完成，若要檔案下載請參考 Q26。
- 若要進行推斷，可參考[<ins>HowTo文件</ins>](https://www.twcc.ai/doc?page=howto_ctn2)於容器內進行，或參考[<ins>虛擬運算文件</ins>](https://www.twcc.ai/doc?page=vm)，建立虛擬運算個體進行推斷。

:::


:::spoiler Q35. 如何知道容器配置的 GPU 數量？ 

:::info
以下兩種方式皆可查詢容器的 GPU 配置數量：
1. 在 terminal 執行指令：`$ nvidia-smi`  
2. 在使用者網站中，開發型容器管理頁 > 容器詳細資料頁的「**基本設定**」欄位即有顯示。

![](https://cos.twcc.ai/SYS-MANUAL/uploads/upload_03f616bd18d162c3dfb11da5e39a3530.png)

:::

:::spoiler Q36. 建立容器時基本設定中，為何有共享記憶體？ 

:::info
共享記憶體是使用某些 framework 運算時會使用到的記憶體空間，例：PyTorch，詳情可查看[<ins>PyTorch document</ins>](https://pytorch.org/docs/stable/multiprocessing.html)。

:::

:::spoiler Q37. 能否將共享記憶體當硬碟空間使用？ 

:::info

若您選擇有共享記憶體設定的規格，`/dev/shm` 即為共享記憶體空間，可供存放資料當硬碟使用
<i class="fa fa-exclamation-triangle fa-20" aria-hidden="true"></i> **重要：**

* 由於存放資料在共享記憶體中會占掉共享記憶體空間，因此存放前請先考量您程式所需要的空間。
* 存放於此的資料會隨容器刪除而消失，若資料需保存，請在刪除容器前將資料搬移到`/home/主機帳號`或`/work/主機帳號`。
:::

:::spoiler Q38. 在容器中如何安裝 cuDNN？ 

:::info

容器的環境中已安裝 cuDNN，詳細版本資訊可透過以下兩種方法確認：
* 在 [<ins>NGC 網站</ins>](https://docs.nvidia.com/deeplearning/frameworks/index.html) 中，在右上角搜尋框依不同框架輸入 **TensorFlow release notes**、**PyTorch release notes** ...等內容，進入 release notes 列表頁面後，再點擊您要確認的框架版本，即可檢視套件內容及版本。
* 建立開發型容器、選擇映像檔類型時，請將滑鼠移至 <i class="fa fa-info-circle" aria-hidden="true"></i> ，提示內容將顯示 NGC 的網址，進入後即可找到相關資訊。
* 連線容器後執行 `$ set | grep CUDNN` 指令
:::
