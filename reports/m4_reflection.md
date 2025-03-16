# Milestone 4 - Reflection

This week, our team focused on **enhancing the DataSalaries Dashboard** by incorporating user feedback, refining visual clarity, and optimizing performance. We made improvements to navigation, interactivity, and data processing speed, ensuring a smoother user experience.

### Key Changes Since Milestone 3

1. **Tabbed Chart Organization**
   - Introduced tabbed navigation to separate salary trends from location and employment factors, improving clarity and accessibility.
2. **Year Selection Feature**
   - Added a year dropdown to enable users to explore historical salary trends rather than defaulting to the latest available data.
3. **Improved Handling of Missing Data**
   - Instead of displaying blank charts when no data is available, the dashboard now displays an informative message, helping users understand their selection constraints.
4. **Dashboard Information Button**
   - Added a new "About" button in the header, providing a concise description of the dashboard’s purpose, allowing users to quickly understand the data and context.
5. **Performance Enhancements**
   - Switched from `read_csv` to a binary format for faster data loading, reducing the time it takes to process and display data. 
   - Implemented caching for all charts to improve rendering speed, making the dashboard more responsive.
6. **UI Refinements**
   - Enhanced the collapsible button description and added a disclaimer in the sidebar to clearly highlight data limitations.
   - Ensured that line chart colors and y-axis labels remain consistent across different selections to avoid confusion.
7. **Challenging: Testing and Documentation**
   - Set up unit tests to validate the key functions of the dashboard, ensuring the data and visualizations behave as expected.
   - Added docstrings to all functions and necessary code comments to improve code clarity and maintainability.

### Deviations from the Proposal

1. **Tabbed Navigation:**: Instead of displaying all four charts on a single page as originally planned, we implemented tabbed navigation for better usability. 
2. **Refined Year Filtering:** Rather than applying year filters globally, we introduced a dropdown in the second tab, so that users can filter the year for location info without breaking trend charts.
3. **Handling of Missing Data:** The dashboard now explicitly informs users when their selections result in no data, enhancing usability by providing immediate feedback instead of leaving users with empty visualizations.
4. **Header Button Addition:** Added an "About" button in the header to provide quick context about the dashboard’s purpose, which was not part of the original plan but significantly improves the user experience.

### Reflection on Visualization and Functionality

Our dashboard follows **DSCI 531 best practices**, prioritizing **clarity, usability, and accessibility**.
1. **User Experience & Navigation**  
   - The tabbed layout allows for easy switching between trend analysis and yearly comparisons.  
   - The year dropdown lets users analyze historical salary trends dynamically.
2. **Enhanced Interactivity & Data Interpretation**   
   - Consistent color mapping ensures that job roles always retain the same color, improving readability.  
   - Dynamic messaging for missing data enhances usability, preventing confusion.
3. **Performance Optimizations**  
   - Parquet format significantly speeds up data loading compared to CSV.  
   - Caching reduces redundant computations, making the dashboard more responsive.

#### Limitations and Areas for Improvement
1. **Rendering Performance**  
   - Despite optimizations, Altair’s processing time is still a bottleneck, especially when we click the demo link for the first time.  
   - Future Improvement: We could consider using Plotly or Vega for faster rendering.  
2. **Y-Axis Scaling for Bar Charts**  
   - While the trend line chart has a fixed y-axis scale, the bar charts do not, due to extreme executive-level salaries that distort scaling.  
   - Future Improvement: Allow users to toggle between fixed and dynamic scaling for better clarity.  
3. **Additional Features for Future Consideration**  
   - Incorporating salary percentiles to visualize the distribution rather than relying solely on averages.  
   - Predictive analytics to project future salary trends based on historical data.

### Insights and Feedback Reflection

One key insight we gained was from feedback on the clarity of the map visualization. Initially, our map was cluttered with excessive geographical areas, which detracted from its effectiveness. By removing Antarctica, we were able to streamline the visualization and allow the remaining regions to have more focused attention. This was a valuable realization about how minor adjustments in visualization can significantly enhance clarity.

Additionally, the feedback we received regarding interactivity highlighted that users preferred smoother transitions between data views, leading to the decision to incorporate tabbed navigation. The ability to switch between trends and yearly data seamlessly has proven to improve the user experience substantially.

However, one aspect that could have further supported the development of a high-quality dashboard would be more detailed user testing focused on edge cases or rare data combinations. While the overall functionality is solid, having more input on how users interact with the dashboard in real-world scenarios could help refine it further.
