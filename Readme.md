# 🧬 Human Longevity Index (HLI)

> **“Where you live shouldn't decide how long you live.”**

The **Human Longevity Index** is a public-data-driven project that explores **what truly drives long life** across 150+ countries.

Using the **World Bank API**, this project analyzes real-time global health and development indicators to generate custom **longevity scores**, highlight inequalities, and build actionable insights.

---

## 🌍 Problem Statement

Why do some countries live longer than others?

We explore this using real-world data — from **clean air** and **healthcare** to **education**, **nutrition**, and **sanitation** — to understand the drivers of **human longevity** globally.

This project is a step toward turning open data into **policy-ready insights** that can inform change.

---

## 🎯 Project Goals

- ✅ Build a **global Human Longevity Index** (HLI) using real-time API data
- 📊 Create a **Longevity Impact Score (LIS)** per country
- ⚠️ Identify vulnerable regions with a **Policy Risk Index (PRI)**
- 📈 Build an interactive dashboard to visualize and explore longevity drivers
- 🔁 Automate the pipeline for continuous updates

---

## 🧪 Tech Stack

| Area          | Tools Used                                                 |
| ------------- | ---------------------------------------------------------- |
| Programming   | Python 3.11                                                |
| Data Source   | World Bank API (Health & Development Indicators)           |
| Libraries     | pandas, requests, matplotlib, seaborn, plotly              |
| Visualization | Streamlit (dashboard), geopandas (maps)                    |
| API Handling  | REST-based API queries (World Bank)                        |
| Analytics     | Correlation analysis, KPI design, scoring systems          |
| Automation    | Scheduled refresh scripts (optional: cron/Streamlit Cloud) |

---

## 📌 Key Features

- 🔄 Real-time API data pull from 150+ countries
- 💡 Custom KPIs to quantify impact of various development indicators on life expectancy
- 🌍 Streamlit dashboard to explore, filter, and compare countries
- 🧠 Insightful visualizations: maps, rankings, time trends, correlation heatmaps
- 🔁 Fully automated pipeline for repeatable analysis

---

## 📈 Unique KPIs Designed

| KPI Name                         | Description                                                                 |
| -------------------------------- | --------------------------------------------------------------------------- |
| **Longevity Impact Score (LIS)** | Weighted score combining factors like sanitation, education, GDP, pollution |
| **Policy Risk Index (PRI)**      | Flags countries with declining life expectancy or volatility in health data |
| **Health Inequality Gap %**      | Measures longevity disparity between top and bottom deciles                 |
| **Clean Life Years (CLY)**       | Adjusted life expectancy factoring in air & water quality                   |
| **Income vs Health ROI**         | Correlation between income growth and health outcome improvement            |

---

## 🗂️ Project Structure

📦human-longevity-index/
┣ 📁 data/ # Cached or downloaded data
┣ 📁 notebooks/ # Exploratory and development notebooks
┣ 📁 scripts/ # API pull, KPI calculation, plots
┣ 📁 dashboard/ # Streamlit app for visualization
┣ 📄 requirements.txt # Dependencies
┣ 📄 README.md # Project overview
┗ 📄 LICENSE
