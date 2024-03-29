# coding=utf-8
import logging
import colorlog

class logs:
    def __init__(self,name='my_logger',file_name='test.log',level=logging.DEBUG):
        # 实例化，创建日志记录器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)


        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = colorlog.ColoredFormatter(
            '%(asctime)s - %(log_color)s%(levelname)s%(reset)s-%(filename)s -(%(lineno)d):%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            reset=True,
            log_colors={
                'DEBUG':'cyan',
                'INFO':'green',
                'WARNING':'yellow',
                'ERROR':'red',
                'CRITICAL':'bold_red'
            }
        )
        console_handler.setFormatter(console_formatter)

        # 创建文件处理器
        file_handler=logging.FileHandler(file_name,encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_formatter=logging.Formatter('%(asctime)s - %(levelname)s -%(filename)s -(%(lineno)d): %(message)s')
        file_handler.setFormatter(file_formatter)

        # 将处理器添加到日至记录器中
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)



if __name__ == '__main__':
    logss = logs()
    logss.logger.debug("this is a debug message")
    logss.logger.info("this is a info message")
    logss.logger.warning("this is a warning message")
    logss.logger.error("this is a error message")
    logss.logger.critical("this is a critical message")