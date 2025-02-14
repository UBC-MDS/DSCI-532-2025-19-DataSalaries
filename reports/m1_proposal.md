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

#### Target Audience Persona

**Name:** Alex  
**Occupation:** Data Science Job Seeker  
**Location:** San Francisco, California  
**Experience Level:** Mid-level Data Scientist  
**Career Goals:** Alex is looking to make informed decisions about job offers and salary expectations in the data science field. He wants to ensure that he is getting competitive compensation and is particularly interested in understanding how his experience level and location may affect his earning potential.  

#### Research Questions
1. **How do salaries for data science roles vary by experience level?**  
2. **Which locations offer the highest salary potential for data scientists?**  
3. **What is the salary difference between remote, hybrid, and onsite roles?**  
4. **How do job titles and company size impact salaries?**  
5. **What trends can be observed in data science salaries over the last few years?**

#### Usage Scenario

Alex is actively exploring job opportunities in the data science field and wants to evaluate his earning potential as he looks at different roles and locations. He is particularly interested in the influence of experience level and remote work options on salary.

1. **[Exploring Salary Trends Over Time]**  
   When Alex logs into the "Data Science Salary Trends" app, he is first presented with a dashboard showcasing an overview of the salary distributions over the past few years. He sees that the app tracks salaries by year and can immediately compare how salaries have evolved over time for data scientists in general.

2. **[Comparing Salaries by Experience Level]**  
   Alex clicks on the "Job Market Insights" section and filters the data by his **experience level** (mid-level). He quickly sees how his salary compares to other experience levels, such as entry-level and senior-level data scientists. The app shows salary ranges for each experience level and highlights that senior-level roles offer significantly higher salaries.

3. **[Evaluating Location-Based Salary Differences]**  
   Alex is interested in relocating and wants to compare salaries in different regions. He navigates to the "Geographical Analysis" section and filters the data by location, focusing on cities like San Francisco, New York, and Austin. He is able to view the average salaries for data scientists in each city and notices that San Francisco offers the highest salary range, confirming his initial assumption about the cost of living in major tech hubs.

4. **[Exploring the Impact of Remote vs. Onsite Roles]**  
   Alex also wants to assess how working remotely or onsite impacts salary. He selects the "Work Environment Comparison" filter and compares salaries between fully remote, hybrid, and onsite data science roles. The data shows that remote roles tend to offer slightly lower salaries, but hybrid roles seem to offer a middle ground. This insight helps Alex understand that while fully remote work offers flexibility, it may come with a salary trade-off.

5. **[Job Title and Company Size Comparison]**  
   Alex is also curious about how different job titles, such as "Data Analyst" and "Data Engineer," compare in terms of salary. In the "Job Market Insights" section, he filters the data by job title and discovers that "Data Scientist" roles tend to offer higher salaries than "Data Analyst" or "Data Engineer" roles. He also examines salary differences between small, medium, and large companies and finds that larger companies tend to offer higher compensation.

6. **[Decision-Making and Job Search Strategy]**  
   Based on these insights, Alex realizes that his salary expectations align well with major cities like San Francisco, but he needs to adjust his expectations if considering remote roles. He decides to target larger companies for his job search and is now more confident in evaluating job offers. Furthermore, Alex can use the app’s historical salary trends to gauge potential salary growth in his field over the next few years.

In summary, Alex's use of the app enables him to make informed decisions regarding his job search and salary expectations, and he can now prioritize roles and locations that align with his career goals and desired compensation.

## App Sketch and Description
<!-- Describe the planned application, including its functionality and features. -->

![App Sketch](path/to/image.png)
