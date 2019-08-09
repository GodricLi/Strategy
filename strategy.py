# _*_ coding=utf-8 _*_
"""
内容：定义一系列的算法，把它们一个个封装起来，并且使它们可相互替换。
    本模式使得算法可独立于使用它的客户而变化。
角色：
抽象策略（Strategy）
具体策略（ConcreteStrategy）
上下文（Context）

优点：
    定义了一系列可重用的算法和行为
    消除了一些条件语句
    可以提供相同行为的不同实现
缺点：
    客户必须了解不同的策略
"""

from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    """抽象策略"""

    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    """快速执行策略"""

    def execute(self, data):
        print("Fast...")


class SlowStrategy(Strategy):
    """慢执行策略"""

    def execute(self, data):
        print("Slow...")


class Context:
    """上下文角色，切换对应策略"""

    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


d = "[...]"
fast = FastStrategy()
slow = SlowStrategy()
# 快速策略
context = Context(fast, d)
context.do_strategy()

# 慢策略
context.set_strategy(slow)
context.do_strategy()
