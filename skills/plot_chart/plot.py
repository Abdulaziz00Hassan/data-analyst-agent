import pandas as pd
import matplotlib
matplotlib.use('Agg')  # مهم: بدون GUI
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
import sys
import os
from pathlib import Path
from datetime import datetime

def plot_chart(
    file_path: str,
    chart_type: str = "line",
    x_column: str = "Date",
    y_column: str = "Close",
    title: str = None
) -> dict:
    """
    Generates a chart from CSV data.
    
    Returns:
        dict with image_path and description
    """
    try:
        df = pd.read_csv(file_path)
        
        # تحويل تاريخ تلقائياً
        if x_column in df.columns:
            try:
                df[x_column] = pd.to_datetime(df[x_column])
            except:
                pass
        
        # إنشاء اسم ملف الصورة
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path("output/charts")
        output_dir.mkdir(parents=True, exist_ok=True)
        image_path = str(output_dir / f"chart_{chart_type}_{timestamp}.png")
        
        # =================== رسم حسب النوع ===================
        
        if chart_type == "line":
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(df[x_column], df[y_column], 
                   linewidth=1.5, color='#2196F3', alpha=0.9)
            ax.fill_between(df[x_column], df[y_column], 
                           alpha=0.1, color='#2196F3')
            
        elif chart_type == "bar":
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.bar(df[x_column], df[y_column], 
                  color='#4CAF50', alpha=0.8, edgecolor='white')
            
        elif chart_type == "histogram":
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.hist(df[y_column].dropna(), bins=50, 
                   color='#9C27B0', alpha=0.8, edgecolor='white')
            ax.set_xlabel(y_column)
            ax.set_ylabel("Frequency")
            
        elif chart_type == "price_history":
            # خاص بـ Aramco — يرسم السعر + حجم التداول معاً
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), 
                                            gridspec_kw={'height_ratios': [3, 1]})
            
            # السعر
            ax1.plot(df[x_column], df["Close"], 
                    linewidth=1.5, color='#2196F3', label='Close Price')
            ax1.fill_between(df[x_column], df["Close"], 
                            alpha=0.1, color='#2196F3')
            ax1.set_ylabel("Price (SAR)", fontsize=11)
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            
            # حجم التداول
            if "Volume" in df.columns:
                ax2.bar(df[x_column], df["Volume"], 
                       color='#FF9800', alpha=0.7, width=1)
                ax2.set_ylabel("Volume", fontsize=9)
                ax2.grid(True, alpha=0.3)
            
            plt.tight_layout()
            chart_title = title or "Saudi Aramco (2222.SR) — Price & Volume History"
        
        # =================== التنسيق العام ===================
        if chart_type != "price_history":
            ax.set_xlabel(x_column, fontsize=11)
            ax.set_ylabel(y_column, fontsize=11)
            ax.grid(True, alpha=0.3)
            plt.tight_layout()
        
        # العنوان
        if title:
            plt.suptitle(title, fontsize=14, fontweight='bold', y=1.02)
        elif chart_type != "price_history":
            plt.title(f"{y_column} over {x_column}", fontsize=13, pad=15)
        
        # تنسيق تواريخ المحور السيني
        if hasattr(ax if chart_type != "price_history" else ax1, 'xaxis'):
            target_ax = ax if chart_type != "price_history" else ax1
            if hasattr(df[x_column].iloc[0], 'year'):
                target_ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
                plt.setp(target_ax.xaxis.get_majorticklabels(), rotation=45)
        
        # حفظ الصورة
        plt.savefig(image_path, dpi=150, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        plt.close('all')
        
        return {
            "status": "success",
            "image_path": image_path,
            "chart_type": chart_type,
            "description": f"Chart saved: {Path(image_path).name}"
        }
        
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    # اختبار مباشر
    result = plot_chart(
        "../../data/aramco_stock.csv",
        chart_type="price_history",
        x_column="Date",
        y_column="Close"
    )
    print(json.dumps(result, indent=2))