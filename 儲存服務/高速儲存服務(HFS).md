# TWCC FAQs | 高速儲存服務 (HFS)


:::spoiler Q1. HFS 空間已滿，將部分資料刪除，為何容量還是一樣沒變化？

:::info
- 如需詳細了解資料夾中資訊，可以在 CLI 中下 `du –sh 資料夾名稱` 指令，方可了解是那些檔案佔據了空間。
- 計算過程產生的暫存檔，也有可能是造成您空間滿的原因。暫存檔會存放在以下兩個隱藏目錄，可下 `ls -la` 指令查看：

    /home/主機帳號/.cache/

    /home/主機帳號/.local/  
:::

:::spoiler Q2. 我使用 SFTP 的方式連入 xdata1.twcc.ai 資料傳輸節點，為何無法登入？

:::info
請先確認您登入憑證使用的是 SSH 私密金鑰，而非您的主機密碼。若確認登入憑證無誤但登入仍有問題，請洽詢客服人員。 
:::

:::spoiler Q3. 如何將檔案上傳到 HFS?

:::info
* 請先利用容器環境取得金鑰，再利用 SFTP 軟體(例：Filezilla)連線到資料傳輸節點(xdata1.twcc.ai)
* 請參考 https://www.twcc.ai/doc?page=hfs。
:::
