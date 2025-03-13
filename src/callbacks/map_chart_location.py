import altair as alt
import pandas as pd
from vega_datasets import data

def create_salary_by_location_chart(df_filtered):
    """
    Generates a choropleth map of average salaries by country.
    """
    
    # Compute average salary by country
    avg_salary_by_country = df_filtered.groupby('company_location', as_index=False)['salary_in_usd'].mean()
    
    # Country mapping to numeric IDs for visualization
    country_mapping = {
        'Australia': 36, 'United States': 840, 'Ireland': 372, 'Portugal': 620, 'United Kingdom': 826,
        'Germany': 276, 'India': 356, 'Spain': 724, 'Netherlands': 528, 'Canada': 124, 'Ukraine': 804,
        'Italy': 380, 'Vietnam': 704, 'Mexico': 484, 'Poland': 616, 'Egypt': 818, 'Denmark': 208,
        'Honduras': 340, 'Colombia': 170, 'Armenia': 51, 'Central African Republic': 140, 'Philippines': 608,
        'Lithuania': 440, 'Russia': 643, 'New Zealand': 554, 'Japan': 392, 'France': 250, 'South Africa': 710,
        'Slovenia': 705, 'Estonia': 233, 'Greece': 300, 'Brazil': "076", 'Switzerland': 756, 'Austria': 40,
        'Malaysia': 458, 'Sweden': 752, 'Malta': 470, 'Luxembourg': 442, 'Argentina': 32, 'Nigeria': 566,
        'Ecuador': 218, 'Ghana': 288, 'Finland': 246, 'United Arab Emirates': 784, 'Romania': 642,
        'American Samoa': 16, 'Singapore': 702, 'Latvia': 428, 'Belgium': 56, 'Turkey': 792, 'Thailand': 764,
        'Pakistan': 586, 'South Korea': 410, 'Israel': 376, 'Iraq': 368
    }

    # Convert to three-digit formatted integers
    country_mapping = {k: f"{int(v):03d}" for k, v in country_mapping.items()}
    
    # Apply mapping
    avg_salary_by_country['id'] = avg_salary_by_country['company_location'].map(country_mapping)

    # Base map with country outlines
    # Base map with country outlines (excluding Antarctica)
    base_map = alt.Chart(
        alt.topo_feature('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json', 'countries')
    ).mark_geoshape(
        stroke='white',
        fill='lightgrey'
    ).transform_filter(
        "datum.properties.name !== 'Antarctica'"
    ).project(
        type='naturalEarth1'
    ).properties(
        width=800,
        height=400
    )

    # Salary choropleth (excluding Antarctica)
    salary_for_map = alt.Chart(
        alt.topo_feature('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json', 'countries')
    ).mark_geoshape().transform_filter(
        "datum.properties.name !== 'Antarctica'"
    ).encode(
        color=alt.Color('salary_in_usd:Q', 
                        scale=alt.Scale(scheme="blues"), 
                        legend=alt.Legend(title="Avg Salary (USD)", labelFontSize=12, titleFontSize=14)),
        tooltip=[alt.Tooltip('company_location:N', title="Country"),
                alt.Tooltip('salary_in_usd:Q', format="$,.0f", title="Avg Salary (USD)")]
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(avg_salary_by_country, 'id', ['salary_in_usd', 'company_location'])
    )

    # Combine map layers
    salary_location_chart = base_map + salary_for_map

    return salary_location_chart.to_dict()