---
title : FAQ-VDS | zh
tags: FAQ, ZH
GA: UA-155999456-1
---

{%hackmd @docsharedstyle/default %}

# TWCC FAQs | 虛擬磁碟服務 (VDS)

:::spoiler Q1. 為何保留的 HDD 無法成功掛載到新的虛擬運算服務個體上？

:::info

1. 掛載 HDD 至虛擬運算服務個體前，請先確認其狀態為 **`AVAILABLE`**，才可以掛載至新的個體。
2. 如非此狀態請先將 HDD 與原本的個體分離，或是將原先的個體刪除，確認狀態為 **`AVAILABLE`** 後，再進行掛載。

若上述情況確認後，仍無法掛載，請洽技術支援服務：isupport@twcc.ai。
:::

:::spoiler Q2. 無法讀取新掛載的磁碟？

:::info
新掛載的磁碟，需完成初始化才能存取資料，初始化步驟請參考：
[<ins>HowTo：初始化磁碟- Linux 個體</ins>](https://www.twcc.ai/doc?page=howto-bss-init-vol-linux) 或 [<ins>HowTo：初始化磁碟- Windows</ins>](https://www.twcc.ai/doc?page=howto-bss-init-vol-windows)。
:::

:::spoiler Q3. 如何上傳及下載檔案？

:::info
將磁碟掛載至虛擬運算個體後，[<ins>使用 MobaXterm 連線個體</ins>](https://www.twcc.ai/doc?page=vm#%E9%80%A3%E7%B7%9A%E8%99%9B%E6%93%AC%E9%81%8B%E7%AE%97%E5%80%8B%E9%AB%94)，並完成磁碟初始化，於 MobaXterm 頁面左側處選取 「**Sftp**」 圖示，即可檢視、上傳與下載檔案。
:::

:::spoiler Q4. 我想要將舊有的資料碟換成新的資料碟，請問要如何操作？

:::info
詳細操作方式請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/howto-bss-replace-data-vol-zh)，可變更磁碟類型、容量，並透過同步方式將舊磁碟資料保存至新磁碟。
:::

:::spoiler Q5. 為何我的資料碟刪不掉？

:::info
1. 刪除前請先檢查該資料碟是否已經與虛擬運算個體分離，並確認狀態為 **`AVAILABLE`**，再進行刪除。
2. 若有對資料碟製作快照，您必須先將資料碟的快照刪除，再對該資料碟進行刪除。

若上述情況確認後，仍無法刪除，請洽技術支援服務： isupport@twcc.ai。
:::

:::spoiler Q6. 為什麼已經將計畫中虛擬磁碟全部刪除卻還是持續出現用量計費？

:::info

虛擬磁碟計費項目除了資料磁碟，亦包含虛擬運算個體映像檔。請檢查您是否有建立虛擬運算個體映像檔，若無需使用建議刪除以停止計費。

:::
