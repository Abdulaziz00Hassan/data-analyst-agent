```markdown
# 📊 Data Analyst Agent — Saudi Aramco Stock Analysis

> AI-powered Telegram bot that analyzes Saudi Aramco (2222.SR) stock data, generates charts, and answers natural language questions.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Node.js](https://img.shields.io/badge/Node.js-20-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🔍 What It Does

Send a message to Telegram → Agent analyzes Aramco stock data → Returns insights + charts instantly.

**Commands:**
| Command | Description |
|---------|-------------|
| `/analyze` | Full dataset summary (shape, stats, insights) |
| `/plot` | Price history + volume chart |
| `/ask [question]` | Natural language question answering |

**Example Questions:**
- `/ask what is the highest price?`
- `/ask what was the average volume in 2022?`
- `/ask which year had the best return?`

## 🛠 Tech Stack

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

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/data-analyst-agent.git
cd data-analyst-agent

# 2. Python setup
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

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
