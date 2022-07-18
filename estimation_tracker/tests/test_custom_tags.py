from datetime import datetime
from datetime import timedelta
from django.test import TestCase
from tracker.templatetags.custom_tags import (
    calculate_correctness_ratio,
    convert_time_to_seconds,
    estimate_time,
)

import pdb


class TestCustomTags(TestCase):
    def setUp(self) -> None:
        self.real_time = datetime.strptime("00:12:34", "%H:%M:%S").time()

    def test_convert_time_to_seconds_good(self):
        seconds = convert_time_to_seconds(self.real_time)

        self.assertEqual(seconds, 755.0)

    def test_convert_time_to_seconds_bad(self):
        time = "test"

        with self.assertRaises(AttributeError) as error:
            _ = convert_time_to_seconds(time)

    def test_calculate_correctness_ratio_good(self):
        self_estimated_time = datetime.strptime("00:10:34", "%H:%M:%S").time()

        seconds = calculate_correctness_ratio(self.real_time, self_estimated_time)

        self.assertEqual(seconds, 119)

    # TODO: Do this
    # FIXME: needs be fixed
    def test_calculate_correctness_ratio_bad(self):
        self_estimated_time = "time"

        with self.assertRaises(AttributeError) as error:
            calculate_correctness_ratio(self.real_time, self_estimated_time)

    def test_estimate_time_good(self):
        self_estimated_time = datetime.strptime("00:10:34", "%H:%M:%S").time()

        time = estimate_time(self.real_time, self_estimated_time)
        expected_data = datetime.strptime("00:21:08", "%H:%M:%S")

        self.assertEqual(time, expected_data.time())

    def test_estimate_time_bad(self):
        self_estimated_time = "timee"

        with self.assertRaises(AttributeError) as error:
            estimate_time(self.real_time, self_estimated_time)