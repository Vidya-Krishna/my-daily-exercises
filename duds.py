#pip install nsetools
#Learning for not to buy stock! 

from nsetools import *

nse = Nse() #creted an object
ticker_symbols = nse.get_stock_codes()  #accessing method get_stock_codes using obj nse, an instance of class Nse
print(ticker_symbols)   #get_stock_codes() returns list

"""'get_future_quote'
""" 
#'get_stock_codes' returns a list
#get_quote(code, all_data=False) returns dict
#is_valid_code("code") returns bool
#get_52_week_low() returns a dict
#get_index_quote(index = "NIFTY") returns a dict
#get_index_list returns list
#get_all_index_quote returns dicts, multiple dicts in a list == isn't this **kwargs
#get_top_gainers(index="NIFTY") returns list of dictionaries
#get_advances_declines(index="NIFTY") returns a single dict {"advances": int, "declines": int}
#get_stocks_in_index returns a list: ticker symbols of stocks
# get_stock_quote_in_index returns a list of dict

# print(nse.get_quote('abb', all_data=True))    #kaput
# print(nse.is_valid_code("DRONACHARYA"))
                    #----------------------------------------------------
print(nse.get_52_week_high())                 #worked once, from then it did not.
try:
    result = nse.get_52_week_high()
    print(result)
except Exception as e:
    print("Something went wrong:", e)
"""
NSE might be blocking scripts
API endpoint might be down
nsetools might be outdated
"""
                    #----------------------------------------------------
print(nse.get_index_quote(index="NIFTY 50"))
print(nse.get_index_list())
print(nse.get_all_index_quote())
print(nse.get_top_gainers(index="NIFTY"))
print(nse.get_top_losers(index="NIFTY"))
print(nse.get_advances_declines(index='nifty 50'))
print(nse.get_stocks_in_index(index="NIFTY 50"))



#------------------------------------------------------------
#DUD NO. 2
#Tried unsing pytube 
from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=VIDEO_ID'

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

stream.download(output_path='~/Downloads')

print("Download complete!")

#------------------------------------------------------------
#DUD NO. 1
# make a line a comment line
def comment_code_blocks(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    in_comment_block = False
    modified_lines = []
    
    for line in lines:
        if line.strip() == "#-----":
            in_comment_block = not in_comment_block
            modified_lines.append(line)
        elif in_comment_block and not line.strip().startswith('#'):
            modified_lines.append(f"# {line}")
        else:
            modified_lines.append(line)
    
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    
    print(f"Processed file: {file_path}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        comment_code_blocks(file_path)
    else:
        print("Please provide a file path as an argument")
