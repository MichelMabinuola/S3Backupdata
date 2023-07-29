import os
import boto3
from datetime import datetime, date, timedelta
import logging

class S3DataBackUp:
    def __init__(self, error_path, LOCAL_DIR, bucket_name, region_name):
        self.error_path = error_path
        self.LOCAL_DIR = LOCAL_DIR
        self.bucket_name = bucket_name
        self.region_name = region_name
        self.filter_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        self.s3_client = boto3.client('s3', region_name=self.region_name)
        logging.basicConfig(filename=self.error_path, level=logging.ERROR)

    def upload_files_to_s3(self):
        for file_name in os.listdir(self.LOCAL_DIR):
            file_path = os.path.join(self.LOCAL_DIR, file_name)
            subfolders = [f.path for f in os.scandir(file_path) if f.is_dir()]

            if len(subfolders) < 1:
                pass
            else:
                for sub_sub_folders in subfolders:
                    for f in os.listdir(sub_sub_folders):
                        # anyfile path will do. this is just an examples
                        if f.endswith('.json'):
                            filetime = datetime.fromtimestamp(os.path.getmtime(
                                os.path.join(sub_sub_folders, f))).strftime('%Y-%m-%d')

                            # upload the files to AWS S3 based on date but only previous dates
                            if filetime == self.filter_date:
                                local_dir_files_yesterday = os.path.join(
                                    sub_sub_folders, f)
                                s3_dir_path = local_dir_files_yesterday.replace(
                                    self.LOCAL_DIR, '')

                                try:
                                    self.s3_client.upload_file(
                                        local_dir_files_yesterday, self.bucket_name, s3_dir_path)
                                    print(f"Uploading {local_dir_files_yesterday} to S3 bucket...")
                                except Exception as e:
                                    logging.error(
                                        f"Error uploading {local_dir_files_yesterday} to S3 bucket: {str(e)}")
                                    print(f"Error uploading {local_dir_files_yesterday} to S3 bucket: {str(e)}")

