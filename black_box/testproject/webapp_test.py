#!/usr/bin/env python3
"""
References:
    https://github.com/testproject-io/python-opensdk/blob/master/README.rst
    https://blog.testproject.io/2020/07/27/html-test-reports-for-selenium-and-appium-python-test-automation/
    https://www.digitalocean.com/community/tutorials/how-to-use-subprocess-to-run-external-programs-in-python-3
    https://www.programiz.com/python-programming/time/sleep
"""
import time
from selenium.webdriver.common.action_chains import ActionChains
from src.testproject.sdk.drivers import webdriver
from selenium.webdriver import ChromeOptions
from sys import argv
import subprocess
from src.testproject.enums.report_type import ReportType 
from src.testproject.sdk.exceptions.agentconnectexception import AgentConnectException

def start_agent(agent_path):
    subprocess.Popen([agent_path], 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.STDOUT
            )

    print("Pausing to let agent complete preliminary steps...")
    time.sleep(120)
    return 

def start_driver(reportName, reportPath):
    # Open Browser through webdriver
    option = ChromeOptions()
    #option.set_capability('browserName', 'Brave')
    option.binary_location = "/usr/bin/brave-browser"
    # 'capabilities': {'browserName': 'chrome', 'version': '', 'platform': 'ANY', 'goog:chromeOptions': {'extensions': [], 'args': []}}
    # capa_dict = {'browserName': 'brave-browser'}
    # Chrome(chrome_options: selenium.webdriver.chrome.options.Options = None, desired_capabilities: dict = None, token: str = None, project_name: str = None, job_name: str = None, disable_reports: bool = False, report_type: src.testproject.enums.report_type.ReportType = <ReportType.CLOUD_AND_LOCAL: 2>, agent_url: str = None, report_name: str = None, report_path: str = None, socket_session_timeout: int = 120000)
    driver = webdriver.Chrome(token="L9uFbgNVurZw6wZmr79aIhRTdJsgkqWKH1315_e8qYg1",
            chrome_options = option,
            project_name = "Automated Testing Pipeline",
            job_name = "Automated Web Application Test",
            #report_type = ReportType.LOCAL,
            report_name = f"{reportName}",
            report_path = f"{reportPath}"
            )
    return driver

def generateAction(driver, action, act_description):
    ActionChains(driver).send_keys(action).perform()
    driver.report().step(
            description=act_description,
            message="Screenshot",
            passed=True,
            screenshot=True
            )
    return

def test_main(ApplicationURL):
    reportName = f"test_{int(time.time())}"
    reportPath = "/home/metaverseops/testproject/code/test_reports"
    agentPath = "/home/metaverseops/testproject/agent/bin/testproject-agent-app"
    try:
        driver = start_driver(reportName, reportPath)
    except (AgentConnectException, ConnectionRefusedError) as e:
        print(e)
        print("Agent not running! Starting it now...")
        start_agent(agentPath)
        driver = start_driver(reportName, reportPath)
    #driver.step_settings = StepSettings(screenshot_condition=TakeScreenshotConditionType.Always)
    driver.get(f'{ApplicationURL}')

    # Send keys
    generateAction(driver, "wwww", "Entering sequence of 'w' keys")
    generateAction(driver, "aaaa", "Entering sequence of 'a' keys")
    generateAction(driver, "ssss", "Entering sequence of 's' keys")
    generateAction(driver, "dddd", "Entering sequence of 'd' keys")

    driver.quit()
    return f"{reportPath}/{reportName}"

if __name__ == "__main__":
    #help(ChromeOptions)
    
    if len(argv) < 2:
        report_loc = test_main("http://35.225.117.79/content/worlds/solipsisworld/movements.html")
    else:
        """
        webapp_address = open(argv[1]).read()
        statement = webapp_address.strip() #+ "/content/worlds/solipsisworld/movements.html"
        time.sleep(60)
        """
        report_loc = test_main(argv[1])
    print(report_loc+'.html')
