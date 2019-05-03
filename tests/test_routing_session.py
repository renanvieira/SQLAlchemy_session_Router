from unittest import TestCase
from unittest.mock import Mock

from sqlalchemy.engine import Engine

from SQLAlchemy_session_router import RoutingSession


class RoutingSessionTestCase(TestCase):

    def setUp(self):
        self.write_engine = Mock(Engine)
        self.read_engine = Mock(Engine)
        self.engine_registry = {"write_replica": self.write_engine, "read_replica": self.read_engine}

    def tearDown(self):
        self.write_engine = None
        self.read_engine = None
        self.engine_registry.clear()

    def test_routing_session(self):
        with self.subTest("with engine_selector raising error"):
            with self.assertRaises(ValueError):
                def engine_selector(flushing):
                    raise ValueError("Mocked error")

                session = RoutingSession(engine_selector)
                session.get_bind()

        with self.subTest("with engine_selector returning write engine"):

            def engine_selector(flushing):
                if flushing:
                    return self.write_engine
                else:
                    return self.read_engine

            session = RoutingSession(engine_selector)
            session._flushing = True

            engine = session.get_bind()

            self.assertIsNotNone(engine)
            self.assertEqual(engine, self.write_engine)

        with self.subTest("with engine_selector returning read engine"):

            session = RoutingSession(engine_selector)
            session._flushing = False

            engine = session.get_bind()

            self.assertIsNotNone(engine)
            self.assertEqual(engine, self.read_engine)