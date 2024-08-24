"""
This module provides a utility function to download and extract zipped CSV datasets from a specified URL.

The main function, `download_zipped_csv_data`, handles downloading a zip file from a given URL, extracting its contents, and saving them to a specified directory. This is particularly useful for preparing datasets for data analysis or machine learning tasks.  # noqa: E501


Author:
- Dr. Saad Laouadi

License:
- This material is intended for educational purposes only and may not be used directly in courses, video recordings, or similar without prior consent from the author. Proper credit must be attributed to the author when using or referencing this material.
"""

import zipfile
import tempfile
import os
import sys
from urllib.request import urlretrieve
from urllib.parse import urlparse, unquote
import pathlib


def download_data(dataset_root_url, dataname, target_dir=None, local_root_path=None, verbose=False):  # noqa: E501
    """
    Download and extracts a zip file containing CSV data from a specified URL.

    This function downloads a zip file from the provided dataset URL, extracts its contents, and saves them  # noqa: E501
    in the specified directory. If no target directory is provided, it uses the dataset name to create one.
    The function can also provide verbose output detailing each step.

    Parameters
    ----------
    dataset_root_url : str
        The base URL where the dataset is hosted.
    dataname : str
        The name of the dataset zip file to be downloaded.
    target_dir : str, optional
        The directory where the extracted files should be stored. If not provided, a directory with the dataset 
        name will be created in the current working directory or the specified local root path.
    local_root_path : str, optional
        The local root path where the target directory will be created. Defaults to the current working directory.
    verbose : bool, optional
        If True, enables verbose output, providing information about the download and extraction process.

    Returns
    -------
    None
        This function does not return any value. It downloads and extracts files to the specified location.

    Raises
    ------
    zipfile.BadZipFile
        If the downloaded zip file is corrupted, the function will raise this error and terminate.
    Exception
        If any other error occurs during the process, it will be captured, and a message will be printed if verbose is enabled.

    Examples
    --------
    Download and extract a dataset with verbose output:
    >>> download_zipped_csv_data('https://example.com/data', 'dataset.zip', target_dir='data', verbose=True)
    """
    if not local_root_path:
        local_root_path = os.getcwd()

    if target_dir:
        if not os.path.isabs(target_dir):
            home_dir = os.path.expanduser('~')
            target_dir_path = os.path.join(home_dir, target_dir)
        else:
            target_dir_path = target_dir
    else:
        parsed_url = urlparse(dataset_root_url)
        dataset_dir = unquote(os.path.basename(parsed_url.path))
        dataset_dir = pathlib.Path(dataset_dir).stem
        target_dir_path = os.path.join(local_root_path, dataset_dir)

    try:
        dataset_url = os.path.join(dataset_root_url, dataname)

        if not os.path.exists(target_dir_path):
            os.makedirs(target_dir_path)
            if verbose:
                print(f"Created directory: {target_dir_path}")

        with tempfile.TemporaryDirectory() as tmp_dir:
            zip_path = os.path.join(tmp_dir, 'temp.zip')
            urlretrieve(dataset_url, zip_path)

            if verbose:
                print(f"Downloading {dataname}...")

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(target_dir_path)
                if verbose:
                    print(f"Extracted to {target_dir_path}")

    except zipfile.BadZipFile:
        if verbose:
            sys.stderr.write("Corrupted zip file encountered, aborting.\n")
        return None
    except Exception as e:
        if verbose:
            sys.stderr.write(f"An error occurred: {e}\n")
        return None
