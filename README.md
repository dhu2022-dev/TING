# TING
TING Pavilion Consulting



## Testing Script
1. First, cd into "Testing Scripts" folder and run ```conda env create -f environment.yml```
2. Activate the conda environment using ```conda activate ting_dev```
3. Create a .env file and enter your client id and client secret via 
    - SPOTIFY_CLIENT_ID=[your id]
    - SPOTIFY_CLIENT_SECRET=[your secret]
4. Run ```python artist_retrieval.py```
5. Optionally, retrieve your access_token and then put it into the .env so you don't need to retrieve it every time
