from backup_script import S3DataBackUp
import os

if __name__ == "__main__":
    error_path = os.getenv(localPath)
    LOCAL_DIR = os.getenv(databackup_dir)
    bucket_name = os.getenv(bucketname)
    region_name = os.getenv(region)

    data_artisan = S3DataBackUp(error_path, LOCAL_DIR, bucket_name, region_name)
    data_artisan.upload_files_to_s3()
