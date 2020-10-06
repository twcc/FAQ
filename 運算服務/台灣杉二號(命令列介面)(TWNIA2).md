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

:::spoiler Q6. 為什麼我無法索取32個CPU資源，我看文件上不是說一個節點最多有32個CPU嗎?
:::info
使用台灣杉二號的資源比例須為 1 GPU : 4 CPU : 90 GB Memory，所以注意GPU要設定成8個才可使用32個CPU。
:::