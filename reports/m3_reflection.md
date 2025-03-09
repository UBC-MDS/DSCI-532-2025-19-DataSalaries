# **Milestone 3 - Reflection**

Since **Milestone 2**, we have focused on enhancing the **DataSalaries Dashboard** based on both the professor’s feedback and the evolving needs of the project. This week, we implemented several key features and improvements to **increase interactivity**, **improve usability**, and enhance **visual clarity**.

## **Implemented Features**

### 1. Map to Show Average Salary by Location
We added a **choropleth map** to visualize **average salary by location**, providing **geographic insights** into salary trends. Additionally, we introduced a **location dropdown filter** in the sidebar, making it easier for users to filter the data by specific regions. This map adds valuable interactivity, enabling users to compare salaries geographically and gain insights into regional salary trends.

### 2. Reorganization of Job Titles   
   To improve the layout and user experience, we reorganized the **job titles** into **five high-level categories**. This adjustment simplifies the filtering process, reducing the complexity of the job title list and improving the dashboard’s readability. The decision to group job titles into broader categories was made to enhance usability and minimize visual clutter, making it easier for users to navigate and filter data efficiently.

### 3. Updated Line Chart Color Scheme 
   To prevent confusion and improve readability, we updated the **line chart’s color scheme** to the **‘plasma’ gradient** (purple to yellow). This ensures the line chart is visually distinct from other charts, preventing misinterpretation and enhancing overall dashboard clarity.

### 4. Breaking Code into Multiple Files   
   This week, we also focused on improving the organization of our codebase by breaking it into multiple files. Previously, the code was inside one giant `app.py` file, which made it harder to manage and extend. By dividing the code into separate files, we made the project more modular and maintainable. This structure not only simplifies future updates but also improves collaboration among team members by making each component more easily understandable and editable.

### 5. Further App Refinement  
   We have continued refining the visualization and usability of our dashboard by implementing several improvements. These include sorting input selections alphabetically for better navigation, increasing legend font sizes to enhance readability, and adding currency labels to chart titles to provide clearer financial context.

## **Changes from Proposal**

- The **map visualization** was modified to display location-specific salary data instead of a generalized view, providing more actionable insights.
- The **company location filter** (dropdown selection) was added to enhance interactivity, deviating from our original static design.
- The **job title filter** was adjusted to broader categories rather than keeping every individual job title, improving filtering efficiency and addressing layout limitations.
- The **dashboard layout** was significantly restructured to allocate more space for key visualizations, ensuring a more balanced and user-friendly interface.

## **Reflection on Visualization and Functionality**

Our dashboard follows **DSCI 531 best practices**, prioritizing **clarity, usability, and accessibility**. 
- The newly added map and improved color scheme enhance visual differentiation and prevent misinterpretation. 
- The job title categorization makes the filtering process smoother.
- Overall, the layout changes also have improved readability.

However, minor areas for improvement remain:
- **Donut charts** may need further refinement to display proportional data more effectively.
- The **filtering process** can be further optimized for a more seamless experience.
- Additional **annotations** could be included in the trend chart to ensure insights remain visible when filtering by job title.

## **Looking Ahead**

In the next phase, we plan to:
- **Introduce a section button** to provide additional insights and improve the interface.
- **Enhance visual consistency** by refining colors and layouts for a more cohesive design.
- **Incorporate peer feedback** to make further usability improvements.

## **Get Inspiration from Peers (Challenging)**

Some of this week's updates were inspired by other groups. Specifically:

- **Dropdown input for location selection**: We adopted this idea from **Group 18**, which used a dropdown for city selection. Initially, we used checklists for all filters, but due to the long list of countries in our dataset, a dropdown was a more suitable option for improving usability.
- **Chart cards for improved layout**: Inspired by **Group 18**, we implemented chart cards to organize visualizations more effectively, making the dashboard look more structured and professional.
- **Rearranged layout for better clarity**: We took inspiration from **Group 17**, which placed key visualizations like the trend line and map at the top while keeping other elements below. This helped us refine our dashboard layout to enhance readability and navigation.

These peer-inspired improvements challenged us to rethink our design choices, leading to a more interactive, structured, and user-friendly dashboard.
