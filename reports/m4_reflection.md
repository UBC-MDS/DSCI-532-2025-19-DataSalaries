## **Milestone 4 - Reflection**

This week, our team focused on **refining** the **DataSalaries Dashboard**, incorporating user feedback, and addressing areas that could further enhance both **usability** and **visual clarity**. Additionally, we made several **performance improvements** to speed up data loading and enhance user experience. These included **binary data format loading**, **caching for specific functions**, and various updates to the dashboard’s UI, such as setting a **favicon**, updating the **GIF animation**, and refreshing outdated **screenshots and descriptions** in the README. We also **added docstrings for functions** to improve code documentation and maintainability.

### **Changes Since Milestone 3**

1. **Tabbed Chart Organization:**
   We restructured the dashboard into **tabbed pages**, enabling users to separately explore **salary trends**, **location-based salaries**, and **employment factors** across different years. This change improves navigation by clearly dividing the data into manageable sections, making the dashboard more organized and user-friendly.

2. **Year Selection Feature:**
   Instead of defaulting to the most recent data, we added a **dropdown** to let users select and analyze salary data from different years. This new feature offers greater flexibility and allows users to explore historical salary trends.

3. **Improved Handling of Missing Data:**
   When filtered data is unavailable, the dashboard now displays a **message** indicating that there is no data available instead of showing empty charts. This prevents the dashboard from appearing broken and improves user experience by offering clarity.

4. **Dashboard Information Button:**
   A new **"About" button** was added in the header, providing a concise description of the dashboard’s purpose. This feature allows users to quickly understand the data and context, enhancing the overall user experience.

5. **Testing and Documentation:**
   - We set up **unit tests** to validate the key functions of the dashboard, ensuring the data and visualizations behave as expected.
   - We also **added docstrings** to all functions to improve **code clarity** and maintainability, ensuring future developers can easily understand and extend the code.
   - **Code comments** were added throughout to enhance readability and explain the purpose behind key sections of the code.

### **Performance Enhancements**

1. **Faster Data Loading:**
   We switched from **read_csv** to a **binary format** for faster data loading, reducing the time it takes to process and display data. This was a significant performance improvement.

2. **Caching:**
   We implemented **caching** for all charts to improve rendering speed, making the dashboard more responsive, especially when interacting with different filters.

### **Code and UI Refinements**

1. **Code Structure:**
   To improve the maintainability of the project, we moved the layout code from the main `app.py` file into a separate file. This modular approach simplifies future updates and enhances collaboration.

2. **UI Enhancements:**
   - Enhanced the **collapsible button description** and added a **disclaimer** in the sidebar to clearly highlight data limitations.
   - Ensured that **line chart colors remain consistent** across different selections to avoid confusion.
   - Fixed minor **formatting issues** to improve UI consistency.

### **Branding Enhancements**

We updated the **favicon** and changed the browser tab title from "Dash" to our dashboard’s name. These branding updates contribute to a more professional and polished look.

### **Deviations from the Proposal**

1. **Tabbed Navigation:**
   Instead of displaying all four charts on a single page as originally planned, we implemented **tabbed navigation** for better usability. This allows users to focus on one section of data at a time, improving the dashboard’s overall clarity and flow.

2. **Refined Year Filtering:**
   Rather than applying **year filters globally**, we introduced a **dropdown in the second tab** for focused analysis. This makes it easier to filter and examine data by specific years without overwhelming the user.

3. **Handling of Missing Data:**
   The dashboard now explicitly informs users when their selections result in **no data**, enhancing usability by providing immediate feedback instead of leaving users with empty visualizations.

4. **Header Button Addition:**
   Added an **About** button in the header to provide quick context about the dashboard’s purpose, which was not part of the original plan but significantly improves the user experience.

### **Limitations and Areas for Improvement**

1. **Rendering Performance:**
   While we implemented performance improvements, the dashboard still experiences **slow rendering** when accessed via the demo link due to **Altair’s processing time**. This could potentially impact user experience, especially when working with large datasets or numerous filters.

2. **Y-Axis Scaling Considerations:**
   Although we fixed the **y-axis scale** for the trend line chart to maintain consistency across filters, the **bar chart** does not have a fixed y-axis scale. This is because extreme values, particularly at the executive level, could distort the visualization if a fixed scale were applied. This remains a challenge for the bar chart’s effectiveness in certain scenarios.

### **Insights and Feedback Reflection**

One key insight we gained this week was from feedback on the clarity of the map visualization. Initially, our map was cluttered with excessive geographical areas, which detracted from its effectiveness. By removing Antarctica, we were able to streamline the visualization and allow the remaining regions to have more focused attention. This was a valuable realization about how minor adjustments in visualization can significantly enhance clarity.

Additionally, the feedback we received regarding interactivity highlighted that users preferred smoother transitions between data views, leading to the decision to incorporate tabbed navigation. The ability to switch between trends and yearly data seamlessly has proven to improve the user experience substantially.

However, one aspect that could have further supported the development of a high-quality dashboard would be more detailed user testing focused on edge cases or rare data combinations. While the overall functionality is solid, having more input on how users interact with the dashboard in real-world scenarios could help refine it further.
