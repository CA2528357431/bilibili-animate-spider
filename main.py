import sqlite3
import requests


def getdata():
    i = 1
    url = "https://api.bilibili.com/pgc/season/index/result?"
    headers = {
        "accept": 'application/json, text/plain, */*',
        "accept-encoding": 'gzip, deflate, br',
        "accept-language": 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        "cookie": "_uuid=932EB299-9EA8-D536-CC94-81D3FD012FEF37270infoc; buvid3=E747FA96-C23E-4A04-AAB2-CFBE41A16887143078infoc; sid=9nk6sfl4; rpdid=|(k|~RRmJRJ~0J'ulm~YJ~|)J; CURRENT_FNVAL=80; blackside_state=1; bp_t_offset_220921047=485998192616365274; CURRENT_QUALITY=80; bp_video_offset_220921047=488578849481034897; balh_is_closed=; balh_server_inner=__custom__; fingerprint=728612a83458cf1401017349695e14d9; buvid_fp=E747FA96-C23E-4A04-AAB2-CFBE41A16887143078infoc; buvid_fp_plain=E747FA96-C23E-4A04-AAB2-CFBE41A16887143078infoc; DedeUserID=220921047; DedeUserID__ckMd5=748dd32d249f6e36; SESSDATA=b70dd386%2C1628944588%2Cbfc47*21; bili_jct=e2eea57ef5d2ef3ebe1e0abf84bd3b5a; PVID=3; bfe_id=603589b7ce5e180726bfa88808aa8947",
        "origin": 'https://www.bilibili.com',
        "referer": 'https://www.bilibili.com/',
        "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    data = []
    for i in range(1, 163):

        params = {"season_version": "-1",
                  "area": "-1",
                  "is_finish": "-1",
                  "copyright": "-1",
                  "season_status": "-1",
                  "season_month": "-1",
                  "year": "(1900,2022)",
                  "style_id": "-1",
                  "order": "2",
                  "st": "1",
                  "sort": "0",
                  "page": str(i),
                  "season_type": "1",
                  "pagesize": "20",
                  "type": "1"}

        dataR = requests.get(url, headers=headers, params=params)

        re = (eval(dataR.text))["data"]["list"]

        for x in re:
            r = []
            r.append(x["title"])
            r.append(x["order"])
            r.append(x["index_show"])
            r.append(x["link"])
            r.append(x["badge"])
            data.append(r)

    data_s = []
    for i in range(1, 163):

        params = {"season_version": "-1", "area": "-1", "is_finish": "-1", "copyright": "-1", "season_status": "-1",
                  "season_month": "-1", "year": "(1900,2022)", "style_id": "-1", "order": "4", "st": "1", "sort": "0",
                  "page": str(i), "season_type": "1", "pagesize": "20", "type": "1"}

        dataR = requests.get(url, headers=headers, params=params)

        re = (eval(dataR.text))["data"]["list"]

        for x in re:
            r = []
            r.append(x["title"])
            r.append(x["order"])
            data_s.append(r)
    for x in data:
        for y in data_s:
            if x[0] == y[0]:
                x.append(y[1])

    data_f = []
    for i in range(1, 163):

        params = {"season_version": "-1", "area": "-1", "is_finish": "-1", "copyright": "-1", "season_status": "-1",
                  "season_month": "-1", "year": "(1900,2022)", "style_id": "-1", "order": "3", "st": "1", "sort": "0",
                  "page": str(i), "season_type": "1", "pagesize": "20", "type": "1"}

        dataR = requests.get(url, headers=headers, params=params)

        re = (eval(dataR.text))["data"]["list"]

        for x in re:
            r = []
            r.append(x["title"])
            r.append(x["order"])
            data_f.append(r)
    for x in data:
        for y in data_f:
            if x[0] == y[0]:
                x.append(y[1])

    data_t = []
    for i in range(1, 163):

        params = {"season_version": "-1", "area": "-1", "is_finish": "-1", "copyright": "-1", "season_status": "-1",
                  "season_month": "-1", "year": "(1900,2022)", "style_id": "-1", "order": "5", "st": "1", "sort": "0",
                  "page": str(i), "season_type": "1", "pagesize": "20", "type": "1"}

        dataR = requests.get(url, headers=headers, params=params)

        re = (eval(dataR.text))["data"]["list"]

        for x in re:
            r = []
            r.append(x["title"])
            r.append(x["order"])
            data_t.append(r)
    for x in data:
        for y in data_t:
            if x[0] == y[0]:
                x.append(y[1])

    return data


def savedata(data):
    con = sqlite3.connect("data.db")
    c = con.cursor()

    sql = '''          
    CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT ,follow TEXT,score TEXT,num TEXT ,length TEXT ,time TEXT ,web TEXT ,pay TEXT);
    '''
    c.execute(sql)
    for x in data:
        sql0 = '''
        INSERT INTO data (name,follow,score,num,length,time,web,pay)
        VALUES ( ?,?,?,?,?,?,?,? );
        '''
        c.execute(sql0, (x[0], x[6], x[5], x[1], x[2], x[7], x[3], x[4]))
    con.commit()


def main():
    data = getdata()
    savedata(data)


main()


