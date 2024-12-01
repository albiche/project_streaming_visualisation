# Project_streaming_visualisation

## Description

This project is designed to process raw listening data from Last.fm and transform it into structured relational tables for analysis in Power BI. The script automates the data pipeline by loading CSV files, cleaning and filtering the data, and generating three key relational tables: **users.csv**, **musics.csv**, and **listens.csv**. These tables are then used in Power BI to create interactive dashboards for analyzing music listening habits and trends. 

The Python script follows a clear structure:
- **Load Files**: Reads all CSV files from the input directory while skipping empty files.
- **Process Data**: Cleans and filters the data, ensuring proper date formatting and building relationships between users, music tracks, and listening activity.
- **Export Data**: Saves the relational tables in the output directory, ready for use in Power BI.

The Power BI dashboard uses these tables to create visualizations such as the most listened-to tracks and albums (both all-time and weekly), a cross-tabulation of listening activity by listener and artist, and rankings of the top 10 listeners. This combination of Python and Power BI enables seamless and scalable insights from the raw data.

---

## Features

- Transformation of raw CSV files into three relational tables:
  - **users.csv**: Contains unique user information.
  - **musics.csv**: Contains unique information about music tracks.
  - **listens.csv**: Details the listening activity, including timestamps and relationships between users and tracks.
- Power BI dashboard for analyzing music listening habits:
  - **Most Listened Track (All-Time)**: Displays the most popular track across all data.
  - **Most Listened Track (Weekly)**: Highlights the most listened-to track for each week.
  - **Most Listened Album (All-Time)**: Identifies the most popular album across the entire dataset.
  - **Most Listened Album (Weekly)**: Highlights the most popular album for each week.
  - **Cross Tabulation**: Shows the number of tracks listened to by each listener for each artist.
  - **Top 10 Listeners (All-Time)**: Ranks the 10 users with the most listens.
  - **Top 10 Listeners (Weekly)**: Ranks the 10 users with the most listens for each week.

This project automates the process of data cleaning, structuring, and visualization, making it easy to derive insights and track trends in music listening behavior over time.

---

## Folder Structure

```plaintext
Project_streaming_visualisation/
├── data/
│   └── raw/
│       └── Lastfm/               # Contains raw CSV files
├── scripts/
│   └── process_data.py           # Python script for data transformation
├── output/                       # Contains the relational tables
├── power_bi/
│   └── Dashboard.pbix      # Power BI dashboard
├── README.md                     # Main documentation
└── requirements.txt              # Required Python dependencies
```

---

## Prerequisites

1. **Python**: Version 3.8 or higher.
2. **Power BI Desktop**: Download and install from [the official website](https://powerbi.microsoft.com/desktop/).

---

## Installation and Usage Guide

### Step 1: Clone the repository

Download the project to your local machine:

```bash
git clone https://github.com/albiche/Project_streaming_visualisation.git
cd Project_streaming_visualisation
```

### Step 2: Add your data
Place your raw CSV files in the following folder:

```plaintext
data/raw/Lastfm/
```

### Step 3: Run the Python script
Run the script to transform raw data into relational tables:

```bash
python scripts/process_data.py
```

The generated files (users.csv, musics.csv, listens.csv) will be created in the `output/` folder.

### Step 4: Update Power BI
#### 1. Open the Power BI file
Launch Power BI Desktop.  
Open the file `power_bi/LastfmDashboard.pbix`.

#### 2. Configure data sources

Go to Transform Data (top ribbon).  

Ensure the following files point to the `output/` folder:

```plaintext
users.csv
musics.csv
listens.csv
```
If the path is incorrect:  

Click on Source in the steps on the right.  
Edit the path to point to the file in `output/`.  

#### 3. Update table relationships
Verify the relationships between tables:  
users.User_ID → listens.User_ID  
musics.Music_ID → listens.Music_ID  

#### 4. Refresh the data
Click on Refresh (top ribbon) to load the new data.
