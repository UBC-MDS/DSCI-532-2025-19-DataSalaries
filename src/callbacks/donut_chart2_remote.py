import altair as alt

def create_salary_by_remote_type_chart(df_filtered):
    """Creates a donut chart for average salary by remote type."""
    
    salary_by_remote_ratio_data = df_filtered.groupby('remote_ratio', as_index=False)['salary_in_usd'].mean()
    salary_by_remote_ratio_data['total_salary'] = salary_by_remote_ratio_data['salary_in_usd'].sum()
    salary_by_remote_ratio_data['percentage'] = (salary_by_remote_ratio_data['salary_in_usd'] / salary_by_remote_ratio_data['total_salary']) * 100


    salary_by_remote_ratio_chart = alt.Chart(salary_by_remote_ratio_data).mark_arc(innerRadius=80).encode(
        theta=alt.Theta('salary_in_usd:Q', title="Average Salary"),
        color=alt.Color('remote_ratio:N', scale=alt.Scale(scheme="oranges"), legend=alt.Legend(title=None, orient="top", offset=-20),
            sort=['On-site', 'Hybrid', 'Fully Remote']),
        tooltip=[alt.Tooltip('remote_ratio', title="Remote Type"),
                alt.Tooltip('salary_in_usd:Q', format="$,.0f", title="Avg Salary (USD)"),
                alt.Tooltip('percentage:Q', format=".1f", title="Percentage (%)")
                ]
    ).properties(
        width=300,
        height=400,
        title=alt.TitleParams(
            text="Average Salary by Remote Type, USD",
            anchor="middle"
        )
    )

    return salary_by_remote_ratio_chart.to_dict()