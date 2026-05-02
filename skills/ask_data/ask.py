import pandas as pd
import json
import re

def ask_data(file_path: str, question: str) -> dict:
    """
    Answers natural language questions about the data.
    
    Examples:
    - "What is the highest price?"
    - "How many missing values?"
    - "What is the average volume in 2022?"
    - "Which year had the best returns?"
    """
    try:
        df = pd.read_csv(file_path)
        
        # تحويل التاريخ
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"])
            df["Year"] = df["Date"].dt.year
        
        question_lower = question.lower()
        
        # =================== قاعدة الأسئلة ===================
        
        # أسئلة السعر الأعلى
        if any(w in question_lower for w in ["highest", "maximum", "max", "أعلى", "أكبر"]):
            if "close" in question_lower or "price" in question_lower or "سعر" in question_lower:
                max_row = df.loc[df["Close"].idxmax()]
                return {
                    "status": "success",
                    "answer": f"Highest closing price: **{max_row['Close']:.2f} SAR** on {max_row['Date'].strftime('%B %d, %Y')}",
                    "value": float(max_row["Close"]),
                    "date": str(max_row["Date"].date())
                }
        
        # أسئلة السعر الأدنى
        if any(w in question_lower for w in ["lowest", "minimum", "min", "أدنى", "أقل"]):
            if "close" in question_lower or "price" in question_lower:
                min_row = df.loc[df["Close"].idxmin()]
                return {
                    "status": "success",
                    "answer": f"Lowest closing price: **{min_row['Close']:.2f} SAR** on {min_row['Date'].strftime('%B %d, %Y')}",
                    "value": float(min_row["Close"]),
                    "date": str(min_row["Date"].date())
                }
        
        # أسئلة المعدل
        if any(w in question_lower for w in ["average", "mean", "avg", "معدل", "متوسط"]):
            col = "Close" if "price" in question_lower else "Volume"
            
            # هل يسأل عن سنة معينة؟
            year_match = re.search(r'\b(201[9]|202[0-4])\b', question)
            if year_match and "Year" in df.columns:
                year = int(year_match.group())
                df_year = df[df["Year"] == year]
                avg = df_year[col].mean()
                return {
                    "status": "success",
                    "answer": f"Average {col} in {year}: **{avg:.2f}**",
                    "value": round(float(avg), 2)
                }
            else:
                avg = df[col].mean()
                return {
                    "status": "success",
                    "answer": f"Average {col} (all time): **{avg:.2f}**",
                    "value": round(float(avg), 2)
                }
        
        # أسئلة المفقودة
        if any(w in question_lower for w in ["missing", "null", "nan", "مفقود", "ناقص"]):
            missing = df.isnull().sum()
            missing_cols = missing[missing > 0]
            if len(missing_cols) == 0:
                return {"status": "success", "answer": "✅ No missing values found in the dataset."}
            else:
                details = "\n".join([f"• {col}: {count} missing" for col, count in missing_cols.items()])
                return {"status": "success", "answer": f"Found missing values:\n{details}"}
        
        # أفضل سنة
        if any(w in question_lower for w in ["best year", "أفضل سنة", "best return"]):
            if "Year" in df.columns:
                yearly = df.groupby("Year")["Close"].agg(["first", "last"])
                yearly["return"] = (yearly["last"] - yearly["first"]) / yearly["first"] * 100
                best_year = yearly["return"].idxmax()
                best_return = yearly["return"].max()
                return {
                    "status": "success",
                    "answer": f"Best year for Aramco: **{best_year}** with +{best_return:.1f}% return"
                }
        
        # إذا لم يتعرف على السؤال
        return {
            "status": "unclear",
            "answer": "I understood your question but couldn't map it to a specific analysis. Try asking about: highest/lowest price, average price/volume, missing values, or best year.",
            "suggestion": "Example: 'What is the highest price?' or 'What was the average volume in 2022?'"
        }
        
    except Exception as e:
        return {"status": "error", "message": str(e)}