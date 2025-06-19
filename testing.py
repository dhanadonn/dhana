#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to My Simple Python Web Page</h1><p>This is created using Flask!</p>'

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




