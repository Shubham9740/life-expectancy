# Life Expectancy Visualizer

A Python-based data visualization tool that analyzes WHO life expectancy data by gender and predicts future trends using linear regression.

## Features

- **Gender-based analysis** - Separate visualization for male, female, and combined life expectancy
- **Color-coded graphs** - Blue for males, red for females, purple for both sexes
- **Future predictions** - Predicts life expectancy for the next 2 years based on historical trends
- **Country-specific insights** - Analyze any country in the WHO database
- **Statistical summaries** - View latest values and predicted trends for each gender category

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Required Libraries
Install the required packages using pip:

```bash
pip install pandas matplotlib
```

Or create a `requirements.txt` file with:
```txt
pandas>=1.3.0
matplotlib>=3.4.0
```

Then install with:
```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Get the Data
Download the WHO life expectancy dataset and save it as `Life expectancy at birth.csv` in the same directory as the script.

**Expected CSV structure:**
- ParentLocationCode
- ParentLocation
- SpatialDimValueCode
- Location
- Period
- Dim1 type
- Dim1 (gender: Male, Female, Both sexes)
- Dim1ValueCode
- FactValueNumeric
- FactValueNumericLow
- FactValueNumericHigh
- Value
- Language
- DateModified

### Step 2: Run the Script
```bash
python life_expectancy_graph.py
```

### Step 3: Enter Country Name
When prompted, type the country name you want to analyze:
```
Enter country name: Japan
```

### Step 4: View Results
The script will display:
- Statistical summary for all gender categories
- 2-year predictions for each category
- A color-coded graph showing historical data and predictions

## Example Output

```
==================================================
Life Expectancy at Birth - Data Visualization
==================================================

Total countries available: 195

Enter country name: Japan

Japan - Life Expectancy Statistics
--------------------------------------------------
Data available: 2000 - 2019
Latest life expectancy (Both sexes): 84.4 years
Predicted (Both sexes) - Year 2020: 84.6 years
Predicted (Both sexes) - Year 2021: 84.8 years
Latest life expectancy (Male): 81.5 years
Predicted (Male) - Year 2020: 81.7 years
Predicted (Male) - Year 2021: 81.9 years
Latest life expectancy (Female): 87.3 years
Predicted (Female) - Year 2020: 87.5 years
Predicted (Female) - Year 2021: 87.7 years

Graph displayed successfully!
```

## Understanding the Graph

The graph displays three color-coded lines:

- **Blue line** - Male life expectancy
  - Solid line with dots = Historical data
  - Dashed line with dots = Predictions
  
- **Red line** - Female life expectancy
  - Solid line with dots = Historical data
  - Dashed line with dots = Predictions
  
- **Purple line** - Both sexes combined
  - Solid line with dots = Historical data
  - Dashed line with dots = Predictions

- **Vertical dotted line** - Separates historical data from predictions
- **X-axis** - Years
- **Y-axis** - Life expectancy in years

## How It Works

### Prediction Algorithm

The tool uses **linear regression** to forecast future life expectancy for each gender category:

1. **Data Separation**: Splits data into three categories (Male, Female, Both sexes)
2. **Gradient Calculation**: For each category, computes the trend line slope using least squares:
   ```
   gradient = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)
   intercept = (Σy - gradient × Σx) / n
   ```
3. **Prediction**: Projects future values by extending each trend line:
   ```
   predicted_life_expectancy = gradient × future_year + intercept
   ```
4. **Individual Trends**: Each gender category has its own gradient, allowing for gender-specific predictions

### Why Track Life Expectancy by Gender?

Life expectancy differences by gender reveal important health patterns:
- Women typically live longer than men globally
- Gender gap varies significantly by country and region
- Trends can indicate healthcare improvements or disparities
- Helps policymakers target health interventions effectively

## Data Source

This project uses WHO (World Health Organization) Global Health Observatory data.

Download the dataset from: [WHO Global Health Observatory](https://www.who.int/data/gho)

Look for "Life expectancy at birth" dataset.

## Limitations

- **Linear assumption**: Assumes life expectancy trends continue linearly
- **Short-term predictions**: Best suited for 2-year forecasts
- **Unpredictable events**: Cannot account for pandemics, wars, or major policy changes
- **Data dependency**: Accuracy depends on WHO data quality and completeness
- **Country-level only**: Does not analyze regional or socioeconomic variations within countries

## Troubleshooting

### Country Not Found
If you get "No data found for [country name]", the script will show suggestions. Common issues:
- Check spelling (e.g., "United Kingdom" not "UK")
- Use the full official name
- Some regions may be listed separately from countries

### Incomplete Gender Data
Some countries may only have data for "Both sexes" and not separate male/female data. The graph will display whichever categories are available.

### Graph Not Displaying
- Ensure matplotlib is properly installed
- Check if you're in a GUI-enabled environment
- On some systems, you may need to run in interactive mode

## Project Structure

life-expectancy-visualizer/
├── life_expectancy_graph.py           # Main script
├── Life expectancy at birth.csv       # WHO data (user provided)
├── requirements.txt                   # Python dependencies
└── README.md                          # This file

## Interpreting Results

### Gender Gap Analysis
The difference between male and female lines shows the gender life expectancy gap:
- Larger gap = Greater difference in life expectancy between genders
- Converging lines = Gap is closing over time
- Diverging lines = Gap is widening

### Trend Analysis
- **Rising lines** = Life expectancy is improving
- **Flat lines** = Stagnant life expectancy
- **Declining lines** = Life expectancy is decreasing (rare, but can indicate crisis)

### Predictions Reliability
Predictions are most reliable when:
- Historical data shows consistent trends
- At least 5-10 years of data available
- No major disruptions in recent years

## Future Enhancements

Planned improvements include:
- [ ] Confidence intervals for predictions
- [ ] Multi-country comparison on single graph
- [ ] Gender gap analysis calculator
- [ ] Export graphs as PNG/PDF
- [ ] Historical event markers (pandemics, policy changes)
- [ ] Regional/income level comparisons
- [ ] Interactive web dashboard
- [ ] Advanced models (polynomial, exponential trends)

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- World Health Organization (WHO) for providing comprehensive health statistics
- Python data science community for matplotlib and pandas
- All contributors and users of this project

## Contact

For questions, suggestions, or bug reports, please open an issue on GitHub.

## Real-World Applications

This tool can be useful for:
- **Students** - Learning about global health trends and data analysis
- **Researchers** - Quick visualization of life expectancy patterns
- **Public Health Officials** - Monitoring progress toward health goals
- **Journalists** - Creating data-driven stories about health trends
- **Educators** - Teaching statistics and demographic analysis

**Note**: Always use the latest WHO dataset for the most accurate analysis. Life expectancy data is typically updated annually.