#!/usr/bin/python3

from google.cloud import storage
import os
import sys

__REMOTE_FOLDER__='test-robot'

def upload(bucket_name, local_file):    
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        filename = get_filename(local_file)
        blob = bucket.blob(__REMOTE_FOLDER__ + '/' + filename)
        blob.upload_from_filename(local_file)        
        print(f'Upload do arquivo {local_file} efetuado com sucesso para o bucket {bucket_name}/{__REMOTE_FOLDER__}')
    except Exception as e:
        print(f'Erro ao fazer o upload do arquivo {local_file} para o bucket {bucket_name}. Motivo={e}')


def get_filename(local_file):
    head, tail = os.path.split(local_file)
    return tail

def main(bucket_name, local_file):    
    upload(bucket_name, local_file)
    
def validate(args):
    if args is not None and len(args) == 3:
        return True
    else:
        print("Exemplo de uso")
        print("python3 upload_bucket.py <nome do bucket> <caminho absoluto do arquivo>")
        return False
    
if __name__ == "__main__":
    if validate(sys.argv):
        main(sys.argv[1], sys.argv[2])