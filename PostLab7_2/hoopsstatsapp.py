"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(df):
  
    columns_to_clean = ['FG', '3PT', 'FT']
    
    for col in columns_to_clean:
        if col in df.columns:
          
            idx = df.columns.get_loc(col)
            
         
            new_col_makes = col + "M"
            new_col_attempts = col + "A"
            
         
            split_data = df[col].fillna("0/0").str.split("-", expand=True)
        
            if split_data.shape[1] < 2:
                split_data = split_data.reindex(columns=range(2), fill_value="0")
            
          
            split_data[0] = pd.to_numeric(split_data[0], errors='coerce')
            split_data[1] = pd.to_numeric(split_data[1], errors='coerce')
            
          
            df.drop(columns=col, inplace=True)
            
        
            df.insert(loc=idx, column=new_col_makes, value=split_data[0])
            df.insert(loc=idx + 1, column=new_col_attempts, value=split_data[1])
    
    return df


def main():
    """Loads the CSV, cleans the stats, and launches the view."""
    try:
        frame = pd.read_csv("cleanbrogdonstats.csv")
        frame = cleanStats(frame)  # Clean the stats using the dataframe read from CSV
        app = HoopStatsView(frame)  # Instantiate the view with the cleaned data
        app.mainloop()              # Start the GUI event loop
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
