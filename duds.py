



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
