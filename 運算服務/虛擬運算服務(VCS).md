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

可以直接掛載 COS，您在 VCS 個體擁有管理者權限，可以對 VCS 個體進行任意操作，掛載建議使用 s3fs 或是相關的套件，可參考 [<ins>s3fs-fuse</ins>](https://github.com/s3fs-fuse/s3fs-fuse)。

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

- [安全性群組](https://www.twcc.ai/doc?page=security_group)
[基礎虛擬防火牆](https://www.twcc.ai/doc?page=firewall_fwaas)

:::

:::spoiler Q11. 快照建立的時間需要多久？

:::info

快照建立的時間約 10-15 分鐘。

:::

:::spoiler Q12. 如何節省快照製作的時間？

:::info

若製作快照的同時，仍有資料進行傳輸，不僅無法確保資料的完整與一致性且花費的時間較多，因此建議先將個體進行手動關機 (SHUTDOWN) ，確認資料都已寫入 BSS 儲存後，再進行快照。

:::

:::spoiler Q13. 建立虛擬運算個體失敗該怎麼處理？

:::info

請您至虛擬運算個體詳細資料頁面，游標移至狀態`Unsuccessful`上將顯示建立失敗的訊息，
請將此頁面截圖 (和建立失敗訊息)，連同計畫代碼與虛擬運算個體的資訊 (ID、映像檔、硬體規格...等) 寄發 e-mail 至 isupport@twcc.ai，技術團隊將協助您處理。

:::

:::spoiler Q14. 用快照所建立的虛擬運算個體無法連線進入作業該怎麼處理？

:::info

請先檢查快照前虛擬運算個體的以下兩項設定：
1. 若有設定 /etc/fstab 自動掛載磁碟，請註解該設定或加入 `nofail` 的相關設定，否則利用快照所建立的虛擬運算個體找不到裝置，便會導致無法連入虛擬運算個體的情況。
2. 若您所使用的作業系統版本為 Ubuntu 18.04，且有更改 /etc/network/interfaces 網路設定 ，也會造成無法連線。

確認檢查以上兩項設定無誤後，對該台虛擬運算個體再進行一次快照，並利用新建的快照建立虛擬運算個體，如仍無法連線，請詳述情況並寄發 e-mail 至 isupport@twcc.ai，技術團隊將協助您處理。

:::

:::spoiler Q15. 忘記 Windows 虛擬運算個體登入密碼該怎麼處理？

:::info

在建立虛擬運算個體時，請務必妥善自行保存您的密碼，如忘記密碼您可以刪除該個體並重新建立；如須保存原個體的資料與配置，請先對該個體進行快照，並利用該快照建立新的個體，即可重設密碼。
:::

:::spoiler Q16. 遺失 Linux 虛擬運算個體的金鑰該怎麼處理？

:::info

在建立虛擬運算個體時，請務必下載並妥善自行保存您的金鑰，如果遺失金鑰您可以刪除該個體並重新建立；如須保存原個體的資料與配置，請先對該個體進行快照，並利用該快照建立新的個體，即可使用新的金鑰。
:::

:::spoiler Q17. SSH 連線個體速度有點慢該如何解決？

:::info

請調整虛擬運算個體的 DNS 設定來提升 SSH 連線的速度，設定的方法與步驟如下：
1. 輸入指令：
```
$ sudo vi /etc/ssh/sshd_config
```
2. 輸入`i` 進入編輯模式
4. 新增一行指令： 

```
Use DNS no
```
6. 按 `esc` 鍵跳離編輯模式，接著輸入 `:wq!` 存檔。
7. 如修改後還是有連線較慢的問題，請您洽詢 TWCC 技術支援服務信箱：isupport@twcc.ai，並提供所在地 IP 與 traceroute 至個體之結果。

:::

:::spoiler Q18. 已經外掛區塊儲存到指定的虛擬運算個體，卻無法在虛擬運算個體中找到儲存空間該如何解決?

:::info

掛上區塊儲存後，仍需要進行初始化的動作，才可以使用儲存空間，如何初始化可以參考以下文件:

Windows: https://man.twcc.ai/@twccdocs/HykztzH_D

Linux: https://man.twcc.ai/@twccdocs/rkyc_bHdP

:::
