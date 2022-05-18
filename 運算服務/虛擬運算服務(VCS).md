---
title : FAQ-VCS | zh
tags: FAQ, ZH
GA: UA-155999456-1
---

{%hackmd @docsharedstyle/default %}

# TWCC FAQs | 虛擬運算服務 (VCS)

## 連線登入
:::spoiler Q1. SSH 連線至 TWCC 上的資源 CCS、VCS 和 HPC 有哪些可使用的的開源軟體？
:::info

可以使用 MobaXterm、PuTTY 和 VSCode...等第三方開源軟體。

:::

:::spoiler Q2. 欲使用虛擬運算個體架設服務，卻無法連入？

:::info

請檢查個體的安全性群組或防火牆規則是否阻擋連線，相關文件請參考：

- [安全性群組](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fguide-vcs-sg-zh)
- [基礎虛擬防火牆](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fguide-vcs-vnf-zh)

:::

:::spoiler Q3. 使用映像檔所建立的虛擬運算個體無法連線進入作業該怎麼處理？

:::info

建立映像檔前請先檢查虛擬運算個體的以下兩項設定：
1. 若有設定 /etc/fstab 自動掛載磁碟，請註解該設定或加入 `nofail` 的相關設定，否則利用映像檔所建立的虛擬運算個體找不到裝置，便會導致無法連入虛擬運算個體的情況。
2. 若您所使用的作業系統版本為 Ubuntu 18.04，且有更改 /etc/network/interfaces 網路設定 ，也會造成無法連線。

確認檢查以上兩項設定無誤後，對該台虛擬運算個體再進行一次建立映像檔，並利用新建的映像檔建立虛擬運算個體，如仍無法連線，請詳述情況並寄發 e-mail 至 isupport@twcc.ai，技術團隊將協助您處理。

:::

:::spoiler Q4. 對網路卡設定進行更改，導致無法連線該怎麼處理？

:::info

網路卡設定經修改後，將會導致無法連線進入虛擬運算個體，因此我們強烈不建議您更動網卡設定，請您操作與部署時特別留意。

如遇無法連線的情形，請詳述情況與虛擬運算個體資訊，寄發 e-mail 至 isupport@twcc.ai，技術團隊將協助您處理。

:::

:::spoiler Q5. SSH 連線個體速度有點慢該如何解決？

:::info

請調整虛擬運算個體的 DNS 設定來提升 SSH 連線的速度，設定的方法與步驟如下：

**Step 1.** 輸入指令
```
$ sudo vi /etc/ssh/sshd_config
```
**Step 2.** 輸入`i` 進入編輯模式
**Step 3.** 新增一行指令
```
Use DNS no
```
**Step 4.** 按 `esc` 鍵跳離編輯模式，接著輸入 `:wq!` 存檔。
<br>
如修改後還是有連線較慢的問題，請您洽詢 TWCC 技術支援服務信箱：isupport@twcc.ai，並提供所在地 IP 與 traceroute 至個體之結果。

:::


:::spoiler Q6. 如何使用帳號密碼連線 Linux 個體？

:::info
請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fhowto-vcs-create-usr-linux-zh)操作，即可使用帳號密碼連線 Linux 個體，可預防鑰匙對遺失或檔案毀損。

:::

:::spoiler Q7. SSH 連線虛擬運算個體時，出現錯誤訊息```WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!```該如何排除？

:::info
此訊息出現的原因為儲存在 local 端電腦的認證與虛擬運算個體不同，因此只要刪除 local 端電腦的認證資訊，並在連線時重新產生，即可避免發生此問題，您可以參考以下的指令

```
$ ssh-keygen  -f  "/Your_Path/.ssh/known_hosts"  -R  "公用IP"
```

{%hackmd @docsharedstyle/note-zh %}


`Your_Path` 是您 local 端電腦的個人路徑，再次連線會出現以下訊息：

```Are you sure you want to continue connecting (yes/no)? ```

輸入```Yes```即可順利連線，並產生新的認證。

:::

:::spoiler Q8. 使用 macOS 電腦連線 Linux 個體，出現無法連線的情況？

:::info

