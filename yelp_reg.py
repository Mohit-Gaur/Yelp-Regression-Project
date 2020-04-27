import pandas as pd

businesses = pd.read_json('yelp_business.json',lines=True)
reviews = pd.read_json('yelp_review.json',lines=True)
users = pd.read_json('yelp_user.json',lines=True)
checkins = pd.read_json('yelp_checkin.json',lines=True)
tips = pd.read_json('yelp_tip.json',lines=True)
photos = pd.read_json('yelp_photo.json',lines=True)

pd.options.display.max_columns = 60 #In order to more clearly see the information in our DataFrame
pd.options.display.max_colwidth = 500

#Inspecting the first 5 rows of each dataframe
businesses.head()

reviews.head()

users.head()

checkins.head()

tips.head()

photos.head()

print(len(businesses))
print(reviews.columns)
