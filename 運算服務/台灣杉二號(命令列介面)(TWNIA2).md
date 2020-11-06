---
title : FAQ-TWNIA2 | zh
tags: FAQ, ZH
GA: UA-155999456-1
---

{%hackmd @docsharedstyle/default %}


# TWCC FAQs | 台灣杉二號 (命令列介面) (TWNIA2)

:::spoiler Q1. 是否可以在台灣衫二號上安裝 Rclone 軟體同步工具？

:::info

台灣杉二號有安裝最新版的 Rclone，可以使用 `module load rclone` 指令來取得 Rclone 的使用環境。而 Rclone 是使用 Go 語言撰寫，解壓縮在家目錄即可直接使用。 
:::

:::spoiler Q2. 請問台灣杉二號的登入節點 IP 位置為何？ 

:::info
203.145.219.98

:::

:::spoiler Q3. 使用跨節點運算，節點是系統自動選取或需手動選取？
:::info
您可以使用 Slurm 指令選取節點，相關指令請參考[<ins>此文件</ins>](https://www.twcc.ai/doc?page=hpc_cli#6-Slurm%E6%8C%87%E4%BB%A4)。
:::

:::spoiler Q4. 排程系統 Slurm 是什麼？
:::info
請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/B15nJXe-B#Slurm-%E5%9F%BA%E6%9C%AC%E8%AA%AA%E6%98%8E)有 Slurm 系統架構的詳細說明。
:::

:::spoiler Q5. 登入後發現 /home/$USER 沒什麼檔案是正常的嗎？
:::info
台灣杉二號的儲存空間是採用高速檔案系統，而此空間的使用權限為您個人所有，若您未曾載入檔案，此空間便是空的。
:::

:::spoiler Q6. 可以協助我安裝套件嗎？
:::info
您擁有自由安裝套件的權限，請您依所需自行安裝。此外，我們建議您使用 Conda 或 Singularity 容器管理套件。
:::

:::spoiler Q7. 為什麼我執行任務要索取多個 CPU 資源會發生錯誤？
:::info
請確認使用的資源比例，因台灣杉二號的資源比例必須為 1 GPU : 4 CPU : 90 GB Memory，例：GPU 數量須設定為 8 個才能取得 32 個 CPU。
:::

:::spoiler Q8. 計畫到期後儲存在台灣杉二號的檔案會刪除嗎？
:::info
登入台灣杉二號使用的儲存空間為高速檔案系統，儲存空間是跟著個人帳號非計畫，因此計畫到期後檔案不會隨計畫刪除。

<i class="fa fa-exclamation-triangle fa-20" aria-hidden="true"></i> **重要：** **系統會定期清理 TWCC 帳號下久未使用之資源，請務必定期備份您的資料。**
:::

:::spoiler Q9. 台灣杉二號有支援 Nvidia 的 CUDA 運算架構嗎?
:::info
有的，在登入台灣杉二號節點後執行 `module avail` 指令，將會列出所有的可被載入的 module 資訊，您可使用 `module load` 指令選擇所需的 CUDA 版本。
:::

:::spoiler Q10. 半年前登入過台灣杉二號 (命令列介面)，而最近想使用時卻無法成功登入?
:::info
因為個人主機密碼時效是180天，如超過時效，需至 iService 更改個人主機密碼，修改完成後再進行登入。
:::

:::spoiler Q11. 使用台灣杉二號時出現此錯誤訊息`QOSMaxSubmitJobPerUserLimit Error`？
:::info
此錯誤訊息顯示您提交超過 20 個計算工作上限 (**gtest** 為測試用 Queue，僅能提交 5 個工作)。若遇此情況，建議您先使用 `squeue` 指令查看任務狀態，再使用 `scancel` 取消狀態為等待中或運行中的任務，減少提交的任務數量。Queue 與計算資源使用說明可參考[<ins>此文件</ins>](https://www.twcc.ai/doc?page=hpc_cli#4-Queue-%E8%88%87%E8%A8%88%E7%AE%97%E8%B3%87%E6%BA%90%E4%BD%BF%E7%94%A8%E8%AA%AA%E6%98%8E)。
:::
