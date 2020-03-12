import requests


def call_mask_api(lat, long, rad):
    # 위도/경도에 따른 반경 내 마스크 약국
    url_format = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat={lat}&lng={long}&m={rad}'
    url = url_format.format(lat=lat, long=long, rad=rad)
    response = requests.get(url)
    phar_cnt = response.json()['count']
    print("근처 약국 수 (반경", rad, "m 내) :", phar_cnt)

    for store in range(phar_cnt):
        name = response.json()['stores'][store]['name']
        remain_stat = response.json()['stores'][store]['remain_stat']
        # type = response.json()['stores'][store]['type']
        stock_at = response.json()['stores'][store]['stock_at']
        print(store, ":", name, "/", remain_stat, "/", stock_at)


if __name__ == '__main__':
    company_lat = 37.5081  # 회사 위도
    company_long = 127.0563  # 회사 경도
    home_lat = 37.5272  # 집 위도
    home_long = 127.123  # 집 경도
    radius = 300  # 반경

    call_mask_api(company_lat, company_long, radius)
    print("-------------------------------------------------")
    # call_mask_api(home_lat, home_long, radius)
