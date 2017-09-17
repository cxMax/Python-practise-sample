import time
from GameCenterTestMethod import *

package_name = 'com.meizu.flyme.gamecenter'

driver = initializeAtx(package_name)
navigateToMainActivity(driver)
time.sleep(2000)
navigateToWelfareFragment(driver)
