# M1 Proposal

## Motivation and Purpose
<!-- Describe the motivation behind the project and its intended purpose. -->
Our Role: Data analytics consultancy firm specializing in job market insights.

Target Audience: Job seekers and industry analysts.

Data-related job salaries vary widely based on experience, location, industry, and skill set. 
Understanding these salary trends is crucial for both job seekers and employers to make informed career and hiring decisions. 
If we could analyze the key factors influencing salaries in data-related roles, we could provide valuable insights to professionals navigating the job market.
To address this challenge, we propose building a data visualization app that allows users to explore a dataset of salaries and job trends across different industries, locations, and roles.
Our app will display salary distributions, trends over time, and comparisons between job titles, enabling users to identify patterns and insights.
Additionally, interactive filtering will allow users to explore pattern changes by data role and year.

## Description of the Data
<!-- Provide an overview of the data sources, structure, and key attributes. -->
We will be visualizing a dataset containing approximately 5,000 records describing salaries of various roles in the data science field. Each record has 11 associated variable (we will be using 7 of them) that describe the following characteristics that we think would be helpful in understanding the salary trends:
	•	Job info: `job_title`, `experience_level` (Entry-level, Mid-level, Senior-level, or Executive-level), `employment_type` (Full Time or not), `remote_ratio` (On_site, Hybrid, or Fully Remote)
	•	Compensation info: `salary_in_usd`
	•	Location info: `company_location`
	•	Company info: `company_size` (Small, Medium, or Large)

Since our key audience is job seekers in the data science field, we believe that this dashboard will help them to better understand salary trends by experience level, job title, region, remote status, etc and improve their efficiency in job seeking.

#### Variables Planning to Visualize:
	1.	Job Title & Experience Level: Key factors influencing salaries
	2.	Salary (USD): Central metric for comparisons
	3.	Company Size: Can indicate how large companies pay compared to smaller ones
	4.	Remote Ratio: Helps understand if remote jobs pay differently
	5.	Company Location vs. Employee Residence: Highlights salary differences by region and remote work trends

#### New variables to Derive
We will derive:
	•	Salary per Year of Experience (salary_per_year_exp):
Formula: salary_in_usd / (years_of_experience + 1)
This will help job seekers understand how experience translates to compensation.

## Research Questions
<!-- List the key research questions that the project aims to address. -->

## App Sketch and Description
<!-- Describe the planned application, including its functionality and features. -->

![App Sketch](path/to/image.png)
