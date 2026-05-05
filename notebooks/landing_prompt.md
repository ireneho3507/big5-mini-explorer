# docs/index.html 生成 Prompt

本檔記錄產生 GitHub Pages 落地頁（`docs/index.html`）所使用的 prompt 與設計規格。
頁面由 Claude（Opus 4.7）依此規格生成，並由作者人工審閱後 commit。

---

## 設計需求

- **語言**：繁體中文。
- **配色**：白底、灰階為主，搭配一個藍色強調色（`#4C72B0`，與 matplotlib 圖表色一致）。**禁止黑底**。
- **排版**：單欄、置中、最大寬度約 720px；行距寬鬆、留白足夠。
- **字體**：系統 sans-serif，body ≥ 17px；標題依層級加大。
- **圖像**：兩張圖以 `<figure>` + `<figcaption>` 嵌入，路徑相對於 `docs/`；`max-width: 100%` 防止溢出。
- **語意 HTML**：使用 `<main>`、`<header>`、`<section>`、`<footer>`、`<figure>` 等語意標籤。
- **可攜性**：純單檔 HTML + 內嵌 CSS，不依賴外部 framework / CDN。

---

## 七個必要區塊（依此順序）

| # | 區塊 | 內容要點 |
|---|---|---|
| 1 | **Title + Tagline** | 標題與 README 一致；tagline 一句話說明專案 |
| 2 | **Goal** | 1–3 句研究問題（性別差異、年齡梯度） |
| 3 | **Procedure** | 4–6 條散文式步驟，**不放程式碼** |
| 4 | **Outcome** | 嵌入 `figure1_descriptive.png` 與 `figure2_relational.png`，各配 1–2 句結論 |
| 5 | **Caveats** | 至少 2 點誠實侷限（取樣、自陳、橫斷推論等） |
| 6 | **Repository** | 連回 GitHub repo |
| 7 | **Author + Date** | 姓名、學號、日期 |

---

## 用過的 Prompt（節錄）

> 請以上述規格產出 `docs/index.html`。內容要呼應 `README.md` 的 Motivation、Procedure 與 Caveats，但用適合落地頁的散文寫法（README 是說明文件，landing page 是「展示」），不要直接 copy README。
>
> Procedure 部分請寫 5 條，分別對應：(1) 資料下載與來源、(2) 清理與過濾、(3) 反向計分與五因子平均、(4) Figure 1 設計、(5) Figure 2 設計。
>
> Caveats 至少寫 3 點：(a) 自選樣本不具人口代表性、(b) 自陳量表的方法侷限、(c) 橫斷資料無法排除世代效應。
