# InstagramSalesHelper
A Python project that I am working on my spare time. InstagramSalesHelper is a helper tool for IG Business accounts that are selling products.

The project is consisting of Selenium, FaceBook Graph API, Instagram Graph API which are renewed official API's of Instagram for 
Business Accounts. Selenium is automating for user login and accept the requested permissions from API's.

I made this project in order to practise Python, the new Facebook and Instagram API's. I also believe that it will be useful tool for IG
accounts that are selling products.

Current Usage: (Also explained in documents I shared in detail)
1) Create a Facebook Developer Account and create an app. 
2) Add FacebookLogin and Instagram products to the app.
3) Configure the FacebookLogin product.(Except redirect url can be kept default)
4)Insert Instagram Business Account(which must be connected to a FacebookPage) email and password to the UserCredentials class.
5) Insert your Facebook Developer App datas to the AppCredentials Class.
6) Enjoy.

Current planned aims of this project are:
    1)Reading from a .txt file that contains URL links of jpeg images every line. The jpeg images are expected to be user's product images.
After getting every jpeg url line, InstagramSalesHelper will automatically publish the image to IG as a post with user defined captions.
(Since content publishing of Instagram Graph API is in closed beta this have to wait :( )
    2) Since I am creating this project as a sandbox and for practising purposes, I created a class called AppCredentials which consists
of private data like client-id and app-secrets. This creates a huge security flaw for the entire project. Putting the Facebook Developer
app data into a server and handling them privately from there is a must. For now, all the data that should be kept private are left blank.

Current features are:
    1)Automated log in when app credentials and user credentials are properly defined. Generates all the necessary data automatically after
the login.
    2) Ready to consume any Facebook/Instagram API endpoint 
    
Current bugs:
    1) Selenium throws exception when any unexpected window is displayed. Especially when a permission window is displayed. 
    
Some documentations and explanatory documents(That helped me learn which might also help you):
https://developers.facebook.com/docs/graph-api/
https://developers.facebook.com/docs/instagram-api/
https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/ (For desktop apps)
