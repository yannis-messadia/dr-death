# Dr Death - Analysis of Harold Shipman's Murders with Power BI

A/- Technological Watch: Power BI

1. Introduction to Power BI:

Power BI is a data analysis and visualization platform developed by Microsoft. It allows connection to many data sources, data transformation, and creation of interactive reports and visual dashboards. It is widely used in business, and Power BI facilitates data-driven decision-making thanks to its intuitive interface and powerful modeling tools.

3. Key Concept: the Dashboard

A dashboard is a graphical interface that brings together multiple data visualizations on a single screen. Its goal is to summarize key information clearly and interactively to enable quick understanding and informed decision-making. Key elements in the dashboard: Charts (bar, line, pie…), KPIs (key performance indicators), Dynamic filters, Geographic maps

5. Advantages of Power BI:

* Free locally
* Broad connectivity: Compatible with Excel, CSV, SQL, Azure, web APIs, etc.
* Drag-and-drop functionality, easy to use.
* Automatic refresh: If the source is connected, data can be updated automatically.
* Ability to publish reports via Power BI Service (cloud version).
* Customization with visualizations and filters.

4. Limitations and Disadvantages:

   * Technical learning required for advanced features (DAX language, Power Query M).
   * Limited features in the free version, especially for sharing in Power BI Service.
   * The tool can slow down with very large, unoptimized data volumes.

5. Main Features:

   * Connection to multiple sources: local files, databases, cloud services, web APIs…
   * Data transformation via Power Query editor (cleaning, filtering, merging…).
   * Modeling: creating relationships between tables, advanced calculations with DAX.
   * Creation of interactive reports: dynamic charts, filters, performance indicators, maps…
   * Publishing & collaboration: sharing reports on the cloud via Power BI Service.

6. Types of Compatible Data Sources:

   * Flat files: Excel, CSV, JSON, XML
   * Databases: SQL Server, MySQL, PostgreSQL, Oracle…
   * Cloud services: Azure, Salesforce, Google Analytics, SharePoint…
   * Web APIs: data extraction via URL
   * Local sources: manual import from computer

7. Visualizations:

   * Bar / column charts: comparison between categories
   * Line charts: time evolution analysis
   * Pie / donut charts: data distribution
   * Maps: geographic visualization
   * Heat maps: value intensity on areas
   * KPI dashboards: performance tracking
   * Slicers: interactive filters to explore data

B/- Context:

This project aims to analyze the murders committed by Harold Shipman, one of the most prolific serial killers in UK history, using Power BI. Two datasets are used:

* shipman-confirmed-victims.csv: Contains the list of Shipman's confirmed victims, with their name, age, gender, date and place of death. Used to analyze victim profiles and the timeline of the murders.
* shipman-times-comparison.csv: Compares the time of death of Shipman's patients to those of other general practitioners. Used to identify an abnormal hourly pattern in the deaths.

C/- Research Question:

What kinds of people did Harold Shipman kill, and when did they die?

D/- Data Analysis:

a. Gender Distribution:

Among all confirmed victims, around 80% were women, compared to only 20% men. This female overrepresentation suggests a targeted strategy by Shipman, who likely exploited the vulnerability of elderly women living alone. This disparity, statistically significant, highlights a strong gender bias in his murders.

b. Age Distribution:

Analysis of the "age" variable shows that over 75% of victims were between 70 and 90 years old, with an average age of about 76. This heavily right-skewed distribution indicates that Shipman primarily targeted elderly individuals, often considered to be at the end of life, which made his actions more difficult to detect. People under 60 accounted for less than 5% of victims.

c. Temporal Evolution of Murders:

The yearly distribution of deaths shows a progressive intensification of his killings: nearly 60% of deaths occurred in the last ten years (1988–1998), with a peak between 1995 and 1998. This increase in frequency reflects an escalation in his criminal behavior, possibly linked to a growing sense of impunity.

d. Place of Death:

More than 90% of deaths occurred at home, where Shipman had total control and the trust of his patients. This confirms that he acted in a controlled environment, thereby minimizing the risk of external suspicion or intervention by other healthcare professionals.

e. Time Distribution of Deaths: comparison between Shipman and other doctors

The analysis of death times reveals a major behavioral anomaly. For patients of other general practitioners, deaths are relatively evenly distributed over 24 hours, with a natural slight concentration during the night and early morning, corresponding to typical geriatric mortality peaks.
In contrast, for Harold Shipman's patients, over 60% of deaths occurred between 1 PM and 5 PM, right in the afternoon. This concentration has no medical justification and strongly contrasts with normal mortality curves. This artificial peak matches Shipman’s consultation hours, strongly suggesting he deliberately administered lethal substances during his visits.
This repetitive time pattern constitutes a clear statistical anomaly. It could have been detected earlier through medical record monitoring or death certificate analysis. This data point is one of the key clues that helped confirm the intentionality of the murders.