請於入口網站進入「虛擬運算個體詳細資料」頁，點選「**連線**」按鈕，並按照視窗提供的指令設定鑰匙對存取權限、SSH 連線個體。

:::

:::spoiler Q9. 使用 Console 連線虛擬運算個體，是否有預設的密碼？

:::info

無預設密碼，使用 Console 連線 Linux 個體前需先另外建立密碼，Windows 個體則輸入您建立個體時設定的密碼即可，請參考[快速除錯與維護工具：TWCC VCS Console](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fguide-vcs-debug-tool-console-zh#Step-3-%E8%BC%B8%E5%85%A5%E9%80%A3%E7%B7%9A%E8%B3%87%E8%A8%8A%EF%BC%8C%E5%AE%8C%E6%88%90%E9%80%A3%E7%B7%9A)。

:::




## 管理個體
:::spoiler Q1. 建立虛擬運算個體失敗該怎麼處理？

:::info

請您至「**虛擬運算個體詳細資料頁面**」，游標移至狀態 **`Unsuccessful`** 上將顯示建立失敗的訊息。

請截圖此頁面 (和建立失敗訊息)，連同計畫代碼與虛擬運算個體的資訊 (ID、映像檔、硬體規格...等) 寄發 e-mail 至 isupport@twcc.ai，技術團隊將協助您處理。

:::


:::spoiler Q2. 忘記 Windows 虛擬運算個體登入密碼該怎麼處理？

:::info

在建立虛擬運算個體時，請務必妥善自行保存您的密碼，如忘記密碼您可以刪除該個體並重新建立；如須保存原個體的資料與配置，可先對該個體建立映像檔，再利用該映像檔建立新的個體，即可重設密碼。
:::

:::spoiler Q3. 遺失 Linux 虛擬運算個體的金鑰該怎麼處理？

:::info

在建立虛擬運算個體時，請務必下載並妥善自行保存您的金鑰，如果遺失金鑰您可以刪除該個體並重新建立；如須保存原個體的資料與配置，可先對該個體建立映像檔，再利用該映像檔建立新的個體，即可使用新的金鑰。
:::

:::spoiler Q4. 想了解虛擬運算個體狀態與用量計費關係？

:::info

| 個體狀態 | 個體用量計費| 
| -------- | -------- | 
| ```Starting```   | 不計費    | 
| ```Ready```      | 計費     |
| ```Stopping```   | 計費     |
| ```Shutdown```   | 計費     |
| ```Queueing```   | 不計費     |
| ```Deleting```   | 計費，刪除成功後便立即不再計費   |
| ```Stopped```    | 不計費   |
| ```Error```      | 不計費   |

如果使用情境為虛擬運算個體在```Shutdown```的情況下，重新啟動該台虛擬運算個體，```Starting```的過程中會納入用量計費。

:::

:::spoiler Q5. 虛擬運算個體在哪些狀態下不會收費？

:::info

虛擬運算個體僅在```Queueing```、```Stopped```與```Error```的狀態下不會收費，其他狀態皆會收費。

```Starting```則需是使用情境來決定是否納入用量計費，詳細解說請參考Q4。
:::

:::spoiler Q6. 建立虛擬運算個體出現錯誤訊息```440301: The request exceeded the quotas of ['floating_ip']```該如何解決？

:::info

出現此錯誤訊息的原因為浮動 IP (floating ip) 數量已經達到該計畫的上限，您可以參考以下做法：
1. 移除虛擬運算個體暫不需使用的浮動 IP (個體狀態為 `Ready` 才可移除) 後，再次選取建立。
2. 浮動 IP 在您停止或刪除個體後即釋放回資源池，無法循環使用。若您的使用情境適用固定 IP，建議您訂閱並使用靜態 IP (static IP)。
3. 若有特殊需求，請洽客服人員。
     
:::

## 資源配置與監控
:::spoiler Q1. 如何調整已建立好的虛擬運算個體規格？
:::info

如選用的規格在建立後不符使用需求，需調整至較小規格或更大規格的個體，請參考文件：[<ins>HowTo：調整虛擬運算個體規格</ins>](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fhowto-vcs-resize-instance-zh)。

:::

:::spoiler Q2. 為什麼我在建立虛擬運算個體時，母錢包與子錢包皆有額度，卻出現`計畫資源已用盡，無法創建資源`的訊息？

:::info

該訊息顯示您的 CPU 使用數量已達計畫配額之上限，建議您將不需使用或少用的個體建立成映像檔以利未來重建使用，並刪除虛擬運算個體，即可釋放出 CPU 使用額度。

:::

:::spoiler Q3. 請問要如何知道虛擬運算服務個體網路流量狀態？ 

:::info

使用者介面上有簡易呈現監控 CPU、硬碟、記憶體、網路的狀態及流量，若需要更詳細的資訊可以自行安裝程式監控。

:::

:::spoiler Q4. 請問該如何取得 GPU 資源？ 

:::info
由於虛擬運算個體之 GPU 資源詢問度踴躍，為了讓資源更能妥善利用與調度，如有 GPU 的需求請來信致 isupport@twcc.ai，將由專人與您進行聯繫。
:::

## 套件軟體
:::spoiler Q1. 虛擬運算服務是否支援 SMTP？ 

:::info

在虛擬運算個體中，使用者可以依需求安裝任何軟體或應用程式，因此您可以將虛擬運算個體作為 SMTP 伺服器來發送信件。

:::

:::spoiler Q2. 對虛擬運算個體安裝套件或進行更新，出現`E: Could not get lock /var/lib/apt/lists/lock`該如何解決？

:::info

1. 安裝套件或進行更新時，可能產生許多類似與 lock 檔案相關的錯誤訊息。請您將 lock 檔案刪除後，再次執行您的任務。
2. 建議改為使用映像檔 Ubuntu 20.04，可避免產生此問題。

:::
## 儲存與資料傳輸
:::spoiler Q1. 虛擬運算服務個體是否可直接掛載雲端物件儲存 (COS)？

:::info

可以直接掛載 COS，您在 VCS 個體擁有管理者權限，可以對 VCS 個體進行任意操作，掛載建議使用 s3fs 或是相關的套件，可參考 [<ins>s3fs-fuse</ins>](https://github.com/s3fs-fuse/s3fs-fuse)。

:::

:::spoiler Q2. 如何將虛擬運算中資料定期備份至雲端物件儲存 (COS)？ 

:::info

您可透過 TWCC-CLI 與 `crontab -e` 進行定時建立映像檔設定。
- TWCC-CLI 使用詳情請參考 [<ins>4-3. 上傳檔案至儲存體</ins>](https://man.twcc.ai/@twccdocs/twcc-cli-v05#4-3-%E4%B8%8A%E5%82%B3%E6%AA%94%E6%A1%88%E8%87%B3%E5%84%B2%E5%AD%98%E9%AB%94)。
- `crontab -e` 請參考 [<ins>crontab guru</ins>](https://crontab.guru/) 或 [<ins>crontab(5) - Linux man page</ins>](https://linux.die.net/man/5/crontab)。

:::

:::spoiler Q3. 如果把超過 100GB 的映像檔輸入虛擬運算服務個體，會有什麼影響？

:::info

系統碟的大小為 100GB，使用超過 100GB 會使整台虛擬運算個體無法開啟，但不會額外收費。

:::


:::spoiler Q4.如何將虛擬運算個體內的資料下載至本機？

:::info

請參考以下兩種下載方式：

1. 透過雲端物件儲存服務 (COS)傳入本機，此方法不僅能達到資料傳輸的目的，更可以將個體資料備份至 COS：
    - **Step 1.** [<ins>將資料備份到 COS</ins>](https://www.twcc.ai/doc?page=backup)。
    - **Step 2.** 至 TWCC 使用者網站 COS 管理介面[<ins>下載檔案</ins>](https://www.twcc.ai/doc?page=object#%E4%B8%8B%E8%BC%89%E6%AA%94%E6%A1%88)，如需要一次下載多個檔案，可搭配[<ins>第三方軟體</ins>](https://www.twcc.ai/doc?page=object#%E4%BD%BF%E7%94%A8%E7%AC%AC%E4%B8%89%E6%96%B9%E8%BB%9F%E9%AB%94%E7%AE%A1%E7%90%86%E6%AA%94%E6%A1%88)使用。

2. [<ins>使用 MobaXterm 連線虛擬運算個體</ins>](https://www.twcc.ai/doc?page=vm#%E9%80%A3%E7%B7%9A%E8%99%9B%E6%93%AC%E9%81%8B%E7%AE%97%E5%80%8B%E9%AB%94)，於頁面左側處選取 「**Sftp**」 圖示，即可檢視、上傳與下載檔案。
:::

:::spoiler Q5.如何將本機內的資料上傳至虛擬運算個體？

:::info

請參考以下兩種上傳方式：
1. 透過雲端物件儲存服務 (COS)
    - **Step 1.** 將本機檔案[<ins>上傳至雲端物件儲存服務 (COS)</ins>](https://www.twcc.ai/doc?page=object#%E4%B8%8A%E5%82%B3%E6%AA%94%E6%A1%88)
    - **Step 2.** [<ins>連線進入虛擬運算個體</ins>](https://www.twcc.ai/doc?page=vm#%E9%80%A3%E7%B7%9A%E8%99%9B%E6%93%AC%E9%81%8B%E7%AE%97%E5%80%8B%E9%AB%94)
    - **Step 3.** 透過內建之 TWCC-CLI 工具[<ins>將 COS 檔案下載到指定位置</ins>](https://man.twcc.ai/@twccdocs/twcc-cli-v05#4-%E9%9B%B2%E7%AB%AF%E7%89%A9%E4%BB%B6%E5%84%B2%E5%AD%98%E6%9C%8D%E5%8B%99COS-Cloud-Object-Storage)。
3. [<ins>使用 MobaXterm 連線虛擬運算個體</ins>](https://www.twcc.ai/doc?page=vm#%E9%80%A3%E7%B7%9A%E8%99%9B%E6%93%AC%E9%81%8B%E7%AE%97%E5%80%8B%E9%AB%94)，於頁面左側處選取 「**Sftp**」 圖示，即可檢視、上傳與下載檔案。
:::


## 網路安全

### 彈性 IP

:::spoiler Q1. 可以取回虛擬運算個體在 `Stopped` 之前所使用的公用 IP 嗎？

:::info
停止虛擬運算個體後，浮動 IP (floating IP) 將會釋放回資源池，個體啟動後，將取得新的浮動 IP。

若您的使用情境適用固定 IP，建議您訂閱並使用靜態 IP (static IP)。請參考 [<ins>彈性 IP </ins>](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fguide-vcs-eip-zh) 了解更多。

:::

:::spoiler Q2. 計畫預設可使用 IP 數量用完後，是否就無法建立虛擬運算個體？

:::info
浮動 IP 額度使用完後，您可以持續建立虛擬運算個體，但無法配置浮動 IP。若需要額外的 IP，請您訂閱靜態 IP (static IP) 使用。若有特殊需求，請洽客服人員。

請參考 [<ins>彈性 IP 訂閱政策</ins>](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fguide-vcs-eip-zh#%E5%BD%88%E6%80%A7-IP-%E8%A8%82%E9%96%B1%E6%94%BF%E7%AD%96) 了解更多。

:::

:::spoiler Q3. 請問為什麼不能訂閱靜態 IP (static IP)？

:::info
請先檢視您的使用身分，專案內僅「租戶管理員」可執行訂閱靜態 IP、停止訂閱。
若身分確認為管理員仍無法訂閱，請您聯繫客服人員處理。
:::

:::spoiler Q4. 我想將 DNS 綁定的浮動 IP 轉換為 靜態 IP，是否有轉換期的過渡方式？

:::info
若伺服器 (虛擬運算個體) 僅架設單一對外服務，您可以將預定使用的靜態 IP (static IP) 先掛載至負載平衡器，並將流量從負載平衡器轉發至後端服務伺服器。待 DNS IP 轉換完畢後，再將靜態 IP 掛載至伺服器上。
:::


### 虛擬網路

:::spoiler Q1. 虛擬運算個體建立後為何無法連線網路？ 

:::info

請檢查虛擬網路設定是否有誤；

若有啟用基礎虛擬網路防火牆，但不清楚規則是否設定正確，我們建議您先把防火牆關閉，並再次嘗試連線。

有關基礎虛擬網路防火牆的設定，請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fguide-vcs-vnf-zh)，或洽詢技術支援：[isupport@twcc.ai](isupport@twcc.ai)。

:::

:::spoiler Q2. 如何開啟虛擬運算個體非預設埠進行服務？

:::info

- Linux 個體預設開啟的埠為： 22、443
- Windows 個體預設開啟的埠為： 22、443、9833
  如需開啟額外的埠，請在安全性群組處進行設定，設定方法與步驟請參考[<ins>此文件</ins>](https://man.twcc.ai/@twccdocs/doc-vcs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fguide-vcs-sg-zh)。

:::

:::spoiler Q3. 建立虛擬網路時出現錯誤訊息 `440301: The request exceeded the quotas of ['floating_ip']` 該如何解決？

:::info

出現此錯誤訊息的原因為浮動 IP (floating IP) 數量已經達到該計畫的上限，您可以參考以下做法：
1. 移除虛擬運算個體暫不需使用的浮動 IP (個體狀態為 `Ready` 才可移除) 後，再次建立虛擬網路。
2. 若有特殊需求，請洽客服人員。

:::

:::spoiler Q4. 是否有限制網路速度？

:::info

TWCC 沒有對虛擬運算個體內的網速進行限制，如果您發現傳輸速度緩慢，建議您可以進行以下操作：
1. 使用網路測速工具 (例：[Speedtest](https://www.speedtest.net/))，並將測試結果寄發到技術支援信箱 (isupport@twcc.ai)，我們將會根據您提供的資料判斷是否速度異常。
2. 確認來源端的網速是否受到限制。

:::


### Auto Scaling

:::spoiler Q1. 如何讓 Auto scaling 擴展出的個體，符合我需求的環境？

:::info

請按照以下步驟進行：

* 建立環境映像檔
  1. 建立虛擬運算個體，部署環境與檔案，並建立個體映像檔 (或使用您現有的個體建立映像檔)
  2. 利用步驟1所建立的映像檔，再建立一虛擬運算個體
* 設定 Auto Scaling
  3. 建立 Auto Scaling
  4. 將 Auto Scaling 掛載至步驟2所建立的個體

經以上步驟設定，Auto Scaling 擴展出的個體，即會符合您所需的環境。

:::

## 個體映像檔

:::spoiler Q1. 映像檔建立的時間需要多久？

:::info

映像檔建立的時間約 10-15 分鐘。

:::

:::spoiler Q2. 如何節省映像檔建立的時間？

:::info

若建立映像檔的同時，仍有資料進行傳輸，不僅無法確保資料的完整與一致性且花費的時間較多，因此建議先將個體進行手動關機 (`$ sudo shutdown`) ，確認資料都已寫入虛擬磁碟後，再進行建立映像檔。

:::

:::spoiler Q3. 如何使虛擬運算個體進行自動建立映像檔？ 

:::info

您可透過 TWCC-CLI 與 `crontab -e` 進行定時建立映像檔設定。
- TWCC-CLI 使用詳情請參考 [<ins>3-6. 虛擬運算個體映像檔</ins>](https://man.twcc.ai/@twccdocs/twcc-cli-v05#3-6-%E8%99%9B%E6%93%AC%E9%81%8B%E7%AE%97%E5%80%8B%E9%AB%94%E5%BF%AB%E7%85%A7-TBD%E2%80%A6)。
- `crontab -e` 請參考 [<ins>crontab guru</ins>](https://crontab.guru/) 或 [<ins>crontab(5) - Linux man page</ins>](https://linux.die.net/man/5/crontab)。

:::

:::spoiler Q4. 為什麼無法將映像檔分享至另一個計畫？ 

:::info

1. 僅租戶管理員能分享映像檔至其他目標計畫，且需同時為來源與目標計畫的租戶管理員。
2. 不支援跨計畫分享含授權的映像檔 (例：含授權之 Windows Server)。

:::

:::spoiler Q5. GPU VM的映像檔使用映像檔分享後，為何無法在目標計畫中選擇GPU規格建立虛擬運算個體？

:::info

映像檔分享功能，在目的計畫中只支援建立CPU虛擬運算個體，暫不支援建立GPU擬運算個體

:::
