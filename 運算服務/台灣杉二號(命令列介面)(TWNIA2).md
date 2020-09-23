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
您可以使用 Slurm 指令選取節點，相關指令請參考[<ins>此文件</ins>](https://www.twcc.ai/doc?page=hpc_cli#6-Slurm%E6%8C%87%E4%BB%A4)
:::

:::spoiler Q4. 請問台灣杉二號使用的排程系統Slurm是什麼
:::info
請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/B15nJXe-B#Slurm-%E5%9F%BA%E6%9C%AC%E8%AA%AA%E6%98%8E)有Slurm系統架構的詳細說明
:::

:::spoiler Q5. 請問登入台灣杉二號後看到/home/$USER 太乾淨是正常的嗎?
:::info
在台灣杉二號節點上，是使用高速檔案系統，高速檔案系統是跟著個人帳號，所以此空間使用者沒載入檔案此空間就是乾淨的。
:::

:::spoiler Q6. 請問在台灣杉二號可以幫忙協助安裝套件嗎?
:::info
請使用者自助安裝套件，建議可以使用Conda或Singularity容器去管理套件
:::

