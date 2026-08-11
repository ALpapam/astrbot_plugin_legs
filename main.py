import time
import random
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register

@register("astrbot_plugin_legs", "YourName", "看腿插件", "1.0.0")
class LegsPlugin(Star):
    def __init__(self, context: Context, config: dict = None):
        super().__init__(context)
        # config 变量会自动接收从 WebUI (配置界面) 保存的设定值
        self.config = config or {}

    @filter.command("白丝")
    async def baisi(self, event: AstrMessageEvent):
        """用户输入'白丝'时触发"""
        # 加时间戳防止平台（如 QQ）缓存同一张图片，导致每次发一样的图
        url = f"https://api.nycnm.cn/api/v2/baisi1?t={int(time.time())}"
        yield event.image_result(url)

    @filter.command("黑丝")
    async def heisi(self, event: AstrMessageEvent):
        """用户输入'黑丝'时触发"""
        url = f"https://api.nycnm.cn/api/v2/heisi1?t={int(time.time())}"
        yield event.image_result(url)

    @filter.command("看看腿")
    async def kankantui(self, event: AstrMessageEvent):
        """用户输入'看看腿'时触发，读取配置的概率，按比例随机掉落"""
        # 实时获取配置中黑丝的概率，默认 50%
        heisi_prob = self.config.get("heisi_prob", 50)
        
        # 在 1 到 100 之间随机摇一个点数
        roll = random.randint(1, 100)
        
        if roll <= heisi_prob:
            # 摇点落在黑丝概率区间内
            url = f"https://api.nycnm.cn/api/v2/heisi1?t={int(time.time())}"
        else:
            # 摇点在黑丝概率外，剩余概率全都给白丝
            url = f"https://api.nycnm.cn/api/v2/baisi1?t={int(time.time())}"
            
        yield event.image_result(url)