# TWCC FAQs | OneAI 


## 訂閱收費

:::spoiler Q1. 使用 OneAI 會產生哪些費用，以及如何收費？
:::info
使用 OneAI 服務將會產生訂閱費用，以及用於使用標註工具、託管筆記本、訓練模型、執行推論、資料儲存和資料處理資源相關費用。請參閱 OneAI 定價頁了解詳細資訊：

<a href="https://man.twcc.ai/@twsdocs/pricing-zh#%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%EF%BC%9AOneAI"><b><font style="background-color:#008ad8;border-radius: 30px;padding: 0.3em; font-size: 16px;"><font style="color:white;"> &nbsp;Enterprise&nbsp;</font></font></b></a> <a href="https://man.twcc.ai/@twccdocs/SJWlN3YDr#%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7"><font style="background-color:#FF0000;border-radius: 30px;padding: 0.3em; font-size: 16px;"><font style="color:white;"> <b>&nbsp;Academic&nbsp;</b></font></font></a> 

:::


:::spoiler Q2. OneAI 為何無法訂閱？
:::info
1. 專案限制：若專案該月到期，或是專案可用額度小於100，將無法訂閱。
2. 身分限制：需租戶管理員才能進行訂閱，租戶使用者將無法訂閱。

請參閱 [<ins>OneAI訂閱政策</ins>](https://man.twcc.ai/@twccdocs/doc-oneai-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Foneai-subscription-policy-zh) 了解詳細資訊。
:::


:::spoiler Q3. 如何查看 OneAI 服務的分項費用？
:::info
您可以在會員中心查看 OneAI 的分項費用。從會員中心選擇欲查看的專案，在上方選單選擇「額度用量」，從下拉式清單選取「OneAI」，即可根據商品項目可逐一查看分項費用：


<font style="background-color:#008ad8;border-radius: 30px;padding: 0.3em; font-size: 16px;"><font style="color:white;"> **&nbsp;Enterprise&nbsp;**</font></font>


![](https://i.imgur.com/dsFrIcC.png)

<font style="background-color:#FF0000;border-radius: 16px;padding: 0.3em; font-size: 16px;"><font style="color:white;"> **&nbsp;Academic&nbsp;**</font></font> 與 Enterprise 步驟雷同，選擇「OneAI」前，需先選擇服務「TWCC」。

:::


## 服務功能

:::spoiler Q1. 什麼是筆記本服務？
:::info
OneAI筆記本服務整合了主流的深度學習框架（TensorFlow、PyTorch、 MXNet）與套件以及支援資料科學語言（Julia、R）與數據分析引擎（Spark）的預置映像檔，是一個彈性、受管的 JupyterLab 互動式協作開發環境。請參閱 [<ins>OneAI筆記本服務</ins>](https://docs.oneai.twcc.ai/s/Z8LdmjL9M#%E7%AD%86%E8%A8%98%E6%9C%AC%E6%9C%8D%E5%8B%99) 了解更多內容。

:::

:::spoiler Q2. OneAI AI Maker 已預先建置哪些解決方案？
:::info
OneAI AI Maker 提供 8 種公用範本可應用在物件偵測、圖像分類、醫學影像、分類問題、回歸問題、行人屬性辨識等領域：YOLOv3、YOLOv4、Nvidia Clara Train 3.0、Nvidia Clara Train 4.0、Scikit-learn: regression、Scikit-learn: classification、Image-classification、PAR。可參閱 [<ins>案例教學</ins>](https://docs.oneai.twcc.ai/s/xKNcU3O5D#%E6%A1%88%E4%BE%8B%E6%95%99%E5%AD%B8) 了解詳細資訊。
:::

:::spoiler Q3. OneAI AI Maker 與 AI Maker (搶鮮版) 有何不同？
:::info
AI Maker (搶鮮版) 功能增加了 整合 MLflow 去管理模型訓練的細節。
1. [<ins>AI Maker (搶鮮版) > MLflow 模型</ins>](https://docs.oneai.twcc.ai/s/3uxGFglX0#%E6%A8%A1%E5%9E%8B%E7%AE%A1%E7%90%86) 可管理模型生命週期。
2. AI Maker (搶鮮版) > 訓練任務中內建的範本訓練模型時，會自動套用 MLflow 來提供更詳盡的 AI/ML 研究過程；使用自定義訓練程式碼需在程式碼中手動配置 [MLflow Logging Function <i class="fa fa-external-link" aria-hidden="true"></i>](https://mlflow.org/docs/latest/tracking.html#logging-functions) ，則可通過 OneAI 的使用者介面統一管理模型。

請參閱 [<ins>OneAI AI Maker (搶鮮版)</ins>](https://docs.oneai.twcc.ai/s/3uxGFglX0#AI-Maker%EF%BC%88%E6%90%B6%E9%AE%AE%E7%89%88%EF%BC%89) 了解詳細資訊。
:::

:::spoiler Q4. 是否可讓非專案成員進行標註作業？
:::info
可透過 [<ins>CVAT 標註工具</ins>](https://docs.oneai.twcc.ai/s/QFn7N5R-H#%E6%A8%99%E8%A8%BB%E5%B7%A5%E5%85%B7) 派發標註作業給非專案成員使用。您須自行提供非專案成員使用：
1. CVAT 標註工具進入點網址如下圖示意：
![](https://i.imgur.com/f2cEHEV.png)
2. CVAT 標註工具的帳號密碼設定方式請參閱 [<ins>操作指南</ins>](https://hackmd.io/@6Na-9uAFTYa8-bo874eWrA/S1mZuWyc5) 以了解相關設定。
:::


## 容器使用

:::spoiler Q1. OneAI 容器服務 port 範圍？
:::info
OneAI 容器服務 提供 Static Port 的範圍 30000-32767。請參閱 [<ins>OneAI容器服務 > 網路設定</ins>](https://docs.oneai.twcc.ai/s/yGbG4JJyi#3-%E7%B6%B2%E8%B7%AF%E8%A8%AD%E5%AE%9A) 了解更多內容。

:::

:::spoiler Q2. OneAI 容器映像檔該如何產生？
:::info
準備好您的容器映像檔即可使用 Docker CLI 來 push 容器映像檔至 OneAI容器映像檔。Docker CLI 詳細資訊至 [Docker官方文件 <i class="fa fa-external-link" aria-hidden="true"></i>](https://docs.docker.com/get-started/#cli-references)查看。

:::

:::spoiler Q3. OneAI 容器服務是否可以使用 SSH 連線？
:::info
依據映像檔來源會限制 SSH 連線。系統內建的 nvidia-official-images 公用映像檔可用 SSH 連線。用戶自行上傳的私人映像檔則依照映像檔內容，若要使用 SSH 連線則建議須在映像檔[安裝sshd相關套件 <i class="fa fa-external-link" aria-hidden="true"></i>](https://docs.docker.com/samples/running_ssh_service/)。OneAI 容器服務 使用 SSH 連線方式請參閱 [<ins>使用手冊</ins>](https://docs.oneai.twcc.ai/s/yGbG4JJyi#%E4%BD%BF%E7%94%A8-SSH-%E7%99%BB%E5%85%A5%E9%80%A3%E7%B7%9A) 以了解操作步驟。

:::

:::spoiler Q4. 為何從本地環境上傳的容器映像檔容量會變小？
:::info
OneAI 容器映像檔會將您上傳的容器映像檔進行壓縮，導致容器映像檔的容量變小，其內容則無影響。

:::

## 資料儲存

:::spoiler Q1. OneAI 適用何種資料儲存服務 ？
:::info
OneAI 使用 [<ins>OneAI 儲存服務</ins>](https://docs.oneai.twcc.ai/s/_F4C_EzEa#%E5%84%B2%E5%AD%98%E6%9C%8D%E5%8B%99) 作為資料儲存、管理的工具，提供安全、可靠與 Amazon S3 相容之儲存服務，也支援第三方工具 (S3 browser)，使得在 OneAI 的服務之間或與其他專案成員分享資料。
:::

:::spoiler Q2. OneAI 容器服務掛載的儲存空間有多少 ？
:::info
建立容器的儲存空間以掛載 OneAI 儲存服務的儲存體的大小為主。
:::

:::spoiler Q3. OneAI 儲存服務可存放哪種資料？
:::info
可存放的資料不限格式、不限類型。
:::

:::spoiler Q4. OneAI 儲存服務存放空間和檔案數量上限是多少？
:::info
OneAI 儲存服務可以存放的總資料量和物件數量無使用上限制。
:::


## 訓練模型

:::spoiler Q1. OneAI 是否支援多 GPU 訓練？
:::info
OneAI AI Maker 公用範本可以自動在多 GPU 中分配深度學習模型和大型訓練集，自定義訓練程式碼需手動調整程式碼調用 GPU，調用方式會依深度學習框架有所不同。
:::

:::spoiler Q2. 透過 OneAI AI Maker SmartML 訓練任務 可調整哪些模型？
:::info
[<ins>SmartML 訓練任務</ins>](https://docs.oneai.twcc.ai/s/QFn7N5R-H#%E8%A8%93%E7%B7%B4%E4%BB%BB%E5%8B%99) 提供 4 種演算法：Bayesian、TPE、Grid、Random，來執行模型訓練的優化策略。若您不是使用公用範本，須在訓練程式碼中，使用 `os.environ` 來[<ins>手動配置變數設定</ins>](https://docs.oneai.twcc.ai/s/QFn7N5R-H#23-%E8%A8%AD%E5%AE%9A%E8%B6%85%E5%8F%83%E6%95%B8)，可調整超參數、模型種類等，更多資訊可參考[<ins>公用範本 image-classification 案例教學</ins>](https://docs.oneai.twcc.ai/s/6FCAc5sdI#AI-Maker-%E6%A1%88%E4%BE%8B%E6%95%99%E5%AD%B8---%E5%BD%B1%E5%83%8F%E5%88%86%E9%A1%9E%E6%A8%A1%E5%9E%8B%E6%87%89%E7%94%A8)的設定。
:::

:::spoiler Q3. OneAI AI Maker 模型可匯入哪些模型種類？
:::info
OneAI 模型可存放不限種類的模型。在匯入前，您須將模型打包成 ZIP 檔並上傳到 OneAI 儲存服務。可參閱 [<ins>AI Maker 模型</ins>](https://docs.oneai.twcc.ai/s/QFn7N5R-H#%E6%A8%A1%E5%9E%8B) 了解詳細資訊。
:::

:::spoiler Q4. 如何確認有使用到 GPU 資源？
:::info
- OneAI 筆記本服務、容器服務、推論服務 所使用到的運算資源可透過 [<ins>OneAI 資源監控</ins>](https://docs.oneai.twcc.ai/s/gEQO9lvF8) 檢視。
- OneAI 訓練任務可查詢 7 天內的運算資源情形，請洽詢客服查詢並取得監控資料。

:::
