# TWCC FAQs

Got a question? We're here to help!

Link to our FAQ page: 
[中文](https://man.twcc.ai/@twccdocs/faq-zh) | [English](https://man.twcc.ai/@twccdocs/faq-en)

## TOC

## [平台與帳號計畫](平台與帳號計畫)
### [使用者網站.md](平台與帳號計畫/使用者網站.md)
- Q1. 為何登入後畫面空白？
- Q2. 登入密碼連續輸入錯誤會有甚麼情況？
## [網路與安全服務](網路與安全服務)
### [虛擬網路.md](網路與安全服務/虛擬網路.md)
- Q1. 我在建虛擬運算服務的時候要選填虛擬網路才能建立，但我無法去建立虛擬網路？
### [基礎虛擬防火牆.md](網路與安全服務/基礎虛擬防火牆.md)
- Q1. 為什麼防火牆裡面的規則沒有作用？
## [運算服務](運算服務)
### [容器運算服務(CCS).md](運算服務/容器運算服務(CCS).md)
- Q1. 容器的 Port 範圍是什麼？
- Q2. 如何從容器轉移至 HPC 進行訓練運算？
- Q3. 如何使用 8 張 GPU 以上的資源？
- Q4. 開發型容器 SSH 連線時顯示 Permission denied？
- Q5. 執行程式時發現 I/O 緩慢？
- Q6. 程式執行時效能不如預期？
- Q7. 程式執行時顯示 insufficient shared memory？
- Q8. 程式執行時顯示 bus error？
- Q9. 容器只能建立一次複本？
- Q10. 如何建立第二次複本？
- Q11. 如何暫停容器？
- Q12. 程式執行時發現比 local 端還慢？
- Q13. 程式執行時發生有些 library 無法載入 (Could not load dynamic library...)？
- Q14. 無法連線 Jupyter notebook 時如何處理？
- Q15. 為何切換成 root 無法存取自己的 /home 與 /work？
- Q16. 要如何分享/home與/work的資料給其他同計畫使用者？
- Q17. 為何 sudo  apt  update 產生 Unable  to  change  to  /home/wistron1/ -chdir  (13:  Permission  denied)？
### [虛擬運算服務(VCS).md](運算服務/虛擬運算服務(VCS).md)
- Q1. 虛擬運算的浮動 IP 範圍？
- Q2. 如何使虛擬運算個體進行自動快照？
- Q3. 如何將虛擬運算中資料定期備份至雲端物件儲存 (COS)？
- Q4. 虛擬運算服務是否支援 SMTP？
- Q5. 虛擬運算服務個體是否可直接掛載雲端物件儲存 (COS)？
- Q6. 請問我要如何知道我們開的虛擬運算服務個體網路流量狀態？
- Q7. 虛擬運算個體建立後為何無法連線網路？
- Q8. 如果把超過 100GB 的映像檔輸入虛擬運算服務個體，會有什麼影響？
- Q9. 對虛擬運算個體安裝套件或進行更新，出現`E: Could not get lock /var/lib/apt/lists/lock`該如何解決？
- Q10. 請問虛擬運算個體是否支援 WSL？
- Q11. 欲使用虛擬運算個體架設服務，卻無法連入？
- Q12. 請問快照建立的時間需要多久？
- Q13. 請問如何節省快照製作的時間？
- Q14. 請問建立虛擬運算個體失敗該怎麼處理？
### [台灣杉二號(命令列介面)(TWNIA2).md](運算服務/台灣杉二號(命令列介面)(TWNIA2).md)
- Q1. 是否可以在台灣衫二號上安裝 Rclone 軟體同步工具？
## [儲存服務](儲存服務)
### [區塊儲存服務(BSS).md](儲存服務/區塊儲存服務(BSS).md)
- Q1. 為何之前保留的 SSD 無法成功掛載到新的虛擬運算服務個體上？
### [高速儲存服務(HFS).md](儲存服務/高速儲存服務(HFS).md)
- Q1. HFS 空間已滿，將部分資料刪除，為何容量還是一樣沒變化？
- Q2. 我使用 SFTP 的方式連入 xdata1.twcc.ai 資料傳輸節點，為何無法登入？
- Q3. 如何將檔案上傳到 HFS?
- Q4. 如何增購 HFS 空間？
### [雲端物件儲存服務(COS).md](儲存服務/雲端物件儲存服務(COS).md)
- Q1. 請問在舊計畫的雲端物件儲存資料，可以直接沿用到新計畫內嗎？
- Q2. 為什麼我在 TWCC 網頁下載檔案失敗了？
## [TWCC CLI](TWCC CLI)
### [部屬環境.md](TWCC CLI/部屬環境.md)
- Q1. 請問 TWCC-CLI 怎麼安裝？
