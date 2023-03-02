# News to you email script
Script that helps user to receive selected 
news over the email.

### Special Requirements
You need to have Gmail account

### Script instructions
1. Get your API key from https://newsapi.org/
2. Replace `api_key` variable with your personal api_key
3. News topics can set inside `url` variable, under `q` parameter
4. Specify your email.
   - Create a custom Application password in your Google Account

### Description: 
Script is generating email with a selected news. As of now you need to manually 
go inside the script and change topics and relevance of the news. News are coming from: https://newsapi.org/

### TODOs
- [ ] Implement CLI interface
- [ ] Implement News theme selection via cli
- [ ] Implement news relevance selection via cli
- [x] Implement delta time

