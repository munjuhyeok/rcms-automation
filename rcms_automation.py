loginId = "ANS1118"
loginPasswd = "hyeok@9718"
startDate = "20250301"
endDate = "20250331"
filePath = "C:\\Users\\180569\\DeskTop\\3월증빙\\"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import glob

driver = webdriver.Chrome()

## login
driver.get('https://www.rcms.go.kr/login/rid.do?PORTAL_YN=Y')
driver.implicitly_wait(15)
driver.find_element(By.ID, "loginId").send_keys(loginId)
driver.find_element(By.ID, "loginPasswd").send_keys(loginPasswd)
driver.find_element(By.ID, "btn_login").click()

driver.implicitly_wait(5)
driver.find_element(By.ID, "wfm_main_btn_banner01").click() ## 연구개발기관 클릭

driver.implicitly_wait(5)

driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div/div[2]/div[1]/ul/li[2]/a").click() ## 연구비사용 클릭
# driver.find_element(By.CSS_SELECTOR, "#wfm_header_gen_menuLvl1_1_btn_menuLvl1").click() ## 연구비사용 클릭
# driver.find_element(By.ID, "wfm_header_gen_menuLvl1_1_btn_menuLvl1").click() ## 연구비사용 클릭
driver.find_element(By.ID, "wfm_header_gen_menuLvl1_1_gen_menuLvl2_0_btn_menuLvl2").click() ## 연구비사용등록 클릭

driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_wframe_sbjtSelectMain_report_btn > i").click() ## 과제선택 팝업
driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_wframe_sbjtSelectMain_wframe_sbjtSelect_gridView_body_tbody > tr:nth-child(2)").click() # 3번째 과제 클릭
driver.find_element(By.ID, "tac_layout_contents_21210_body_wframe_sbjtSelectMain_wframe_sbjtSelect_btnClose").click() # 선택 버튼 

driver.find_element(By.ID, "tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_sel_evdcSe").click() # 증빙선택
driver.find_element(By.ID, "tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_sel_evdcSe_itemTable_2").click() # 카드
driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_gv_crdGridLstIqrRes_cell_0_3')]").click() # 카드 체크
start_day = driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_cal_startDate_input')]") # 시작일
start_day.clear()
start_day.send_keys(startDate)
end_day = driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_cal_endDate_input')]") # 종료일
end_day.clear()
end_day.send_keys(endDate)
driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_btn_searchCarduse')]").click()
num_pages = len(driver.find_elements(By.XPATH, f"//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_pgl_gridView_page_')]"))
driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_close')]").click() # 창닫기

approval_numbers = {'00402542':'[DT-24] 가나다라마바사', '00103042':'[DT-24] 아자차카타파하'}
for approval_number in approval_numbers.keys():    
    driver.find_element(By.ID, "tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_sel_evdcSe").click() # 증빙선택
    driver.find_element(By.ID, "tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_sel_evdcSe_itemTable_2").click() # 카드
    driver.find_element(By.ID, "tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_anc_evdcSeView").click() # 열기

    driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_gv_crdGridLstIqrRes_cell_0_0')]").click() # 카드 체크
    start_day = driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_cal_startDate_input')]") # 시작일
    start_day.clear()
    start_day.send_keys(startDate)
    end_day = driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_cal_endDate_input')]") # 종료일
    end_day.clear()
    end_day.send_keys(endDate)
    driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_btn_searchCarduse')]").click()
    
    num_pages = len(driver.find_elements(By.XPATH, f"//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_pgl_gridView_page_')]"))

    for page_num in range(1, num_pages + 1):
        driver.find_element(By.XPATH, f"//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_pgl_gridView_page_{page_num}')]").click()
        driver.implicitly_wait(1)
        table = driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, 'wframe_gv_cardFrpcBrdnIqrRes_body_tbody')]")
        row = table.find_elements(By.XPATH, f"//table//tr[contains(., '{approval_number}')]")

        if (row):
            row[0].click()
            driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_btn_save')]").click() # 적용
            driver.find_element(By.XPATH, "//label[contains(text(), '10%')]").click() # 10%
            driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_txt_FAT_AMT')]").clear() # 부가세액 0
            driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_cardVatChngLayer') and contains(@id, '_wframe_btn_save')]").click() # 저장
            driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_cardUseBrdnIqrLayer') and contains(@id, '_wframe_confirm') and contains(@id, '_wframe_btn_yes')]").click() # 예

            driver.find_element(By.ID, "tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg_cell_0_1").click() # 항목 선택
            driver.find_element(By.ID, "G_tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg___selectbox_PTC_ITEPD_CD_itemTable_3").click() # 연구재료비

            driver.find_element(By.ID, "tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg_cell_0_4").click() # 세부항목 선택
            driver.find_element(By.ID, "G_tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg___selectbox_0_DPTC_ITEPD_CD_dynamic_select_0_4_itemTable_2").click() # 연구재료 구입비

            driver.find_element(By.ID, "tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg_cell_0_6").click() # 품목
            driver.find_element(By.ID, "G_tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg__ART_NM").send_keys(approval_numbers[approval_number]) # 품목

            driver.find_element(By.CSS_SELECTOR, "#tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_grd_excRechUseReg_cell_0_16 > button").click() # 등록하기


            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_RcmsServiceServlet') and contains(@id, '_wframe_gridView_cell_9_3')]"))
            )
            element.click()
            driver.find_element(By.ID, "files").send_keys(glob.glob(filePath + approval_number + "\\검수(설치)완료확인서\\*")[0])
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_RcmsServiceServlet') and contains(@id, '_wframe_gridView_cell_3_3')]"))
            )
            element.click()
            driver.find_element(By.ID, "files").send_keys(glob.glob(filePath + approval_number + "\\구매의뢰서\\*")[0])
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_RcmsServiceServlet') and contains(@id, '_wframe_gridView_cell_2_3')]"))
            )
            element.click()
            driver.find_element(By.ID, "files").send_keys(glob.glob(filePath + approval_number + "\\거래명세서\\*")[0])
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_RcmsServiceServlet') and contains(@id, '_wframe_gridView_cell_1_3')]"))
            )
            element.click()
            driver.find_element(By.ID, "files").send_keys(glob.glob(filePath + approval_number + "\\카드매출전표\\*")[0])

            driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_RcmsServiceServlet') and contains(@id, '_wframe_btnSave')]").click() # 저장
            
            driver.find_element(By.XPATH, "//*[contains(@id, 'tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_RcmsServiceServlet') and contains(@id, '_wframe_alert') and contains(@id, '_wframe_btn_confirm')]").click() # 저장
            
            
            driver.find_element(By.ID, "tac_layout_contents_21210_body_tab_regMenu_contents_content_evdcInfo_body_anc_save").click() # 등록
            break
