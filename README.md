# 📊 ANVI - Data Analysis and Visualization Dashboard  

ANVI (**A**nalytics **N** **Vi**sualization) is a powerful **data analysis and visualization dashboard** built using **Django** and **Matplotlib/Plotly**. It allows users to **upload datasets, perform data preprocessing, and generate insightful visualizations** through an intuitive UI.  

## 🔥 Features  
- 📂 **Dataset Upload:** Supports CSV file uploads for analysis.  
- 🛠 **Data Preprocessing:** Handles missing values, duplicates, and basic transformations.  
- 📊 **Interactive Visualizations:** Generates **bar charts, line graphs, scatter plots, heatmaps, and more** using **Matplotlib & Plotly**.  
- 🔍 **Filter & Search:** Allows filtering data based on specific conditions.  
- 🎯 **User-Friendly UI:** Built using Django templates for a smooth user experience.  

## 🏗️ Tech Stack  
- **Backend:** Django, Pandas, NumPy  
- **Frontend:** HTML, CSS
- **Data Visualization:** Matplotlib, Plotly  
- **Database:** SQLite / PostgreSQL (configurable)  


## 🚀 Installation & Setup  
### **Prerequisites**  
Ensure you have **Python 3.8+** and **pip** installed.  


## 📸 Screenshots  


### Home
![Image](https://github.com/user-attachments/assets/12514ada-a1b0-4233-8c93-64f9fba5cb62)



### Login Page
![Image](https://github.com/user-attachments/assets/19965d02-067f-4a0c-b433-85c6418cc908)



### Uploading Dataset
![Image](https://github.com/user-attachments/assets/fc040048-d26c-4240-8549-5145718cca87)



### Upload List
![Image](https://github.com/user-attachments/assets/3bf5980d-88a3-4ab2-966d-0fac36318e30)



### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/rakeshputakala/ANVI
cd ANVI
```

### **Step 2: Create a Virtual Environment**

```bash
python -m venv venv  
source venv/bin/activate  # On Windows use: venv\Scripts\activate  
```

### **Step 3: Install Dependencies**

```bash
pip install django
pip install Numpy
```

### **Step 4: Apply Migrations**

```bash
python manage.py migrate  
```

### **Step 5: Run the Development Server**

```bash
python manage.py runserver  
```


### **1️⃣ Upload a Dataset**

- Click on **"Upload Data"** and select a CSV file.
- The system will read the dataset and display a preview.

### **2️⃣ Preprocess the Data**

- Handle missing values by choosing options like drop, fill with mean, etc.
- Remove duplicates and apply basic transformations if needed.

### **3️⃣ Generate Visualizations**

- Choose a visualization type:
  - 📊 **Bar Chart**
  - 📈 **Line Graph**
  - 🔘 **Scatter Plot**
- Select the relevant columns and generate the graph.

### **4️⃣ Analyze Summary Statistics**

- View mean, median, standard deviation, and correlation metrics.
- Download the summary report if needed.

### **5️⃣ Export & Download**

- Save the **processed dataset** or **visualizations** in CSV, PNG, or PDF formats.


## 🌟 Show Your Support

If you find this project useful, **⭐ star this repository** and contribute!



