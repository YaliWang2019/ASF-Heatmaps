Example code:
import asf_search as asf

opts = {'platform': asf.SENTINEL1, 'processingLevel': asf.SLC}

count = asf.search_count(**opts) # search_count() is a light-weight way to preview result set sizes
print(count) # about 2.3 million

opts['maxResults'] = 10 # limit our results for quicker experimentation

results = asf.search(**opts)
print(results[0]) # note the 'geometry' attribute of each result

Results:
2366363
{
  "geometry": {
    "coordinates": [
      [
        [
          -37.684502,
          57.157383
        ],
        [
          -37.067875,
          58.654526
        ],
        [
          -41.399738,
          59.069122
        ],
        [
          -41.836529,
          57.56575
        ],
        [
          -37.684502,
          57.157383
        ]
      ]
    ],
    "type": "Polygon"
  },
  "properties": {
    "beamModeType": "IW",
    "browse": null,
    "bytes": 7150965102,
    "centerLat": 58.1295,
    "centerLon": -39.4877,
    "faradayRotation": null,
    "fileID": "S1A_IW_SLC__1SDH_20231121T085808_20231121T085833_051313_0630F0_2C76-SLC",
    "fileName": "S1A_IW_SLC__1SDH_20231121T085808_20231121T085833_051313_0630F0_2C76.zip",
    "flightDirection": "DESCENDING",
    "frameNumber": 398,
    "granuleType": "SENTINEL_1A_FRAME",
    "groupID": "S1A_IWDH_0399_0404_051313_141",
    "insarStackId": null,
    "md5sum": "5f1e0c4e68f4f99c57775e278ffa3d00",
    "offNadirAngle": null,
    "orbit": 51313,
    "pathNumber": 141,
    "pgeVersion": "003.71",
    "platform": "Sentinel-1A",
    "pointingAngle": null,
    "polarization": "HH+HV",
    "processingDate": "2023-11-21T08:58:08.605Z",
    "processingLevel": "SLC",
    "sceneName": "S1A_IW_SLC__1SDH_20231121T085808_20231121T085833_051313_0630F0_2C76",
    "sensor": "C-SAR",
    "startTime": "2023-11-21T08:58:08.605Z",
    "stopTime": "2023-11-21T08:58:33.796Z",
    "url": "https://datapool.asf.alaska.edu/SLC/SA/S1A_IW_SLC__1SDH_20231121T085808_20231121T085833_051313_0630F0_2C76.zip"
  },
  "type": "Feature"
}
