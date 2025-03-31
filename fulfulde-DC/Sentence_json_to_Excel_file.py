import json
import pandas as pd

# Read JSON file
with open('sentences_dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create list of dictionaries with English and Fulfulde pairs
processed_data = []
for entry in data:
    processed_data.append({
        'English': entry.get('source', ''),
        'Fulfulde': entry.get('target', '')
    })

# Create DataFrame and save as Excel
df = pd.DataFrame(processed_data)
df.to_excel('translations.xlsx', index=False, engine='openpyxl')

print("Excel file created successfully!")