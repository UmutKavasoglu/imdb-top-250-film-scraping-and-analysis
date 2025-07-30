from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import openpyxl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.imdb.com/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
driver.get(url)

time.sleep(1)

accept_button = driver.find_element(By.CSS_SELECTOR, 'div.sc-pyfCe.iAReIO button[data-testid="accept-button"]')
actions.move_to_element(accept_button).perform()
accept_button.click()

time.sleep(1)

menu_button = driver.find_element(By.CSS_SELECTOR, 'div.sc-fbIVIu.cPMrpb label#imdbHeader-navDrawerOpen')
actions.move_to_element(menu_button).perform()
menu_button.click()

time.sleep(1)

top250_movies_href = driver.find_element(By.CSS_SELECTOR, 'div.navlinkcat__listContainerInner a.ipc-list__item.nav-link.sc-iBzDrC.fzqpfp.ipc-list__item--indent-one:nth-of-type(2)').get_attribute("href")
driver.get(top250_movies_href)

def scroll_to_bottom():
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')

while True:
    scroll_to_bottom()
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == old_height:
        break
    old_height = new_height

degiskenler = {
    "isim": [],
    "puan": [],
    "turler": [],
    "yorum sayisi": [],
    "puan_sayisi": [],
    "yonetmenler": [],
    "senaristler": [],
    "yil": [],
    "sure": [],
    "butce": [],
    "hasilat": [],
    "ulkeler": [],
}

movies_href = []

for i in range(1, 251):
    movie_href = driver.find_element(By.CSS_SELECTOR, f'div.ipc-page-grid.ipc-page-grid--bias-left ul[role="presentation"] li:nth-of-type({i}) a.ipc-title-link-wrapper').get_attribute("href")
    movies_href.append(movie_href)

for m in movies_href:
    driver.get(m)

    old_height2 = driver.execute_script('return document.body.scrollHeight')

    while True:
        scroll_to_bottom()
        new_height2 = driver.execute_script('return document.body.scrollHeight')
        if new_height2 == old_height2:
            break
        old_height2 = new_height2

    time.sleep(1)

    scroll_element = driver.find_element(By.XPATH, '//section[@data-testid="MoreLikeThis"]')
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

    time.sleep(1)

    isim = driver.find_element(By.CSS_SELECTOR, 'div.sc-70a366cc-0.bxYZmb span').text
    degiskenler["isim"].append(isim)

    yil = driver.find_element(By.CSS_SELECTOR, 'div.sc-70a366cc-0.bxYZmb ul:nth-of-type(1) li:nth-of-type(1) a').text
    degiskenler["yil"].append(yil)

    try:
        sure = driver.find_element(By.CSS_SELECTOR, 'div.sc-70a366cc-0.bxYZmb ul:nth-of-type(1) li:nth-of-type(3)').text
        degiskenler["sure"].append(sure)
    except:
        sure = driver.find_element(By.CSS_SELECTOR, 'div.sc-70a366cc-0.bxYZmb ul:nth-of-type(1) li:nth-of-type(2)').text
        degiskenler["sure"].append(sure)

    puan = driver.find_element(By.CSS_SELECTOR, 'div.sc-3a4309f8-1.dOjKRs div.sc-d541859f-2.kxphVf span.sc-d541859f-1.imUuxf').text
    degiskenler["puan"].append(puan)

    puan_sayisi = driver.find_element(By.CSS_SELECTOR, 'div.sc-3a4309f8-1.dOjKRs span.ipc-btn__text div.sc-d541859f-3.dwhNqC').text
    degiskenler["puan_sayisi"].append(puan_sayisi)

    yorum_sayisi = driver.find_element(By.CSS_SELECTOR, 'ul[data-testid="reviewContent-all-reviews"] li span span').text
    degiskenler["yorum sayisi"].append(yorum_sayisi)


    movie_directors = []

    d = 1

    while True:
        try:
            directorx = driver.find_element(By.CSS_SELECTOR,
                                            f'ul.ipc-metadata-list.ipc-metadata-list--dividers-all.sc-cd7dc4b7-8.immMHv.ipc-metadata-list--base div li:nth-of-type({d})').text
            if directorx not in movie_directors:
                movie_directors.append(directorx)
                d += 1
            else:
                break
        except:
            break
    degiskenler["yonetmenler"].append(", ".join(movie_directors))


    movie_writers = []

    w = 1

    while True:
        try:
            writerx = driver.find_element(By.CSS_SELECTOR,
                                            f'section[data-testid="title-cast"] ul.ipc-metadata-list.ipc-metadata-list--dividers-all.sc-cd7dc4b7-8.immMHv.ipc-metadata-list--base li:nth-of-type(2) div ul li:nth-of-type({w})').text
            if writerx not in movie_writers:
                movie_writers.append(writerx)
                w += 1
            else:
                break
        except:
            break
    degiskenler["senaristler"].append(", ".join(movie_writers))


    time.sleep(1)


    movie_genres = []

    g = 1

    while True:

        try:
            genrex = WebDriverWait(driver, 1).until(
                EC.visibility_of_element_located(
                    (By.XPATH, f'//section[@data-testid="Storyline"]/div[2]/ul[2]/li[2]//li[{g}]')
                )
            )

            movie_genres.append(genrex.text)
            g += 1
        except Exception as e:
            #print(e)
            break

    degiskenler["turler"].append(", ".join(movie_genres))


    time.sleep(1)


    movie_countries = []

    c = 1

    while True:
        try:
            countryx = WebDriverWait(driver, 1).until(
                EC.visibility_of_element_located(
                    (By.XPATH, f'//section[@data-testid="Details"]/div[2]/ul/li[2]//ul/li[{c}]')
                )
            )
            movie_countries.append(countryx.text)
            c += 1
        except Exception as e:
            #print(e)
            break
    degiskenler["ulkeler"].append(", ".join(movie_countries))

    try:
        butce = driver.find_element(By.XPATH, f'//li[span[text()="Budget"]]/div//li').text
        degiskenler["butce"].append(butce)
    except:
        butce = "Bilgi yok"
        degiskenler["butce"].append(butce)

    try:
        hasilat = driver.find_element(By.XPATH, f'//li[span[text()="Gross worldwide"]]/div//li').text
        degiskenler["hasilat"].append(hasilat)
    except:
        hasilat = "Bilgi yok"
        degiskenler["hasilat"].append(hasilat)



df = pd.DataFrame(degiskenler)
df.to_excel('imdb_top_250_data.xlsx')



time.sleep(1)
driver.quit()