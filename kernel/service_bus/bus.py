from kernel.service_bus.router import Router
from kernel.service_bus.dispatcher import Dispatcher
from kernel.service_bus.publisher import Publisher
from kernel.service_bus.subscriber import Subscriber
from kernel.service_bus.envelope import Envelope


class ServiceBus:
    """
    Atlas Enterprise Service Bus

    Central communication backbone
    for the Atlas Operating System.
    """

    def __init__(self):

        self.router = Router()

        self.dispatcher = Dispatcher(
            self.router
        )

        self.publisher = Publisher(
            self
        )

    def publish(
        self,
        envelope: Envelope,
    ):

        self.dispatcher.dispatch(
            envelope
        )

    def subscribe(
        self,
        subscriber: Subscriber,
    ):

        self.router.subscribe(
            subscriber
        )

    def unsubscribe(
        self,
        subscriber: Subscriber,
    ):

        self.router.unsubscribe(
            subscriber
        )