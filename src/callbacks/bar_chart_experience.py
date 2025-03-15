import altair as alt
from src.utils.cache import cache

@cache.memoize()
def create_salary_by_experience_chart(df_filtered):
    """
    Creates a bar chart showing salary by experience level.
    """
    # Assign consistent color to each experience level
    exp_colors = {
    "Entry-level/Junior": "#4E79A7", 
    "Mid-level": "#F28E2B", 
    "Senior-level": "#E15759",
    "Executive-level": "#76B7B2",  
    }
    color_scale_exp = alt.Scale(domain=list(exp_colors.keys()), range=list(exp_colors.values()))
    
    # bar chart
    salary_by_experience_level_chart = alt.Chart(df_filtered).mark_bar().encode(
        x=alt.X('experience_level:N', axis=None, sort=['Entry-level/Junior', 'Mid-level', 'Senior-level', 'Executive-level']),  
        y=alt.Y(
            'mean(salary_in_usd):Q', 
            title=None, 
            axis=alt.Axis(grid=False, tickCount=6)),  
        color=alt.Color(
            'experience_level:N', 
            legend=alt.Legend(title=None, orient="top", labelFontSize=14, offset=10),  
            sort=['Entry-level/Junior', 'Mid-level', 'Senior-level', 'Executive-level'],
            scale=color_scale_exp
        ),
        column=alt.Column('work_year:N', title=None, header=alt.Header(labelOrient="bottom")),  
        tooltip=[alt.Tooltip('work_year', title="Year"),
                alt.Tooltip('experience_level', title="Experience Level"),
                alt.Tooltip('mean(salary_in_usd):Q', format="$,.0f", title="Avg Salary (USD)")]  
    ).properties(
        width=150,
        height=300,
    ).configure_header(
        labelFontSize=12,
        titleFontSize=16
    )

    return salary_by_experience_level_chart.to_dict()