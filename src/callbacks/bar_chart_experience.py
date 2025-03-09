import altair as alt

def create_salary_by_experience_chart(df_filtered):
    """
    Creates a bar chart showing salary by experience level.
    """
    salary_by_experience_level_chart = alt.Chart(df_filtered).mark_bar().encode(
        x=alt.X('experience_level:N', axis=None, sort=['Entry-level/Junior', 'Mid-level', 'Senior-level', 'Executive-level']),  
        y=alt.Y('mean(salary_in_usd):Q', title=None, axis=alt.Axis(grid=False)),  
        color=alt.Color(
            'experience_level:N', 
            legend=alt.Legend(title=None, orient="top", offset=10),  
            sort=['Entry-level/Junior', 'Mid-level', 'Senior-level', 'Executive-level']  
        ),
        column=alt.Column('work_year:N', title=None, header=alt.Header(labelOrient="bottom")),  
        tooltip=[alt.Tooltip('work_year', title="Year"),
                alt.Tooltip('experience_level', title="Experience Level"),
                alt.Tooltip('mean(salary_in_usd):Q', format="$,.0f", title="Avg Salary (USD)")]  
    ).properties(
        width=60,
        height=400,
    ).configure_header(
        labelFontSize=12,
        titleFontSize=16
    )

    return salary_by_experience_level_chart.to_dict()