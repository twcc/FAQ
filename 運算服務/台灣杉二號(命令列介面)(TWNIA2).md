---
title : FAQ-TWNIA2 | zh
tags: FAQ, ZH
GA: UA-155999456-1
---

{%hackmd @docsharedstyle/default %}


# TWCC FAQs | 台灣杉二號 (命令列介面) (TWNIA2)

## 連線登入
:::spoiler Q1. 請問如何登入台灣杉二號(命令列介面)？
:::info

使用 SSH 方式登入，登入節點為 ln01.twcc.ai，先輸入主機密碼再輸入OTP，即完成登入，詳細登入步驟請參考[<ins>此文件<ins>](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/%2F%40twccdocs%2Fguide-twnia2-prerequisite-for-connection-zh)。

:::

:::spoiler Q2. SSH 連線至 TWCC 上的資源 CCS、VCS 和 HPC 有哪些可使用的的開源軟體？
:::info

可以使用 MobaXterm、PuTTY 和 VSCode...等第三方開源軟體。

:::

:::spoiler Q3. 半年前登入過台灣杉二號 (命令列介面)，而最近想使用時卻無法成功登入?
:::info
因為個人主機密碼時效是 180 天，如超過時效，需至 [<ins>Service 會員服務系統 <i class="fa fa-question-circle fa-question-circle-for-service" aria-hidden="true"></i></ins>](https://man.twcc.ai/@twsdocs/howto-service-access-service-zh) 更改個人主機密碼，修改完成後再進行登入。
:::


## 資源配置與監控


:::spoiler Q1. 台灣杉二號 (命令列介面) 是否可使用跨節點的運算？
:::info

台灣杉二號 (命令列介面) 可透過 [<ins>Slurm</ins>](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/%2F%40twccdocs%2Fguide-twnia2-slurm-intro-zh) 指令索取計算資源，執行[<ins>跨節點高速運算</ins>](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fhowto-twnia2-run-parallel-job-container-zh)，將高負載的工作量平均分派，提升處理效率。

:::

:::spoiler Q2. 使用跨節點運算，節點是系統自動選取或需手動選取？
:::info
您可以使用 Slurm 指令選取節點，相關指令請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/%2F%40twccdocs%2Fguide-twnia2-job-parameter-zh)。
:::

:::spoiler Q3. 為什麼我執行任務索取多個 CPU 資源會發生錯誤？
:::info
請確認使用的資源比例，因台灣杉二號的資源比例必須為 1 GPU : 4 CPU : 90 GB Memory，例：GPU 數量須設定為 8 個才能取得 32 個 CPU。
:::



## 套件軟體
:::spoiler Q1. 請問在台灣杉二號 (命令列介面) 如何部屬環境執行我的程式？
:::info
1. Conda：使用簡單的 Conda 指令即可將套件安裝完成，並能切換至指定的虛擬環境，使用不同版本的 Python，解決多版本的相容問題，請參考[<ins>此文件<ins>](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fhowto-twnia2-conda-manage-packages-submit-job-zh)了解更多。
2. Singularity：透過 Singularity 包裝您所需的套件與程式，建立可在台灣杉二號 (命令列介面)  服務執行運算工作的容器環境，並可以快速部署套件、搬移、以及分享，請參考[<ins>此文件<ins>](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fhowto-twnia2-create-sglrt-container-zh)了解更多。


:::

:::spoiler Q2. 可以協助我安裝套件嗎？
:::info
您擁有自由安裝套件的權限，請您依所需自行安裝。此外，我們建議您使用 Conda 或 Singularity 容器管理套件。
:::


:::spoiler Q3. 排程系統 Slurm 是什麼？
:::info
請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/%2F%40twccdocs%2Fguide-twnia2-slurm-intro-zh)有 Slurm 系統架構的詳細說明。
:::

:::spoiler Q4. 是否可以在台灣杉二號上安裝 Rclone 軟體同步工具？

:::info

台灣杉二號有安裝最新版的 Rclone，可以使用 `module load rclone` 指令來取得 Rclone 的使用環境。而 Rclone 是使用 Go 語言撰寫，解壓縮在家目錄即可直接使用。 
:::

:::spoiler Q5. 台灣杉二號有支援 Nvidia 的 CUDA 運算架構嗎?
:::info
有的，在登入台灣杉二號節點後執行 `module avail` 指令，將會列出所有的可被載入的 module 資訊，您可使用 `module load` 指令選擇所需的 CUDA 版本。
:::

:::spoiler Q6. 為什麼有些套件在開發型容器可以使用，但在台灣杉二號不能，兩者不是共用高速儲存空間 (HFS) 嗎?
:::info
兩者儲存環境相同，但計算環境不同：

- 開發型容器的計算環境是由 TWCC 容器映像檔所建置。
- 而台灣杉二號則需使用者自行部署計算環境。
    <i class="fa fa-lightbulb-o fa-20" aria-hidden="true"></i> **提示：** 台灣杉二號可使用 `module` 載入所需之套件，詳細使用方法請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/%2F%40twccdocs%2Fguide-twnia2-module-intro-zh)。
:::

## 儲存與資料傳輸
:::spoiler Q1. 登入後發現 /home/$USER 沒什麼檔案是正常的嗎？
:::info
台灣杉二號的儲存空間是採用高速檔案系統，而此空間的使用權限為您個人所有，若您未曾載入檔案，此空間便是空的。
:::

:::spoiler Q2. 計畫到期後儲存在台灣杉二號的檔案會刪除嗎？
:::info
登入台灣杉二號使用的儲存空間為高速檔案系統，儲存空間是跟著個人帳號非計畫，因此計畫到期後檔案不會隨計畫刪除。

<i class="fa fa-exclamation-triangle fa-20" aria-hidden="true"></i> **重要：** **系統會定期清理 TWCC 帳號下久未使用之資源，請務必定期備份您的資料。**
:::

## 網路安全
:::spoiler Q1. 請問台灣杉二號的登入節點 IP 位置為何？ 

:::info
203.145.219.98

:::


## 執行錯誤
:::spoiler Q1. 使用台灣杉二號時出現此錯誤訊息`QOSMaxSubmitJobPerUserLimit Error`？
:::info
此錯誤訊息顯示您提交超過 20 個計算工作上限 (**gtest** 為測試用 Queue，僅能提交 5 個工作)。

若遇此情況，建議您先使用 `squeue` 指令查看任務狀態，再使用 `scancel` 取消狀態為等待中或運行中的任務，減少提交的任務數量。Queue 與計算資源使用說明可參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/doc-twnia2-main-zh/%2F%40twccdocs%2Fguide-twnia2-queue-zh)。
:::











