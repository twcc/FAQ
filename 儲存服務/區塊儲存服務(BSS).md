---
title : FAQ-BSS | zh
tags: FAQ, ZH
GA: UA-155999456-1
---

{%hackmd @docsharedstyle/default %}

# TWCC FAQs | 區塊儲存服務 (BSS)

:::spoiler Q1. 為何保留的 HDD 無法成功掛載到新的虛擬運算服務個體上？

:::info

1. 掛載 HDD 至虛擬運算服務個體前，請先確認其狀態為 **`AVAILABLE`**，才可以掛載至新的個體。
2. 如非此狀態請先將 HDD 與原本的個體分離，或是將原先的個體刪除，確認狀態為 **`AVAILABLE`** 後，再進行掛載。

若上述情況確認後，仍無法掛載，請洽技術支援服務：isupport@twcc.ai。
:::

:::spoiler Q2. 我想要將舊有的資料碟換成新的資料碟，請問要如何操作？

:::info
詳細操作方式請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/howto-bss-replace-data-vol-zh)，可變更磁碟類型、容量，並透過同步方式將舊磁碟資料保存至新磁碟。
:::

:::spoiler Q3. 為何我的資料碟刪不掉？

:::info
1. 刪除前請先檢查該資料碟是否已經與虛擬運算個體分離，並確認狀態為 **`AVAILABLE`**，再進行刪除。
2. 若有對資料碟製作快照，您必須先將資料碟的快照刪除，再對該資料碟進行刪除。

若上述情況確認後，仍無法刪除，請洽技術支援服務： isupport@twcc.ai。
:::
