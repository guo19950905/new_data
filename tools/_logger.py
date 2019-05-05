import logging.handlers
#定义获取logger类
class GetLogger:
    logger = None
    @classmethod
    def get_logger(cls,logname):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置日志器级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理 控制台
            sh = logging.StreamHandler()
            filename = '../log/' + logname
            th = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding='utf-8')
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            #将格式器添加到 处理器 控制台
            sh.setFormatter(fm)
            # 将格式器添加到 处理器 文件
            th.setFormatter(fm)
            #将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger

if __name__ == '__main__':
    logger = GetLogger().get_logger('log1.log')
    logger.info("info信息被执行")
    logger.error("error信息被执行")