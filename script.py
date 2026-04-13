import requests
import os

# هذه المعلومات سنضعها في إعدادات غيت هاب لاحقاً لتبقى سرية
BLOG_ID = "975648452386542935"
ACCESS_TOKEN = os.getenv("BLOGGER_TOKEN") 

def send_to_blogger():
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # محتوى المقال (يمكنك تعديله لاحقاً ليكون تلقائياً بالكامل)
    data = {
        "kind": "blogger#post",
        "title": "تجربة النشر الآلي من GitHub Actions",
        "content": "هذا المقال تم نشره تلقائياً باستخدام كود بايثون وعبر منصة غيت هاب بدون الحاجة لـ RDP."
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("✅ تم النشر بنجاح!")
    else:
        print(f"❌ فشل النشر: {response.text}")

if __name__ == "__main__":
    send_to_blogger()
