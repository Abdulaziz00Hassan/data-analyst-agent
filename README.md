# 📊 Data Analyst Agent — OpenClaw

An AI agent that analyzes Saudi Aramco (2222.SR) stock data via Telegram.
Built with OpenClaw + Python (pandas, matplotlib).

## Demo

![analyze](demo/demo1.png)
![plot](demo/demo2.png)
![ask](demo/demo3.png)

## Commands

| Command | What it does |
|---------|-------------|
| `plot aramco` | Sends price history chart as image |
| `analyze aramco` | Returns full statistical summary |
| `ask [question]` | Answers questions about the data |

## Stack

- OpenClaw — AI agent framework
- Python + pandas + matplotlib
- Telegram Bot API
- Dataset: Saudi Aramco (2222.SR) 2019–2024

<<<<<<< HEAD
- **Python** (pandas, matplotlib) — data analysis & visualization
- **Node.js + Telegraf** — Telegram bot framework
- OpenClaw — AI agent framework
- Google Gemini API — LLM backend
- **Dataset**: Saudi Aramco (2222.SR) 2019–2024 stock data

## 📁 Project Structure

```
data-analyst-agent/
├── skills/
│   ├── analyze_csv/     ← dataset analysis skill
│   ├── plot_chart/      ← chart generation skill
│   └── ask_data/        ← natural language Q&A skill
├── scripts/
│   ├── telegram_bot.js  ← Telegram bot entry point
│   └── run_skill.py     ← Python skills runner
├── data/
│   └── aramco_stock.csv
├── tests/
│   └── test_skills.py
├── requirements.txt
└── README.md
```

## ⚡ Quick Start
=======
## Setup
>>>>>>> 167ec92 (feat: Data Analyst Agent - OpenClaw skill with plot, analyze, and ask commands for Saudi Aramco stock data)

```bash
git clone https://github.com/Abdulaziz00Hassan/data-analyst-agent 
pip install -r requirements.txt
<<<<<<< HEAD

# 3. Node.js setup
npm install

# 4. Environment
cp .env.example .env
# Edit .env: Add TELEGRAM_TOKEN and GOOGLE_API_KEY

# 5. Run
node scripts/telegram_bot.js
```

## 📊 Sample Output

**`/analyze` response:**
```
📊 Dataset Overview
• Rows: 1,164 | Columns: 7
• Missing values in: 0 column(s)

📈 Stock Analysis (Aramco)
• Price Range: 22.98 — 38.64 SAR
• Latest Close: 28.15 SAR
• Avg Daily Return: 0.0034%
• Best Single Day: +9.88%
• Worst Single Day: -9.09%
```

## 🧪 Tests

```bash
python tests/test_skills.py
```

## Built by

Abdulaziz Ali Hassan — Data Analyst & AI Developer
[LinkedIn](https://linkedin.com/in/abdulaziz-ali-data-analyst-py88) | [GitHub](https://github.com/Abdulaziz00Hassan)
```
=======
# Add your data CSV to /data/aramco_stock.csv
# Configure OpenClaw with your Telegram bot token
>>>>>>> 167ec92 (feat: Data Analyst Agent - OpenClaw skill with plot, analyze, and ask commands for Saudi Aramco stock data)
