# **Milestone 2 - Reflection**

In this milestone, we successfully implemented a functional prototype of our **DataSalaries Dashboard** based on our proposal. The following key features have been integrated:

### **✅ Implemented Features**

- **Dashboard Title**: A clear, informative title enhances usability.
- **Interactive Filters**: Users can dynamically filter the data using checklists for: `Job Title`, `Experience Level`, `Employment Type`, `Remote Type`.
- **Data Preprocessing & Cleaning**: Grouped similar job titles to improve readability. Processed experience levels and employment types for better clarity.
- **Visualizations**:
    - **Trend Line Chart**: Displays salary trends over time.
    - **Bar Chart**: Shows salary distribution by experience level.
    - **Donut Chart**: Represents salary distribution by company size.
    - **Donut Chart**: Displays salary breakdown by remote work type.
-   **UI & Styling Enhancements**: Applied a **clean, structured layout** for easy navigation. Implemented **distinct color palettes** for different variables to improve contrast and readability.

### **Deviations from Proposal**

- **🚫 Removed Year Filter**: Initially planned as a filter, but removing it was necessary as filtering to a single year made the **trend line meaningless**.
- **🚫 Excluded Map Chart**: Since most jobs in the dataset were **from the US**, the map visualization was highly imbalanced and **did not provide meaningful insights**.

## **Reflection on Visualization Choices**

We followed **DSCI 531 best practices** for effective visualizations:

✅ **Minimal Clutter**: Focused on key insights without overwhelming users.
✅ **Distinct Color Palettes**: Different charts use separate color schemes for clarity.
✅ **Proper Axis Labels & Legends**: Ensured all visualizations are properly labeled.
✅ **Grid-Based Layout**: Structured the dashboard to maximize readability.

## **What Our Dashboard Does Well**

✅ **Clear salary trends** across job roles, experience levels, and employment types.
✅ **Interactive filters** for dynamic exploration.
✅ **Clean, structured UI** with good readability.
✅ **Multi-year salary insights** instead of focusing on single-year snapshots.

## **Current Limitations & Future Improvements**

- **Donut Chart Improvements** → Proportion numbers are currently only visible via tooltips. The initial plan was to display them directly on the donut charts, but this requires more time. This could be a potential improvement for next week.
- **Color Palette & UI Enhancements** → The dashboard is currently using the default template from our class notes, but refining the overall color palette and background could improve its visual appeal.
- **No Regional Salary Comparison** → Since the map was removed, **adding a country location filter categorized into major regions** (e.g., **US, Canada, Europe, Asia**) would allow users to compare salaries across different locations. **This is especially useful for those looking for jobs in Canada and the US, where salary differences can be significant.**

## **7. Implement More of Your Proposal (Challenging)**

Our dashboard already includes **eight interactive components**: **four filters** (job title, experience level, employment type, and remote type) and **four charts** (salary trend, experience level, company size, and remote type). Instead of adding extra components, we focused on improving the **dashboard’s functionality and visualization choices** to ensure the most **effective data representation**.

These improvements are useful because they:
- **Enhance interactivity** by ensuring filters update smoothly.
- **Prevent errors** when filters result in no matching data.
- **Improve performance** by reducing unnecessary calculations.
- **Ensure clarity** by choosing the most suitable visualizations.

By refining both **functionality and visualization choices**, we created a **clearer, faster, and more user-friendly dashboard** that helps users analyze salary trends effectively.