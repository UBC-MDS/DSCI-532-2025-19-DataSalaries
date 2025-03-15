## **Milestone 4 - Reflection**

This week, our team focused on **refining** the **DataSalaries Dashboard**, incorporating user feedback, and addressing areas that could further enhance both **usability** and **visual clarity**. Additionally, we made several **performance improvements** to speed up data loading and enhance user experience. These included **binary data format loading**, **caching for specific functions**, and various updates to the dashboard’s UI, such as setting a **favicon**, updating the **GIF animation**, and refreshing outdated **screenshots and descriptions** in the README. We also **added docstrings for functions** to improve code documentation and maintainability.

### **Implemented Features**

#### 1. **Tabbed Layout for Improved Data Organization (#81)**
   We introduced a **tabbed layout** to better organize the dashboard into two distinct sections: one displaying **trends over time** with line and bar charts, and the other showcasing **yearly data** with a map and pie charts. This new layout enhances **navigation** by clearly separating different types of data, allowing users to easily focus on either trends or yearly statistics. The tabs provide a more structured user experience, improving usability by reducing clutter.

#### 2. **Dropdown for Data Selection and No Data Handling (#82)**
   We added a **dropdown menu** on the second tab to enable users to filter yearly data. Additionally, we implemented a **text notification** that informs users when no data is available for a specific selection. This feature prevents the dashboard from appearing broken when certain data is missing and ensures a seamless user experience, especially when users may choose filters that result in empty datasets.

### **Minor Updates**

#### 1. **Collapsible About Section (#83)**
   We introduced a **collapsible "About" section** that provides background information about the dashboard and its data. This feature improves the user interface by keeping the layout clean while still offering additional details when needed.

#### 2. **Map Refinement: Removal of Antarctica (#84)**
   To enhance the map’s focus, we decided to **remove Antarctica**. This adjustment allows the rest of the map to expand and makes the visual display cleaner, focusing the user’s attention on the relevant data regions. This change contributes to a more visually balanced presentation.

#### 3. **Consistency in Y-Axis Scale (#85)**
   We ensured that the **y-axis scale** remains consistent across different filters. This update improves data comparison by providing a more stable reference point, allowing users to evaluate trends and data points more easily without having to adjust to shifting scales.

#### 4. **Font Size Increase for Year on X-Axis (#88)**
   To improve readability, we **increased the font size** for the **year labels** on the x-axis. This small change improves the clarity of the time-based data and makes it easier for users to understand trends over time, particularly for those viewing the dashboard on smaller screens.

#### 5. **Legend Enhancement (#86)**
   We made adjustments to the **legend** by displaying the **full names** of job titles rather than abbreviations. This change improves the clarity and usability of the dashboard, ensuring that users can quickly and accurately interpret the data represented by each color.

#### 6. **Color Consistency in Line Chart (#87)**
   To ensure that the **line chart** remains consistent, we fixed the color mappings for job titles. Now, the colors are **mapped consistently** to the same job titles regardless of the filter or selection, preventing confusion and making the chart easier to understand.

### **Changes from Proposal**

- The **tabbed layout** was added as a response to usability concerns from earlier iterations, offering a clearer way to present different data views (trends vs yearly data).
- The **dropdown filter** and **text notification for no data** were introduced to improve user interaction and prevent a broken experience.
- We also **removed Antarctica from the map** for better map usability, deviating from the original design but improving visual clarity.

### **Reflection on Visualization and Functionality**

This week’s updates are in line with **DSCI 531 best practices**, focusing on **clear communication, effective design**, and **usability**:
- The **tabbed layout** significantly improves organization and navigation between data views.
- The **dropdown filter** and **text notification** enhance the user experience, especially when no data is available.
- **Consistency in color and axes** helps maintain clarity and avoids visual confusion, particularly in charts and maps.

However, there are still a few areas that need improvement:
- **Advanced Analytical Tools**: If we had more time, the addition of **advanced filtering** or **customizable data views** would allow users to interact with the data in more complex ways, offering deeper insights.
