# logger.py

from abc import ABC, abstractmethod

# Strategy Pattern: Output methods
class LogStrategy(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(LogStrategy):
    def log(self, message):
        print(f"[Console] {message}")

class FileLogger(LogStrategy):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(f"[File] {message}\n")

# Bridge Pattern: Logger abstraction
class Logger:
    def __init__(self, strategy: LogStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: LogStrategy):
        self.strategy = strategy

    def log(self, message):
        self.strategy.log(message)

# Example Usage
if __name__ == "__main__":
    logger = Logger(ConsoleLogger())
    logger.log("System started.")

    logger.set_strategy(FileLogger("log.txt"))
    logger.log("Logged to file.")
