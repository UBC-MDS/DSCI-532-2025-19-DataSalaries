import altair as alt
from src.utils.cache import cache

@cache.memoize()
def create_salary_by_remote_type_chart(df_filtered_year):
    """
    Creates a donut chart displaying the average salary distribution by remote work type.

    Parameters
    ----------
    df_filtered_year : pandas.DataFrame
        A filtered DataFrame containing salary data for a specific year.

    Returns
    -------
    dict
        A dictionary representation of an Altair donut chart displaying 
        the average salary by company size, with color-coded categories 
        and percentage breakdown.

    Example
    -------
    >>> create_salary_by_remote_type_chart(data)
    """

    salary_by_remote_ratio_data = df_filtered_year.groupby('remote_ratio', as_index=False)['salary_in_usd'].mean()
    salary_by_remote_ratio_data['total_salary'] = salary_by_remote_ratio_data['salary_in_usd'].sum()
    salary_by_remote_ratio_data['percentage'] = (salary_by_remote_ratio_data['salary_in_usd'] / salary_by_remote_ratio_data['total_salary']) * 100


    salary_by_remote_ratio_chart = alt.Chart(salary_by_remote_ratio_data).mark_arc(innerRadius=80).encode(
        theta=alt.Theta('salary_in_usd:Q', title="Average Salary"),
        color=alt.Color('remote_ratio:N', scale=alt.Scale(scheme="oranges"), legend=alt.Legend(title=None, orient="top", labelFontSize=14, offset=30),
            sort=['On-site', 'Hybrid', 'Fully Remote']),
        tooltip=[alt.Tooltip('remote_ratio', title="Remote Type"),
                alt.Tooltip('salary_in_usd:Q', format="$,.0f", title="Avg Salary (USD)"),
                alt.Tooltip('percentage:Q', format=".1f", title="Percentage (%)")
                ]
    ).properties(
        width=300,
        height=350,
    )

    return salary_by_remote_ratio_chart.to_dict()