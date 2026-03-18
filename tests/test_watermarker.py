"""Tests for Watermarker."""
import pytest
from src.watermarker import Watermarker

def test_init():
    obj = Watermarker()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = Watermarker()
    result = obj.encode_text(input="test")
    assert result["processed"] is True
    assert result["operation"] == "encode_text"

def test_multiple_ops():
    obj = Watermarker()
    for m in ['encode_text', 'decode_text', 'encode_image']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = Watermarker()
    r1 = obj.encode_text(key="same")
    r2 = obj.encode_text(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = Watermarker()
    obj.encode_text()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = Watermarker()
    obj.encode_text(x=1)
    obj.decode_text(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
