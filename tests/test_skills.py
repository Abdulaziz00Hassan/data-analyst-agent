import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from skills.analyze_csv.analyze import analyze_csv
from skills.plot_chart.plot import plot_chart
from skills.ask_data.ask import ask_data

DATA_PATH = r"data\aramco_stock.csv"

def test_analyze():
    result = analyze_csv(DATA_PATH)
    assert result["status"] == "success"
    assert result["analysis"]["shape"]["rows"] > 0
    assert "stock_insights" in result["analysis"]
    print("✅ analyze_csv PASSED")
    print(result["summary"])

def test_plot_line():
    result = plot_chart(DATA_PATH, "line", "Date", "Close")
    assert result["status"] == "success"
    assert os.path.exists(result["image_path"])
    print("✅ plot_chart (line) PASSED")

def test_plot_price_history():
    result = plot_chart(DATA_PATH, "price_history", "Date", "Close")
    assert result["status"] == "success"
    print("✅ plot_chart (price_history) PASSED")

def test_ask_highest():
    result = ask_data(DATA_PATH, "What is the highest price?")
    assert result["status"] == "success"
    assert "SAR" in result["answer"]
    print("✅ ask_data (highest) PASSED")
    print(result["answer"])

def test_ask_missing():
    result = ask_data(DATA_PATH, "Are there missing values?")
    assert result["status"] == "success"
    print("✅ ask_data (missing) PASSED")
    print(result["answer"])

def test_ask_best_year():
    result = ask_data(DATA_PATH, "What was the best year?")
    assert result["status"] == "success"
    print("✅ ask_data (best year) PASSED")
    print(result["answer"])

if __name__ == "__main__":
    print("=" * 50)
    print("Running Data Analyst Agent Tests")
    print("=" * 50)
    test_analyze()
    test_plot_line()
    test_plot_price_history()
    test_ask_highest()
    test_ask_missing()
    test_ask_best_year()
    print("\n✅ All tests passed!")