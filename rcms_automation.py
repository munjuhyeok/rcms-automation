
import os
import time
from random import randint
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, WebDriverException, UnexpectedAlertPresentException

driver = webdriver.Chrome()

driver.get('https://www.rcms.go.kr/login/rid.do?PORTAL_YN=Y')
driver.implicitly_wait(15)
driver.find_element(By.ID, "loginId").send_keys("ANS1118")
driver.find_element(By.ID, "loginPasswd").send_keys("hyeok@9718")
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div/a").click()

driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "#wfm_main_btn_banner01").click()
driver.implicitly_wait(5)
# driver.find_element(By.CSS_SELECTOR, "#wfm_header_gen_menuLvl1_1_btn_menuLvl1").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div/div[2]/div[1]/ul/li[2]/a").click()
driver.find_element(By.CSS_SELECTOR, "#wfm_header_gen_menuLvl1_1_gen_menuLvl2_0_btn_menuLvl2").click()
driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_wframe_sbjtSelectMain_report_btn > i").click()
driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_wframe_sbjtSelectMain_wframe_sbjtSelect_gridView_body_tbody > tr:nth-child(3)").click()
driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_wframe_sbjtSelectMain_wframe_sbjtSelect_btnClose").click()
#tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg_cell_0_1

driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_sel_evdcSe").click()
driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_sel_evdcSe_itemTable_2").click()
driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer05153112007350167_wframe_gv_crdGridLstIqrRes_cell_0_0 > label").click()

table = driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg_cell_0_1").click()
driver.find_element(By.CSS_SELECTOR, "#G_tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg___selectbox_PTC_ITEPD_CD_itemTable_main > tbody > tr:nth-child(4)").click()
# driver.find_element(By.CSS_SELECTOR, "").click()


# driver.find_element(By.CSS_SELECTOR, "").click()
# driver.find_element(By.CSS_SELECTOR, "").click()

#
#wfm_main_sbjtTab1_gen_list_2_PMS_SBJT_ID

#tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg_cell_0_1 > nobr
time.sleep(10)
driver.implicitly_wait(15)
