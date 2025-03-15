## Milestone 4 - Reflection

This week, our team focused on **refining the DataSalaries Dashboard**, incorporating user feedback, and addressing areas that could further enhance both usability and visual clarity. Additionally, we made several performance improvements to speed up data loading and updated the dashboard’s UI to make our app more appealing.

### Key Changes Since Milestone 3

1. **Tabbed Chart Organization:**
   We restructured the dashboard into tabbed pages, enabling users to separately explore **salary trends**, **location-based salaries**, and **employment factors** across different years. This change improves navigation by clearly dividing the data into manageable sections, making the dashboard more organized and user-friendly.

2. **Year Selection Feature:**
   Instead of defaulting to the most recent data, we added a dropdown to let users select and analyze salary data from different years. This new feature offers greater flexibility and allows users to explore historical salary trends.

3. **Improved Handling of Missing Data:**
   When filtered data is unavailable, the dashboard now displays a message indicating that there is no data available instead of showing empty charts. This prevents the dashboard from appearing broken and improves user experience by offering clarity.

4. **Dashboard Information Button:**
   A new "About" button was added in the header, providing a concise description of the dashboard’s purpose. This feature allows users to quickly understand the data and context, enhancing the overall user experience.

5. **Performance Enhancements:**
   - We switched from `read_csv` to a binary format for faster data loading, reducing the time it takes to process and display data. 
   - We implemented caching for all charts to improve rendering speed, making the dashboard more responsive.

6. **UI Refinements**
   - Enhanced the collapsible button description and added a disclaimer in the sidebar to clearly highlight data limitations.
   - Ensured that line chart colors and y-axis labels remain consistent across different selections to avoid confusion.

7. **Challenging: Testing and Documentation:**
   - We set up unit tests to validate the key functions of the dashboard, ensuring the data and visualizations behave as expected.
   - We also added docstrings to all functions and necessary code comments to improve code clarity and maintainability, ensuring future developers can easily understand and extend the code.

### Deviations from the Proposal

1. **Tabbed Navigation:**: Instead of displaying all four charts on a single page as originally planned, we implemented tabbed navigation for better usability. 

2. **Refined Year Filtering:** Rather than applying year filters globally, we introduced a dropdown in the second tab, so that users can filter the year for location info without breaking trend charts.

3. **Handling of Missing Data:** The dashboard now explicitly informs users when their selections result in no data, enhancing usability by providing immediate feedback instead of leaving users with empty visualizations.

4. **Header Button Addition:** Added an "About" button in the header to provide quick context about the dashboard’s purpose, which was not part of the original plan but significantly improves the user experience.

### Reflection on Visualization and Functionality

Our dashboard follows **DSCI 531 best practices**, prioritizing **clarity, usability, and accessibility**.
### What Works Well
1. **User Experience & Navigation:** The tabbed layout improves clarity by separating trend analysis from location and company-related insights. And the year filter dropdown allows users to analyze salary trends across different years dynamically.

2. **Enhanced Interactivity & Data Interpretation:**
  - Consistent color mapping ensures that job roles retain the same color in the trend charts, improving readability.
  - Dynamic messaging for empty selections ensures users receive guidance instead of encountering blank charts.

3. **Performance Optimizations:**
  - Transitioning from CSV to a binary format (Parquet) significantly improved data loading speed.
  - Implementing caching for chart generation reduced redundant computations and improved response times.
  
### Limitations and Areas for Improvement
1. **Rendering Performance:**
   - Despite optimizations, **Altair’s processing time** remains a bottleneck, especially when we click demo link for the first time.
   - Potential Improvement: Consideration for **alternative visualization libraries** such as Plotly or Vega to improve rendering efficiency.
2. **Y-Axis Scaling Considerations:**
   - While the trend line chart has a fixed y-axis scale for consistency, the bar charts do not due to extreme salary values at the executive level.
   - Potential improvement: Adaptive scaling where users can toggle between fixed and dynamic y-axis scales.
3. **Other Possible Additions:**
   - Incorporating salary percentiles to show salary distributions rather than just averages.
   - Introducing trend projections using predictive analytics to estimate future salary trends.

### Insights and Feedback Reflection

One key insight we gained was from feedback on the clarity of the map visualization. Initially, our map was cluttered with excessive geographical areas, which detracted from its effectiveness. By removing Antarctica, we were able to streamline the visualization and allow the remaining regions to have more focused attention. This was a valuable realization about how minor adjustments in visualization can significantly enhance clarity.

Additionally, the feedback we received regarding interactivity highlighted that users preferred smoother transitions between data views, leading to the decision to incorporate tabbed navigation. The ability to switch between trends and yearly data seamlessly has proven to improve the user experience substantially.

However, one aspect that could have further supported the development of a high-quality dashboard would be more detailed user testing focused on edge cases or rare data combinations. While the overall functionality is solid, having more input on how users interact with the dashboard in real-world scenarios could help refine it further.
