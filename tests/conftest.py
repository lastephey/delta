# -*- Encoding: UTF-8 -*-

import pytest
import json


@pytest.fixture(scope="module")
def config_all():
    """Provides a configuration object for all unit tests."""    
    config_str = """{
        "diagnostic":
          {
    "name": "kstarecei",
    "shotnr": 18431,
    "datasource":
    {
      "source_file": "/global/cscratch1/sd/rkube/KSTAR/kstar_streaming/018431/ECEI.018431.LFS.h5",
      "chunk_size": 10000,
      "num_chunks": 500,
      "channel_range": ["L0101-2408"],
      "datatype": "float"
    },
    "parameters": {
      "Device": "L",
      "TriggerTime": [-0.12, 61.2, 60],
      "t_norm": [-0.119, -0.109],
      "SampleRate": 500,
      "TFcurrent": 23000.0,
      "Mode": "O",
      "LoFreq": 81,
      "LensFocus": 80,
      "LensZoom": 340}
  },
  "transport_nersc":
  {
    "datapath": "tmp_nersc",
    "engine": "BP4",
    "params":
    {
      "IPAddress": "128.55.205.18",
      "Timeout": "120",
      "Port": "50001",
      "TransportMode": "fast"
    }
  },
  "storage_mongo":
  {
    "backend": "mongo",
    "datastore": "gridfs",
    "datadir": "/global/cscratch1/sd/rkube/delta"
  },
  "storage":
  {
    "backend": "null"
  },
 "preprocess": {
   "plot": {"time_range": [0.0, 0.00002], "plot_dir": "/global/homes/r/rkube/delta_runs/plots/"},
   "wavelet": {"wavelet": "db5", "method": "BayesShrink", "wavelet_levels": 5, "rescale_sigma": false},
   "stft": {"nfft": 512, "fs": 500000, "window": "hann", "overlap": 0.5, "noverlap": 256, "detrend": "constant", "full": true},
   "no_bandpass_fir": {"N": 5, "Wn": [0.02, 0.036], "btype": "bandpass", "output": "sos"}
   },
 "task_list": [{
                "task_description" : "cross_correlation",
                "analysis": "cross_correlation",
                "channel_chunk_size": 32768,
                "ref_channels" : [1, 1, 24, 8],
                "cmp_channels" : [1, 1, 24, 8]
              },
              {
                "task_description" : "cross_power",
                "analysis": "cross_power",
                "channel_chunk_size": 32768,
                "ref_channels" : [1, 1, 24, 8],
                "cmp_channels" : [1, 1, 24, 8]
              },
              {
                "task_description" : "cross_phase",
                "analysis": "cross_phase",
                "channel_chunk_size": 32768,
                "ref_channels" : [1, 1, 24, 8],
                "cmp_channels" : [1, 1, 24, 8]
              },
              {
                "task_description" : "coherence",
                "analysis": "coherence",
                "channel_chunk_size": 32768,
                "ref_channels" : [1, 1, 24, 8],
                "cmp_channels" : [1, 1, 24, 8]
              }]
    }"""

    config = json.loads(config_str)
    return config


# End of file conftest.py
