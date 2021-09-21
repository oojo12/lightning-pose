import os
import numpy as np
from pose_est_nets.datasets.DALI import video_pipe
from nvidia.dali import pipeline_def
import nvidia.dali.fn as fn
import nvidia.dali.types as types

video_directory = os.path.join("/home/jovyan/mouseRunningData/unlabeled_videos")
assert os.path.exists(video_directory)
video_files = [video_directory + "/" + f for f in os.listdir(video_directory)]


def test_video_pipe():
    pipe = video_pipe(
        sequence_length=7,
        batch_size=2,
        device_id=0,
        num_threads=2,
        filenames=video_files,
        resize_dims=[384, 384],
    )
    pipe.build()
    n_iter = 3
    for i in range(n_iter):
        pipe_out = pipe.run()
        sequences_out = pipe_out[0].as_cpu().as_array()
        assert sequences_out.shape == (2, 7, 3, 384, 384)
    pass


def test_DALI_wrapper():
    pass