from enum import Enum, unique


@unique
class TestCaseSeverity(Enum):
    BLOCKER = {'blocker': '阻塞缺陷'}
    CRITICAL = {'critical': '严重缺陷'}
    NORMAL = {'normal', '一般缺陷'}
    MINOR = {'minor': '次要缺陷'}
    TRIVIAL = {'trivial': '轻微缺陷'}

    def get_severity(self):
        return list(self.value.values())[0]
