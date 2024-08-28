import os
import shutil

# 다운로드 폴더 경로
downloads_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로
images_folder = r'C:\Users\student\Downloads\images'
data_folder = r'C:\Users\student\Downloads\data'
docs_folder = r'C:\Users\student\Downloads\docs'
archive_folder = r'C:\Users\student\Downloads\archive'

# 이동할 폴더가 없으면 생성
os.makedirs(images_folder, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# 다운로드 폴더 내의 모든 파일을 확인
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    
    # 파일이 아닌 경우는 무시
    if not os.path.isfile(file_path):
        continue
    
    # 파일 확장자 확인 및 이동
    if filename.lower().endswith(('.jpg', '.jpeg','.webp')):
        shutil.move(file_path, images_folder)
    elif filename.lower().endswith(('.csv', '.xlsx')):
        shutil.move(file_path, data_folder)
    elif filename.lower().endswith(('.txt', '.doc', '.pdf')):
        shutil.move(file_path, docs_folder)
    elif filename.lower().endswith('.zip'):
        shutil.move(file_path, archive_folder)

print("파일 이동이 완료되었습니다.")
