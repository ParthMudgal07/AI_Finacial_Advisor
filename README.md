AI Financial Advisor

An interactive AI-powered financial dashboard built with Python and Streamlit.
Upload your raw financial CSV data, and the app provides:

Cleaned and processed data

Interactive visualizations (Line, Bar, Area, Scatter, Pie)

AI-generated insights using Google Gemini AI

Key metrics and anomaly detection

🚀 Features

File Upload & Data Cleaning

Upload any CSV financial data without preprocessing.

Automatic cleaning and processing using pandas and custom clean_financial_data function.

Interactive Visualizations

Choose numeric columns for X and Y axes.

Multiple chart types: Line, Bar, Area, Scatter, Pie.

Dynamic charts rendered inside the Streamlit app.

AI-Powered Insights

Uses Google Gemini AI to analyze your dataset.

Generates structured insights: trends, outliers, top categories, suggestions for further analysis.

Dashboard Layout

Tabs for Raw Data, Processed Data, Graphical Illustrations, and AI Insights.

Sidebar for file upload and plot selection.

Metrics displayed in card-style format (min, max, mean).

Expanders for raw and processed data to reduce clutter.

📦 Technologies & Libraries

Python 3.x

Streamlit – Web app framework

pandas – Data processing

matplotlib – Plotting and visualization



🔧 Installation

Clone the repository:

git clone https://github.com/your-username/ai-financial-advisor.git
cd ai-financial-advisor


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install required packages:

pip install -r requirements.txt


Add your Gemini API key in a .env file:

GEMINI_API_KEY=your_api_key_here

⚡ Usage

Run the Streamlit app:

streamlit run app.py


Upload your CSV file in the sidebar.

Explore Raw Data and Processed Data tabs.

Use Graphical Illustrations tab to select columns and chart types.

View AI Insights tab for structured analysis and recommendations.


📝 Notes

The app automatically detects numeric columns for plotting.

AI insights are generic and depend on the uploaded dataset.

For Pie charts, the app aggregates Y-axis values by X-axis categories.

📄 License

MIT License – feel free to use, modify, and share.

python-dotenv – Environment variable management

Google Generative AI (genai) – AI insights generation
