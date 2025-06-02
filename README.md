 📊 Marketing Campaign Data Cleaning

This project involves cleaning and preprocessing a marketing campaign dataset using ‘Python’ and ‘pandas’. The objective is to prepare the data for further analysis or machine learning by handling missing values, formatting dates, standardizing text fields, and exporting the cleaned dataset.


📁 Dataset

The dataset is provided in Excel format: Marketing campaign Dataset

✅ Tasks Performed

- Loaded the dataset using `pandas.read_excel()`.
- Checked for null values and removed rows with missing `Income`.
- Checked for duplicates (none found).
- Converted date column `Dt_Customer` to `datetime` format.
- Created a new column `customer_tenure` based on current year minus joining year.
- Standardized text columns (`Education`, `Marital_Status`):
- Trimmed whitespace
- Replaced spaces with underscores
- Mapped `"Alone"` to `"Single"`
- Converted all column names to lowercase for consistency.
- Exported cleaned DataFrame to a new Excel file.
