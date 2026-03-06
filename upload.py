import os
import vk_api
import requests
from vk_api.upload import VkUpload

# هێنانی کلیلە زێڕینەکە لە سندوقەکەی گیتھەب
token = os.environ.get('VK_TOKEN')
group_id = 236480315  # ئایدی قەڵاکەت

def main():
    print("چوونەژوورەوە بە کلیلە زێڕینەکە...")
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)

    video_url = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4"
    video_filename = "test_video.mp4"

    print("دادەگرتنی ڤیدیۆکە...")
    response = requests.get(video_url)
    with open(video_filename, 'wb') as f:
        f.write(response.content)

    print("بەرزکردنەوەی ڤیدیۆکە بۆ ناو کۆگاکە...")
    video = upload.video(
        video_file=video_filename,
        name="ڤیدیۆی تاقیکردنەوەی سیستەم",
        description="ئەمە یەکەم تاقیکردنەوەی پەخشی ڤیدیۆیە لەناو کۆگای سەرەکی. بەبێ کێشە کار دەکات.",
        group_id=group_id
    )

    print("سەرکەوتوو بوو! ڤیدیۆکە گەیشتە ناو قەڵاکە.")
    print("زانیاری ڤیدیۆکە:", video)

if __name__ == '__main__':
    main()
