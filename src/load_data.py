"""Big Five 資料載入與清理模組。

提供 `load_clean_data()`：讀入 Open Psychometrics Big Five 原始檔，
過濾不合理的年齡與未填性別後回傳乾淨的 DataFrame。
"""
from pathlib import Path

import pandas as pd

# 作業規格指定的年齡範圍（13–80 歲）
AGE_MIN, AGE_MAX = 13, 80


def load_clean_data(path: str) -> pd.DataFrame:
    """載入 Big Five 資料並做基本清理。

    Parameters
    ----------
    path : str
        資料檔路徑（例如 ``data/raw/BIG5/data.csv``）。

    Returns
    -------
    pd.DataFrame
        經過下列步驟清理後的 DataFrame：

        1. 以 tab 分隔讀取（含 utf-8 → latin-1 編碼 fallback）
        2. 篩選 13 ≤ age ≤ 80
        3. 排除 gender == 0（未填答者）

    Raises
    ------
    ValueError
        若讀入後僅有單一欄位，表示分隔符可能不是 tab。
    """
    csv_path = Path(path)

    # utf-8 是首選；Open Psychometrics 偶爾出現 latin-1 字元，留 fallback 防呆
    try:
        df = pd.read_csv(csv_path, sep="\t", encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(csv_path, sep="\t", encoding="latin-1")

    # 若 sep 猜錯，所有資料會塞進一欄，需主動偵測避免下游靜默失敗
    if df.shape[1] == 1:
        raise ValueError(
            f"只讀到 1 欄（{df.columns.tolist()}），分隔符可能不是 tab。"
        )

    raw_n = len(df)

    # 同時套用年齡與性別兩個條件，較依序 mask 易讀
    mask = df["age"].between(AGE_MIN, AGE_MAX) & (df["gender"] != 0)
    cleaned = df.loc[mask].copy()
    clean_n = len(cleaned)
    dropped = raw_n - clean_n

    print(f"原始 n     : {raw_n:,}")
    print(f"清理後 n   : {clean_n:,}")
    print(f"流失       : {dropped:,} 筆（{dropped / raw_n:.2%}）")
    print(f"  └ age 不在 {AGE_MIN}–{AGE_MAX} : {(~df['age'].between(AGE_MIN, AGE_MAX)).sum():,}")
    print(f"  └ gender == 0          : {(df['gender'] == 0).sum():,}")

    return cleaned


if __name__ == "__main__":
    # 直接執行模組可快速檢查資料：python -m src.load_data
    df = load_clean_data("data/raw/BIG5/data.csv")
    print("\n前 3 筆：")
    print(df.head(3))
