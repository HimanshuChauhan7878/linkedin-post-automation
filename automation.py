import subprocess
import time
import socket
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
USER_DATA_DIR = r"C:\ChromeAutomationProfile"
DEBUG_PORT = 9222

def is_debug_port_open():
    try:
        with socket.create_connection(("localhost", DEBUG_PORT), timeout=0.5):
            return True
    except:
        return False


def kill_all_chrome():
    subprocess.run(
        "taskkill /F /IM chrome.exe",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def launch_chrome_debug():
    cmd = (
        f'"{CHROME_PATH}" '
        f'--remote-debugging-port={DEBUG_PORT} '
        f'--user-data-dir="{USER_DATA_DIR}" '
        "--no-first-run --no-default-browser-check"
    )

    print("\n[automation] Launching Chrome with:")
    print(cmd)

    subprocess.Popen(cmd, shell=True)
    time.sleep(2)

    print("[automation] Waiting for debug port...")
    for _ in range(30):
        if is_debug_port_open():
            print("[automation] ✓ Chrome debug port open!")
            return True
        time.sleep(0.3)

    print("[automation] ❌ Debug port failed to open.")
    return False


def attach_selenium():
    print("[automation] Attaching Selenium...")

    try:
        opts = Options()
        opts.add_experimental_option("debuggerAddress", f"localhost:{DEBUG_PORT}")
        driver = webdriver.Chrome(options=opts)
        print("[automation] ✓ Selenium attached!")
        return driver
    except Exception as e:
        print("[automation] ❌ Selenium attach failed:", e)
        print(traceback.format_exc())
        return None

def close_popups(driver):
    time.sleep(1)
    selectors = [
        "//button[contains(text(),'Accept')]",
        "//button[contains(@aria-label,'Dismiss')]",
        "//button//*[contains(text(),'Skip')]",
        "//button[contains(text(),'Got it')]",
        "//button[contains(text(),'Not now')]",
    ]

    for xp in selectors:
        try:
            btn = driver.find_element(By.XPATH, xp)
            driver.execute_script("arguments[0].click();", btn)
            print(f"[automation] ✓ Closed popup: {xp}")
            time.sleep(0.3)
        except:
            pass

def click_start_post(driver):
    wait = WebDriverWait(driver, 20)
    try:
        feed = driver.find_element(By.CSS_SELECTOR, "div.scaffold-layout__main")
        driver.execute_script("arguments[0].scrollTop = 0;", feed)
        time.sleep(0.3)
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", feed)
        time.sleep(0.6)
    except:
        pass
    XPATHS = [
        "//button[@id='ember30']",
        "//button[contains(@class,'artdeco-button') and .//strong[text()='Start a post']]",
        "//strong[text()='Start a post']/ancestor::button",
    ]

    for xp in XPATHS:
        try:
            print(f"[automation] Trying selector: {xp}")
            elem = wait.until(EC.presence_of_element_located((By.XPATH, xp)))

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
            time.sleep(0.3)
            driver.execute_script("arguments[0].click();", elem)

            print("[automation] ✓ Start a post clicked (your UI version)!")
            return True

        except Exception as e:
            print(f"[automation] Failed {xp}: {e}")

    print("[automation] ❌ Could not click Start a post automatically.")
    return False

def paste_into_editor(driver, text):
    wait = WebDriverWait(driver, 20)
    editor = None

    XPATHS = [
        "//div[@role='textbox']",
        "//div[contains(@class,'ql-editor')]",
    ]

    for xp in XPATHS:
        try:
            editor = wait.until(EC.presence_of_element_located((By.XPATH, xp)))
            break
        except:
            pass

    if editor is None:
        input("[automation] Click inside editor, then press ENTER...")
        editor = driver.find_element(By.XPATH, "//div[@role='textbox']")

    editor.click()
    time.sleep(0.2)
    editor.send_keys(Keys.CONTROL, "a")
    editor.send_keys(Keys.DELETE)
    editor.send_keys(text)

    print("\n[automation] ✓ Post text pasted successfully!")


def open_linkedin_and_paste(post_text: str):
    print("\n========== LINKEDIN AUTOMATION START ==========\n")

    kill_all_chrome()
    time.sleep(1)

    if not launch_chrome_debug():
        return

    driver = attach_selenium()
    if not driver:
        return

    driver.get("https://www.linkedin.com/feed/")
    time.sleep(5)

    input("[automation] Login if needed → press ENTER...")

    close_popups(driver)

    print("[automation] Attempting to click Start a post (custom UI)...")
    if not click_start_post(driver):
        input("[automation] Please manually click Start a post → press ENTER...")

    time.sleep(2)

    paste_into_editor(driver, post_text)

    print("\n[automation] Now you must manually click POST (LinkedIn restriction).")
    input("Press ENTER to finish automation...")

    driver.quit()

    print("\n========== AUTOMATION COMPLETE ==========\n")
[]