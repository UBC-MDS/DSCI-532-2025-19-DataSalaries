import altair as alt

def create_salary_by_company_size_chart(df_filtered):
    """Creates a donut chart for average salary by company size."""
    
    salary_by_company_size_data = df_filtered.groupby(['company_size'] , as_index=False)['salary_in_usd'].mean()
    company_size_labels = {
    'L': 'Large (251+)',
    'M': 'Medium (51-250)',
    'S': 'Small (1-50)'
    }

    salary_by_company_size_data['company_size'] = salary_by_company_size_data['company_size'].map(company_size_labels)
    salary_by_company_size_data['percentage'] = (
    salary_by_company_size_data['salary_in_usd'] / salary_by_company_size_data['salary_in_usd'].sum()) * 100

    salary_by_company_size_chart = alt.Chart(salary_by_company_size_data).mark_arc(innerRadius=80).encode(
        theta=alt.Theta('salary_in_usd:Q', title="Average Salary"),  
        color=alt.Color('company_size:N', 
            scale=alt.Scale(scheme="blues"), legend=alt.Legend(title=None, orient="top", offset=-20),
            sort=['Small (1-50)', 'Medium (51-250)', 'Large (251+)']
        ), 
        tooltip=[alt.Tooltip('company_size', title="Company Size"),
                alt.Tooltip('salary_in_usd:Q', format="$,.0f", title="Avg Salary (USD)"), 
                alt.Tooltip('percentage:Q', format=".1f", title="Percentage (%)")]
    ).properties(
        width=300,  
        height=400,
        title=alt.TitleParams(
            text="Average Salary by Company Size, USD",
            anchor="middle"
        )
    )

    return salary_by_company_size_chart.to_dict()