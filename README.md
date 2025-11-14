# fuzzy-engine
My data analytics project about handmade crafts. I explore Etsy data to see what’s popular and learn more about trends in crochet, knitting, macrame, jewelry and other DIY. That was the plan. Unfortunatey I did not receive API (v3) kety for Etsy on time, so I had to change it. I was planning to collect live marketplace data. The project was completed using an open dataset containing Etsy shops statistics. The analytical goal remains the same - exploring trends in handmade shops, understanding factors affecting performance, and building predictions.

# dataset Content
This Etsy handmade shop dataset contains information about online shops selling handmade products.
Each row represents a single shop, and the columns are described below:
creation_date – the date when the shop was created.
listing_active_count – number of currently active products listed in the shop.
num_favorers – number of users who marked the shop as a favourite.
currency_code – shop’s primary currency.
is_shop_us_based – TRUE/FALSE flag indicating whether the shop is located in the U.S. (I’m planning to delete this column as I’m more interested where are shops mainly from)
sale_message – TRUE/FALSE flag indicating whether the shop displays a marketing message (e.g. promotions)
sales_count – total number of sales completed by the shop.
review_count – number of customer reviews.
shop_location – textual description of the shop’s geographic location.

Date downloaded: 11/11/2025 
https://www.kaggle.com/datasets/sepidafs/etsy-shops
 Original plan: Etsy API v3 data extraction.
 Final approach: analysis of an available dataset due to delayed API key approval.

# business requirements
To understand how shop attributes and buyer engagement influence the performance of handmade online shops, and to identify key factors that help predict shop sales.

# hytheses and analytical approaches

H1: Shop performance varies by geographic region
Hypothesis: Find out which location in Europe may influence higher sales, due to larger customer markets.
 Figure 1: Number of shops by world region (bar chart)
 Figure 2: Sales distribution per region (boxplot)

H2: Sales increase with shop age and number of active listings
Hypothesis: Older shops with more active products generate more sales.
 Figure 3: Sales Count vs Shop Age (scatterplot)
 Figure 4: Sales Count vs Number of Listings (scatterplot with trendline)

H3: Shops with marketing enabled (“sale_message = TRUE”) perform better
Hypothesis: Shops using marketing or promotion messages achieve higher sales and more reviews.
 Figure 5: Sales by Marketing Status (boxplot)
 Figure 6: Reviews vs Marketing Status (bar chart)

H4: Customer engagement (favourers, reviews) is correlated with sales
Hypothesis: Shops that receive more favourites and reviews have higher sale counts.
 Figure 7: Correlation heatmap (num_favorers, review_count, sales_count)

# project plan
The dataset was imported into Python and processed through a structured ETL workflow.
Data Cleaning & Preprocessing;
-Dropped the column is_shop_us_based as it was inconsistent and not relevant for analysis.
-Parsed the creation date by extracting the year from the text (all dates correspond to 2019).
 (Parsing = splitting text into meaningful components.)
-Converted boolean variables (TRUE/FALSE) into 1/0 for analysis and modelling.
-Checked and handled missing values across numerical and categorical fields.
-Removed duplicates to ensure each shop appeared only once.

# location processing & classification
Shop location data was messy and inconsistent across entries.
To make geographic analysis possible:
-Extracted country names when available.
-When only a city/region was given, inferred the country where possible.
-If currency_code = “USD” and no country was listed → shop assumed to be U.S.-based.

# Exploratory Data Analysis (EDA)
EDA was conducted using Seaborn, Matplotlib, and Plotly, including:
Histograms and KDE plots for variable distributions
Scatterplots for relationships between shop attributes and sales
Boxplots for comparing marketing vs non-marketing shops
Correlation heatmaps for numerical variables
Bar charts for location-based analysis
All visualisations supported hypothesis evaluation.

# Business Requirements → Visualisations
Geographic effects explored through bar charts and sales distributions
Shop age and listing activity analysed using scatterplots with trendlines
Marketing influence visualised using grouped boxplots
Engagement metrics investigated through correlation matrices and scatterplots

This combination of plots clarified how different shop-level factors contribute to performance.

# Analysis Techniques Used
All analysis was completed using Python (3.14) in Visual Studio Code.
Key tools and modules:
pandas and NumPy – ETL and preprocessing
Matplotlib and Seaborn – static visualisations
scikit-learn – simple regression model predicting sales
Copilot – debugging assistance and plot styling suggestions

Preprocessing steps included extracting shop_age, cleaning locations, encoding boolean fields, and outlier inspection.

# summary of findings

# Ethical Considerations
-Dataset contains no personal or customer-identifiable information (GDPR compliant).
-Location data required assumptions due to inconsistent formatting.
-All shops were assumed to sell handmade products since product-level data is unavailable.

# unfixed Bugs

# Development Roadmap
Challenges included:
-Changes in project scope (API → downloaded dataset)
-Cleaning inconsistent location text
-Ensuring correct numeric encoding

Future goals:

# Main Data Analysis Libraries
numpy  
pandas  
matplotlib  
seaborn  
plotly  
scikit-learn

# Credits
- Code Institute Data Analytics Bootcamp learning materials
- Copilot for debugging and visualisation suggestions
