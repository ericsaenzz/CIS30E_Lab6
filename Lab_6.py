class Legacylogger:
    def logmsg(self,message)
    print(message)

class Loggerinterface:
    def writelog(self,log):
        pass

class LoggerAdapter(Loggerinteface):
    def __init__(self,legacy_loger):
        self.legacy_logger = legacy_logger

    def write_log(self,log):
        self.legacy_logger.log_message(log)

def main():

    legacy_logger = Legacylogger()
    adapter = LoggerAdapter(legacy_loger)
    adapter.write_log("System rebooted successfully")

if __name__ = "__main__":
    main()