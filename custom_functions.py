
# coding: utf-8

# In[1]:


import json
import requests as req


# In[3]:


geonames_username = get_file_contents('.geonames_username')


# In[4]:


def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)


# In[5]:


def get_zip_code(lat, lng):
    geonames_username = get_file_contents('.geonames_username')
    base_url = 'http://api.geonames.org/findNearbyPostalCodesJSON?'
    full_url = base_url + 'lat=%s&lng=%s&username=%s' % (lat, lng, geonames_username)
    
    zipcode = req.get(constructed_url).json()["postalCodes"][0]['postalCode']
    
    return zipcode

