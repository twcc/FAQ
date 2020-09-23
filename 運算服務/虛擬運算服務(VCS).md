# TWCC FAQs | 虛擬運算服務 (VCS)

<!-- 
:::spoiler Q1. 虛擬運算的浮動 IP 範圍？

:::info

- 203.145.217.0/24
- 203.145.218.0/24
- 203.145.220.0/22
- 203.145.219.0/24
- 103.124.73.0/24
- 103.124.74.0/24
- 103.124.75.0/24

:::
 -->

:::spoiler Q1. 如何使虛擬運算個體進行自動快照？ 

:::info

您可透過 TWCC-CLI 與 `crontab -e` 進行定時快照設定。
- TWCC-CLI 使用詳情請參考 [3-7. 虛擬運算個體快照](https://man.twcc.ai/@twccdocs/twcc-cli-v05#3-7-%E8%99%9B%E6%93%AC%E9%81%8B%E7%AE%97%E5%80%8B%E9%AB%94%E5%BF%AB%E7%85%A7-TBD%E2%80%A6)。
- `crontab -e` 請參考 [crontab guru](https://crontab.guru/) 或 [crontab(5) - Linux man page](https://linux.die.net/man/5/crontab)。

:::

:::spoiler Q2. 如何將虛擬運算中資料定期備份至雲端物件儲存 (COS)？ 

:::info

您可透過 TWCC-CLI 與 `crontab -e` 進行定時快照設定。
- TWCC-CLI 使用詳情請參考 [4-3. 上傳檔案至儲存體](https://man.twcc.ai/@twccdocs/twcc-cli-v05#4-3-%E4%B8%8A%E5%82%B3%E6%AA%94%E6%A1%88%E8%87%B3%E5%84%B2%E5%AD%98%E9%AB%94)。
- `crontab -e` 請參考 [crontab guru](https://crontab.guru/) 或 [crontab(5) - Linux man page](https://linux.die.net/man/5/crontab)。

:::


:::spoiler Q3. 虛擬運算服務是否支援 SMTP？ 

:::info

在虛擬運算個體中，使用者可以依需求安裝任何軟體或應用程式，因此您可以將虛擬運算個體作為 SMTP 伺服器來發送信件。

:::


:::spoiler Q4. 虛擬運算服務個體是否可直接掛載雲端物件儲存 (COS)？

:::info

可以直接掛載 COS，您在 VCS 個體擁有管理者權限，可以對 VCS 個體進行任意操作，掛載建議使用 s3fs 或是相關的套件，可參考 https://github.com/s3fs-fuse/s3fs-fuse

:::

:::spoiler Q5. 請問我要如何知道我們開的虛擬運算服務個體網路流量狀態？ 

:::info

使用者介面上有簡易呈現監控 CPU、硬碟、記憶體、網路的狀態及流量，若需要更詳細的資訊可以自行安裝程式監控。

:::

:::spoiler Q6. 虛擬運算個體建立後為何無法連線網路？ 

:::info

- 請檢查虛擬網路設定是否有誤。
- 如果有啟用虛擬網路防火牆，但不清楚規則如何設定，我們建議您先把防火牆關閉。

:::


:::spoiler Q7. 如果把超過 100GB 的映像檔輸入虛擬運算服務個體，會有什麼影響？

:::info

系統碟的大小為 100GB，使用超過 100GB 會使整台虛擬運算個體無法開啟，但不會額外收費。

:::

:::spoiler Q8. 對虛擬運算個體安裝套件或進行更新，出現`E: Could not get lock /var/lib/apt/lists/lock`該如何解決？

:::info

安裝套件或進行更新時，可能產生許多類似與 lock 檔案相關的錯誤訊息。請您將 lock 檔案刪除後，再次執行您的任務。

:::

:::spoiler Q9. 如何讓 Auto scaling 擴展出的個體，符合我需求的環境？

:::info

請按照以下步驟進行：

* 建立環境映像檔
   1. 建立虛擬運算個體，部署環境與檔案，並製作個體快照 (或使用您現有的個體製作快照)
   2. 利用步驟1所建立的快照，再建立一虛擬運算個體
* 設定 Auto Scaling
   3. 建立 Auto Scaling
   4. 將 Auto Scaling 掛載至步驟2所建立的個體

經以上步驟設定，Auto Scaling 擴展出的個體，即會符合您所需的環境。

:::

:::spoiler Q10. 欲使用虛擬運算個體架設服務，卻無法連入？

:::info

請檢查個體的安全性群組或防火牆規則是否阻擋連線，相關文件請參考：

安全性群組：https://www.twcc.ai/doc?page=security_group

基礎虛擬防火牆：https://www.twcc.ai/doc?page=firewall_fwaas

:::

:::spoiler Q11. 請問快照建立的時間需要多久？

:::info

快照建立的時間約 10-15 分鐘。

:::

:::spoiler Q12. 請問如何節省快照製作的時間？

:::info

若製作快照的同時，仍有資料進行傳輸，將會增加製作快照的時間，因此我們建議您先「停止」虛擬運算個體，再進行快照的功能。

:::

:::spoiler Q13. 請問建立虛擬運算個體失敗該怎麼處理？

:::info

請您至虛擬運算個體詳細資料頁面，游標移至狀態`Unsuccessful`上將顯示建立失敗的訊息，
請將此頁面截圖 (和建立失敗訊息)，連同計畫代碼與虛擬運算個體的資訊 (ID、映像檔、硬體規格...等) 寄發 e-mail 至 `isupport@twcc.ai`，技術團隊將協助您處理。

:::

:::spoiler Q14. 請問為什麼我用快照所建立的虛擬運算個體無法連線進入？

:::info

請先檢查原快照前虛擬運算個體的以下兩項設定
1. /etc/fstab 自動掛載磁碟-若有設定的話要記得註解掉，否則利用快照所建立的虛擬運算個體會找不到裝置就會導致無法連入虛擬運算個體的情況
2. 若您所使用的作業系統版本為ubuntu18.04，且有更改到/etc/network/interfaces，也會造成無法連線

確認檢查以上兩項設定無誤後，對該台虛擬運算個體在進行一次快照，並利用新建的快照建立虛擬運算個體，如仍無法連線，請詳述情況並寄發e-mail 至isupport@twcc.ai，技術團隊將協助您處理。
:::