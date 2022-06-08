# chicken-feeder-bot

## Steps
1) make sure you have the required libraries (pip install requests, pip install requests)
2) Get auth token by pasting this in the url 
 https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=<client_id>&redirect_uri=http://localhost:443&scope=whispers%3Aread+chat%3Aread+chat%3Aedit+channel%3Aread%3Asubscriptions+channel%3Aread%3Asubscriptions
3) paste the authorization code into the run.py file token=<your token from step 2>
4) run bot.py
