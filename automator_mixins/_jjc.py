from automator_mixins._tools import ToolsMixin
from core.constant import MAIN_BTN, JJC_BTN, PCRelement


class JJCMixin(ToolsMixin):
    """
    竞技场插片
    包含日常行动相关的脚本
    """

    # 进入jjc
    # 做jjc任务
    def doJJC(self):
        # 进入jjc
        self.lock_home()
        self.click_btn(MAIN_BTN["maoxian"], until_appear=MAIN_BTN["zhuxian"])
        self.lock_img(JJC_BTN["list"], elseclick=[MAIN_BTN["zdjjc"], (1, 290)], elsedelay=2)
        self.click_btn(JJC_BTN["shouqu"], until_appear=JJC_BTN["shouqu_ok"],
                       elsedelay=4, retry=2, side_check=self.right_kkr)
        for _ in range(5):
            self.click(24, 84)

        out = self.lock_img({
            JJC_BTN["zdks"]: 1,
            JJC_BTN["tzcs"]: 2,
        }, is_raise=False, elseclick=JJC_BTN["player"], elsedelay=4, timeout=30)
        if not out:
            self.log.write_log("error", "无法进入战斗竞技场！")
            self.lock_home()
            return
        if out == 2:
            self.log.write_log("info", "战斗竞技场次数不足！")
            self.lock_home()
            return
        self.click_btn(JJC_BTN["zdks"])
        # 803 496
        self.lock_img(JJC_BTN["xyb"], timeout=180, alldelay=1)
        self.click_btn(PCRelement(803, 496), until_disappear=JJC_BTN["xyb"])
        self.lock_home()
        # 做pjjc任务

    def doPJJC(self):
        self.lock_home()
        self.click_btn(MAIN_BTN["maoxian"], until_appear=MAIN_BTN["zhuxian"])
        self.lock_img(JJC_BTN["list"], elseclick=[MAIN_BTN["gzjjc"], (1, 290)], elsedelay=2)
        self.click_btn(JJC_BTN["shouqu"], until_appear=JJC_BTN["shouqu_ok"],
                       elsedelay=4, retry=2, side_check=self.right_kkr)
        for _ in range(5):
            self.click(24, 84)

        out = self.lock_img({
            JJC_BTN["dwbz"]: 1,
            JJC_BTN["tzcs"]: 2,
        }, is_raise=False, elseclick=JJC_BTN["player"], elsedelay=4, timeout=30)
        if not out:
            self.log.write_log("error", "无法进入公主竞技场！")
            self.lock_home()
            return
        if out == 2:
            self.log.write_log("info", "公主竞技场次数不足！")
            self.lock_home()
            return
        for _ in range(10):
            self.click(843, 452, post_delay=0.5)
        self.lock_img(JJC_BTN["xyb"], elseclick=[(843, 452)], timeout=180 * 3, alldelay=1)
        self.click_btn(PCRelement(803, 506), until_disappear=JJC_BTN["xyb"])
        self.lock_home()