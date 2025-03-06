import altair as alt
import pandas as pd

def create_salary_trend_chart(df_filtered, selected_jobs):
    """Creates the salary trend chart over the years."""
    
    if not selected_jobs:
        # Show average salary per year if no job title is selected
        avg_salary_per_year = df_filtered.groupby('work_year', as_index=False)['salary_in_usd'].mean()
        
        salary_trend_chart = alt.Chart(avg_salary_per_year).mark_line().encode(
            x=alt.X('work_year:O', title="Year"),
            y=alt.Y('salary_in_usd:Q', title="Avg Salary (USD)"),
            tooltip=['work_year', 'salary_in_usd']
        ).properties(
            width=550, 
            height=370, 
            title="Salary Trend Over Years"
        )

        points = alt.Chart(avg_salary_per_year).mark_point(size=60, filled=True, color='coral').encode(
            x='work_year:O',
            y='salary_in_usd:Q'
        )
        
        text_labels = alt.Chart(avg_salary_per_year).mark_text(
            align='center', dy=25, fontSize=12, color="black"
        ).encode(
            x='work_year:O',
            y='salary_in_usd:Q',
            text=alt.Text('salary_in_usd:Q', format=',.0f')
        )

        return (salary_trend_chart + points + text_labels).configure_view(stroke=None).to_dict()

    else:
        # Show salary trend by job title if one or more jobs are selected
        salary_trend_data = df_filtered.groupby(['work_year', 'job_title'], as_index=False)['salary_in_usd'].mean()
        
        salary_trend_chart = alt.Chart(salary_trend_data).mark_line().encode(
            x=alt.X('work_year:O', title="Year"),
            y=alt.Y('salary_in_usd:Q', title="Avg Salary (USD)"),
            color=alt.Color('job_title:N', legend=alt.Legend(title="Job Title")),
            tooltip=['job_title', 'work_year', 'salary_in_usd']
        ).properties(
            width=550, 
            height=370, 
            title="Salary Trend by Job Title"
        ).configure_view(stroke=None)
        
        return salary_trend_chart.to_dict()