from backup_script import S3DataBackUp

if __name__ == "__main__":
    error_path = "localPath"
    LOCAL_DIR = 'databackup_dir'
    bucket_name = "bucketname"
    region_name = "region"

    data_artisan = S3DataBackUp(error_path, LOCAL_DIR, bucket_name, region_name)
    data_artisan.upload_files_to_s3()