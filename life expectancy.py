import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Life expectancy at birth.csv')
df = df[df['FactValueNumeric'].notna()]
countries = sorted(df['Location'].dropna().str.strip().unique())

print("=" * 50)
print("Life Expectancy at Birth - Data Visualization")
print("=" * 50)
print(f"\nTotal countries available: {len(countries)}")
print("Source","https://www.who.int/data/gho/data/indicators/indicator-details/GHO/life-expectancy-at-birth-(years)")

country_name = input("\nEnter country name: ").strip()
country_data = df[df['Location'] == country_name].copy()

if country_data.empty:
    print(f"\nNo data found for '{country_name}'")
else:
    country_data = country_data.sort_values('Period')
    male_data = country_data[country_data['Dim1'] == 'Male'].sort_values('Period')
    female_data = country_data[country_data['Dim1'] == 'Female'].sort_values('Period')
    both_data = country_data[country_data['Dim1'] == 'Both sexes'].sort_values('Period')
    
    def predict_years(data, num_years=2):
        if len(data) < 2:
            return None, None
        
        years = data['Period'].values
        values = data['FactValueNumeric'].values
        
        n = len(years)
        sum_x = sum(years)
        sum_y = sum(values)
        sum_xy = sum(years * values)
        sum_x2 = sum(years ** 2)
        
        gradient = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        intercept = (sum_y - gradient * sum_x) / n
        
        last_year = years[-1]
        future_years = [last_year + i for i in range(1, num_years + 1)]
        predictions = [gradient * year + intercept for year in future_years]
        
        return future_years, predictions
    
    male_future_years, male_predictions = predict_years(male_data) if not male_data.empty else (None, None)
    female_future_years, female_predictions = predict_years(female_data) if not female_data.empty else (None, None)
    both_future_years, both_predictions = predict_years(both_data) if not both_data.empty else (None, None)

    print(f"\n{country_name} - Life Expectancy Statistics")
    print("-" * 50)
    
    if not both_data.empty:
        print(f"Data available: {both_data['Period'].min()} - {both_data['Period'].max()}")
        if both_predictions:
            print(f"Predicted (Both) - Year {both_future_years[0]}: {both_predictions[0]:.1f} years")
            print(f"Predicted (Both) - Year {both_future_years[1]}: {both_predictions[1]:.1f} years")
    
    if not male_data.empty:
        
        if male_predictions:
            print(f"Predicted (Male) - Year {male_future_years[0]}: {male_predictions[0]:.1f} years")
            print(f"Predicted (Male) - Year {male_future_years[1]}: {male_predictions[1]:.1f} years")
    
    if not female_data.empty:
        
        if female_predictions:
            print(f"Predicted (Female) - Year {female_future_years[0]}: {female_predictions[0]:.1f} years")
            print(f"Predicted (Female) - Year {female_future_years[1]}: {female_predictions[1]:.1f} years")
    
    plt.figure(figsize=(12, 6))   
    
    if not male_data.empty:
        plt.plot(male_data['Period'], 
                 male_data['FactValueNumeric'], 
                 'o-', 
                 color='blue',
                 label='Male', 
                 linewidth=2, 
                 markersize=6)

        if male_predictions:
            plt.plot(male_future_years, 
                     male_predictions, 
                     'o--', 
                     color='blue',
                     alpha=0.6,
                     linewidth=2, 
                     markersize=6)

        if not female_data.empty:
            plt.plot(female_data['Period'], 
                 female_data['FactValueNumeric'], 
                 'o-', 
                 color='red',
                 label='Female', 
                 linewidth=2, 
                 markersize=6)

        if female_predictions:
            plt.plot(female_future_years, 
                     female_predictions, 
                     'o--', 
                     color='red',
                     alpha=0.6,
                     linewidth=2, 
                     markersize=6)

        if not both_data.empty:
            plt.plot(both_data['Period'], 
                 both_data['FactValueNumeric'], 
                 'o-', 
                 color='purple',
                 label='Both', 
                 linewidth=2, 
                 markersize=6)

        if both_predictions:
            plt.plot(both_future_years, 
                     both_predictions, 
                     'o--', 
                     color='purple',
                     alpha=0.6,
                     linewidth=2, 
                     markersize=6)

    if both_data.empty and not male_data.empty:
        last_year = male_data['Period'].max()
    elif both_data.empty and not female_data.empty:
        last_year = female_data['Period'].max()
    elif not both_data.empty:
        last_year = both_data['Period'].max()
    
    if 'last_year' in locals():
        plt.axvline(x=last_year + 0.5, color='gray', linestyle=':', linewidth=1)
        
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy (years)')
    plt.title(f'Life Expectancy at Birth for {country_name} ')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
