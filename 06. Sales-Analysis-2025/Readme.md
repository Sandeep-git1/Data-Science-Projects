#Sales Analysis (2025)

## Overview

This repository contains the files and documentation for a Power BI dashboard assignment focused on analyzing sales and profit data for an electronics company in 2025.

The project involves data modeling, DAX measure creation, interactive visualization, and generating key business insights.

## Project Deliverables

| File | Description |
| :--- | :--- |
| `Tas Dashboard.pbix` | The final, interactive Power BI Desktop file. |
| `Report.docx` | A static doc of the main dashboard view. |

## Key Insights

* **Overall Profitability:** The company achieved a **9.59%** profit margin for the period.
* **Peak Performance:** Sales volume **peaked in August**, indicating potential seasonality or effective mid-year promotions.
* **Top Product:** The **Printer** was identified as the highest-grossing product by total revenue.
* **Customer Focus:** The top customer, **Customer\_53**, is critical to the revenue stream.

---
*Refer to the `Report.md` file for a complete process guide and detailed findings.*

# Comprehensive Sales and Profit Analysis Report (2025)

## Part A: Executive Summary of Insights

This report summarizes the analysis of the 2025 sales and profit data, providing actionable insights for guiding future business strategy.

### 1. Performance Summary

The analysis confirms a strong year with balanced profit performance.

| Key Metric | Value | Insight |
| :--- | :--- | :--- |
| **Total Revenue** | $5,03,29,13,420.00| High volume and high-value transactions drove the total. |
| **Total Profit** | $5,03,10,89,08,661.30 | Solid profit delivery across core product categories. |
| **Profit Margin %** | **9.59%** | Demonstrates healthy cost management relative to sales price. |

### 2. Product and Sales Trend Analysis

* **Top Revenue Driver (Task 1):** The **Printer** product generated the highest absolute revenue, significantly impacting the total profit figure.
* **Category Contribution (Task 4):** The **Computers** and **Accessories** categories are the primary segments driving revenue, with Accessories often providing steady volume and turnover.
* **Sales Trend (Task 2):** The Line Chart analysis showed sales **peaked in August**. This seasonal high point should be leveraged by timing future inventory and marketing campaigns around this period.

### 3. Customer and Geographic Focus

* **High-Value Customer (Task 3):** The customer with the highest total revenue is **Customer\_53**. Retention strategies should be focused on securing repeat business from this individual, as they are disproportionately critical to the revenue stream.
* **Geographic Strength:** The highest volume of sales activity is centered in the city of **Kolkata**.

## Part B: Power BI Dashboard Development Process

This section details the methodical steps taken to create the dashboard, ensuring data integrity and accurate visualization.

### Phase 1: Data Modeling and Cleaning

1.  **Data Loading:** All four source CSV files (`Sales`, `Products`, `Customers`, `Tasks`) were imported via **Get Data**.
2.  **Data Cleaning:** The **`Date`** column in the Sales table was converted to the **Date** data type in Power Query to enable correct time-series analysis.
3.  **Relationships:** A **Star Schema** model was established by linking the central **Sales** table to the **Products** and **Customers** tables using `ProductID` and `CustomerID`.

### Phase 2: Measure Creation (DAX)

The following core measures were created in the Sales table:

| Measure Name | DAX Logic |
| :--- | :--- |
| **Total Revenue** | `SUMX(Sales, Sales[Quantity] * Sales[Unit Price])` |
| **Total Cost** | `SUMX(Sales, Sales[Quantity] * Sales[unit Cost])` |
| **Total Profit** | `[Total Revenue] - [Total Cost]` |
| **Profit Margin %** | `DIVIDE([Total Profit], [Total Revenue], 0)` (Formatted as **Percentage**) |

### Phase 3: Visualization (Addressing Assignment Tasks)

The following visuals were constructed to meet the assignment requirements:

| Assignment Task | Power BI Visual Setup |
| :--- | :--- |
| **Dashboard Heading** | Used a **Text Box** for the title: *Electronics Sales and Profit Performance 2025*. |
| **Interactivity** | **Slicers** were added for **City** and **Category** to enable dynamic report filtering. |
| **1. Total Sales by Product** | **Bar Chart** showing `Total Revenue` by `ProductName`, sorted descending. |
| **2. Sales Trend Over Time** | **Line Chart** plotting `Total Revenue` across the **Month** level of the Date Hierarchy. |
| **3. Top 5 Customers** | **Table** visual using a **Top N** filter set to Top 5 by `Total Revenue`. |
| **4. Category-wise Sales** | **Donut Chart** with `Category` as the legend and `Total Revenue` as the value. |
| **5. Profit Analysis** | **Matrix** with a hierarchy of `Category` and `ProductName` in the **Rows** and all four profit measures in the **Values**. |
