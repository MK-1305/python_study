import os
from datetime import datetime

def create_today_folder_on_desktop():
    # 今日の日付を YYYYMMDD 形式で取得
    today_str = datetime.now().strftime('%Y%m%d')

    # Windows で OneDrive にデスクトップがある場合のパス
    if os.name == 'nt' and 'OneDrive' in os.environ:
        # 日本語版Windowsでは「デスクトップ」フォルダ名が日本語の場合
        desktop_dir_name = 'デスクトップ'
        desktop_path = os.path.join(os.environ['OneDrive'], desktop_dir_name)
    else:
        # それ以外は従来の Desktop フォルダ
        desktop_path = os.path.join(
            os.path.expanduser('~'),
            'Desktop'
        )

    # フォルダのフルパス
    folder_path = os.path.join(desktop_path, today_str)

    # フォルダを作成（既にあれば何もしない）
    os.makedirs(folder_path, exist_ok=True)

    print(f"フォルダを作成しました: {folder_path}")

if __name__ == "__main__":
    create_today_folder_on_desktop()

