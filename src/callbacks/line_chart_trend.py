import altair as alt
import pandas as pd
from src.utils.cache import cache

@cache.memoize()
def create_salary_trend_chart(df_filtered, selected_jobs):
    """Creates the salary trend chart over the years."""
    
    # Assign consistent color to each job position
    job_colors = {
    "Data Analyst": "#00A5E3", 
    "Data Engineer": "#8DD7BF", 
    "Data Scientist": "#FF96C5",
    "Machine Learning Engineer": "#FF5768",  
    "Research Scientist": "#FFBF65"
    }
    color_scale = alt.Scale(domain=list(job_colors.keys()), range=list(job_colors.values()))

    # Line charts based on selection
    if not selected_jobs:
        # If no job title selected, show average salary per year
        avg_salary_per_year = df_filtered.groupby('work_year', as_index=False)['salary_in_usd'].mean()
        avg_salary_per_year["Category"] = "Average Salary"

        salary_trend_chart = alt.Chart(avg_salary_per_year).mark_line().encode(
            x=alt.X('work_year:O', title=None, axis=alt.Axis(labelAngle=0, labelFontSize=12)),
            y=alt.Y(
                'salary_in_usd:Q', 
                title=None, 
                axis=alt.Axis(grid=False, tickCount=6),
                scale=alt.Scale(domain=[0, 250000])),
            color=alt.Color('Category:N', legend=alt.Legend(title=None, orient="top", labelFontSize=14,)),
            tooltip=['salary_in_usd']
        ).properties(
            width=850,
            height=300,
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
        salary_trend_chart = (salary_trend_chart + points + text_labels).configure_view(stroke=None)
        return salary_trend_chart.to_dict()

    else:
        # If job titles are selected, show salary trend by job title
        salary_trend_data = df_filtered.groupby(['work_year', 'job_title'], as_index=False)['salary_in_usd'].mean()
        salary_trend_chart = alt.Chart(salary_trend_data).mark_line().encode(
            x=alt.X('work_year:O', title=None, axis=alt.Axis(labelAngle=0, labelFontSize=12)),
            y=alt.Y(
                'salary_in_usd:Q', 
                title=None, 
                axis=alt.Axis(grid=False, tickCount=6),
                scale=alt.Scale(domain=[0, 250000])),
            color=alt.Color(
                'job_title:N', 
                legend=alt.Legend(
                    title=None, 
                    orient="top",
                    labelFontSize=14,
                    labelLimit=200), 
                scale=color_scale),
            tooltip=[alt.Tooltip('job_title', title="Job Title"),
                    alt.Tooltip('work_year', title="Year"),
                    alt.Tooltip('salary_in_usd:Q', format="$,.0f", title="Avg Salary (USD)")]
        ).properties(
            width=850,
            height=300
        ).configure_view(
            stroke=None
        )
        
        return salary_trend_chart.to_dict()