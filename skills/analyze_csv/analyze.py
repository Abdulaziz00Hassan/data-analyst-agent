import pandas as pd
import json
import sys
from pathlib import Path

def analyze_csv(file_path: str, columns: list = None) -> dict:
    """
    Analyzes a CSV file and returns comprehensive statistics.
    
    Args:
        file_path: Path to CSV file
        columns: Optional list of specific columns to analyze
    
    Returns:
        Dictionary containing analysis results
    """
    try:
        # قراءة البيانات
        df = pd.read_csv(file_path)
        
        # تحديد الأعمدة المطلوبة
        if columns:
            df = df[columns]
        
        # =================== التحليل الأساسي ===================
        analysis = {
            "file": Path(file_path).name,
            "shape": {
                "rows": int(df.shape[0]),
                "columns": int(df.shape[1])
            },
            "columns": list(df.columns),
            "dtypes": df.dtypes.astype(str).to_dict(),
            "missing_values": {
                col: int(df[col].isna().sum()) 
                for col in df.columns 
                if df[col].isna().sum() > 0
            },
            "missing_percentage": {
                col: round(df[col].isna().sum() / len(df) * 100, 2)
                for col in df.columns
                if df[col].isna().sum() > 0
            }
        }
        
        # =================== الإحصائيات العددية ===================
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        
        if len(numeric_cols) > 0:
            stats = df[numeric_cols].describe()
            analysis["statistics"] = {
                col: {
                    "min": round(float(stats[col]["min"]), 4),
                    "max": round(float(stats[col]["max"]), 4),
                    "mean": round(float(stats[col]["mean"]), 4),
                    "std": round(float(stats[col]["std"]), 4),
                    "median": round(float(df[col].median()), 4)
                }
                for col in numeric_cols
            }
        
        # =================== تحليل خاص بـ Aramco ===================
        if "Close" in df.columns and "Volume" in df.columns:
            df_clean = df.dropna(subset=["Close"])
            
            analysis["stock_insights"] = {
                "price_range": {
                    "lowest": round(float(df_clean["Close"].min()), 2),
                    "highest": round(float(df_clean["Close"].max()), 2),
                    "current": round(float(df_clean["Close"].iloc[-1]), 2)
                },
                "daily_return": {
                    "avg": round(float(df_clean["Close"].pct_change().mean() * 100), 4),
                    "std": round(float(df_clean["Close"].pct_change().std() * 100), 4),
                    "best_day": round(float(df_clean["Close"].pct_change().max() * 100), 2),
                    "worst_day": round(float(df_clean["Close"].pct_change().min() * 100), 2)
                },
                "total_trading_days": int(len(df_clean)),
                "avg_daily_volume": int(df_clean["Volume"].mean())
            }
        
        # =================== أول 3 صفوف كعينة ===================
        analysis["sample_data"] = df.head(3).to_dict(orient="records")
        
        return {
            "status": "success",
            "analysis": analysis,
            "summary": generate_summary(analysis)
        }
        
    except FileNotFoundError:
        return {"status": "error", "message": f"File not found: {file_path}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def generate_summary(analysis: dict) -> str:
    """Generates a human-readable summary in Arabic and English."""
    shape = analysis["shape"]
    missing = len(analysis.get("missing_values", {}))
    
    summary = f"""📊 **Dataset Overview**
- Rows: {shape['rows']:,} | Columns: {shape['columns']}
- Missing values in: {missing} column(s)
"""
    
    if "stock_insights" in analysis:
        insights = analysis["stock_insights"]
        price = insights["price_range"]
        returns = insights["daily_return"]
        summary += f"""
📈 **Stock Analysis (Aramco)**
- Price Range: {price['lowest']} — {price['highest']} SAR
- Latest Close: {price['current']} SAR
- Avg Daily Return: {returns['avg']}%
- Best Single Day: +{returns['best_day']}%
- Worst Single Day: {returns['worst_day']}%
- Trading Days Analyzed: {insights['total_trading_days']:,}
"""
    
    return summary


if __name__ == "__main__":
    # للاختبار المباشر من terminal
    result = analyze_csv("data/aramco_stock.csv")
    print(json.dumps(result, indent=2, ensure_ascii=False))