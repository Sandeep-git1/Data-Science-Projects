# Panic Attack Analysis Dashboard

Welcome to the **Panic Attack Analysis Dashboard** — a data-driven exploration into the patterns, symptoms, triggers, and lifestyle factors associated with panic attacks. Built with **Power BI** and fueled by data from over **1,200 anonymized patient records**, this project aims to transform raw mental health data into actionable insights.

Whether you're a **researcher**, **healthcare professional**, or simply curious about **mental health analytics**, this interactive dashboard helps make sense of the chaos that panic attacks can bring.

---

## About Panic Attacks

- Panic attacks are **sudden, intense episodes of fear or anxiety**.
- Common symptoms: **rapid heart rate**, **difficulty breathing**, **dizziness**, **sweating**, **chest pain**, and **trembling**.
- They can strike **without warning** or **obvious cause**.
- Recurring attacks may lead to **panic disorder** — a persistent fear of future episodes.

---

## Dashboard Overview

- **Developed in Power BI** with live connection to a **Snowflake data warehouse**.
- Source data: `panic_attack_dataset.csv` containing 1,200+ anonymized entries.
- Real-time filters: **Gender**, **Smoking Status**, **Medical History**, **Panic Attack Type**, and more.
- Interactive charts include:
  - **Pie charts** for trigger distribution.
  - **Bar graphs** for sleep patterns and exercise.
  - **Trend lines** for panic frequency and severity.
  - **Symptom heatmaps** for visual correlation.

---

## Dataset Summary

Key columns include: ID, Age, Gender, Panic_Attack_Frequency, Duration_Minutes, Trigger,
Heart_Rate, Sweating, Shortness_of_Breath, Dizziness, Chest_Pain,
Trembling, Medical_History, Medication, Caffeine_Intake,
Exercise_Frequency, Sleep_Hours, Alcohol_Consumption,
Smoking, Therapy, Panic_Score

---

## Data Pipeline & Transformations

### ETL Process
- Raw CSV cleaned and uploaded to **Snowflake**.
- Null handling, duplicate removal, and data validation applied for scalability and governance.

### Key Transformations

- **Panic Attack Categorization**  
  Added a calculated column `Panic_Attack(HML)` based on frequency:
  - **High**: 7–9 attacks
  - **Medium**: 4–6 attacks
  - **Low**: 0–3 attacks

- **Heart Rate Correction**  
  A device glitch inflated values by +1. Fixed using a DAX measure: Corrected_Heart_Rate = [Heart_Rate] - 1 
Resulting average heart rate during attacks: **120–140 bpm**.

---

## Key Findings & Insights

### Prevalent Symptoms
- **Dizziness** (52%)
- **Trembling** (48%)
- **Chest Pain** (40%)
- **Shortness of Breath** (38%)
- **Sweating** (30%)

> Dizziness and shortness of breath often co-occur in **PTSD** cases.

### Top Triggers (by frequency)
- **Unknown**, **Caffeine**, **Phobia** (~17% each)
- **PTSD** (17%)
- **Social Anxiety**, **Stress** (16% each)

### Demographics & Habits
- **Females** report **higher attack frequencies**.
- **Smokers** show **50% more sweating** during attacks.
- Common medical conditions:
- **Anxiety (45%)**
- **PTSD (30%)**
- **Depression (20%)**

> Therapy users show a **15% lower severity score** on average.

### Lifestyle Links
- <6 hours of sleep → **20% higher attack frequency**
- Gaps in **caffeine management** or **exercise** correlate with **higher panic risk**

---

## Actionable Insights

- Patients with **high-frequency attacks (7+)** are: **3x more likely** to have PTSD
- Reducing caffeine and improving sleep can lower panic triggers by **25–30%**

---

## Technologies Used

- **Power BI** – Interactive dashboards and data visualizations
- **Snowflake** – Scalable data warehousing
- **DAX** – Calculated columns and custom measures
- **CSV** – Raw data format

---



