
import requests

img_url = 'https://vsegda-pomnim.com/uploads/posts/2022-04/1649559789_13-vsegda-pomnim-com-p-derevya-posle-ledyanogo-dozhdya-foto-14.jpg'

def download_img(url=''):

    try:
        response = requests.get(url=url)
        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)

        return 'Img succesffulle downloaded'
    except Exception as _ex:
        return 'Upps....'

def main():
    print(download_img(url= img_url))

if __name__ == '__main__':
    main()




