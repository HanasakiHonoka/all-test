import requests

cookies = {
    'remember_me_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltYzFWVGxGZEdSU2NYQlNZbE5RZWtONVpUSnpJZz09IiwiZXhwIjoiMjAyMi0wOS0yMVQyMDowMDoxNy4wMDBaIiwicHVyIjpudWxsfX0%3D--4c1f99b2d285e7ab1f8bee28625c346e2ecda465',
    'Hm_lvt_79251201618e9337c1169fef9b3e4786': '1661438858',
    'Hm_lpvt_79251201618e9337c1169fef9b3e4786': '1661438858',
    '_project_hgc_session': 'M3FOTm00c3IwSmhSM3lwZUR0SnF2ajVUS0NrRS9Tbm1Pb2NyZVBJaG1XSzREc1Q5L01OcWV4WmNFejVBU2tlWWtjREVYRFNqZit6bm83WjFxZjF4NVY1ZVB6Zy9VYWkwNFluTUk0ME9rUGFMRnhZOHlIU1lsUHJycHIrNy85ZzR0Y3ljSE00Z0ZuK1ZGSnNiY3JNbVR4RlpBaFVpQXZrNjIwNEJqRnFyTTFOYmtWZG54blcwcm1BTzJsa0RDMjBmLS1VRGJWVENyU2s1NjZ4M3FMSkRmOXZnPT0%3D--6e11830775301eac93f60217b93e6bc5f133955b',
    '_project_hgc_session': 'eUE0RGNXcmRscG11SFFJRmd5UUpGeFZTcEVySkNIN2dzUGFocFdsb1Z0cEhtWDJ6Uzl4Z0lXOVZ4RVFKak5tcDkxK282TzMzeTEzVStFSjNrTm83ak53amNWeWJKVUEzazhkUkVPZ21UbTFtckR1NDJ2VElwVXdMU1hHSlVkcFFvUVdPMTYvUU1IU1pPSE5VeFY5MlNRb2cyc0Fnc0x0TFhVeUF4SFlWcWhkK0E1Y3djUjhTSFZmeUZhRUVUMVpVLS02QUlPa1N2VTZwZm15cms0STNaUWVRPT0%3D--80bc5b49f3254cdffd0e7d52612eae7322cbab8c',
}

headers = {
    'authority': 'galge.fun',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'remember_me_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltYzFWVGxGZEdSU2NYQlNZbE5RZWtONVpUSnpJZz09IiwiZXhwIjoiMjAyMi0wOS0yMVQyMDowMDoxNy4wMDBaIiwicHVyIjpudWxsfX0%3D--4c1f99b2d285e7ab1f8bee28625c346e2ecda465; Hm_lvt_79251201618e9337c1169fef9b3e4786=1661438858; Hm_lpvt_79251201618e9337c1169fef9b3e4786=1661438858; _project_hgc_session=M3FOTm00c3IwSmhSM3lwZUR0SnF2ajVUS0NrRS9Tbm1Pb2NyZVBJaG1XSzREc1Q5L01OcWV4WmNFejVBU2tlWWtjREVYRFNqZit6bm83WjFxZjF4NVY1ZVB6Zy9VYWkwNFluTUk0ME9rUGFMRnhZOHlIU1lsUHJycHIrNy85ZzR0Y3ljSE00Z0ZuK1ZGSnNiY3JNbVR4RlpBaFVpQXZrNjIwNEJqRnFyTTFOYmtWZG54blcwcm1BTzJsa0RDMjBmLS1VRGJWVENyU2s1NjZ4M3FMSkRmOXZnPT0%3D--6e11830775301eac93f60217b93e6bc5f133955b; _project_hgc_session=eUE0RGNXcmRscG11SFFJRmd5UUpGeFZTcEVySkNIN2dzUGFocFdsb1Z0cEhtWDJ6Uzl4Z0lXOVZ4RVFKak5tcDkxK282TzMzeTEzVStFSjNrTm83ak53amNWeWJKVUEzazhkUkVPZ21UbTFtckR1NDJ2VElwVXdMU1hHSlVkcFFvUVdPMTYvUU1IU1pPSE5VeFY5MlNRb2cyc0Fnc0x0TFhVeUF4SFlWcWhkK0E1Y3djUjhTSFZmeUZhRUVUMVpVLS02QUlPa1N2VTZwZm15cms0STNaUWVRPT0%3D--80bc5b49f3254cdffd0e7d52612eae7322cbab8c',
    'origin': 'https://galge.fun',
    'pragma': 'no-cache',
    'referer': 'https://galge.fun/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-csrf-token': 'ZFBGcZn5pxxycRu3vCFXuiy55ZGul6DPyqZs/RLDpDNKI7iaBqi7WOPVsa9AHN1kqDUe3fcRT4ZkDwYDp68mhg==',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.post('https://galge.fun/checkins', cookies=cookies, headers=headers)

print(response.text)