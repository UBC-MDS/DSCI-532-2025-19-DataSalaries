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
We will be visualizing a dataset containing approximately 5,000 records describing salaries of various roles in the data science field. Each record includes 11 variables (with 8 selected for our app) that capture key characteristics relevant to understanding salary trends:
- Compensation info (Numerical) **(Key Focus)**: `salary_in_usd`
- Time info (Numerical): `work_year`
- Job info (Categorical): `job_title`, `experience_level` (Entry-level, Mid-level, Senior-level, or Executive-level), `employment_type` (Full-Time or not), `remote_ratio` (On_site, Hybrid, or Fully Remote)
- Location info (Categorical): `company_location`
- Company info (Categorical): `company_size` (Small, Medium, or Large)

Since our key audience is job seekers in the data science field, we believe that this dashboard will help them to better understand salary trends by experience level, job title, region, remote status, etc and improve their efficiency in job seeking.

#### New variables to Derive
We will create the following derived variables to provide deeper insights into salary trends and their relationship with job roles and locations:
- `avg_salary_(year)`: This metric will help identify salary trends over time, highlighting potential salary growth patterns.
- `avg_salary_(location)`/`min_salary_(location)`/`max_salary_(location)`: These metrics will allow job seekers to compare salaries across regions, helping them assess which locations offer competitive compensation.
- `avg_salary_(job title)`/`min_salary_(job title)`/`max_salary_(job title)`: By analyzing salary ranges within job titles, job seekers can better understand which roles provide the highest earning potential and where they fit within the salary distribution.

#### High Level Description of Visualization:
To ensure a clear structure in our dashboard while maintaining focus on the most insightful variables, we have grouped the visualizations into key sections based on their relevance:
- Salary Overview: `salary_in_usd`,  `work_year`
  - Visual: Average salary distribution over time
- Job Market Insights: `job_title`, `experience_level`, `employment_type`, `company_size`
  - Visual: Salary variations by job title, experience level, employment type, and company size
- Geographical Analysis: `company_location`
  - Visual: Comparison of regional salaries
- Work Environment Comparison: `employment_type`, `remote_ratio`
  - Visual: Comparison of salaries for onsite, hybrid, and remote roles, and salary trends by employment type

## Research Questions
<!-- List the key research questions that the project aims to address. -->

## App Sketch and Description
<!-- Describe the planned application, including its functionality and features. -->

![App Sketch](path/to/image.png)
