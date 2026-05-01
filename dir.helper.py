import os

def get_data():
    try:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
        
        return {
            "DESKTOP_FILES": str(len(os.listdir(desktop))),
            "DL_FILES": str(len(os.listdir(downloads)))
        }
    except:
        return {"DESKTOP_FILES": "N/A", "DL_FILES": "N/A"}