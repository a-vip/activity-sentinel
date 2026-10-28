import os
import unittest
import tempfile
import json
from unittest.mock import patch

from sentinel import load_heartbeat, record_pulse

class TestActivitySentinel(unittest.TestCase):

    def test_record_pulse(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = os.path.join(tmpdir, "heartbeat.json")
            with patch("sentinel.HEARTBEAT_FILE", test_file):
                # First pulse
                data1 = record_pulse()
                self.assertEqual(data1["streak_days"], 1)
                self.assertEqual(data1["total_pulses"], 1)
                self.assertIsNotNone(data1["last_pulse"])

                # Reload
                loaded = load_heartbeat()
                self.assertEqual(loaded["streak_days"], 1)

if __name__ == "__main__":
    unittest.main()
