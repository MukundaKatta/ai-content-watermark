"""Tests for AiContentWatermark."""
from src.core import AiContentWatermark
def test_init(): assert AiContentWatermark().get_stats()["ops"] == 0
def test_op(): c = AiContentWatermark(); c.detect(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = AiContentWatermark(); [c.detect() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = AiContentWatermark(); c.detect(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = AiContentWatermark(); r = c.detect(); assert r["service"] == "ai-content-watermark"
