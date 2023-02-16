dns_config = """
#!/bin/bash

dset:
  train: /home/gpuadmin/kawon/0_demucs/content/train/
  valid: /home/gpuadmin/kawon/0_demucs/content/test/
  test: /home/gpuadmin/kawon/0_demucs/content/test/
  noisy_json:
  noisy_dir:
  matching: dns
#eval_every: 1
"""

with open("/home/gpuadmin/kawon/0_demucs/content/TAPLoss-master/Demucs/denoiser/conf/dset/custom_dns.yaml", "w") as f:
    # Writing data to a file
    f.write(dns_config)
