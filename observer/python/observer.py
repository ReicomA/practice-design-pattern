from abc import abstractmethod, ABCMeta

# Subject
class NewsPublisher:
    
    def __init__(self):
        self.subscribers = []
        self.news = None

    def attach_subscriber(self, new_subscriber):
        self.subscribers.append(new_subscriber)

    def detatch_subscriber(self):
        self.subscribers.pop()

    def set_news(self, news):
        self.news = news

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def get_news(self):
        return self.news

# Observer
class Subscriber(metaclass=ABCMeta):
    
    def __init__(self, new_publisher):
        self.publisher = new_publisher
        self.publisher.attach_subscriber(self)
    
    @abstractmethod
    def update(self):
        pass


class SubscriberA(Subscriber):
    def __init__(self, new_publisher):
        super().__init__(new_publisher)
    
    def update(self):
        print("Subscriber A: " + self.publisher.get_news())

class SubscriberB(Subscriber):
    def __init__(self, new_publisher):
        super().__init__(new_publisher)
    
    def update(self):
        print("Subscriber B: " + self.publisher.get_news())


if __name__ == "__main__":
    news_publisher = NewsPublisher()
    for subscriber_class in [SubscriberA, SubscriberB]:
        subscriber_class(news_publisher)

    news_publisher.set_news("This is the first news")
    news_publisher.notify()