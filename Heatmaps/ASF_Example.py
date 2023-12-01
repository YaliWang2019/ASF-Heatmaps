import asf_search as asf

opts = {'platform': asf.SENTINEL1, 'processingLevel': asf.SLC}

count = asf.search_count(**opts) # search_count() is a light-weight way to preview result set sizes
print(count) # about 2.3 million

opts['maxResults'] = 10 # limit our results for quicker experimentation

results = asf.search(**opts)
print(results[0]) # note the 'geometry' attribute of each result