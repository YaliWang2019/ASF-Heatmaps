from time import perf_counter

import asf_search as asf
asf.CMR_TIMEOUT = 120 # just in case CMR is being grumpy

opts = {
    'platform': 'SENTINEL-1',
    'processingLevel': 'SLC',
    'beamMode': 'IW',
    'start': '2022-01-01T00:00:00Z',
    'end': '2022-12-31T23:59:59Z'
}
print(asf.search_count(**opts))

start = perf_counter()
results = asf.search(**opts)
end = perf_counter()

print(f'Fetched {len(results)} in {(end - start)} seconds')