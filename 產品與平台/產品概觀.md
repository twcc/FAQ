---
title : FAQ-product | zh
tags: FAQ, ZH
GA: UA-155999456-1
---

{%hackmd @docsharedstyle/default %}

<style>
.fa-times{color:#ADADAD; font-size:25px}
.fa-check{color:#27a5bd; font-size:25px}
</style>


# TWCC FAQs | 產品概觀

:::spoiler Q1. 容器運算 (CCS)、虛擬運算 (VCS) 及高速運算 (HPC) 有什麼不同？

:::info

三種服務的功能與特色、資源規格、儲存空間比較如下：

| 服務       | 容器運算服務 (CCS)                                                       | 虛擬運算服務 (VCS)                                                     | 高速運算 (HPC) |
| -------- | -------- | -------- | -------- |
| 功能與特色 | ● 適用 AI 模型訓練與推斷<br>● 可隨時調整參數，利於開發<br>● 資源選項固定 | ● 功能與一般虛擬機雷同，適合架設服務伺服器<br>● 可調整網路及安全相關設定<br>● 資源選項固定 | ● 跨節點運算<br>● 命令列介面<br>● 彈性選用 GPU 數量          |
| 資源規格   | ● 最多可調用 8 顆 GPU<br>● 資源比 GPU:CPU:RAM(GB) 為 1:4:90              | ● 提供 vCPU，最多可調用 48 核                                                                   | ● 可彈性依<br>需求調整 GPU 數量       |
| 儲存空間   | ● 高速儲存服務 (HFS)，註冊帳號及獲得 200 GB，可依需求增購空間        | ● 虛擬運算個體系統碟 (100 GB)<br>● 虛擬磁碟服務 (VDS) 附加資料碟，可自行選擇容量                                                                   | ● 高速儲存服務 (HFS)，註冊帳號及獲得 200 GB，可依需求增購空間          |
:::


:::spoiler Q2. 高速儲存服務 (HFS)、虛擬磁碟服務 (VDS) 及雲端物件儲存服務 (COS) 有什麼不同？

:::info

三種服務的搭配運算服務與價位、存取速度、特色比較如下：

| 服務 | 高速儲存服務 (HFS) | 虛擬磁碟服務 (VDS)     | 雲端物件儲存服務 (COS) |
| -------- | -------- | -------- | -------- |
| 搭配運算服務 | ● 容器運算服務 (CCS)<br>● 高速運算服務 (HPC)<br> | ● 虛擬運算服務 (VCS)<br> | ● 藉由 TWCC CLI 與容器運算服務及虛擬運算服務傳輸資料        |
| 價位 | 高 | 中 | 低 |
| 資料傳輸 | ● 透過 SFTP 上傳及下載檔案<br> ● 透過 TWCC CLI 與雲端物件儲存服務 (COS) 進行傳輸 | ● 透過 TWCC CLI 與雲端物件儲存服務 (COS) 進行傳輸 <br> ● 使用 SSH 連線虛擬運算個體，掛載且初始化虛擬磁碟，並透過 SFTP 上傳與下載檔案| ● 透過第三方軟體上傳及下載檔案 |
:::

:::spoiler Q3. 容器運算 (CCS) 跟虛擬運算 (VCS) 使用上分別適用於那些情境？

:::info
- 容器運算 (CCS) 適用於大規模且資料密集的高負載工作，例：建立 AI 模型訓練。
- 虛擬運算 (VCS) 適用於工作負載小的應用程式，例：網站架設，AI 推論服務。
:::

:::spoiler Q4. TWCC 資訊安全相關認證與機制？

:::info
關於 TWCC 的資安認證與機制請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fsecurity-overview-zh)之說明。
:::
