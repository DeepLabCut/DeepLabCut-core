"""
deeplabcutcore2.0 Toolbox (deeplabcut.org)
© A. & M. Mathis Labs
https://github.com/AlexEMG/deeplabcut

Please see AUTHORS for contributors.
https://github.com/AlexEMG/deeplabcut/blob/master/AUTHORS
Licensed under GNU Lesser General Public License v3.0
"""

import os
import platform

# Supress tensorflow warning messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
DEBUG = True and 'DEBUG' in os.environ and os.environ['DEBUG']
from deeplabcutcore import DEBUG


from deeplabcutcore.create_project import create_new_project, create_new_project_3d, add_new_videos, load_demo_data
from deeplabcutcore.create_project import create_pretrained_project, create_pretrained_human_project
from deeplabcutcore.generate_training_dataset import extract_frames, select_cropping_area
from deeplabcutcore.generate_training_dataset import check_labels,create_training_dataset, mergeandsplit, create_training_model_comparison
from deeplabcutcore.utils import create_labeled_video,plot_trajectories, auxiliaryfunctions, convertcsv2h5, convertannotationdata_fromwindows2unixstyle, analyze_videos_converth5_to_csv, auxfun_videos
from deeplabcutcore.utils.auxfun_videos import ShortenVideo, DownSampleVideo, CropVideo

# Train, evaluate & predict functions / require TF
from deeplabcutcore.pose_estimation_tensorflow import train_network, return_train_network_path
from deeplabcutcore.pose_estimation_tensorflow import evaluate_network, return_evaluate_network_data
from deeplabcutcore.pose_estimation_tensorflow import analyze_videos, analyze_time_lapse_frames
from deeplabcutcore.pose_estimation_tensorflow import export_model

from deeplabcutcore.pose_estimation_3d import calibrate_cameras,check_undistortion,triangulate,create_labeled_video_3d

from deeplabcutcore.refine_training_dataset import extract_outlier_frames, merge_datasets
from deeplabcutcore.post_processing import filterpredictions, analyzeskeleton
