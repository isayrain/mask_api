import requests


def call_mask_api(name, lat, long, rad):
    # 위도/경도에 따른 반경 내 마스크 약국
    url_format = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat={lat}&lng={long}&m={rad}'
    url = url_format.format(lat=lat, long=long, rad=rad)
    response = requests.get(url)
    pharmacy_cnt = response.json()['count']
    print(name, "근처 약국 수 (반경", rad, "m 내) :", pharmacy_cnt)

    for store in range(pharmacy_cnt):
        cnt = store + 1
        name = response.json()['stores'][store]['name']
        remain_stat = response.json()['stores'][store]['remain_stat']
        # type = response.json()['stores'][store]['type']
        stock_at = response.json()['stores'][store]['stock_at']
        remain_txt = ""
        if remain_stat == "plenty":
            remain_txt = "100개 이상"
        elif remain_stat == "some":
            remain_txt = "30개 이상 100개 미만"
        elif remain_stat == "few":
            remain_txt = "2개 이상 30개 미만"
        elif remain_stat == "empty":
            remain_txt = "1개 이하"
        elif remain_stat == "break":
            remain_txt = "판매중지"
        else:
            remain_txt = "확인불가"
        print(cnt, ":", name, "/", remain_txt, "/", stock_at)


if __name__ == '__main__':
    company_name = "회사"
    company_lat = 37.5081  # 회사 위도
    company_long = 127.0563  # 회사 경도
    home_name = "집"
    home_lat = 37.5272  # 집 위도
    home_long = 127.123  # 집 경도
    radius = 500  # 반경
    rnd_name = "우면"
    rnd_lat = 37.465922  # 우면 위도
    rnd_long = 127.022690  # 우면 경도

    call_mask_api(company_name, company_lat, company_long, radius)
    print("-------------------------------------------------")
    call_mask_api(home_name, home_lat, home_long, radius)
    print("-------------------------------------------------")
    call_mask_api(rnd_name, rnd_lat, rnd_long, radius)
    print("-------------------------------------------------")
